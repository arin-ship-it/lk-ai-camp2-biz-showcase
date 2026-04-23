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
<p class="cover-presenter"><strong>발표자</strong> 세일즈 매니저 &nbsp;｜&nbsp; Evan</p>
<div class="cover-tags"><span class="tag">신규 고객 온보딩 자동화</span><span class="tag">신규 온보딩 자동화: 미진행</span></div>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 문제와 해결 방향
<p class="slide-sub">신규 고객 온보딩 자동화</p>

<div class="two-col">
  <div class="col-l"><p class="sec-label">① 문제 상황</p><ul><li>신규 고객 온보딩 자동화</li><li>상품 세일즈(강의안·상페·모객 자료) 기획 자동화</li><li>통화 녹음 및 미팅 기록 자동화</li><li>신규 주제 도메인 이해도 높이기 (학습 튜터)</li></ul><hr class="sec-divider"><p class="sec-label">③ 지향했던 방향성</p><ul><li>온보딩: 고객사 LLM 에 코드 입력 시 자동 구현 (부트캠프 Day 4 유사 구조)</li><li>세일즈 기획: 핵심 논리 방법론 + 자료 정교화 → 통합 스킬에서 개별 스킬로 분리해 효율화</li><li>기록: 녹음파일 자동 전달 — 현재 MacroDroid 로 자동화 중</li><li>도메인 이해: 주제별 라이브러리화 + 교육학 기반 학습 시스템 프롬프트</li></ul></div>
  <div class="col-r"><p class="sec-label">② 기존 방식의 병목</p><table><thead><tr><th>병목 유형</th><th>구체적 문제</th></tr></thead><tbody><tr><td>온보딩</td><td>개별 온·오프 미팅 외 대안 없음</td></tr><tr><td>세일즈 기획</td><td>매번 새로 기획·문서화·미팅 반복</td></tr><tr><td>기록</td><td>매번 직접 기록</td></tr><tr><td>도메인 이해</td><td>파편화된 정보 수동 리서치</td></tr></tbody></table></div>
</div>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 현재 구현 단계
<p class="slide-sub">자동화 전·후 비교</p>

<table class="cmp-table"><thead><tr><th class="h-left">기존 방식</th><th class="h-mid">구분</th><th class="h-right">자동화 후</th></tr></thead><tbody><tr><td>개별 온·오프 미팅 외 대안 없음</td><td class="m-mid">온보딩</td><td>신규 온보딩 자동화: 미진행</td></tr><tr><td>매번 새로 기획·문서화·미팅 반복</td><td class="m-mid">세일즈 기획</td><td>세일즈 기획 자동화: 무료 강의안 기획부터 일부 진행</td></tr><tr><td>매번 직접 기록</td><td class="m-mid">기록</td><td>기록 자동화: 녹음 → 드라이브 업로드 구간 해결 중</td></tr><tr><td>파편화된 정보 수동 리서치</td><td class="m-mid">도메인 이해</td><td>학습 튜터: 미진행</td></tr></tbody></table>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 추후 과제 &amp; 소감
<p class="slide-sub">앞으로 발전시키고 싶은 것, 그리고 이번 캠프를 통해 달라진 것</p>

<p class="sec-label">⑤ 추후 과제</p>
<ul><li>위 에이전트 완성 및 현재 진행 단계 문제 해결</li></ul>
<hr class="sec-divider">
<p class="sec-label">⑥ 소감</p>
<p>AI 가 미지의 영역처럼 막연했는데, 작동 구조와 운영 방식을 배울 수 있어 좋았습니다. 배운 기틀을 기준으로 계속 업데이트해나가겠습니다.</p>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

<!-- === /발표자: Evan === -->

---

<!-- header: "**CHAEEUN JANG** · LK AI Camp 2기" -->
<!-- === 발표자: Chaeeun Jang === -->

<!-- _class: cover -->

<div class="cover-title">Chaeeun Jang의<br>자동화 도구</div>
<p class="cover-presenter"><strong>발표자</strong> 그로우 매니저 &nbsp;｜&nbsp; Chaeeun Jang</p>
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
<p class="cover-presenter"><strong>발표자</strong> 그로우 매니저 &nbsp;｜&nbsp; mjshin</p>
<div class="cover-tags"><span class="tag">매니저 1명이 담당 가능한 고객사</span><span class="tag">3단계 자동화 워크플로우</span><span class="tag">질문 플로우 설계: 매니저 킥오프 인</span></div>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 문제와 해결 방향
<p class="slide-sub">매니저 1명이 담당 가능한 고객사 수는 리소스에 의해 결정된다. 매 고객사마다 두 단계가 리소스를 반복 소모하고 있었다.</p>

<div class="two-col">
  <div class="col-l"><p class="sec-label">① 문제 상황</p><p>매니저 1명이 담당 가능한 고객사 수는 리소스에 의해 결정된다. 매 고객사마다 두 단계가 리소스를 반복 소모하고 있었다.</p>
<ul><li>소통 단계 — 브랜딩·퍼널·상품 기획 정보 수집용 반복 커뮤니케이션</li><li>기획 단계 — 수집한 정보를 실제 기획물로 변환하는 작업</li></ul>
<p>두 단계를 자동화하면 더 많은 고객사 런칭 + 기획 완성도에 집중 가능.</p><hr class="sec-divider"><p class="sec-label">③ 지향했던 방향성</p><ul><li>인풋 최적화: 핵심 질문 체계화 + AI 시뮬레이션 꼬리질문 → 1회 미팅으로 수집 완료</li><li>기획 자동화: 시장조사·경쟁사 분석·차별화 포인트 도출 시간 단축</li><li>산출물 자동화: 광고·무료/유료 상품 페이지·강의 구성 4가지 자동 생성</li><li>얼라인 간소화: 핵심 미팅 1회 + 나머지 비동기</li></ul></div>
  <div class="col-r"><p class="sec-label">② 기존 방식의 병목</p><table><thead><tr><th>병목 유형</th><th>구체적 문제</th></tr></thead><tbody><tr><td>인풋 수집</td><td>매 미팅 전 맞춤 인터뷰 설계 반복</td></tr><tr><td>기획 반복</td><td>시장조사·크리에이티브·기획물 재작성 사이클</td></tr><tr><td>얼라인 비용</td><td>미팅 2~3회마다 고객사 재확인</td></tr><tr><td>시간 구조</td><td>기획 1건에 최소 7일 구조적 고정</td></tr></tbody></table></div>
</div>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 현재 구현 단계
<p class="slide-sub">자동화 전·후 비교</p>

<div class="flow-wrap"><div class="flow-step"><div class="flow-num">01</div>역설 5유형</div><div class="flow-step"><div class="flow-num">02</div>내부자 지식 4유형</div><div class="flow-step"><div class="flow-num">03</div>렌즈 명명</div></div>
<table class="cmp-table"><thead><tr><th class="h-left">기존 방식</th><th class="h-mid">구분</th><th class="h-right">자동화 후</th></tr></thead><tbody><tr><td>매 미팅 전 맞춤 인터뷰 설계 반복</td><td class="m-mid">인풋 수집</td><td>질문 플로우 설계: 매니저 킥오프 인터뷰 역분석으로 핵심 질문 7개 + 꼬리질문 구조 추출</td></tr><tr><td>시장조사·크리에이티브·기획물 재작성 사이클</td><td class="m-mid">기획 반복</td><td>시그니처 발굴 프롬프트: 3단계 사고 프로세스 (역설 5유형 → 내부자 지식 4유형 → 렌즈 명명)</td></tr><tr><td>미팅 2~3회마다 고객사 재확인</td><td class="m-mid">얼라인 비용</td><td>단독성 검증: 이 고객사만의 것인지 자동 검증 3가지 필터</td></tr><tr><td>기획 1건에 최소 7일 구조적 고정</td><td class="m-mid">시간 구조</td><td>Streamlit 프로토타입: 모바일 최적화로 입력~결과 확인 구동 중</td></tr></tbody></table>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

---

# 추후 과제 &amp; 소감
<p class="slide-sub">앞으로 발전시키고 싶은 것, 그리고 이번 캠프를 통해 달라진 것</p>

<p class="sec-label">⑤ 추후 과제</p>
<ul><li>암묵지 유형화: "이 답변에 왜 이 꼬리질문?" 판단 로직 체계화</li><li>꼬리질문 분기 고도화: 답변 품질 · 분기 유형 · 강사 성향 3차원 판단</li><li>강사 유형화 시스템: 답변 기반 자동 태깅 → 30건+ 데이터 후 유형별 분기 전환</li></ul>
<hr class="sec-divider">
<p class="sec-label">⑥ 소감</p>
<p>이번 캠프에서 가장 크게 느낀 건 <strong>구현보다 문제 정의가 먼저</strong>라는 것.</p>
<p>첫 주간보고서봇은 배포까지 했지만 아무도 못 썼다 — 쓸 사람이 뭘 필요로 하는지 물어보지 않고 내가 만들고 싶은 걸 만들었기 때문. 이후 상세페이지봇은 실제 매니저 인터뷰 분석 → 피드백 반영 → 기획서 v1~v4 반복으로 구현보다 설계에 더 많은 시간을 썼다.</p>
<p>진짜 병목은 훨씬 앞 단계 — AI 에게 주는 <strong>인풋의 퀄리티</strong> 였다. 질문 설계, 현장 암묵지 유형화, 수백 가지 경우의 수 시뮬레이션. 도구는 같아도 인풋이 다르면 결과가 달라지고, AI 가 좋아질수록 실력 차이는 인풋 설계의 정밀도에서 벌어진다.</p>
<span class="slide-footer">2026.04</span><span class="corner-sq"></span>

<!-- === /발표자: mjshin === -->

---

<!-- header: "**NOVA** · LK AI Camp 2기" -->
<!-- === 발표자: Nova === -->

<!-- _class: cover -->

<div class="cover-title">Nova의<br>자동화 도구</div>
<p class="cover-presenter"><strong>발표자</strong> 그로우 매니저 &nbsp;｜&nbsp; Nova</p>
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
