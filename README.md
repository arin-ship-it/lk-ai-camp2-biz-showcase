# LK AI Camp 2기 — 사업팀 쇼케이스

사업팀 AI 캠프 2기 참가자들의 쇼케이스 자료를 모으는 곳입니다.

---

## 제출 순서

### 1단계 — 레포 클론

터미널(또는 Claude Code)에서 아래 명령어를 실행하세요.

```bash
git clone https://github.com/arin-ship-it/lk-ai-camp2-biz-showcase.git
cd lk-ai-camp2-biz-showcase
```

---

### 2단계 — 내 브랜치 만들기

`영문이름` 자리에 본인 영문 이름을 넣어주세요. (예: `nova`, `mj`)

```bash
git checkout -b 영문이름/showcase
```

---

### 3단계 — 내 폴더에 템플릿 복사

```bash
# Mac / Linux
cp template/SHOWCASE.md submissions/영문이름/SHOWCASE.md

# Windows
copy template\SHOWCASE.md submissions\영문이름\SHOWCASE.md
```

> `submissions/영문이름/` 폴더가 없으면 먼저 만들어주세요.
> Mac/Linux: `mkdir -p submissions/영문이름`  
> Windows: `mkdir submissions\영문이름`

---

### 4단계 — SHOWCASE.md 작성

`submissions/영문이름/SHOWCASE.md` 파일을 열어 아래 항목을 채워주세요.

| # | 항목 | 작성 가이드 |
|---|------|------------|
| ① | 해결하고 싶은 문제 | 어떤 업무가 불편하거나 비효율적이었나요? |
| ② | 기존 방식의 병목 | AI 쓰기 전에는 어떻게 했나요? 어디서 막혔나요? |
| ③ | 지향했던 방향성 | AI로 어떤 변화를 만들고 싶었나요? |
| ④ | 현재 구현 단계 | 지금까지 무엇을 만들었나요? 어느 정도 완성됐나요? |
| ⑤ | 추후 과제 | 아직 해결 못한 것, 더 발전시키고 싶은 것은? |
| ⑥ | 배운 점 / 소감 | 이번 캠프에서 느낀 점, 달라진 것 |

> 완벽하지 않아도 됩니다. 시도한 것 자체가 중요해요.  
> 스킬 파일, 스크린샷 등 추가 파일도 같은 폴더에 넣어도 OK.

---

### 5단계 — 커밋 & PR 올리기

```bash
git add submissions/영문이름/SHOWCASE.md
git commit -m "영문이름: AI Camp2 Showcase 제출"
git push origin 영문이름/showcase
```

푸시 후 터미널에 출력되는 링크를 클릭하거나,  
[GitHub 레포](https://github.com/arin-ship-it/lk-ai-camp2-biz-showcase/pulls)에서 **"Compare & pull request"** 버튼을 눌러 PR을 만들어주세요.

---

### 6단계 — 다른 팀원 제출물 보기

👉 [전체 PR 목록 보기](https://github.com/arin-ship-it/lk-ai-camp2-biz-showcase/pulls)

---

## 참고

- 막히면 DM 주세요
