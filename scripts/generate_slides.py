#!/usr/bin/env python3
"""
submissions/*/SHOWCASE.md 를 읽어 Marp 슬라이드 마크다운을 생성합니다.

실행:
    python3 scripts/generate_slides.py                     # 전체 재생성
    python3 scripts/generate_slides.py --update-css        # CSS만 최신화
    python3 scripts/generate_slides.py --exclude arin      # 특정 발표자 제외
    python3 scripts/generate_slides.py --exclude arin --exclude evan  # 다중 제외

HTML 빌드:
    bash scripts/build_slides.sh          # 전체
    bash scripts/build_slides.sh --html-only
"""

import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT       = Path(__file__).parent.parent
SUBMISSIONS_DIR = REPO_ROOT / "submissions"
SLIDES_DIR      = REPO_ROOT / "slides"
OUTPUT_MD       = SLIDES_DIR / "showcase.md"
OUTPUT_PDF      = SLIDES_DIR / "showcase.pdf"
THEME_CSS_PATH  = SLIDES_DIR / "theme.css"

TEMPLATE_HINTS = [
    "어떤 업무에서 불편함이나 비효율을",
    "반복적으로 하던 작업, 시간이 오래 걸리던",
    "AI를 쓰기 전에는 어떻게 하고 있었나요",
    "어디서 막히거나, 어디에 시간이",
    "AI로 어떤 변화를 만들고 싶었나요",
    "이렇게 되면 좋겠다",
    "지금까지 무엇을 만들었는지, 어느 정도 완성됐는지",
    "완성이 아니어도 괜찮아요. 시도한 것 자체가",
    "아직 해결하지 못한 것, 더 발전시키고 싶은 것",
    "이번 캠프를 통해 느낀 점, 달라진 것",
    "SHOWCASE.md 제출 후 채움",
]

def build_marp_header() -> str:
    """YAML 프런트매터에 slides/theme.css 를 인라인 주입."""
    if not THEME_CSS_PATH.exists():
        print(f"오류: theme.css가 없습니다 → {THEME_CSS_PATH}")
        sys.exit(1)
    css = THEME_CSS_PATH.read_text(encoding="utf-8")
    # YAML block scalar용 2-space 들여쓰기
    indented = "\n".join(f"  {line}" if line else "" for line in css.splitlines())
    return (
        "---\n"
        "marp: true\n"
        "paginate: true\n"
        "html: true\n"
        "header: ''\n"
        "style: |\n"
        f"{indented}\n"
        "---"
    )


def person_header(name: str) -> str:
    """슬라이드 상단 헤더바에 들어갈 발표자 태그 텍스트."""
    return f"**{name.upper()}** · LK AI Camp 2기"


# ── 파싱 유틸 ─────────────────────────────────────────────────

def is_template(text: str) -> bool:
    return not text or any(hint in text for hint in TEMPLATE_HINTS)


def parse_showcase(path: Path) -> tuple[str, dict]:
    content = path.read_text(encoding="utf-8")
    title_m = re.search(r"^#\s+(.+)", content, re.MULTILINE)
    raw = title_m.group(1).strip() if title_m else ""
    name_m = re.match(r"\[(.+?)\]", raw)
    name = name_m.group(1) if name_m else (raw.replace("AI Camp2 Showcase", "").strip() or path.parent.name)

    sections: dict[str, str] = {}
    for num in "①②③④⑤⑥":
        pat = rf"## {re.escape(num)}\s+[^\n]+\n(.*?)(?=\n## [①②③④⑤⑥]|$)"
        m = re.search(pat, content, re.DOTALL)
        text = m.group(1).strip() if m else ""
        text = re.sub(r"\n---\s*$", "", text).strip()
        sections[num] = "" if is_template(text) else text

    return name, sections


def first_sentence(text: str) -> str:
    for line in text.splitlines():
        line = line.strip().lstrip("#").lstrip("-").lstrip("*").strip()
        line = re.sub(r'^\d+[.)]\s*', '', line).strip()
        if line and not line.startswith(">"):
            return line[:120] + ("…" if len(line) > 120 else "")
    return ""


def fallback(text: str, placeholder: str = "(작성 중)") -> str:
    return text if text else placeholder


def parse_list_items(text: str) -> list[str]:
    items = []
    for line in text.splitlines():
        line = line.strip()
        m = re.match(r'^\d+[.)]\s+(.+)', line)
        if m:
            items.append(m.group(1).strip())
            continue
        m = re.match(r'^[-*]\s+(.+)', line)
        if m:
            items.append(m.group(1).strip())
    return items


def extract_flow_steps(text: str) -> list[str]:
    m = re.search(r'[（(]([^）)\n]+(?:→[^）)\n]+)+)[）)]', text)
    if not m:
        return []
    raw = [s.strip() for s in m.group(1).split('→') if s.strip()]
    steps = []
    for step in raw[:5]:
        step = re.sub(r'\s*[（(][^）)]*[）)]\s*', '', step).strip()
        if len(step) > 10:
            words = step.split()
            step = ' '.join(words[:2]) if len(' '.join(words[:2])) <= 10 else words[0][:10]
        steps.append(step)
    return steps


def md_to_html(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    lines = text.splitlines()
    out, i = [], 0
    while i < len(lines):
        ln = lines[i].strip()
        if re.match(r'^[-*]\s+', ln):
            items = []
            while i < len(lines) and re.match(r'^[-*]\s+', lines[i].strip()):
                items.append(re.sub(r'^[-*]\s+', '', lines[i].strip()))
                i += 1
            out.append('<ul>' + ''.join(f'<li>{it}</li>' for it in items) + '</ul>')
            continue
        if re.match(r'^\d+[.)]\s+', ln):
            items = []
            while i < len(lines) and re.match(r'^\d+[.)]\s+', lines[i].strip()):
                items.append(re.sub(r'^\d+[.)]\s+', '', lines[i].strip()))
                i += 1
            out.append('<ol>' + ''.join(f'<li>{it}</li>' for it in items) + '</ol>')
            continue
        if ln:
            out.append(f'<p>{ln}</p>')
        i += 1
    return '\n'.join(out)


# ── 슬라이드 생성 ─────────────────────────────────────────────

FOOTER_HTML = '<span class="slide-footer">2026.04</span><span class="corner-sq"></span>'


def slide_cover(name: str, s: dict) -> str:
    """커버 슬라이드: 큰 제목 + 발표자 + pill 뱃지"""
    s1 = s.get("①", "")
    s3 = s.get("③", "")
    s4 = s.get("④", "")

    # 제목: SHOWCASE.md 파일 첫 줄 h1에서 가져온 프로젝트명 추출 시도
    # 없으면 이름으로 대체
    project = first_sentence(s1) or f"{name}의 자동화 도구"
    proj_short = project[:30] + ("…" if len(project) > 30 else "")

    # pill 뱃지 키워드 추출
    tags = []
    if s4:
        flow_m = re.search(r'[（(]([^）)\n]+(?:→[^）)\n]+)+)[）)]', s4)
        if flow_m:
            steps = [st.strip() for st in flow_m.group(1).split('→') if st.strip()]
            tags.append(f"{len(steps)}단계 자동화 워크플로우")
        items4 = parse_list_items(s4)
        non_flow = [it for it in items4 if '→' not in it]
        if non_flow:
            tags.append(non_flow[0][:20])
    if s1 and "30분" in s1:
        tags.insert(0, "주 30분 → 0분")
    elif s1:
        tags.insert(0, first_sentence(s1)[:18])

    tags = tags[:3]
    tags_html = ''.join(f'<span class="tag">{t}</span>' for t in tags)

    return (
        f"<!-- _class: cover -->\n\n"
        f'<div class="cover-title">{name}의<br>자동화 도구</div>\n'
        f'<p class="cover-presenter"><strong>발표자</strong> 콘텐츠 디자이너 &nbsp;｜&nbsp; {name}</p>\n'
        + (f'<div class="cover-tags">{tags_html}</div>\n' if tags_html else "")
        + FOOTER_HTML
    )


def slide_problem(name: str, s: dict) -> str:
    """문제와 해결 방향: 2열 (①③ 텍스트 | ② 표)"""
    s1 = s.get("①", "")
    s2 = s.get("②", "")
    s3 = s.get("③", "")
    subtitle = (first_sentence(s1) or "")[:80]

    # 왼쪽: ①③ 텍스트
    s1_html = md_to_html(fallback(s1))
    s3_html = md_to_html(fallback(s3))

    # 오른쪽: ② 표 (병목 유형 | 구체적 문제)
    items2 = parse_list_items(s2)
    if items2:
        rows = ""
        for item in items2:
            lbl_m = re.match(r'^([^:：]{2,10})[：:]\s*(.+)', item)
            if lbl_m:
                lbl = lbl_m.group(1).strip()
                desc = lbl_m.group(2).strip()[:60]
            else:
                lbl = "병목"
                desc = item[:60]
            rows += f"<tr><td>{lbl}</td><td>{desc}</td></tr>"
        table_html = (
            f'<table>'
            f'<thead><tr><th>병목 유형</th><th>구체적 문제</th></tr></thead>'
            f'<tbody>{rows}</tbody>'
            f'</table>'
        )
    else:
        table_html = md_to_html(fallback(s2))

    return (
        f'# 문제와 해결 방향\n'
        f'<p class="slide-sub">{subtitle}</p>\n\n'
        f'<div class="two-col">\n'
        f'  <div class="col-l">'
        f'<p class="sec-label">① 문제 상황</p>'
        f'{s1_html}'
        f'<hr class="sec-divider">'
        f'<p class="sec-label">③ 지향했던 방향성</p>'
        f'{s3_html}'
        f'</div>\n'
        f'  <div class="col-r">'
        f'<p class="sec-label">② 기존 방식의 병목</p>'
        f'{table_html}'
        f'</div>\n'
        f'</div>\n'
        + FOOTER_HTML
    )


def slide_impl(name: str, s: dict) -> str:
    """현재 구현 단계: 펜타곤 플로우 + 비교표"""
    s2 = s.get("②", "")
    s4 = s.get("④", "")

    flow_steps = extract_flow_steps(s4)
    old_items  = parse_list_items(s2)
    new_items  = [it for it in parse_list_items(s4) if '→' not in it]

    # 펜타곤 플로우
    if flow_steps:
        flow_divs = ""
        for i, step in enumerate(flow_steps):
            flow_divs += f'<div class="flow-step"><div class="flow-num">0{i+1}</div>{step}</div>'
        flow_html = f'<div class="flow-wrap">{flow_divs}</div>\n'
    else:
        flow_html = ""

    # 비교표
    n = max(len(old_items), len(new_items), 1)
    while len(old_items) < n: old_items.append("—")
    while len(new_items) < n: new_items.append("—")

    rows = ""
    for old, new in zip(old_items, new_items):
        lbl_m = re.match(r'^([^:：]{2,8})[：:]\s*', old)
        lbl = lbl_m.group(1).strip() if lbl_m else "비교"
        old_s = old[:55] + ("…" if len(old) > 55 else "")
        new_s = new[:55] + ("…" if len(new) > 55 else "")
        rows += f'<tr><td>{old_s}</td><td class="m-mid">{lbl}</td><td>{new_s}</td></tr>'

    cmp_html = (
        f'<table class="cmp-table">'
        f'<thead><tr>'
        f'<th class="h-left">기존 방식</th>'
        f'<th class="h-mid">구분</th>'
        f'<th class="h-right">자동화 후</th>'
        f'</tr></thead>'
        f'<tbody>{rows}</tbody>'
        f'</table>'
    ) if old_items and new_items else md_to_html(fallback(s4))

    return (
        f'# 현재 구현 단계\n'
        f'<p class="slide-sub">자동화 전·후 비교</p>\n\n'
        + flow_html
        + cmp_html + "\n"
        + FOOTER_HTML
    )


def slide_reflection(name: str, s: dict) -> str:
    """추후 과제 & 소감"""
    s5 = s.get("⑤", "")
    s6 = s.get("⑥", "")
    s5_html = md_to_html(fallback(s5))
    s6_html = md_to_html(fallback(s6))

    return (
        f'# 추후 과제 &amp; 소감\n'
        f'<p class="slide-sub">앞으로 발전시키고 싶은 것, 그리고 이번 캠프를 통해 달라진 것</p>\n\n'
        f'<p class="sec-label">⑤ 추후 과제</p>\n'
        f'{s5_html}\n'
        f'<hr class="sec-divider">\n'
        f'<p class="sec-label">⑥ 소감</p>\n'
        f'{s6_html}\n'
        + FOOTER_HTML
    )


def slides_for_person(name: str, s: dict) -> list[str]:
    return [
        slide_cover(name, s),
        slide_problem(name, s),
        slide_impl(name, s),
        slide_reflection(name, s),
    ]


def build_presentation(persons: list[tuple[str, dict]]) -> str:
    first_header = person_header(persons[0][0]) if persons else "LK AI Camp 2기"
    slide_chunks: list[str] = [
        f"<!-- _class: divider -->\n"
        f"<!-- _header: \"{first_header}\" -->\n\n"
        f"# 우리가 만든 것들\n\n"
        f'<span class="slide-footer">2026.04</span>'
        f'<span class="corner-sq"></span>'
    ]

    for name, sections in persons:
        slides = slides_for_person(name, sections)
        header_dir = f"<!-- header: \"{person_header(name)}\" -->"
        slides[0]  = f"{header_dir}\n<!-- === 발표자: {name} === -->\n\n{slides[0]}"
        slides[-1] = f"{slides[-1]}\n\n<!-- === /발표자: {name} === -->"
        slide_chunks.extend(slides)

    body = "\n\n---\n\n".join(slide_chunks)
    warning = (
        "<!--\n"
        "  ⚠️ 자동 생성 파일 — 직접 편집 금지\n"
        "  이 파일은 scripts/generate_slides.py 가 submissions/*/SHOWCASE.md 로부터 생성합니다.\n"
        "  내용 수정은 submissions/<영문이름>/SHOWCASE.md 를 편집한 뒤,\n"
        "  프로젝트 루트에서 `bash scripts/build_slides.sh` 를 실행해 재빌드하세요.\n"
        "  이 파일을 직접 편집하면 다음 빌드에서 변경사항이 전부 사라집니다.\n"
        "-->"
    )
    return f"{build_marp_header()}\n\n{warning}\n\n{body}\n"


def update_css():
    if not OUTPUT_MD.exists():
        print(f"오류: {OUTPUT_MD} 파일이 없습니다.")
        sys.exit(1)
    content = OUTPUT_MD.read_text(encoding="utf-8")
    pattern = re.compile(r"^---\n.*?^---", re.DOTALL | re.MULTILINE)
    m = pattern.search(content)
    if not m:
        print("오류: showcase.md에서 YAML 프런트매터를 찾을 수 없습니다.")
        sys.exit(1)
    updated = content[: m.start()] + build_marp_header() + content[m.end():]
    OUTPUT_MD.write_text(updated, encoding="utf-8")
    print(f"CSS 최신화 완료: {OUTPUT_MD}  (← {THEME_CSS_PATH.name} 반영)")


def parse_excludes(argv: list[str]) -> set[str]:
    """--exclude NAME (중복 허용) 로 지정된 발표자 디렉토리명을 소문자로 수집."""
    excludes: set[str] = set()
    i = 0
    while i < len(argv):
        if argv[i] == "--exclude" and i + 1 < len(argv):
            excludes.add(argv[i + 1].lower())
            i += 2
        else:
            i += 1
    return excludes


def main():
    if "--update-css" in sys.argv:
        update_css()
        return

    excludes = parse_excludes(sys.argv[1:])

    print("SHOWCASE.md 파일 수집 중...\n")
    if not SUBMISSIONS_DIR.exists():
        print(f"오류: {SUBMISSIONS_DIR} 폴더가 없습니다.")
        sys.exit(1)

    persons = []
    for person_dir in sorted(SUBMISSIONS_DIR.iterdir()):
        if not person_dir.is_dir():
            continue
        if person_dir.name.lower() in excludes:
            print(f"  ✗ {person_dir.name:<15} (--exclude 로 제외됨)")
            continue
        f = person_dir / "SHOWCASE.md"
        if not f.exists():
            continue
        name, sections = parse_showcase(f)
        filled = sum(1 for v in sections.values() if v)
        persons.append((name, sections))
        print(f"  ✓ {person_dir.name:<15} ({name})  — {filled}/6 항목 작성됨")

    if not persons:
        if excludes:
            print("\n제외 규칙으로 모든 발표자가 빠졌습니다. 디바이더 슬라이드만 생성합니다.")
        else:
            print("\n제출된 SHOWCASE.md 파일이 없습니다.")
            sys.exit(1)

    print(f"\n총 {len(persons)}명 파싱 완료. 슬라이드 생성 중...")
    SLIDES_DIR.mkdir(exist_ok=True)
    md = build_presentation(persons)
    OUTPUT_MD.write_text(md, encoding="utf-8")
    print(f"마크다운 생성: {OUTPUT_MD}")

    try:
        subprocess.run(
            ["marp", str(OUTPUT_MD), "--pdf", "--allow-local-files", "-o", str(OUTPUT_PDF)],
            check=True, capture_output=True,
        )
        print(f"PDF 생성 완료: {OUTPUT_PDF}")
    except FileNotFoundError:
        print(
            "\n⚠️  marp CLI가 없습니다. HTML 빌드는 build_slides.sh를 사용하세요:\n"
            "    bash scripts/build_slides.sh"
        )
    except subprocess.CalledProcessError as e:
        print(f"\n오류: {e.stderr.decode()}")


if __name__ == "__main__":
    main()
