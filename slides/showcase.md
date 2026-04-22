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
1. 헐킈
2. 뚱츄
3. 수동 복제 관리: 전주 Task list를 복제 → 차주 Task list로 이름, 내용 수정 → 공유하는 반복적인 수동 관리가 필요했음
4. 정보 누락: 피그마, 기획안, 고객사 클래스 링크 등의 정보를 누락해서 작성

## ③ 지향했던 방향성
파편화된 커뮤니케이션 내용을 취합해 1) 디자인 진행 상황 리스트업 & 정리, 2) 디자인 타임라인을 짜주는 자동화를 만들자!

---

# Arin — 현재 구현 단계

<p style="color:#CCC5B9; font-size:0.82em; margin:-0.6em 0 0.7em;">자동화 전·후 비교</p>

<div style="display:flex; gap:3px; margin-bottom:0.9em; font-size:0.68em;">
<div style="flex:1; background:#CCC5B9; clip-path:polygon(0 0,calc(100% - 10px) 0,100% 50%,calc(100% - 10px) 100%,0 100%); padding:8px 14px 8px 10px; color:#403D39; text-align:center;"><div style="font-size:0.75em; font-weight:700; opacity:0.6; margin-bottom:2px;">01</div><div style="font-weight:700;">수집</div></div>
<div style="flex:1; background:#CCC5B9; clip-path:polygon(10px 0,calc(100% - 10px) 0,100% 50%,calc(100% - 10px) 100%,0 100%,10px 50%); padding:8px 14px 8px 16px; color:#403D39; text-align:center;"><div style="font-size:0.75em; font-weight:700; opacity:0.6; margin-bottom:2px;">02</div><div style="font-weight:700;">필터</div></div>
<div style="flex:1; background:#CCC5B9; clip-path:polygon(10px 0,calc(100% - 10px) 0,100% 50%,calc(100% - 10px) 100%,0 100%,10px 50%); padding:8px 14px 8px 16px; color:#403D39; text-align:center;"><div style="font-size:0.75em; font-weight:700; opacity:0.6; margin-bottom:2px;">03</div><div style="font-weight:700;">Human<br>Review</div></div>
<div style="flex:1; background:#403D39; clip-path:polygon(10px 0,calc(100% - 10px) 0,100% 50%,calc(100% - 10px) 100%,0 100%,10px 50%); padding:8px 14px 8px 16px; color:#fff; text-align:center;"><div style="font-size:0.75em; font-weight:700; opacity:0.7; margin-bottom:2px;">04</div><div style="font-weight:700;">Figma<br>플러그인</div></div>
<div style="flex:1; background:#e07a5f; clip-path:polygon(10px 0,100% 0,100% 100%,0 100%,10px 50%); padding:8px 14px 8px 16px; color:#fff; text-align:center;"><div style="font-size:0.75em; font-weight:700; opacity:0.8; margin-bottom:2px;">05</div><div style="font-weight:700;">Notion<br>정리</div></div>
</div>

<table>
<thead><tr>
<th>기존 방식</th>
<th style="background:#CCC5B9; color:#403D39; text-align:center; width:12%;">구분</th>
<th>자동화 후</th>
</tr></thead>
<tbody>
<tr><td>4개 채널 각각 수동 확인 (~30분/주)</td><td style="text-align:center; font-weight:700; color:#403D39;">수집</td><td>월~금 9~19시 매시 정각 자동 수집</td></tr>
<tr><td>요청 형식 불통일 → 정보 재확인 필요</td><td style="text-align:center; font-weight:700; color:#403D39;">정제</td><td>필터 + Human Review 단계로 정리</td></tr>
<tr><td>전주 Task 수동 복제·수정 반복</td><td style="text-align:center; font-weight:700; color:#403D39;">이월</td><td>미완료 Task 자동 이월</td></tr>
<tr><td>시안 공유 날짜 수동 계산</td><td style="text-align:center; font-weight:700; color:#403D39;">날짜</td><td>1차·2차 시안 날짜 자동 산출</td></tr>
</tbody>
</table>

---

# Arin — 추후 과제 & 소감

<p style="color:#CCC5B9; font-size:0.82em; margin:-0.6em 0 1em;">앞으로 발전시키고 싶은 것, 그리고 이번 캠프를 통해 달라진 것</p>

<p style="color:#e07a5f; font-size:0.78em; font-weight:700; margin:0 0 0.3em;">⑤ 추후 과제</p>

디자인 **피드백 사항**도 자동 취합하여 Notion 정리까지 이어지도록 확장

<hr style="border:none; border-top:1px solid #CCC5B9; margin:0.9em 0;">

<p style="color:#e07a5f; font-size:0.78em; font-weight:700; margin:0 0 0.3em;">⑥ 소감</p>

**"이런 나도 자동화 도구를 만들 수 있다"**는 뿌듯한 경험이었습니다.
클로드는 뚜렷한 작업 플로우와 디테일한 조건만 잘 제시하면 누구나 쉽게 만들 수 있겠다는 가능성을 체감했습니다.

<!-- === /발표자: Arin === -->
