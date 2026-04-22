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
---

---

<!-- _class: divider -->

# 우리가 만든 것들

---

<!-- === 발표자: Arin === -->

# Arin

> 배경) 로켓런칭 팀 내에서 매주 미팅을 진행하는데, 미팅 전 노션에 작업 현황을 업데이트해야 하는 작업이 필요했음.

**문제**: 배경) 로켓런칭 팀 내에서 매주 미팅을 진행하는데, 미팅 전 노션에 작업 현황을 업데이트해야 하는 작업이 필요했음.

**해결 방향**: 파편화된 커뮤니케이션 내용을 취합해 1) 디자인 진행 상황 리스트업 & 정리, 2) 디자인 타임라인을 짜주는 자동화를 만들자!

**현재 구현**: 1) 디자인 진행 상황 리스트업 & 정리

---

# Arin — 문제와 해결 방향

## ① 해결하고 싶은 문제
배경) 로켓런칭 팀 내에서 매주 미팅을 진행하는데, 미팅 전 노션에 작업 현황을 업데이트해야 하는 작업이 필요했음.

문제) 여러 곳에서 들어오는 디자인 요청을 취합, 정리하는 과정에서 약 30분가량의 시간 소요

## ② 기존 방식의 병목
1. 요청 경로 파편화: Slack 2개 채널 + 개인 DM + Notion 등 4개 채널에서 각각 수동 확인
2. 요청 형식의 다양성: 요청자마다 요청 형식이 달라 필요한 정보를 다시 확인하거나 정리해야 했음
3. 수동 복제 관리: 전주 Task list를 복제 → 차주 Task list로 이름, 내용 수정 → 공유하는 반복적인 수동 관리가 필요했음
4. 정보 누락: 피그마, 기획안, 고객사 클래스 링크 등의 정보를 누락해서 작성

## ③ 지향했던 방향성
파편화된 커뮤니케이션 내용을 취합해 1) 디자인 진행 상황 리스트업 & 정리, 2) 디자인 타임라인을 짜주는 자동화를 만들자!

---

# Arin — 현재 구현 단계

1) 디자인 진행 상황 리스트업 & 정리
- 5단계 워크플로우 설계 (수집 → 필터 → Human Review → Figma 플러그인 (페이지 생성) → Notion에 내용 정리 완료)
- 수집 스케줄: 월~금 9, 10, 11, 13, 14, 15, 16, 17, 18, 19시 정각 (오후 12시, 아린 연차 날 제외)
- 1차, 2차 시안 공유와 같은 Work Flow 날짜 자동 계산해서 작성
- 미완료 Task 자동 이월 로직

2) 디자인 타임라인 정리

---

# Arin — 추후 과제 & 소감

## ⑤ 추후 과제
추가적인 디자인 피드백 사항도 자동 취합해서 정리되도록 구현

> ⑥ 아직도 기본적인 개념에 대한 확립이 미흡하다고는 생각하지만, 그럼에도 불구하고 이런 나도 자동화 도구를 만들 수 있다는 뿌듯한 경험을 했습니다. 클로드는 내가 만들고자 하는 뚜렷한 작업 플로우와 디테일한 조건만 잘 제시해준다면 누구나 쉽게 만들 수 있겠다는 가능성도 체감할 수 있었습니다.

<!-- === /발표자: Arin === -->
