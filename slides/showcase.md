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

<table class="cmp-table"><thead><tr><th class="h-left">기존 방식</th><th class="h-mid">구분</th><th class="h-right">자동화 후</th></tr></thead><tbody><tr><td>온보딩 → 개별 온/오프 미팅 외에 다른 선택지 없음 (가이드 문서 전달해봤으나, 불가 확인 / 대…</td><td class="m-mid">비교</td><td>신규 온보딩 자동화: 미진행</td></tr><tr><td>고객사 상품 세일즈 기획 자동화 → 매번 새롭게 기획, 문서화, 미팅을 통해 전달</td><td class="m-mid">비교</td><td>상품 세일즈 기획 자동화: 일부 진행 중 (무료 강의안 기획부터)</td></tr><tr><td>기록 자동화: 매번 직접 기록</td><td class="m-mid">기록 자동화</td><td>기록 자동화: 아직 녹음 파일을 구글 드라이브로 자동 업로드하는 과정 해결 중</td></tr><tr><td>신규 주제 도메인 이해도: 파편화된 정보를 리서치하고 취합하는 형태</td><td class="m-mid">비교</td><td>신규 주제 학습 튜터: 미진행</td></tr></tbody></table>
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

<!-- header: "**CHAEEUN JANG** · LK AI Camp 2기" -->
<!-- === 발표자: Chaeeun Jang === -->

<!-- _class: cover -->

<div class="cover-title">Chaeeun Jang의<br>자동화 도구</div>
<p class="cover-presenter"><strong>발표자</strong> 콘텐츠 디자이너 &nbsp;｜&nbsp; Chaeeun Jang</p>
<div class="cover-tags"><span class="tag">상시퍼널 성과 분석을 위해 매일 </span><span class="tag">**analyze.py**: VOD </span></div>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 문제와 해결 방향
<p class="slide-sub">1,000~2,000명 규모 수강생 데이터를 매일 수동 집계 — 고객사가 늘수록 병목도 커졌습니다</p>

<div class="two-col">
  <div class="col-l"><p class="sec-label">① 문제 상황</p><p>매일 수강생 엑셀을 받아 신청자 수·완강률·결제 전환율 등을 직접 계산하고, 일자별·주차별·월별로 정리해 노션에 옮기는 작업을 반복해야 했습니다. 고객사가 늘수록 작업량도 늘고, 실수도 잦아졌습니다.</p>
<hr class="sec-divider"><p class="sec-label">③ 지향했던 방향성</p><p>파일을 폴더에 드롭하고 "inbox 처리해줘" 한 마디면 분석·DB 기록·보고서 생성까지 자동 완료. 숫자가 아닌 인사이트에만 집중할 수 있는 구조.</p></div>
  <div class="col-r"><p class="sec-label">② 기존 방식의 병목</p><ul><li>매번 함수 직접 작성 → 일자별 추적 어려움</li><li>파트별 이탈 시각화 불가</li><li>수치를 노션에 수동 복붙</li><li>결제 전환율 매칭 — 가장 오래 걸리고 오류 많음</li></ul></div>
</div>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 현재 구현 단계
<p class="slide-sub">자동화 전·후 비교</p>

<table class="cmp-table"><thead><tr><th class="h-left">기존 방식</th><th class="h-mid">구분</th><th class="h-right">자동화 후</th></tr></thead><tbody><tr><td>함수 직접 작성, 일자별 수동 집계</td><td class="m-mid">데이터 분석</td><td>analyze.py — 5개 탭 결과 엑셀 자동 생성 + 결제 전환율 이메일 매칭 자동 계산</td></tr><tr><td>수치 수동 복붙, 고객사별 따로 정리</td><td class="m-mid">보고서</td><td>Notion DB 3개 자동 기록 + 바차트 포함 보고서 페이지 자동 생성</td></tr><tr><td>엑셀 직접 관리, 서식 매번 수동 적용</td><td class="m-mid">데이터 누적</td><td>Google Sheets 5탭 누적 업데이트 + 서식 자동 적용</td></tr></tbody></table>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 추후 과제 &amp; 소감
<p class="slide-sub">앞으로 발전시키고 싶은 것, 그리고 이번 캠프를 통해 달라진 것</p>

<p class="sec-label">⑤ 추후 과제</p>
<ul><li>여러 파일 동시 처리 안정성 검증</li><li>인사이트 자동 생성 고도화 — 패턴 감지 및 액션 우선순위 자동 판단</li><li>고객사 바로 공유 가능한 보고서 포맷 자동화</li></ul>
<hr class="sec-divider">
<p class="sec-label">⑥ 소감</p>
<p>개발 경험 없이도 실제로 동작하는 자동화 시스템을 만들 수 있다는 게 가장 큰 발견이었습니다. 세팅을 마치고 나니 업무 효율이 크게 높아졌고, 고객사 보고서 퀄리티도 올라갔습니다. 진작 시도해볼 걸 — 앞으로는 단순 반복은 Claude에 맡기고, 나는 생각하는 일에 집중하려 합니다.</p>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

<!-- === /발표자: Chaeeun Jang === -->

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
