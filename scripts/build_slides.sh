#!/bin/bash
# SHOWCASE.md 파일들을 읽어 슬라이드 HTML을 빌드합니다.
#
# 사용:
#   bash scripts/build_slides.sh              ← 초안 생성 (generate_slides.py + Marp)
#   bash scripts/build_slides.sh --html-only  ← HTML만 재빌드 (수정 반영용, Marp만 실행)
#
# 의존성:
#   - python3
#   - node (npx 사용). 설치된 @marp-team/marp-cli가 있으면 그걸 쓰고, 없으면 npx로 자동 다운로드.

set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SLIDES_DIR="$REPO_ROOT/slides"

# ── Marp 실행기 선택 ────────────────────────────────────────
# 1) 전역 설치된 `marp` 명령이 있으면 사용
# 2) 없으면 npx 로 폴백 (인터넷 필요, 최초 1회 캐시)
if command -v marp >/dev/null 2>&1; then
  MARP=(marp)
else
  if ! command -v npx >/dev/null 2>&1; then
    echo "오류: marp 명령도 npx 도 없습니다. Node.js 를 먼저 설치해주세요." >&2
    exit 1
  fi
  MARP=(npx -y @marp-team/marp-cli@latest)
fi

# ── 1단계: 마크다운 생성 / CSS 최신화 ─────────────────────
if [ "$1" != "--html-only" ]; then
  echo "① SHOWCASE.md → slides/showcase.md 생성 중..."
  python3 "$REPO_ROOT/scripts/generate_slides.py"
else
  echo "① CSS 최신화 중 (--html-only 모드)..."
  python3 "$REPO_ROOT/scripts/generate_slides.py" --update-css
fi

# ── 2단계: HTML 빌드 ───────────────────────────────────────
echo "② Marp → slides/showcase.html 빌드 중..."
"${MARP[@]}" \
  "$SLIDES_DIR/showcase.md" \
  --html \
  --allow-local-files \
  -o "$SLIDES_DIR/showcase.html"

echo ""
echo "완료! 빌드된 파일: slides/showcase.html"
echo "GitHub Pages 링크: https://arin-ship-it.github.io/lk-ai-camp2-biz-showcase/slides/showcase.html"
