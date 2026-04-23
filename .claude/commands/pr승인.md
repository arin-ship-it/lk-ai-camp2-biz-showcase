---
description: 최초 발표자 PR 자동 처리 (merge → pull → submissions 전체 재빌드 → 커밋·푸시)
argument-hint: "[PR번호] (생략 시 열린 PR 중 하나 선택)"
---

**새 발표자가 `submissions/이름/` 폴더를 추가**한 최초 PR을 승인 처리합니다.
(기존 발표자의 HTML/MD 수정 PR이면 대신 `/수정승인` 을 안내하고 중단하세요.)

인자: `$ARGUMENTS` — 비어 있으면 `gh pr list` 로 열린 PR을 보여주고 사용자에게 확인받으세요.

## 아래 4단계를 순서대로 실행

### 1. PR 머지
- `gh pr list` 로 열린 PR 확인
- 대상 PR의 변경 파일을 `gh pr view <번호> --json files -q '.files[].path'` 로 확인
- **submissions/ 경로 변경이 없으면 중단**하고 `/수정승인 <번호>` 를 안내
- 조건을 통과하면 `gh pr merge <번호> --merge` 로 머지 (squash 금지)

### 2. origin/main pull
```bash
git pull origin main
```

### 3. HTML 전체 재빌드
- submissions/ 로부터 showcase.md 를 재생성해야 하므로 **전체 빌드** 실행 (옵션 없이)
```bash
bash scripts/build_slides.sh
```
- 스크립트가 `slides/showcase.md` 와 `slides/showcase.html` 를 모두 갱신함

### 4. 커밋 & 푸시
- 추가된 발표자명을 `ls submissions/` diff 또는 커밋 메시지에서 추출
- 변경되는 파일: `slides/showcase.md`, `slides/showcase.html` (`showcase.pdf` 는 변경되지 않음 — 무시)
- 한국어 커밋 메시지: `slides 재빌드 — <발표자명> 쇼케이스 추가`
- HEREDOC 으로 Co-Authored-By 포함하여 commit
- `git push origin main`
- 완료 후 GitHub Pages 링크 안내: https://arin-ship-it.github.io/lk-ai-camp2-biz-showcase/slides/showcase.html

## 실패/중단 조건
- 대상 PR이 submissions/ 를 수정하지 않음 → `/수정승인` 안내 후 중단
- merge conflict 발생 → 중단하고 사용자에게 상황 보고
- 빌드 실패 → 중단 (스크립트 stderr 그대로 전달)
- `git push` 실패 (예: non-fast-forward) → `--force` 쓰지 말고 중단 후 보고 (글로벌 CLAUDE.md 규칙)
