---
marp: true
paginate: true
html: true
header: ''
style: |
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');

  /* ─── 디자인 토큰 ─────────────────────────────── */
  section {
    /* 팔레트 */
    --c-cream:       #fdf8ec;
    --c-cream-band:  #ece7da;
    --c-cream-soft:  #e5ddd0;
    --c-ink:         #252422;
    --c-ink-deep:    #1a1917;
    --c-ink-mid:     #403D39;
    --c-ink-dim:     #999999;
    --c-ink-muted:   #888888;
    --c-line:        #CCC5B9;
    --c-accent:      #e07a5f;
    --c-accent-soft: rgba(224,122,95,0.10);

    /* 테마 (기본 = 라이트) */
    --c-bg:        var(--c-cream);
    --c-fg:        var(--c-ink);
    --c-band-bg:   var(--c-cream-band);
    --c-band-fg:   rgba(37,36,34,0.62);
    --c-footer-fg: rgba(37,36,34,0.42);
    --c-corner:    var(--c-ink);

    /* 레이아웃 */
    --pad-x:       72px;
    --pad-top:     72px;
    --pad-bot:     56px;
    --band-h:      38px;
    --corner-size: 52px;
  }

  /* ─── 다크/디바이더 테마 토큰 재정의 ─────────── */
  section.dark, section.divider {
    --c-bg:        var(--c-ink);
    --c-fg:        #ffffff;
    --c-band-bg:   var(--c-ink-deep);
    --c-band-fg:   rgba(255,255,255,0.72);
    --c-footer-fg: rgba(255,255,255,0.35);
    --c-corner:    var(--c-accent);
  }

  /* ─── 기본 섹션 ─────────────────────────────── */
  section {
    background: var(--c-bg);
    color: var(--c-fg);
    font-family: 'Noto Sans KR', 'Apple SD Gothic Neo', sans-serif;
    padding: var(--pad-top) var(--pad-x) var(--pad-bot);
    font-size: 20px;
    line-height: 1.65;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    position: relative;
  }
  section.divider { justify-content: center; }
  section.cover   { justify-content: center; align-items: center; text-align: center; }

  /* ─── 헤더바 (Marp <header>) ─────────────────── */
  header {
    position: absolute;
    top: 0; left: 0; right: 0;
    height: var(--band-h);
    margin: 0;
    background: var(--c-band-bg);
    color: var(--c-band-fg);
    font-size: 11px;
    font-weight: 400;
    line-height: var(--band-h);
    padding: 0 20px;
    letter-spacing: 0.02em;
    white-space: nowrap;
    overflow: hidden;
    text-align: left;
  }
  header strong {
    font-weight: 700;
    color: var(--c-band-fg);
    margin-right: 4px;
  }

  /* ─── 페이지 번호 (Marp pagination) ─────────── */
  section::after {
    position: absolute;
    top: 0; right: 20px;
    height: var(--band-h);
    line-height: var(--band-h);
    font-size: 11px;
    font-weight: 400;
    color: var(--c-footer-fg);
    background: transparent;
  }

  /* ─── 푸터 + 코너 스퀘어 ────────────────────── */
  .slide-footer {
    position: absolute;
    bottom: 16px; left: 24px;
    font-size: 11px;
    font-weight: 400;
    color: var(--c-footer-fg);
  }
  .corner-sq {
    position: absolute;
    bottom: 0; right: 0;
    width: var(--corner-size);
    height: var(--corner-size);
    background: var(--c-corner);
  }

  /* ─── 타이포 ──────────────────────────────────── */
  h1 {
    font-size: 1.75em;
    font-weight: 900;
    line-height: 1.15;
    margin: 0 0 0.15em;
    color: inherit;
  }
  h2 {
    font-size: 0.95em;
    font-weight: 700;
    margin: 0.8em 0 0.2em;
    letter-spacing: -0.01em;
    color: inherit;
  }
  strong { font-weight: 900; color: inherit; }

  .slide-sub {
    font-size: 0.72em;
    color: var(--c-ink-dim);
    margin: 0 0 1em;
    line-height: 1.4;
  }

  .sec-label {
    color: var(--c-accent);
    font-size: 0.72em;
    font-weight: 700;
    margin: 0.9em 0 0.25em;
  }
  .sec-label:first-child { margin-top: 0; }

  .sec-divider {
    border: none;
    border-top: 1px solid var(--c-line);
    margin: 0.7em 0;
  }

  /* ─── 인용구 ─────────────────────────────────── */
  blockquote {
    background: var(--c-accent-soft);
    border-left: 4px solid var(--c-accent);
    padding: 10px 16px;
    margin: 10px 0;
    border-radius: 0 4px 4px 0;
    font-size: 0.88em;
    color: #555;
    font-style: normal;
  }
  blockquote p { margin: 0; }

  /* ─── 목록 ───────────────────────────────────── */
  ul, ol { padding-left: 1.3em; margin: 0.2em 0; }
  li { margin-bottom: 0.28em; }

  /* ─── 커버 슬라이드 ──────────────────────────── */
  .cover-title {
    font-size: 2.3em;
    font-weight: 900;
    line-height: 1.2;
    color: var(--c-ink);
    margin: 0 0 0.4em;
  }
  .cover-presenter {
    font-size: 0.8em;
    color: var(--c-ink-muted);
    margin: 0 0 1.2em;
  }
  .cover-presenter strong { color: var(--c-ink); font-weight: 700; }
  .cover-tags {
    display: flex;
    gap: 10px;
    justify-content: center;
    flex-wrap: wrap;
  }
  .tag {
    display: inline-block;
    border: 1.5px solid var(--c-accent);
    background: var(--c-accent-soft);
    color: var(--c-accent);
    font-size: 0.68em;
    font-weight: 700;
    padding: 5px 14px;
    border-radius: 999px;
  }

  /* ─── 2열 레이아웃 (문제 슬라이드) ──────────── */
  .two-col {
    display: flex;
    gap: 48px;
    flex: 1;
    min-height: 0;
  }
  .col-l, .col-r { flex: 1; display: flex; flex-direction: column; }

  /* ─── 기본 표 ────────────────────────────────── */
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.82em;
    margin-top: 0.3em;
  }
  th {
    background: var(--c-ink-mid);
    color: #fff;
    padding: 9px 14px;
    text-align: left;
    font-weight: 700;
  }
  th:last-child { background: var(--c-accent); }
  td {
    padding: 8px 14px;
    border-bottom: 1px solid #e0d8cc;
    vertical-align: top;
  }
  tr:nth-child(even) td { background: rgba(0,0,0,0.025); }

  /* ─── 펜타곤 플로우 (구현 슬라이드) ─────────── */
  .flow-wrap {
    display: flex;
    height: 68px;
    margin-bottom: 16px;
    flex-shrink: 0;
  }
  .flow-step {
    flex: 1;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 0 8px 0 20px;
    margin-right: -14px;
    color: #fff;
    font-size: 0.6em;
    font-weight: 700;
    line-height: 1.35;
    clip-path: polygon(0 0, calc(100% - 14px) 0, 100% 50%, calc(100% - 14px) 100%, 0 100%, 14px 50%);
  }
  .flow-step:first-child {
    clip-path: polygon(0 0, calc(100% - 14px) 0, 100% 50%, calc(100% - 14px) 100%, 0 100%);
    padding-left: 14px;
  }
  .flow-step:last-child {
    clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%, 14px 50%);
    margin-right: 0;
  }
  .flow-step:nth-child(1) { background: #d6cfca; color: var(--c-ink-mid); z-index: 5; }
  .flow-step:nth-child(2) { background: #c4bdb7; color: var(--c-ink-mid); z-index: 4; }
  .flow-step:nth-child(3) { background: #a09890; z-index: 3; }
  .flow-step:nth-child(4) { background: var(--c-ink-mid); z-index: 2; }
  .flow-step:nth-child(5) { background: var(--c-accent); z-index: 1; }
  .flow-num {
    font-size: 0.85em;
    font-weight: 400;
    opacity: 0.75;
    margin-bottom: 2px;
  }

  /* ─── 비교표 (구현 슬라이드) ────────────────── */
  .cmp-table { width: 100%; border-collapse: collapse; font-size: 0.78em; }
  .cmp-table th { padding: 10px 14px; text-align: center; font-weight: 700; font-size: 0.9em; }
  .cmp-table th.h-left  { background: var(--c-ink-mid); color: #fff; }
  .cmp-table th.h-mid   { background: var(--c-line); color: var(--c-ink); width: 16%; font-size: 0.8em; }
  .cmp-table th.h-right { background: var(--c-accent); color: #fff; }
  .cmp-table td {
    padding: 9px 14px;
    text-align: center;
    color: var(--c-ink-mid);
    border-bottom: 1px solid #ddd5c8;
    vertical-align: middle;
  }
  .cmp-table tr:nth-child(even) td { background: rgba(0,0,0,0.02); }
  .cmp-table td.m-mid { background: #ebe5de; color: var(--c-ink-muted); font-size: 0.82em; }
---

<!--
  ⚠️ 자동 생성 파일 — 직접 편집 금지
  이 파일은 scripts/generate_slides.py 가 submissions/*/SHOWCASE.md 로부터 생성합니다.
  내용 수정은 submissions/<영문이름>/SHOWCASE.md 를 편집한 뒤,
  프로젝트 루트에서 `bash scripts/build_slides.sh` 를 실행해 재빌드하세요.
  이 파일을 직접 편집하면 다음 빌드에서 변경사항이 전부 사라집니다.
-->

<!-- _class: divider -->
<!-- _header: "**EVAN** · LK AI Camp 2기" -->

# 우리가 만든 것들

<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

<!-- header: "**EVAN** · LK AI Camp 2기" -->
<!-- === 발표자: Evan === -->

<!-- _class: cover -->

<div class="cover-title">Evan의<br>자동화 도구</div>
<p class="cover-presenter"><strong>발표자</strong> 콘텐츠 디자이너 &nbsp;｜&nbsp; Evan</p>
<div class="cover-tags"><span class="tag">신규 고객 온보딩 자동화</span><span class="tag">신규 온보딩 자동화: 미진행</span></div>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 문제와 해결 방향
<p class="slide-sub">신규 고객 온보딩 자동화</p>

<div class="two-col">
  <div class="col-l"><p class="sec-label">① 문제 상황</p><ul><li>신규 고객 온보딩 자동화</li><li>고객사 상품 세일즈(무료 강의안, 상페, 모객 콘텐츠, 모객용 자료 등) 기획 자동화</li><li>통화 녹음 및 미팅 기록 자동화 (정리 요약 & 노션 DB에 텍스트데이터 입력까지)</li><li>신규 주제 도메인 이해도 높이기 (학습 튜터)</li></ul><hr class="sec-divider"><p class="sec-label">③ 지향했던 방향성</p><ul><li>신규 고객 온보딩 자동화: 부트캠프 Day 4같이 고객사 개인이 이용하는 LLM에 코드 입력 시 구현되는 구조</li><li>고객사 상품 세일즈 기획 자동화: 핵심 논리 방법론, 자료 업데이트 및 정교화 → 메모리 과다 이슈가 있어서 최근 통합 스킬에서 세부 개별 스킬로 전환해서 효율화 과정</li><li>통화 녹음 및 미팅 기록 자동화: 녹음파일 자동 전달 백그라운드 앱을 바이브코딩으로 생성하려 했으나, 현재 MacroDroid(구글 플레이스토어 앱)로 자동화 중</li><li>신규 주제 도메인 이해도 높이기: 라이브러리 형태로 주제별 세부 스킬 분리 및 관리 (지속 업데이트) + 교육학 근거로 빠르게 학습할 수 있는 시스템 프롬프트 제작하여 설정 예정</li></ul></div>
  <div class="col-r"><p class="sec-label">② 기존 방식의 병목</p><table><thead><tr><th>병목 유형</th><th>구체적 문제</th></tr></thead><tbody><tr><td>병목</td><td>온보딩 → 개별 온/오프 미팅 외에 다른 선택지 없음 (가이드 문서 전달해봤으나, 불가 확인 / 대안은 사람</td></tr><tr><td>병목</td><td>고객사 상품 세일즈 기획 자동화 → 매번 새롭게 기획, 문서화, 미팅을 통해 전달</td></tr><tr><td>기록 자동화</td><td>매번 직접 기록</td></tr><tr><td>병목</td><td>신규 주제 도메인 이해도: 파편화된 정보를 리서치하고 취합하는 형태</td></tr></tbody></table></div>
</div>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 현재 구현 단계
<p class="slide-sub">자동화 전·후 비교</p>

<table class="cmp-table"><thead><tr><th class="h-left">기존 방식</th><th class="h-mid">구분</th><th class="h-right">자동화 후</th></tr></thead><tbody><tr><td>온보딩 → 개별 온/오프 미팅 외에 다른 선택지 없음 (가이드 문서 전달해봤으나, 불가 확인 / 대…</td><td class="m-mid">비교</td><td>신규 온보딩 자동화: 미진행</td></tr><tr><td>고객사 상품 세일즈 기획 자동화 → 매번 새롭게 기획, 문서화, 미팅을 통해 전달</td><td class="m-mid">비교</td><td>상품 세일즈 기획 자동화: 일부 진행 중 (무료 강의안 기획부터)</td></tr><tr><td>매번 직접 기록</td><td class="m-mid">기록 자동화</td><td>기록 자동화: 아직 녹음 파일을 구글 드라이브로 자동 업로드하는 과정 해결 중</td></tr><tr><td>신규 주제 도메인 이해도: 파편화된 정보를 리서치하고 취합하는 형태</td><td class="m-mid">비교</td><td>신규 주제 학습 튜터: 미진행</td></tr></tbody></table>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 추후 과제 &amp; 소감
<p class="slide-sub">앞으로 발전시키고 싶은 것, 그리고 이번 캠프를 통해 달라진 것</p>

<p class="sec-label">⑤ 추후 과제</p>
<ul><li>위 에이전트 완성 및 현재 진행 단계에서의 문제 해결</li></ul>
<hr class="sec-divider">
<p class="sec-label">⑥ 소감</p>
<p>항상 AI는 미지의 영역처럼 막연히 느껴졌는데, AI의 작동 구조와 운영되는 방식에 대해서 배울 수 있어서 너무 좋았습니다. AI에 대해 배운 기틀이 잘 마련된 것 같고, 배운 내용을 기준으로 계속 업데이트해보겠습니다!</p>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

<!-- === /발표자: Evan === -->

---

<!-- header: "**ARIN** · LK AI Camp 2기" -->
<!-- === 발표자: Arin === -->

<!-- _class: cover -->

<div class="cover-title">Arin의<br>자동화 도구</div>
<p class="cover-presenter"><strong>발표자</strong> 콘텐츠 디자이너 &nbsp;｜&nbsp; Arin</p>
<div class="cover-tags"><span class="tag">주 30분 → 0분</span><span class="tag">4단계 자동화 워크플로우</span><span class="tag">디자인 진행 상황 리스트업 & 정리</span></div>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 문제와 해결 방향
<p class="slide-sub">배경) 로켓런칭 팀 내에서 매주 미팅을 진행하는데, 미팅 전 노션에 작업 현황을 업데이트해야 하는 작업이 필요했음.</p>

<div class="two-col">
  <div class="col-l"><p class="sec-label">① 문제 상황</p><p>배경) 로켓런칭 팀 내에서 매주 미팅을 진행하는데, 미팅 전 노션에 작업 현황을 업데이트해야 하는 작업이 필요했음.</p>
<p>문제) 여러 곳에서 들어오는 디자인 요청을 취합, 정리하는 과정에서 약 30분가량의 시간 소요</p><hr class="sec-divider"><p class="sec-label">③ 지향했던 방향성</p><p>파편화된 커뮤니케이션 내용을 취합해 1) 디자인 진행 상황 리스트업 & 정리, 2) 디자인 타임라인을 짜주는 자동화를 만들자!</p></div>
  <div class="col-r"><p class="sec-label">② 기존 방식의 병목</p><table><thead><tr><th>병목 유형</th><th>구체적 문제</th></tr></thead><tbody><tr><td>요청 경로 파편화</td><td>Slack 2개 채널 + 개인 DM + Notion 등 4개 채널에서 각각 수동 확인</td></tr><tr><td>요청 형식의 다양성</td><td>요청자마다 요청 형식이 달라 필요한 정보를 다시 확인하거나 정리해야 했음</td></tr><tr><td>수동 복제 관리</td><td>전주 Task list를 복제 → 차주 Task list로 이름, 내용 수정 → 공유하는 반복적인 수동 관리</td></tr><tr><td>정보 누락</td><td>피그마, 기획안, 고객사 클래스 링크 등의 정보를 누락해서 작성</td></tr></tbody></table></div>
</div>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 현재 구현 단계
<p class="slide-sub">자동화 전·후 비교</p>

<div class="flow-wrap"><div class="flow-step"><div class="flow-num">01</div>수집</div><div class="flow-step"><div class="flow-num">02</div>필터</div><div class="flow-step"><div class="flow-num">03</div>Human</div><div class="flow-step"><div class="flow-num">04</div>Figma 플러그인</div></div>
<table class="cmp-table"><thead><tr><th class="h-left">기존 방식</th><th class="h-mid">구분</th><th class="h-right">자동화 후</th></tr></thead><tbody><tr><td>Slack 2개 채널 + 개인 DM + Notion 등 4개 채널에서 각각 수동 확인</td><td class="m-mid">요청 경로 파편화</td><td>디자인 진행 상황 리스트업 & 정리</td></tr><tr><td>요청자마다 요청 형식이 달라 필요한 정보를 다시 확인하거나 정리해야 했음</td><td class="m-mid">요청 형식의 다양성</td><td>수집 스케줄: 월~금 9, 10, 11, 13, 14, 15, 16, 17, 18, 19시 정각 (…</td></tr><tr><td>전주 Task list를 복제 → 차주 Task list로 이름, 내용 수정 → 공유하는 반복적인 …</td><td class="m-mid">수동 복제 관리</td><td>1차, 2차 시안 공유와 같은 Work Flow 날짜 자동 계산해서 작성</td></tr><tr><td>피그마, 기획안, 고객사 클래스 링크 등의 정보를 누락해서 작성</td><td class="m-mid">정보 누락</td><td>미완료 Task 자동 이월 로직</td></tr><tr><td>—</td><td class="m-mid">비교</td><td>디자인 타임라인 정리</td></tr></tbody></table>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 추후 과제 &amp; 소감
<p class="slide-sub">앞으로 발전시키고 싶은 것, 그리고 이번 캠프를 통해 달라진 것</p>

<p class="sec-label">⑤ 추후 과제</p>
<p>추가적인 디자인 피드백 사항도 자동 취합해서 정리되도록 구현</p>
<hr class="sec-divider">
<p class="sec-label">⑥ 소감</p>
<p>아직도 기본적인 개념에 대한 확립이 미흡하다고는 생각하지만, 그럼에도 불구하고 이런 나도 자동화 도구를 만들 수 있다는 뿌듯한 경험을 했습니다. 클로드는 내가 만들고자 하는 뚜렷한 작업 플로우와 디테일한 조건만 잘 제시해준다면 누구나 쉽게 만들 수 있겠다는 가능성도 체감할 수 있었습니다.</p>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

<!-- === /발표자: Arin === -->

---

<!-- header: "**CHAEEUN JANG** · LK AI Camp 2기" -->
<!-- === 발표자: Chaeeun Jang === -->

<!-- _class: cover -->

<div class="cover-title">Chaeeun Jang의<br>자동화 도구</div>
<p class="cover-presenter"><strong>발표자</strong> 콘텐츠 디자이너 &nbsp;｜&nbsp; Chaeeun Jang</p>
<div class="cover-tags"><span class="tag">매일 상시퍼널 클래스의 신청자 목</span></div>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 문제와 해결 방향
<p class="slide-sub">매일 상시퍼널 클래스의 신청자 목록을 다운받아 신청자 수·완강률·결제 전환율 등을 직접 계산</p>

<div class="two-col">
  <div class="col-l"><p class="sec-label">① 문제 상황</p><ul><li>매일 상시퍼널 클래스의 신청자 목록을 다운받아 신청자 수·완강률·결제 전환율 등을 직접 계산</li><li>고객사에 공유 보고서가 필요한 경우 일자별·주차별·월별로 정리해 노션에 옮기는 작업 반복</li><li>상시퍼널을 적용하는 고객사가 빠르게 늘어남에 따라 소요 시간이 크게 늘 것으로 예상됨</li></ul><hr class="sec-divider"><p class="sec-label">③ 지향했던 방향성</p><p>파일을 폴더에 드롭하고 "inbox 처리해줘" 한 마디면 분석·DB 기록·보고서 생성까지 자동 완료. 숫자가 아닌 인사이트에만 집중할 수 있는 구조.</p></div>
  <div class="col-r"><p class="sec-label">② 기존 방식의 병목</p><table><thead><tr><th>병목 유형</th><th>구체적 문제</th></tr></thead><tbody><tr><td>병목</td><td>매번 수동으로 카운트 및 분석 → 일자별 추적 어려움</td></tr><tr><td>병목</td><td>파트별 이탈 시각화 불가</td></tr><tr><td>병목</td><td>고객사의 이해를 도울 차트 등 시각화 어려움</td></tr><tr><td>병목</td><td>결제 전환율 매칭 — 결제자 시트와 대조하며 추적</td></tr></tbody></table></div>
</div>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 현재 구현 단계
<p class="slide-sub">자동화 전·후 비교</p>

<table class="cmp-table"><thead><tr><th class="h-left">기존 방식</th><th class="h-mid">구분</th><th class="h-right">자동화 후</th></tr></thead><tbody><tr><td>수동 집계</td><td class="m-mid">비교</td><td>자동 분석+매칭</td></tr><tr><td>수동 복붙</td><td class="m-mid">비교</td><td>Notion 자동 기록</td></tr><tr><td>데일리 추적 불가</td><td class="m-mid">비교</td><td>Google Sheets 누적 업데이트</td></tr></tbody></table>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 추후 과제 &amp; 소감
<p class="slide-sub">앞으로 발전시키고 싶은 것, 그리고 이번 캠프를 통해 달라진 것</p>

<p class="sec-label">⑤ 추후 과제</p>
<ul><li>여러 파일 동시 처리 안정성 검증</li><li>인사이트 자동 생성 고도화 — 패턴 감지 및 액션 우선순위 자동 판단</li></ul>
<hr class="sec-divider">
<p class="sec-label">⑥ 소감</p>
<p>개발 경험 없이도 실제로 동작하는 자동화 시스템을 만들 수 있다는 게 가장 큰 발견이었습니다. 세팅을 마치고 나니 업무 효율이 크게 높아졌고, 고객사 보고서 퀄리티도 올라갔습니다. 진작 시도해볼 걸 — 앞으로는 단순 반복은 Claude에 맡기고, 나는 생각하는 일에 집중하려 합니다.</p>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

<!-- === /발표자: Chaeeun Jang === -->

---

<!-- header: "**MJSHIN** · LK AI Camp 2기" -->
<!-- === 발표자: mjshin === -->

<!-- _class: cover -->

<div class="cover-title">mjshin의<br>자동화 도구</div>
<p class="cover-presenter"><strong>발표자</strong> 콘텐츠 디자이너 &nbsp;｜&nbsp; mjshin</p>
<div class="cover-tags"><span class="tag">매니저 1명이 담당할 수 있는 고</span><span class="tag">3단계 자동화 워크플로우</span><span class="tag">**질문 플로우 설계** — 실제 매</span></div>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 문제와 해결 방향
<p class="slide-sub">매니저 1명이 담당할 수 있는 고객사 수는 리소스에 의해 결정된다. 문제는 매 고객사마다 두 단계가 리소스를 반복적으로 소모하고 있었다는 것.</p>

<div class="two-col">
  <div class="col-l"><p class="sec-label">① 문제 상황</p><p>매니저 1명이 담당할 수 있는 고객사 수는 리소스에 의해 결정된다. 문제는 매 고객사마다 두 단계가 리소스를 반복적으로 소모하고 있었다는 것.</p>
<p><strong>① 소통 단계</strong> — 브랜딩·퍼널·무료/유료 상품 기획에 필요한 정보를 수집하기 위한 반복 커뮤니케이션</p>
<p><strong>② 기획 단계</strong> — 수집한 정보를 실제 기획물로 변환하는 작업</p>
<p>이 두 단계를 자동화해 리소스를 확보하면, 더 많은 고객사를 런칭하면서도 진짜 차이를 만드는 기획 완성도 작업에 집중할 수 있다.</p><hr class="sec-divider"><p class="sec-label">③ 지향했던 방향성</p><p>목표는 하나였다 — 고객사 소통과 기획 전체에 드는 시간을 구조적으로 줄이는 것. 이를 위해 네 가지 방향을 지향했다.</p>
<p><strong>① 인풋 최적화</strong> — 기획 경험 기반 핵심 질문을 체계화하고, AI 시뮬레이션으로 꼬리질문을 보완. 1회 미팅으로 필요한 정보를 모두 수집하는 구조 설계</p>
<p><strong>② 기획 자동화</strong> — 시장조사·경쟁사 분석·차별화 포인트 도출에 걸리는 시간을 AI로 단축. 현실적인 시장 진입 전략을 빠르게 구축</p>
<p><strong>③ 산출물 자동화</strong> — 확정된 기획 방향을 기반으로 광고·무료 상품 페이지·유료 상품 페이지·강의 구성 4가지 산출물의 구조를 자동으로 생성</p>
<p><strong>④ 얼라인 간소화</strong> — 구두 미팅을 1회 핵심 미팅으로 압축하고, 나머지 방향 확인은 비동기로 마무리. 반복 미팅 없이도 기획 전체 방향을 확정하는 구조</p></div>
  <div class="col-r"><p class="sec-label">② 기존 방식의 병목</p><p>병목은 두 가지였다 — 순수 기획 시간 그 자체, 그리고 매 단계마다 반복되는 고객사 얼라인. 이 두 가지가 맞물리면서 기획 1건에 미팅 2~3회·최소 7일이 구조적으로 고정됐다.</p>
<p>| 회차 | 미팅 목적 | 미팅 전 준비 |</p>
<p>|------|-----------|-------------|</p>
<p>| 1차 | 고객사 스토리 파악 | 인터뷰 설계 |</p>
<p>| 2차 | 퍼널 전략 제안 얼라인 | 시장조사 + 크리에이티브 기획 |</p>
<p>| 3차 | 무료/유료 상품 + 광고 방향 확정 | 기획물 재작성 + 검토 |</p>
<p>각 미팅 사이마다 시장조사 → 크리에이티브 고민 → 기획 → 고객사 재확인 사이클이 반복되면서, 놓치는 것 없이 맞추려 할수록 시간이 선형으로 늘어나는 구조였다.</p></div>
</div>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 현재 구현 단계
<p class="slide-sub">자동화 전·후 비교</p>

<div class="flow-wrap"><div class="flow-step"><div class="flow-num">01</div>역설 5가지 유형</div><div class="flow-step"><div class="flow-num">02</div>내부자 지식</div><div class="flow-step"><div class="flow-num">03</div>렌즈 명명</div></div>
<table class="cmp-table"><thead><tr><th class="h-left">기존 방식</th><th class="h-mid">구분</th><th class="h-right">자동화 후</th></tr></thead><tbody><tr><td>—</td><td class="m-mid">비교</td><td>**질문 플로우 설계** — 실제 매니저 킥오프 인터뷰를 역분석해 추출한 핵심 질문 7개 + 꼬리질…</td></tr><tr><td>—</td><td class="m-mid">비교</td><td>**단독성 검증** — 발굴된 후보가 이 고객사만의 것인지 자동 검증하는 3가지 필터 내장</td></tr><tr><td>—</td><td class="m-mid">비교</td><td>**Streamlit 프로토타입** — 모바일 최적화 인터페이스로 실제 입력~결과 확인 가능한 앱 …</td></tr></tbody></table>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 추후 과제 &amp; 소감
<p class="slide-sub">앞으로 발전시키고 싶은 것, 그리고 이번 캠프를 통해 달라진 것</p>

<p class="sec-label">⑤ 추후 과제</p>
<p>핵심은 완성도를 70%에서 더 끌어올리는 것이며, 구현보다 <strong>질문 설계의 한끝 차이</strong>가 결과물 품질을 결정한다. 이를 위해 세 가지 과제가 남아있다.</p>
<p><strong>① 암묵지 유형화</strong> — 로켓런칭 매니저들이 기획 차별성을 만들 때 실제로 어떻게 사고하고, 어디서 어떤 요소를 가져오는지를 체계화하는 작업. 단순 질문 목록이 아니라 "이 답변이 나왔을 때 왜 이 꼬리질문으로 가는가"의 판단 로직 자체를 유형화해야 한다.</p>
<p><strong>② 꼬리질문 분기 고도화</strong> — 현재는 비어있거나 숫자 없을 때 재질문하는 2분기 수준. 실제 매니저의 인터뷰는 3가지 차원에서 동시에 판단이 일어난다.</p>
<ul><li>차원 1 (답변 품질 판단): 정보 충분성·답변 깊이·시그니처 재료 가능성을 자동 판단</li><li>차원 2 (분기 유형 매핑): 보완형·심화형·연결형·전환형 4가지로 분기</li><li>차원 3 (강사 성향별 전략): 성과 중심형·스토리 중심형·불확실형에 따라 접근 방식 달리 설계</li></ul>
<p><strong>③ 강사 유형화 시스템</strong> — 질문 답변을 바탕으로 강사의 패턴을 자동 태깅하고, 데이터가 쌓이면 유형별 최적 질문 흐름으로 분기하는 구조. 현재는 백엔드 태깅만 수집 중이며, 30건 이상 데이터 확보 후 실제 유형 WoW 노출로 전환 예정.</p>
<hr class="sec-divider">
<p class="sec-label">⑥ 소감</p>
<p>이번 캠프에서 가장 크게 느낀 건 구현보다 문제 정의가 먼저라는 것이었다.</p>
<p><strong>실패 경험</strong> — 가장 먼저 만든 주간보고서봇은 배포까지 완료했고 직접 써보니 잘 작동했다. 하지만 팀원 누구도 못 쓰게 됐다. 이유는 단순했다 — 쓸 사람이 뭘 필요로 하는지 한 번도 물어보지 않고, 내가 만들고 싶은 것을 만들었기 때문이다.</p>
<p><strong>이후 달라진 것</strong> — 상세페이지봇을 만들면서는 순서를 바꿨다. 실제 매니저 인터뷰 기록을 분석해 질문 구조를 잡고, 팀 리더 피드백을 받아 방향을 수정하고, 기획서를 v1부터 v4까지 고쳐가며 구현보다 설계에 더 많은 시간을 썼다.</p>
<p><strong>팀원들에게</strong> — 구현이 병목이 아니라는 말을 많이 들었다. 직접 만들어보니 진짜 병목은 예상보다 훨씬 앞 단계에 있었다. AI에게 주는 인풋의 퀄리티 — 질문의 설계, 현장 암묵지의 유형화, 수백 가지 경우의 수를 시뮬레이션하며 조정하는 과정. 이게 실제로 가장 어렵고 가장 오래 걸렸다. 도구는 같아도 인풋이 다르면 결과가 달라진다. AI가 좋아질수록 실력 차이는 줄어드는 게 아니라, 이 인풋을 얼마나 정밀하게 설계하느냐에서 벌어진다.</p>
<p>첫째, <strong>질문 설계</strong> — 어떤 정보를 어떤 순서로 어떤 제약 조건과 함께 넣느냐가 결과물 방향을 결정한다.</p>
<p>처음엔 강사에게 필요한 정보를 모으는 목적으로 Q1~Q7을 설계했다. 결과물은 나왔지만 누구에게나 적용될 법한 generic한 시그니처였다. 실제 매니저 킥오프 인터뷰 기록을 역분석하면서 이유를 찾았다 — 질문 순서가 틀렸다. 매니저는 목표부터 묻고 과거로 역산하는데, 봇은 배경부터 수집하고 있었다. 순서를 바꾼 것만으로 답변의 밀도가 달라졌다.</p>
<p>순서 다음엔 범위의 문제가 나왔다. 속눈썹 강사 케이스를 테스트할 때 질문 하나의 범위를 열어뒀더니 시그니처가 상품이 아닌 릴스(유통 수단)로 빠졌다. "상품 기반"이라는 제약 한 줄을 추가하자 방향이 돌아왔다. 그 이후로 질문 하나를 바꿀 때마다 결과물이 어떻게 달라지는지 케이스를 돌려가며 확인했고, 기획서는 v1에서 v4까지, 질문 플로우는 4챕터 구조로 전면 재설계됐다. 코드 수정이 아니라 질문 설계의 반복이 완성도를 올렸다.</p>
<p>둘째, <strong>암묵지 유형화</strong> — 현장에서 쌓인 노하우를 AI가 실행 가능한 데이터로 만드는 작업. 실제 매니저 킥오프 인터뷰 기록을 역분석했을 때, 매니저 본인도 명시적으로 인식 못 하던 3단계 패턴이 나왔다. 표면 수집 → 숫자 디깅 → 언어화. 그리고 강사의 경험에서 시그니처를 뽑아내는 역설의 유형이 5가지, 내부자 지식의 유형이 4가지로 체계화됐다. 이 유형화 작업에 전체 기획 시간의 절반 이상이 들었다.</p>
<p>셋째, <strong>무한 시뮬레이션</strong> — 답변의 경우의 수는 무한하다. 업종 12가지 페르소나를 설계하고 돌렸지만, 실제로 결과물 품질을 결정하는 변수는 업종이 아니었다.</p>
<p>런칭하려는 아이템의 성격, 답변을 얼마나 성실하게 쓰는지, 자기 경험을 얼마나 구체적으로 적는지, 강사로서의 성향. 같은 질문을 받아도 이 변수들의 조합에 따라 AI가 뽑아내는 결과물이 완전히 달라졌다. 각 조합마다 어떤 꼬리질문이 필요한지, 어디서 재질문을 해야 하는지를 직접 돌려보고 조정하는 과정이 반복됐다. 시스템 프롬프트가 v0.1에서 v0.3까지 바뀐 건 기능 추가가 아니라 이 경우의 수를 하나씩 막아가는 과정이었다.</p>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

<!-- === /발표자: mjshin === -->

---

<!-- header: "**NOVA** · LK AI Camp 2기" -->
<!-- === 발표자: Nova === -->

<!-- _class: cover -->

<div class="cover-title">Nova의<br>자동화 도구</div>
<p class="cover-presenter"><strong>발표자</strong> 콘텐츠 디자이너 &nbsp;｜&nbsp; Nova</p>
<div class="cover-tags"><span class="tag">단계마다 이전 히스토리를 직접 찾</span></div>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 문제와 해결 방향
<p class="slide-sub">단계마다 이전 히스토리를 직접 찾아 복붙해야 했음. 상품 기획 → 랜딩 페이지 → 광고 소재 → 강의안 → CRM 문자까지 이어지는 5개 레이어</p>

<div class="two-col">
  <div class="col-l"><p class="sec-label">① 문제 상황</p><p>단계마다 이전 히스토리를 직접 찾아 복붙해야 했음. 상품 기획 → 랜딩 페이지 → 광고 소재 → 강의안 → CRM 문자까지 이어지는 5개 레이어가 각각 단절되어 있었고, 매 단계마다 "이전에 뭐라고 했더라"를 다시 찾는 반복 작업이 발생.</p><hr class="sec-divider"><p class="sec-label">③ 지향했던 방향성</p><p>데이터 → 기획 → 메시지 → 콘텐츠가 하나의 논리적 흐름으로 자동 연결되는 구조. 고객사 데이터만 넣으면 모든 하위 산출물이 같은 언어·논리·데이터를 기반으로 자동 생성.</p></div>
  <div class="col-r"><p class="sec-label">② 기존 방식의 병목</p><p>각 산출물이 파편화된 문서/메모/채팅에 흩어져 있어서 광고 카피를 쓸 때 기획안을, 강의안 쓸 때 광고 카피를, CRM 문자 쓸 때 강의안을 다시 찾아 붙여넣는 구조. 논리적 일관성이 사람 손에 달려 있었음.</p></div>
</div>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 현재 구현 단계
<p class="slide-sub">자동화 전·후 비교</p>

<table class="cmp-table"><thead><tr><th class="h-left">기존 방식</th><th class="h-mid">구분</th><th class="h-right">자동화 후</th></tr></thead><tbody><tr><td>—</td><td class="m-mid">비교</td><td>—</td></tr></tbody></table>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 추후 과제 &amp; 소감
<p class="slide-sub">앞으로 발전시키고 싶은 것, 그리고 이번 캠프를 통해 달라진 것</p>

<p class="sec-label">⑤ 추후 과제</p>
<ul><li>우두머리 `02_상품_로드맵.md` 채우기 → 타겟분석 + 유료 상품 기획서 생성 테스트</li><li>01 디자인 기획안 레이어 자동화 설계 — 기획서가 완성되면 랜딩 페이지·광고 카피를 자동 파생시키는 구조</li><li>03 CRM 레이어 연결 — 기획 데이터가 사전/사후 문자 자동 생성까지 이어지는 파이프라인</li><li>루루이펙트·성장연구소 등 다른 고객사에 동일 구조 복제</li></ul>
<hr class="sec-divider">
<p class="sec-label">⑥ 소감</p>
<p>"산출물을 만드는 게 아니라 산출물들이 연결되는 구조를 만들면, 이후 작업이 빨라진다." 지금까지 한 작업의 핵심은 각 기획 파일이 서로를 참조하는 의존성 구조를 코드처럼 명문화한 것. 이 구조가 잡히면 01~03 레이어도 같은 방식으로 확장 가능함.</p>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

<!-- === /발표자: Nova === -->
