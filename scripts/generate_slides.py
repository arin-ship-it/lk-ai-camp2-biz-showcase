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

import base64
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT       = Path(__file__).parent.parent
SUBMISSIONS_DIR = REPO_ROOT / "submissions"
SLIDES_DIR      = REPO_ROOT / "slides"
OUTPUT_MD       = SLIDES_DIR / "showcase.md"
OUTPUT_PDF      = SLIDES_DIR / "showcase.pdf"
THEME_CSS_PATH  = SLIDES_DIR / "theme.css"

# 인트로 전용 폴더 (일반 발표자 템플릿과 다른 구조로 파싱)
INTRO_FOLDER_NAMES = {"인트로", "intro"}
INTRO_HEADER       = "**LK AI Native Camp 2기** · 2026.04.23"

# 발표자 슬라이드 순서 (인트로 이후 등장 순서). 여기 없는 폴더는 뒤쪽에 이름순으로 붙는다.
PRESENTER_ORDER = ["chaeeun-jang", "mjshin", "Evan", "Bryan-ji", "nova"]

# 발표자별 직무 매핑 (name은 소문자로 비교)
# 새 발표자 추가 시 여기에 등록하세요.
ROLE_BY_NAME = {
    "chaeeun jang": "그로스 매니저",
    "mjshin":       "그로스 매니저",
    "nova":         "그로스 매니저",
    "evan":         "세일즈 매니저",
    "bryan":        "세일즈 매니저",
}
DEFAULT_ROLE = "콘텐츠 디자이너"

# 커버 태그 오버라이드 — 지정 시 자동 추출 대신 이 값을 쓴다.
TAGS_BY_NAME = {
    "bryan": ["고객사 정보 조사 자동화"],
}

# "현재 구현 단계" 비교표의 '기존 방식' 열 오버라이드.
# 원본 ②에 구체 리스트가 없을 때 이 값으로 좌측 열을 채운다.
CMP_OLD_BY_NAME = {
    "bryan": ["고객사 정보 수동 수집", "스크립트 수동 작성", "노션에 수동 저장"],
}


def _presenter_sort_key(dirname: str):
    """PRESENTER_ORDER 순서대로 정렬. 명시 안 된 폴더는 뒤쪽에 이름순."""
    low = dirname.lower()
    for i, n in enumerate(PRESENTER_ORDER):
        if n.lower() == low:
            return (0, i)
    return (1, dirname)


def role_for(name: str) -> str:
    return ROLE_BY_NAME.get(name.strip().lower(), DEFAULT_ROLE)


def tags_override_for(name: str):
    return TAGS_BY_NAME.get(name.strip().lower())


def cmp_old_override_for(name: str):
    return CMP_OLD_BY_NAME.get(name.strip().lower())


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
    return f"**{name.upper()}** · LK AI Native Camp 2기"


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
        line = re.sub(r'<[^>]+>', '', line).strip()
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

    # pill 뱃지 키워드 추출 (발표자별 오버라이드가 있으면 그대로 사용)
    override = tags_override_for(name)
    if override is not None:
        tags = list(override)
    else:
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
        f'<p class="cover-presenter"><strong>발표자</strong> {role_for(name)} &nbsp;｜&nbsp; {name}</p>\n'
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


def _has_top_level_arrow(text: str) -> bool:
    """괄호 밖(최상위)에 → 가 있는지."""
    depth = 0
    for ch in text:
        if ch in "(（":
            depth += 1
        elif ch in ")）":
            depth = max(0, depth - 1)
        elif ch == "→" and depth == 0:
            return True
    return False


def _split_top_level_arrow(text: str):
    """괄호 밖 첫 번째 → 로 좌·우 분리. 없으면 None."""
    depth = 0
    for i, ch in enumerate(text):
        if ch in "(（":
            depth += 1
        elif ch in ")）":
            depth = max(0, depth - 1)
        elif ch == "→" and depth == 0:
            return text[:i].strip(), text[i+1:].strip()
    return None


def _build_impl_content(name: str, s: dict) -> tuple:
    """현재 구현 단계 flow_html, cmp_html 반환 (slide_impl / slide_impl_with_image 공유)."""
    s2 = s.get("②", "")
    s4 = s.get("④", "")

    flow_steps = extract_flow_steps(s4)
    items4_all = parse_list_items(s4)

    cmp_pairs = []
    for it in items4_all:
        if _has_top_level_arrow(it):
            pair = _split_top_level_arrow(it)
            if pair:
                cmp_pairs.append(pair)

    if cmp_pairs and len(cmp_pairs) == len(items4_all):
        old_items = [p[0] for p in cmp_pairs]
        new_items = [p[1] for p in cmp_pairs]
    else:
        old_items = parse_list_items(s2)
        new_items = items4_all

    # 발표자별 '기존 방식' 오버라이드: ②에 구체 리스트가 없어도 3행을 확보할 수 있게 한다.
    override_old = cmp_old_override_for(name)
    if override_old is not None:
        old_items = list(override_old)

    if flow_steps:
        flow_divs = ""
        for i, step in enumerate(flow_steps):
            flow_divs += f'<div class="flow-step"><div class="flow-num">0{i+1}</div>{step}</div>'
        flow_html = f'<div class="flow-wrap">{flow_divs}</div>\n'
    else:
        flow_html = ""

    n = max(len(old_items), len(new_items), 1)
    while len(old_items) < n: old_items.append("—")
    while len(new_items) < n: new_items.append("—")

    rows = ""
    for old, new in zip(old_items, new_items):
        lbl_m = re.match(r'^([^:：]{2,10})[：:]\s*(.+)', old)
        if lbl_m:
            lbl = lbl_m.group(1).strip()
            old_text = lbl_m.group(2).strip()
        else:
            lbl = "비교"
            old_text = old
        old_s = old_text[:55] + ("…" if len(old_text) > 55 else "")
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

    return flow_html, cmp_html


def slide_impl(name: str, s: dict) -> str:
    """현재 구현 단계: 펜타곤 플로우 + 비교표"""
    flow_html, cmp_html = _build_impl_content(name, s)
    return (
        f'# 현재 구현 단계\n'
        f'<p class="slide-sub">자동화 전·후 비교</p>\n\n'
        + flow_html
        + cmp_html + "\n"
        + FOOTER_HTML
    )


def slide_impl_with_image(name: str, s: dict, img_rel_path: str) -> str:
    """현재 구현 단계 + 오른쪽 이미지 (2열 레이아웃) — slide_img*.png 자동 생성용.
    이미지를 크게 보여주기 위해 two-col-wide-right 클래스로 오른쪽 열을 넓힌다."""
    flow_html, cmp_html = _build_impl_content(name, s)
    return (
        f'# 현재 구현 단계\n'
        f'<p class="slide-sub">자동화 전·후 비교</p>\n\n'
        + flow_html
        + f'<div class="two-col two-col-wide-right">\n'
        + f'  <div class="col-l">{cmp_html}</div>\n'
        + f'  <div class="col-r"><img src="{img_rel_path}" style="width:100%;height:100%;object-fit:contain;"></div>\n'
        + f'</div>\n'
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


def slides_for_person(name: str, s: dict, person_dir: Path = None) -> list[str]:
    slides = [
        slide_cover(name, s),
        slide_problem(name, s),
        slide_impl(name, s),
    ]
    if person_dir:
        for img in sorted(person_dir.glob("slide_img*.png")):
            rel = f"../submissions/{person_dir.name}/{img.name}"
            slides.append(slide_impl_with_image(name, s, rel))
    slides.append(slide_reflection(name, s))
    return slides


# ── 인트로 전용 파서 & 슬라이드 ────────────────────────────────

def parse_intro(path: Path) -> dict:
    """인트로 SHOWCASE.md 를 `## 섹션명` 기준으로 분해한다."""
    content = path.read_text(encoding="utf-8")
    parts = re.split(r'^## (.+)$', content, flags=re.MULTILINE)
    sections = {}
    for i in range(1, len(parts), 2):
        name = parts[i].strip()
        body = parts[i + 1].strip() if i + 1 < len(parts) else ""
        body = re.sub(r'\n---\s*$', '', body).strip()
        sections[name] = body
    return sections


def _intro_kv(text: str) -> dict:
    """`**키**: 값` 패턴을 딕셔너리로."""
    out = {}
    for line in text.splitlines():
        m = re.match(r'^\s*\*\*(.+?)\*\*\s*[:：]\s*(.+)$', line.strip())
        if m:
            out[m.group(1).strip()] = m.group(2).strip()
    return out


def slide_intro_cover(s: dict) -> str:
    kv = _intro_kv(s.get("커버", ""))
    title    = kv.get("제목", "LK AI Camp 2기")
    subtitle = kv.get("부제", "사업팀 AI 네이티브 캠프")
    date     = kv.get("날짜", "2026.04.23")
    tags_raw = kv.get("태그", "")
    tags = [t.strip() for t in re.split(r'[·,/]', tags_raw) if t.strip()]
    tags_html = ''.join(f'<span class="tag">{t}</span>' for t in tags)

    return (
        f"<!-- _class: cover -->\n\n"
        f'<div class="cover-title">{title}</div>\n'
        f'<p class="cover-presenter">{subtitle} &nbsp;｜&nbsp; <strong>{date}</strong></p>\n'
        + (f'<div class="cover-tags">{tags_html}</div>\n' if tags_html else "")
        + FOOTER_HTML
    )


def _photo_data_uri(src: Path, target_w: int = 800) -> str:
    """sips로 target_w px 로 축소 후 base64 data URI 반환. 실패 시 빈 문자열."""
    if not src.exists():
        return ""
    try:
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tf:
            tmp = Path(tf.name)
        subprocess.run(
            ["sips", "--resampleWidth", str(target_w), str(src), "--out", str(tmp)],
            check=True, capture_output=True,
        )
        data = base64.b64encode(tmp.read_bytes()).decode("ascii")
        return f"data:image/jpeg;base64,{data}"
    except Exception:
        return ""
    finally:
        try:
            tmp.unlink()
        except Exception:
            pass


def slide_intro_photos(s: dict) -> str:
    """1기 현장 사진 그리드 (3×3) — 이미지를 base64로 내장해 경로 문제 우회"""
    text = s.get("사진", "")
    filenames = [
        ln.strip() for ln in text.splitlines()
        if ln.strip() and not ln.strip().startswith("<!--") and "-->" not in ln.strip()
        and re.match(r'.+\.(jpg|jpeg|png|gif|webp)$', ln.strip(), re.IGNORECASE)
    ]
    caption_m = re.search(r'\*\*캡션\*\*\s*[:：]?\s*(.+)', text)
    caption = caption_m.group(1).strip() if caption_m else "2025.03.13 · 1기 현장"

    INTRO_DIR = SUBMISSIONS_DIR / "인트로"
    imgs = filenames[:9]

    CELL_W = "370px"
    CELL_H = "138px"
    cells = ""
    for fn in imgs:
        uri = _photo_data_uri(INTRO_DIR / fn)
        if uri:
            cells += (
                f'<div style="width:{CELL_W};height:{CELL_H};overflow:hidden;display:inline-block">'
                f'<img src="{uri}" style="width:{CELL_W};height:{CELL_H};object-fit:cover;display:block;max-width:none;max-height:none">'
                f'</div>'
            )
        else:
            cells += f'<div style="width:{CELL_W};height:{CELL_H};background:var(--c-cream-band)"></div>'
    for _ in range(9 - len(imgs)):
        cells += f'<div style="width:{CELL_W};height:{CELL_H};background:var(--c-cream-band)"></div>'

    grid_html = (
        f'<div style="display:grid;grid-template-columns:repeat(3,{CELL_W});'
        f'grid-template-rows:repeat(3,{CELL_H});gap:5px;margin-top:8px">'
        f'{cells}'
        f'</div>'
    )

    return (
        f'# 1기가 먼저 증명했습니다\n'
        f'<p class="slide-sub">{caption}</p>\n\n'
        f'{grid_html}\n'
        + FOOTER_HTML
    )


def _render_table_and_paragraphs(text: str) -> str:
    """GFM 표와 일반 단락이 섞인 블록을 HTML로 변환 (인트로 1기 활용 유형용)."""
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        ln = lines[i]
        stripped = ln.strip()
        if (
            stripped.startswith("|")
            and i + 1 < len(lines)
            and re.match(r'^\s*\|[\s\-:|]+\|\s*$', lines[i + 1])
        ):
            headers = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2
            rows: list[list[str]] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            thead = "<thead><tr>" + "".join(f"<th>{h}</th>" for h in headers) + "</tr></thead>"
            tbody = "<tbody>" + "".join(
                "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows
            ) + "</tbody>"
            out.append(f'<table class="mini-table">{thead}{tbody}</table>')
            continue
        if stripped:
            inline = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', stripped)
            out.append(f'<p class="mini-note">{inline}</p>')
        i += 1
    return "\n".join(out)


def slide_intro_frame(s: dict) -> str:
    """프레임: 두 기수 공통 메시지 + 2열 (1기|2기) + 핵심 문장"""
    text = s.get("프레임", "")
    activity_raw = s.get("1기 활용 유형", "")
    activity_html = _render_table_and_paragraphs(activity_raw) if activity_raw else ""
    items = parse_list_items(text)

    camp1 = next((it for it in items if re.match(r'^\s*1기', it)), "")
    camp2 = next((it for it in items if re.match(r'^\s*2기', it)), "")

    def split_date_body(it: str):
        # "1기 (2026.03.13): ..." → label="1기", date="2026.03.13", body="..."
        m = re.match(r'^\s*(\S+기)\s*[（(]([^）)]+)[）)]\s*[:：]\s*(.+)$', it)
        if m:
            return m.group(1), m.group(2), m.group(3)
        m2 = re.match(r'^\s*(\S+)\s*[:：]\s*(.+)$', it)
        if m2:
            return m2.group(1), "", m2.group(2)
        return ("", "", it)

    l1, d1, b1 = split_date_body(camp1)
    l2, d2, b2 = split_date_body(camp2)

    # 불릿 블록 제외한 단락들 → closing 문장들
    paragraphs = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
    closing_paras = [p for p in paragraphs if not p.startswith("-") and not p.startswith("*")]
    closing_html = "".join(md_to_html(p) for p in closing_paras[-2:]) if closing_paras else ""

    def col(label, date, body, extra=""):
        date_span = f'<span style="font-size:0.72em;color:var(--c-ink-dim);margin-left:6px">{date}</span>' if date else ""
        return (
            f'<p class="sec-label">{label}{date_span}</p>'
            f'{md_to_html(body) if body else ""}'
            f'{extra}'
        )

    return (
        f'# 두 기수의 공통점 — AI로 일이 달라졌다\n'
        f'<p class="slide-sub">1기가 증명했고, 2기는 그 사람이 늘어난 것입니다.</p>\n\n'
        f'<div class="two-col">\n'
        f'  <div class="col-l">{col(l1 or "1기", d1, b1, activity_html)}</div>\n'
        f'  <div class="col-r">{col(l2 or "2기", d2, b2)}</div>\n'
        f'</div>\n'
        f'<hr class="sec-divider">\n'
        f'{closing_html}\n'
        + FOOTER_HTML
    )


def slide_intro_preview(s: dict) -> str:
    """오늘의 관람 포인트 + 발표자 프리뷰"""
    text = s.get("오늘의 관람 포인트", "")

    # "보는 법" 섹션 (X/O 대비)
    view_items = []
    speaker_items = []
    closing_quote = ""

    mode = None
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("**보는 법**"):
            mode = "view"; continue
        if stripped.startswith("**오늘의 발표자"):
            mode = "speakers"; continue
        if stripped.startswith(">"):
            closing_quote = stripped.lstrip(">").strip()
            mode = None; continue
        if mode == "view" and re.match(r'^[-*]\s+', stripped):
            view_items.append(re.sub(r'^[-*]\s+', '', stripped))
        elif mode == "speakers" and re.match(r'^[-*]\s+', stripped):
            speaker_items.append(re.sub(r'^[-*]\s+', '', stripped))

    view_html = ""
    if view_items:
        view_html = "<ul>" + "".join(f"<li>{md_to_html(v).strip('<p></p>')}</li>" for v in view_items) + "</ul>"

    speakers_html = ""
    if speaker_items:
        rows = ""
        for item in speaker_items:
            # "**Evan** — 세일즈 매니저 · 신규 고객 온보딩 자동화"
            m = re.match(r'^\*\*(.+?)\*\*\s*[—\-–]\s*(.+?)\s*[·・]\s*(.+)$', item)
            if m:
                rows += (
                    f'<tr>'
                    f'<td><strong>{m.group(1)}</strong></td>'
                    f'<td class="m-mid">{m.group(2)}</td>'
                    f'<td>{m.group(3)}</td>'
                    f'</tr>'
                )
            else:
                rows += f'<tr><td colspan="3">{item}</td></tr>'
        speakers_html = (
            '<table class="cmp-table speakers-table">'
            '<thead><tr>'
            '<th class="h-left">발표자</th>'
            '<th class="h-mid">직무</th>'
            '<th class="h-right">주제</th>'
            '</tr></thead>'
            f'<tbody>{rows}</tbody>'
            '</table>'
        )

    if closing_quote:
        quote_inline = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', closing_quote)
        closing_html = f"<blockquote><p>{quote_inline}</p></blockquote>"
    else:
        closing_html = ""

    speaker_label_suffix = f" ({len(speaker_items)}명)" if speaker_items else ""
    return (
        f'# 오늘의 관람 포인트\n'
        f'<p class="slide-sub">\'AI를 썼구나\'가 아니라 \'일하는 방식이 이렇게 달라지고 있구나\'를 봐주세요.</p>\n\n'
        f'<p class="sec-label">보는 법</p>\n'
        f'{view_html}\n'
        f'<hr class="sec-divider">\n'
        f'<p class="sec-label">오늘의 발표자{speaker_label_suffix}</p>\n'
        f'{speakers_html}\n'
        f'{closing_html}\n'
        + FOOTER_HTML
    )


def slides_for_intro(s: dict) -> list[str]:
    return [
        slide_intro_cover(s),
        slide_intro_photos(s),
        slide_intro_frame(s),
        slide_intro_preview(s),
    ]


def build_presentation(persons, intro=None) -> str:
    slide_chunks: list[str] = []

    # 인트로 (있으면 맨 앞에 배치)
    if intro:
        intro_slides = slides_for_intro(intro)
        header_dir = f"<!-- header: \"{INTRO_HEADER}\" -->"
        intro_slides[0]  = f"{header_dir}\n<!-- === 인트로 === -->\n\n{intro_slides[0]}"
        intro_slides[-1] = f"{intro_slides[-1]}\n\n<!-- === /인트로 === -->"
        slide_chunks.extend(intro_slides)

    # "우리가 만든 것들" 디바이더
    first_header = person_header(persons[0][0]) if persons else "LK AI Camp 2기"
    slide_chunks.append(
        f"<!-- _class: divider -->\n"
        f"<!-- _header: \"{first_header}\" -->\n\n"
        f"# 우리가 만든 것들\n\n"
        f'<span class="slide-footer">2026.04</span>'
        f'<span class="corner-sq"></span>'
    )

    for item in persons:
        name, sections = item[0], item[1]
        person_dir = item[2] if len(item) > 2 else None
        slides = slides_for_person(name, sections, person_dir)
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
    intro_sections = None
    person_dirs = sorted(
        [p for p in SUBMISSIONS_DIR.iterdir() if p.is_dir()],
        key=lambda p: _presenter_sort_key(p.name),
    )
    for person_dir in person_dirs:
        if not person_dir.is_dir():
            continue
        if person_dir.name.lower() in excludes:
            print(f"  ✗ {person_dir.name:<15} (--exclude 로 제외됨)")
            continue
        f = person_dir / "SHOWCASE.md"
        if not f.exists():
            continue

        if person_dir.name in INTRO_FOLDER_NAMES or person_dir.name.lower() in INTRO_FOLDER_NAMES:
            intro_sections = parse_intro(f)
            filled = sum(1 for v in intro_sections.values() if v)
            print(f"  ✓ {person_dir.name:<15} (인트로)       — {filled} 섹션 작성됨")
            continue

        name, sections = parse_showcase(f)
        filled = sum(1 for v in sections.values() if v)
        img_count = len(list(person_dir.glob("slide_img*.png")))
        persons.append((name, sections, person_dir))
        extra = f" + {img_count}장 이미지 슬라이드" if img_count else ""
        print(f"  ✓ {person_dir.name:<15} ({name})  — {filled}/6 항목 작성됨{extra}")

    if not persons and not intro_sections:
        if excludes:
            print("\n제외 규칙으로 모든 발표자가 빠졌습니다. 디바이더 슬라이드만 생성합니다.")
        else:
            print("\n제출된 SHOWCASE.md 파일이 없습니다.")
            sys.exit(1)

    print(f"\n총 {len(persons)}명 파싱 완료" + (" (+ 인트로)" if intro_sections else "") + ". 슬라이드 생성 중...")
    SLIDES_DIR.mkdir(exist_ok=True)
    md = build_presentation(persons, intro=intro_sections)
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
