#!/bin/bash
# SHOWCASE.md 파일들을 읽어 슬라이드 HTML을 빌드합니다.
# 사용: bash scripts/build_slides.sh

set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SLIDES_DIR="$REPO_ROOT/slides"
MARP_NODE="/opt/homebrew/opt/node@22/bin/node"
MARP_CLI="/opt/homebrew/lib/node_modules/@marp-team/marp-cli/marp-cli.js"

echo "① SHOWCASE.md → slides/showcase.md 생성 중..."
python3 "$REPO_ROOT/scripts/generate_slides.py"

echo "② Marp CLI → slides/showcase.html 빌드 중..."
"$MARP_NODE" "$MARP_CLI" \
  "$SLIDES_DIR/showcase.md" \
  --html \
  --allow-local-files \
  -o "$SLIDES_DIR/showcase.html"

echo ""
echo "완료! 빌드된 파일: slides/showcase.html"
echo "GitHub Pages 링크: https://arin-ship-it.github.io/lk-ai-camp2-biz-showcase/slides/showcase.html"
