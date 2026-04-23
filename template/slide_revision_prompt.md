# 슬라이드 수정 요청 프롬프트

> **중요**: `slides/showcase.md` / `slides/showcase.html` 는 **자동 생성 파일**입니다.
> 직접 편집하지 말고, 항상 `submissions/[영문이름]/SHOWCASE.md` (원본)을 편집한 뒤 재빌드하세요.
> 생성물을 직접 편집하면 다음 전체 재빌드 시 변경 내용이 전부 사라집니다.

## 진행 절차

### 1. 영문 이름 확인
발표자의 영문 이름이 무엇인지 먼저 물어본다.
(예: Arin, Evan 등 `submissions/` 폴더명과 동일한 이름 — 대소문자 구분 없음)

### 2. 원본 파일 존재 확인
`submissions/[영문이름]/SHOWCASE.md` 파일이 있는지 대소문자 구분 없이 확인한다.
- 없으면 "해당 발표자의 SHOWCASE.md 를 찾을 수 없습니다. 이름을 다시 확인해주세요."라고 알리고 중단한다.

### 3. 수정 내용 확인
어떤 내용을 수정하고 싶은지 물어본다.

### 4. 원본 파일 수정
`submissions/[영문이름]/SHOWCASE.md` 의 해당 섹션(①~⑥)만 수정한다.
- **절대 `slides/showcase.md` 나 `slides/showcase.html` 를 직접 수정하지 않는다** (생성물이므로 재빌드 시 덮어써짐).
- `submissions/[영문이름]/` 하위 다른 파일(이미지 등)은 필요하면 추가·수정 가능.
- 그 외 다른 발표자의 파일은 읽거나 수정하지 않는다.

### 5. 커밋 전 최신화 (동시 수정 충돌 방지)
수정 완료 후 커밋 전에 origin/main을 rebase로 반영한다.
```bash
git fetch origin
git rebase origin/main
```
- rebase 충돌 발생 시: 본인 `submissions/[영문이름]/` 하위 파일의 내용을 기준으로 해결한다.
- push 후 거절(rejected)되면: git fetch → git rebase origin/main → push 재시도한다.

### 6. 확인 후 커밋
a. 변경된 내용(diff)을 보여주고 최종 확인을 받는다.
b. 확인되면 `bash scripts/build_slides.sh` (옵션 없이 전체 빌드) 실행해서 `slides/showcase.md`, `slides/showcase.html`, `slides/showcase.pdf` 를 재생성한다.
   - `--html-only` 는 **사용하지 않는다** — submissions 변경이 반영되지 않음.
c. `[영문이름]: 슬라이드 수정` 메시지로 커밋하고 main에 push한다.
   - 커밋에는 `submissions/[영문이름]/SHOWCASE.md` + 재빌드된 `slides/*` 가 함께 들어간다.
d. push 완료 후 슬라이드 링크를 알려준다.
   https://arin-ship-it.github.io/lk-ai-camp2-biz-showcase/slides/showcase.html
