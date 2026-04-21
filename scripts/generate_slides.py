#!/usr/bin/env python3
"""
submissions/*/SHOWCASE.md 를 읽어 Marp 슬라이드 마크다운을 생성하고 PDF로 변환합니다.

실행:
    python3 scripts/generate_slides.py

사전 설치 (PDF 변환용):
    npm install -g @marp-team/marp-cli

<!--
<slide-design-guidelines>

  <color-chip confirmed="true">
    <background>#FFFCF2</background>       <!-- Orchid White -->
    <dark-primary>#252422</dark-primary>   <!-- Warm Black -->
    <dark-secondary>#403D39</dark-secondary> <!-- Masala -->
    <accent>#e07a5f</accent>              <!-- Main — 구조 요소에만 사용 -->
    <sub>#CCC5B9</sub>                    <!-- Chrome White -->
  </color-chip>

  <layout>
    <rule>표·비교표·플로우는 콘텐츠 영역 전체 너비 사용</rule>
    <rule>2컬럼 비율: 텍스트+표 = 38:62 / 비교 3열 = 42:16:42</rule>
    <rule>콘텐츠가 상단에 몰리지 않도록 수직 여백 균형 유지</rule>
    <reference-layouts>표 / 비교 / 순서(화살표) / 안내문(구분선)</reference-layouts>
  </layout>

  <content>
    <rule>줄글 지양 — 표·비교·플로우·구분선 항목으로 시각화 우선</rule>
    <rule>단계형 → 화살표 플로우 / 비교형 → 3열 비교표 / 목록형 → 표</rule>
    <rule>슬라이드 1장당 핵심 메시지 1개</rule>
  </content>

  <emphasis>
    <rule>강조는 bold(font-weight:900) 위주</rule>
    <rule>accent 컬러는 h2 라벨·플로우 마지막 단계·비교표 헤더·태그 뱃지에만 사용</rule>
    <rule>본문 텍스트에 accent 컬러 남발 금지</rule>
  </emphasis>

  <structure>
    <rule>헤더바(회사명 좌 / 페이지번호 우) + 하단 다크 블록 코너 일관 적용</rule>
    <rule>커버: 제목 + 발표자 정보 + 키워드 태그 뱃지</rule>
    <rule>디바이더: dark 배경 섹션 구분 슬라이드</rule>
  </structure>

</slide-design-guidelines>
-->
"""

import re
import subprocess
import sys
from pathlib import Path

# ── 경로 설정 ──────────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).parent.parent
SUBMISSIONS_DIR = REPO_ROOT / "submissions"
SLIDES_DIR = REPO_ROOT / "slides"
OUTPUT_MD = SLIDES_DIR / "showcase.md"
OUTPUT_PDF = SLIDES_DIR / "showcase.pdf"

# ── 템플릿 기본 텍스트 감지 ───────────────────────────────────────────────────

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

# ── Marp 스타일 ────────────────────────────────────────────────────────────────

MARP_HEADER = """\
---
marp: true
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');

  section {
    background: #f0e8d8;
    color: #2a2a2a;
    font-family: 'Noto Sans KR', 'Apple SD Gothic Neo', sans-serif;
    padding: 56px 80px;
    font-size: 21px;
    line-height: 1.65;
    box-sizing: border-box;
  }
  section.dark {
    background: #3d3d3d;
    color: #ffffff;
  }
  section.divider {
    background: #3d3d3d;
    color: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  /* 제목 (이름) */
  h1 {
    font-size: 1.85em;
    font-weight: 900;
    border-bottom: 4px solid #e07a5f;
    padding-bottom: 0.12em;
    display: inline-block;
    margin: 0 0 0.55em 0;
    line-height: 1.2;
  }
  section.dark h1,
  section.divider h1 {
    color: #ffffff;
    border-bottom-color: #e07a5f;
  }

  /* 소제목 */
  h2 {
    font-size: 1em;
    font-weight: 700;
    color: #2a2a2a;
    margin: 0.9em 0 0.25em;
    letter-spacing: -0.01em;
  }
  h2:first-of-type { margin-top: 0; }

  /* 인용 박스 (산출물 요약 / 소감) */
  blockquote {
    background: rgba(224, 122, 95, 0.13);
    border-left: 5px solid #e07a5f;
    padding: 13px 20px;
    margin: 14px 0;
    border-radius: 0 6px 6px 0;
    font-size: 0.9em;
    color: #555;
    font-style: normal;
  }
  blockquote p { margin: 0; }

  /* 표 */
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.85em;
    margin-top: 0.5em;
  }
  th {
    background: #2a2a2a;
    color: #ffffff;
    padding: 10px 14px;
    text-align: left;
    font-weight: 700;
  }
  th:last-child { background: #e07a5f; }
  td {
    padding: 9px 14px;
    border-bottom: 1px solid #ddd;
    vertical-align: top;
  }
  tr:nth-child(even) td { background: rgba(0,0,0,0.03); }

  /* 목록 */
  ul, ol { padding-left: 1.3em; margin: 0.3em 0; }
  li { margin-bottom: 0.3em; }

  /* 강조 */
  strong { color: #2a2a2a; }

  /* 페이지 번호 */
  section::after {
    font-size: 0.75em;
    color: #e07a5f;
    font-weight: 700;
  }
---"""

# ── 파싱 ───────────────────────────────────────────────────────────────────────

def is_template(text: str) -> bool:
    return not text or any(hint in text for hint in TEMPLATE_HINTS)


def parse_showcase(path: Path) -> tuple[str, dict]:
    content = path.read_text(encoding="utf-8")

    # 이름 추출
    title_m = re.search(r"^#\s+(.+)", content, re.MULTILINE)
    raw = title_m.group(1).strip() if title_m else ""
    # "[이름] AI Camp2 Showcase" 형식 처리
    name_m = re.match(r"\[(.+?)\]", raw)
    name = name_m.group(1) if name_m else (raw.replace("AI Camp2 Showcase", "").strip() or path.parent.name)

    # ①~⑥ 섹션 추출
    sections: dict[str, str] = {}
    for num in "①②③④⑤⑥":
        pat = rf"## {re.escape(num)}\s+[^\n]+\n(.*?)(?=\n## [①②③④⑤⑥]|$)"
        m = re.search(pat, content, re.DOTALL)
        text = m.group(1).strip() if m else ""
        text = re.sub(r"\n---\s*$", "", text).strip()
        sections[num] = "" if is_template(text) else text

    return name, sections


# ── 슬라이드 생성 ──────────────────────────────────────────────────────────────

SPLIT_THRESHOLD = 600  # ④ 내용이 이 글자 수 초과 시 슬라이드 분할


def fallback(text: str, placeholder: str = "(작성 중)") -> str:
    return text if text else placeholder


def first_sentence(text: str) -> str:
    """텍스트에서 첫 번째 의미 있는 문장을 추출합니다."""
    for line in text.splitlines():
        line = line.strip().lstrip("#").strip()
        if line and not line.startswith(">"):
            return line[:130] + ("…" if len(line) > 130 else "")
    return ""


def slides_for_person(name: str, s: dict) -> list[str]:
    s1, s2, s3, s4, s5, s6 = [s.get(n, "") for n in "①②③④⑤⑥"]
    results = []

    # ── 1장: 이름 + 산출물 요약 ──────────────────────────────────────────────
    summary = first_sentence(s1) if s1 else "(작성 중)"
    results.append(
        f"# {name}\n\n"
        f"> {summary}\n\n"
        f"**문제**: {first_sentence(s1) or '(작성 중)'}\n\n"
        f"**해결 방향**: {first_sentence(s3) or '(작성 중)'}\n\n"
        f"**현재 구현**: {first_sentence(s4) or '(작성 중)'}"
    )

    # ── 2장: ①②③ ────────────────────────────────────────────────────────────
    results.append(
        f"# {name} — 문제와 해결 방향\n\n"
        f"## ① 해결하고 싶은 문제\n{fallback(s1)}\n\n"
        f"## ② 기존 방식의 병목\n{fallback(s2)}\n\n"
        f"## ③ 지향했던 방향성\n{fallback(s3)}"
    )

    # ── 3장: ④ 현재 구현 단계 (길면 분할) ───────────────────────────────────
    impl = fallback(s4)
    if s4 and len(s4) > SPLIT_THRESHOLD:
        paragraphs = [p.strip() for p in re.split(r"\n\n+", s4) if p.strip()]
        mid = max(1, len(paragraphs) // 2)
        part_a = "\n\n".join(paragraphs[:mid])
        part_b = "\n\n".join(paragraphs[mid:])
        results.append(f"# {name} — 현재 구현 단계 ①\n\n{part_a}")
        results.append(f"# {name} — 현재 구현 단계 ②\n\n{part_b}")
    else:
        results.append(f"# {name} — 현재 구현 단계\n\n{impl}")

    # ── 4장: ⑤⑥ ─────────────────────────────────────────────────────────────
    results.append(
        f"# {name} — 추후 과제 & 소감\n\n"
        f"## ⑤ 추후 과제\n{fallback(s5)}\n\n"
        f"> ⑥ {fallback(s6)}"
    )

    return results


# ── 전체 발표 마크다운 조합 ────────────────────────────────────────────────────

def build_presentation(persons: list[tuple[str, dict]]) -> str:
    chunks = [MARP_HEADER]

    # 섹션 구분 슬라이드
    chunks.append("<!-- _class: divider -->\n\n# 우리가 만든 것들")

    for name, sections in persons:
        slides = slides_for_person(name, sections)
        # 첫 슬라이드 앞에 시작 마커 삽입
        slides[0] = f"<!-- === 발표자: {name} === -->\n\n{slides[0]}"
        # 마지막 슬라이드 뒤에 종료 마커 삽입
        slides[-1] = f"{slides[-1]}\n\n<!-- === /발표자: {name} === -->"
        chunks.extend(slides)

    return "\n\n---\n\n".join(chunks) + "\n"


# ── 메인 ───────────────────────────────────────────────────────────────────────

def main():
    print("SHOWCASE.md 파일 수집 중...\n")

    if not SUBMISSIONS_DIR.exists():
        print(f"오류: {SUBMISSIONS_DIR} 폴더가 없습니다.")
        sys.exit(1)

    persons = []
    for person_dir in sorted(SUBMISSIONS_DIR.iterdir()):
        if not person_dir.is_dir():
            continue
        f = person_dir / "SHOWCASE.md"
        if not f.exists():
            continue
        name, sections = parse_showcase(f)
        filled = sum(1 for v in sections.values() if v)
        persons.append((name, sections))
        print(f"  ✓ {person_dir.name:<15} ({name})  — {filled}/6 항목 작성됨")

    if not persons:
        print("\n제출된 SHOWCASE.md 파일이 없습니다.")
        sys.exit(1)

    print(f"\n총 {len(persons)}명 파싱 완료. 슬라이드 생성 중...")

    SLIDES_DIR.mkdir(exist_ok=True)
    md = build_presentation(persons)
    OUTPUT_MD.write_text(md, encoding="utf-8")
    print(f"마크다운 생성: {OUTPUT_MD}")

    # Marp CLI로 PDF 변환
    try:
        subprocess.run(
            ["marp", str(OUTPUT_MD), "--pdf", "--allow-local-files", "-o", str(OUTPUT_PDF)],
            check=True,
            capture_output=True,
        )
        print(f"PDF 생성 완료: {OUTPUT_PDF}")
    except FileNotFoundError:
        print(
            "\n⚠️  marp CLI가 없습니다. 설치 후 아래 명령어를 실행하세요:\n"
            "    npm install -g @marp-team/marp-cli\n"
            f"    marp {OUTPUT_MD} --pdf --allow-local-files -o {OUTPUT_PDF}"
        )
    except subprocess.CalledProcessError as e:
        print(f"\n오류: {e.stderr.decode()}")


if __name__ == "__main__":
    main()
