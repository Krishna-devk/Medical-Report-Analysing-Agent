DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>QuickCare AI</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0a0f1e;
    --surface: #111827;
    --surface2: #1a2234;
    --border: #1e293b;
    --accent: #3b82f6;
    --accent2: #06b6d4;
    --text: #f1f5f9;
    --muted: #64748b;
    --green: #10b981;
    --yellow: #f59e0b;
    --orange: #f97316;
    --red: #ef4444;
    --radius: 16px;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    line-height: 1.6;
    min-height: 100vh;
  }

  /* ── BACKGROUND GRID ── */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(59,130,246,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(59,130,246,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
  }

  .page { position: relative; z-index: 1; max-width: 1200px; margin: 0 auto; padding: 40px 24px; }

  /* ── HEADER ── */
  header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 48px;
    padding-bottom: 24px;
    border-bottom: 1px solid var(--border);
  }

  .logo {
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .logo-icon {
    width: 44px; height: 44px;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
  }

  .logo h1 {
    font-family: 'DM Serif Display', serif;
    font-size: 22px;
    letter-spacing: -0.3px;
  }

  .logo span {
    display: block;
    font-size: 11px;
    color: var(--muted);
    font-weight: 300;
    letter-spacing: 1px;
    text-transform: uppercase;
  }

  .status-badge {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 12px;
    color: var(--green);
    background: rgba(16,185,129,0.1);
    border: 1px solid rgba(16,185,129,0.2);
    padding: 6px 12px;
    border-radius: 20px;
  }

  .status-dot {
    width: 6px; height: 6px;
    background: var(--green);
    border-radius: 50%;
    animation: pulse 2s infinite;
  }

  @keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
  }

  /* ── UPLOAD AREA ── */
  .upload-section {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 32px;
    margin-bottom: 32px;
  }

  .upload-title {
    font-family: 'DM Serif Display', serif;
    font-size: 20px;
    margin-bottom: 6px;
  }

  .upload-subtitle {
    color: var(--muted);
    font-size: 13px;
    margin-bottom: 24px;
  }

  .upload-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr auto;
    gap: 12px;
    align-items: end;
  }

  @media (max-width: 768px) {
    .upload-grid { grid-template-columns: 1fr 1fr; }
    .upload-grid .btn-analyze { grid-column: span 2; }
  }

  .field { display: flex; flex-direction: column; gap: 6px; }

  label {
    font-size: 11px;
    font-weight: 500;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.8px;
  }

  input[type="file"],
  input[type="number"],
  select {
    background: var(--surface2);
    border: 1px solid var(--border);
    color: var(--text);
    border-radius: 10px;
    padding: 10px 14px;
    font-size: 13px;
    font-family: inherit;
    outline: none;
    transition: border-color 0.2s;
    width: 100%;
  }

  input:focus, select:focus { border-color: var(--accent); }

  input[type="file"] { cursor: pointer; padding: 9px 14px; }
  input[type="file"]::file-selector-button {
    background: var(--accent);
    color: white;
    border: none;
    border-radius: 6px;
    padding: 4px 10px;
    font-size: 12px;
    cursor: pointer;
    margin-right: 10px;
  }

  .btn-analyze {
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    color: white;
    border: none;
    border-radius: 10px;
    padding: 11px 24px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    font-family: inherit;
    transition: opacity 0.2s, transform 0.1s;
    white-space: nowrap;
    height: 42px;
  }

  .btn-analyze:hover { opacity: 0.9; }
  .btn-analyze:active { transform: scale(0.98); }
  .btn-analyze:disabled { opacity: 0.5; cursor: not-allowed; }

  /* ── ENDPOINT TABS ── */
  .tabs {
    display: flex;
    gap: 4px;
    margin-bottom: 20px;
    background: var(--surface);
    padding: 4px;
    border-radius: 12px;
    border: 1px solid var(--border);
    width: fit-content;
  }

  .tab {
    padding: 8px 16px;
    border-radius: 8px;
    font-size: 12px;
    font-weight: 500;
    cursor: pointer;
    border: none;
    background: none;
    color: var(--muted);
    font-family: inherit;
    transition: all 0.2s;
  }

  .tab.active {
    background: var(--accent);
    color: white;
  }

  /* ── LOADING ── */
  .loading {
    display: none;
    text-align: center;
    padding: 60px 24px;
    color: var(--muted);
  }

  .loading.visible { display: block; }

  .spinner {
    width: 40px; height: 40px;
    border: 3px solid var(--border);
    border-top-color: var(--accent);
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
    margin: 0 auto 16px;
  }

  @keyframes spin { to { transform: rotate(360deg); } }

  /* ── RESULTS ── */
  #results { display: none; }
  #results.visible { display: block; }

  .results-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-bottom: 20px;
  }

  @media (max-width: 900px) { .results-grid { grid-template-columns: 1fr; } }

  .card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 24px;
  }

  .card-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 20px;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--border);
  }

  .card-icon {
    width: 36px; height: 36px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    flex-shrink: 0;
  }

  .card-title { font-family: 'DM Serif Display', serif; font-size: 16px; }
  .card-subtitle { font-size: 11px; color: var(--muted); }

  /* ── ONE LINE SUMMARY ── */
  .one-liner {
    background: linear-gradient(135deg, rgba(59,130,246,0.08), rgba(6,182,212,0.08));
    border: 1px solid rgba(59,130,246,0.2);
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 20px;
    font-size: 15px;
    font-family: 'DM Serif Display', serif;
    color: var(--text);
    line-height: 1.5;
  }

  /* ── SUMMARY ROWS ── */
  .summary-row {
    display: grid;
    grid-template-columns: 120px 1fr;
    gap: 8px;
    padding: 10px 0;
    border-bottom: 1px solid var(--border);
  }

  .summary-row:last-child { border-bottom: none; }

  .row-label {
    font-size: 11px;
    font-weight: 600;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding-top: 2px;
  }

  .row-value { font-size: 13px; color: var(--text); }

  /* ── LAB TABLE ── */
  .lab-table { width: 100%; border-collapse: collapse; }

  .lab-table th {
    font-size: 10px;
    font-weight: 600;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 6px 10px;
    text-align: left;
    border-bottom: 1px solid var(--border);
  }

  .lab-table td {
    padding: 10px 10px;
    border-bottom: 1px solid var(--border);
    font-size: 13px;
  }

  .lab-table tr:last-child td { border-bottom: none; }

  .lab-table tr:hover td { background: var(--surface2); }

  .sev-badge {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 3px 8px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: 600;
  }

  .sev-normal   { background: rgba(16,185,129,0.12); color: #10b981; }
  .sev-mild     { background: rgba(245,158,11,0.12); color: #f59e0b; }
  .sev-moderate { background: rgba(249,115,22,0.12); color: #f97316; }
  .sev-critical { background: rgba(239,68,68,0.15);  color: #ef4444; }

  .flag-high { color: #ef4444; font-size: 10px; font-weight: 700; }
  .flag-low  { color: #3b82f6; font-size: 10px; font-weight: 700; }
  .flag-normal { color: var(--muted); font-size: 10px; }

  /* ── OVERALL SEVERITY BANNER ── */
  .severity-banner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 14px 18px;
    border-radius: 10px;
    margin-bottom: 16px;
    font-weight: 600;
  }

  .sev-banner-normal   { background: rgba(16,185,129,0.1);  border: 1px solid rgba(16,185,129,0.3); }
  .sev-banner-mild     { background: rgba(245,158,11,0.1);  border: 1px solid rgba(245,158,11,0.3); }
  .sev-banner-moderate { background: rgba(249,115,22,0.1);  border: 1px solid rgba(249,115,22,0.3); }
  .sev-banner-critical { background: rgba(239,68,68,0.12);  border: 1px solid rgba(239,68,68,0.4); }

  .sev-banner-text { font-size: 15px; }
  .sev-banner-counts { font-size: 12px; font-weight: 400; color: var(--muted); }

  /* ── ALERTS ── */
  .alert-box {
    background: rgba(239,68,68,0.08);
    border: 1px solid rgba(239,68,68,0.25);
    border-radius: 10px;
    padding: 12px 16px;
    margin-top: 12px;
    font-size: 13px;
    color: #fca5a5;
    line-height: 1.7;
  }

  /* ── RISK CARDS ── */
  .risk-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 16px; }

  .risk-card {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px;
    text-align: center;
  }

  .risk-percent {
    font-family: 'DM Serif Display', serif;
    font-size: 36px;
    line-height: 1;
    margin-bottom: 4px;
  }

  .risk-label { font-size: 11px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.5px; }

  .risk-bar-wrap { background: var(--border); border-radius: 4px; height: 6px; margin-top: 10px; overflow: hidden; }
  .risk-bar { height: 100%; border-radius: 4px; transition: width 1s ease; }

  /* ── PRIORITY BADGE ── */
  .priority-badge {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    padding: 14px;
    border-radius: 12px;
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 12px;
    letter-spacing: 0.5px;
  }

  .priority-normal   { background: rgba(16,185,129,0.1);  border: 1px solid rgba(16,185,129,0.3); color: #10b981; }
  .priority-medium   { background: rgba(245,158,11,0.1);  border: 1px solid rgba(245,158,11,0.3); color: #f59e0b; }
  .priority-high     { background: rgba(249,115,22,0.1);  border: 1px solid rgba(249,115,22,0.3); color: #f97316; }
  .priority-urgent   { background: rgba(239,68,68,0.12);  border: 1px solid rgba(239,68,68,0.4);  color: #ef4444;
                       animation: urgentPulse 1.5s ease-in-out infinite; }

  @keyframes urgentPulse {
    0%, 100% { box-shadow: 0 0 0 0 rgba(239,68,68,0); }
    50%       { box-shadow: 0 0 0 6px rgba(239,68,68,0.15); }
  }

  /* ── RISK FACTORS ── */
  .risk-factors { display: flex; flex-wrap: wrap; gap: 6px; }

  .risk-tag {
    background: rgba(239,68,68,0.08);
    border: 1px solid rgba(239,68,68,0.2);
    color: #fca5a5;
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 12px;
  }

  /* ── BED MANAGEMENT ── */
  .bed-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }

  .bed-stat {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px;
    text-align: center;
  }

  .bed-value {
    font-family: 'DM Serif Display', serif;
    font-size: 28px;
    color: var(--accent2);
    margin-bottom: 4px;
  }

  .bed-label { font-size: 11px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.5px; }

  /* ── DOCTOR ADVICE ── */
  .advice-box {
    background: linear-gradient(135deg, rgba(59,130,246,0.06), rgba(6,182,212,0.06));
    border: 1px solid rgba(59,130,246,0.15);
    border-radius: 12px;
    padding: 18px;
    font-size: 14px;
    line-height: 1.7;
    color: #cbd5e1;
    grid-column: span 2;
  }

  @media (max-width: 900px) { .advice-box { grid-column: span 1; } }

  .advice-header {
    font-size: 11px;
    font-weight: 600;
    color: var(--accent2);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 10px;
  }

  /* ── CHAT ── */
  .chat-section {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 24px;
    margin-top: 24px;
  }

  .chat-input-row { display: flex; gap: 10px; }

  .chat-input {
    flex: 1;
    background: var(--surface2);
    border: 1px solid var(--border);
    color: var(--text);
    border-radius: 10px;
    padding: 10px 16px;
    font-size: 13px;
    font-family: inherit;
    outline: none;
  }

  .chat-input:focus { border-color: var(--accent); }

  .chat-btn {
    background: var(--accent);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 20px;
    font-size: 13px;
    cursor: pointer;
    font-family: inherit;
    font-weight: 600;
  }

  .chat-response {
    margin-top: 16px;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px;
    font-size: 13px;
    line-height: 1.7;
    display: none;
  }

  .chat-response.visible { display: block; }

  /* ── ERROR ── */
  .error-box {
    background: rgba(239,68,68,0.08);
    border: 1px solid rgba(239,68,68,0.3);
    border-radius: 12px;
    padding: 20px 24px;
    color: #fca5a5;
    display: none;
  }

  .error-box.visible { display: block; }

  /* ── PATIENT INFO BAR ── */
  .patient-bar {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px 24px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 24px;
    flex-wrap: wrap;
  }

  .patient-bar-item { display: flex; flex-direction: column; gap: 2px; }
  .patient-bar-label { font-size: 10px; color: var(--muted); text-transform: uppercase; letter-spacing: 0.5px; }
  .patient-bar-value { font-size: 15px; font-weight: 600; }
  .patient-divider { width: 1px; height: 32px; background: var(--border); }

</style>
</head>
<body>
<div class="page">

  <!-- HEADER -->
  <header>
    <div class="logo">
      <div class="logo-icon">🏥</div>
      <div>
        <h1>QuickCare AI</h1>
        <span>Medical Intelligence System</span>
      </div>
    </div>
    <div class="status-badge">
      <div class="status-dot"></div>
      Gemini 2.5 Flash · Online
    </div>
  </header>

  <!-- UPLOAD SECTION -->
  <div class="upload-section">
    <div class="upload-title">Analyze Patient Report</div>
    <div class="upload-subtitle">Upload a PDF medical report for instant AI analysis</div>

    <!-- Endpoint Tabs -->
    <div class="tabs" style="margin-bottom: 16px;">
      <button class="tab active" onclick="setMode('full')">🏥 Full Analysis</button>
      <button class="tab" onclick="setMode('summary')">📄 Summary</button>
      <button class="tab" onclick="setMode('labs')">🔬 Lab Analysis</button>
      <button class="tab" onclick="setMode('risk')">📊 Risk Score</button>
    </div>

    <div class="upload-grid">
      <div class="field">
        <label>Patient PDF Report</label>
        <input type="file" id="pdfFile" accept=".pdf" onchange="onFileChange()">
      </div>
      <div class="field" id="ageField">
        <label>Age (optional)</label>
        <input type="number" id="ageInput" placeholder="e.g. 67" min="1" max="120">
      </div>
      <div class="field" id="genderField">
        <label>Gender (optional)</label>
        <select id="genderInput">
          <option value="">Select...</option>
          <option value="male">Male</option>
          <option value="female">Female</option>
        </select>
      </div>
      <button class="btn-analyze" id="analyzeBtn" onclick="analyze()" disabled>
        Analyze →
      </button>
    </div>
  </div>

  <!-- ERROR -->
  <div class="error-box" id="errorBox"></div>

  <!-- LOADING -->
  <div class="loading" id="loading">
    <div class="spinner"></div>
    <div style="font-size: 15px; color: var(--text); margin-bottom: 6px;">Gemini is analyzing the report...</div>
    <div style="font-size: 13px; color: var(--muted);">Extracting clinical data, lab values, and risk factors</div>
  </div>

  <!-- RESULTS -->
  <div id="results">

    <!-- Patient Bar -->
    <div class="patient-bar" id="patientBar"></div>

    <!-- One-liner summary -->
    <div class="one-liner" id="oneLiner"></div>

    <!-- Main Grid -->
    <div class="results-grid" id="resultsGrid"></div>

    <!-- Doctor Advice -->
    <div id="adviceSection"></div>

  </div>

  <!-- CHAT -->
  <div class="chat-section">
    <div class="card-header" style="margin-bottom: 16px; padding-bottom: 0; border: none;">
      <div class="card-icon" style="background: rgba(139,92,246,0.15);">💬</div>
      <div>
        <div class="card-title">Ask Medical AI</div>
        <div class="card-subtitle">Clinical questions answered instantly</div>
      </div>
    </div>
    <div class="chat-input-row">
      <input class="chat-input" id="chatInput" placeholder="e.g. What does high creatinine indicate?" onkeydown="if(event.key==='Enter') chat()">
      <button class="chat-btn" onclick="chat()">Ask →</button>
    </div>
    <div class="chat-response" id="chatResponse"></div>
  </div>

</div>

<script>
  let currentMode = 'full';

  function setMode(mode) {
    currentMode = mode;
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    event.target.classList.add('active');
    // Show/hide optional fields
    const showExtra = ['full', 'risk'].includes(mode);
    document.getElementById('ageField').style.opacity = showExtra ? '1' : '0.4';
    document.getElementById('genderField').style.opacity = showExtra ? '1' : '0.4';
  }

  function onFileChange() {
    const f = document.getElementById('pdfFile').files[0];
    document.getElementById('analyzeBtn').disabled = !f;
  }

  function getEndpoint() {
    const map = {
      full: '/report/full-analysis',
      summary: '/report/summary',
      labs: '/report/lab-analysis',
      risk: '/report/risk-score',
    };
    return map[currentMode];
  }

  async function analyze() {
    const file = document.getElementById('pdfFile').files[0];
    if (!file) return;

    // Reset UI
    document.getElementById('results').classList.remove('visible');
    document.getElementById('errorBox').classList.remove('visible');
    document.getElementById('loading').classList.add('visible');
    document.getElementById('analyzeBtn').disabled = true;

    const fd = new FormData();
    fd.append('file', file);
    const age    = document.getElementById('ageInput').value;
    const gender = document.getElementById('genderInput').value;
    if (age)    fd.append('age', age);
    if (gender) fd.append('gender', gender);

    try {
      const res  = await fetch(getEndpoint(), { method: 'POST', body: fd });
      const data = await res.json();

      if (!res.ok || data.error) {
        throw new Error(data.detail || data.error || 'Analysis failed');
      }

      document.getElementById('loading').classList.remove('visible');
      renderResults(data, currentMode);

    } catch(e) {
      document.getElementById('loading').classList.remove('visible');
      const eb = document.getElementById('errorBox');
      eb.innerHTML = '❌ <strong>Error:</strong> ' + e.message;
      eb.classList.add('visible');
    } finally {
      document.getElementById('analyzeBtn').disabled = false;
    }
  }

  function renderResults(data, mode) {
    const results = document.getElementById('results');
    const grid    = document.getElementById('resultsGrid');
    grid.innerHTML = '';

    let analysis = data.analysis || data.summary || data.lab_analysis || data.risk || {};

    // Normalize by mode
    if (mode === 'summary') renderSummaryMode(analysis, data.filename);
    else if (mode === 'labs') renderLabsMode(analysis, data.filename);
    else if (mode === 'risk') renderRiskMode(analysis, data.filename);
    else renderFullMode(analysis, data.filename);

    results.classList.add('visible');
    results.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function renderFullMode(a, filename) {
    // Patient bar
    const pi = a.patient_info || {};
    document.getElementById('patientBar').innerHTML = `
      <div class="patient-bar-item">
        <span class="patient-bar-label">Patient</span>
        <span class="patient-bar-value">${pi.name || 'Unknown'}</span>
      </div>
      <div class="patient-divider"></div>
      <div class="patient-bar-item">
        <span class="patient-bar-label">Age</span>
        <span class="patient-bar-value">${pi.age || '—'}</span>
      </div>
      <div class="patient-divider"></div>
      <div class="patient-bar-item">
        <span class="patient-bar-label">Gender</span>
        <span class="patient-bar-value">${pi.gender || '—'}</span>
      </div>
      <div class="patient-divider"></div>
      <div class="patient-bar-item">
        <span class="patient-bar-label">File</span>
        <span class="patient-bar-value" style="font-size:13px">${filename}</span>
      </div>
    `;

    // One-liner
    const s = a.summary || {};
    document.getElementById('oneLiner').textContent = s.one_line_summary || s.diagnosis || 'Analysis complete.';

    const grid = document.getElementById('resultsGrid');

    // Summary card
    grid.innerHTML += buildSummaryCard(s);

    // Lab card
    const lab = a.lab_analysis || {};
    if (lab.findings) grid.innerHTML += buildLabCard(lab);

    // Risk card
    const risk = a.risk_assessment || {};
    if (risk.readmission_risk_percent !== undefined) grid.innerHTML += buildRiskCard(risk);

    // Bed card
    const bed = a.bed_management || {};
    if (bed.recommended_ward) grid.innerHTML += buildBedCard(bed);

    // Doctor advice
    if (a.doctor_advice) {
      document.getElementById('adviceSection').innerHTML = `
        <div class="advice-box">
          <div class="advice-header">🩺 AI Clinical Advice for Doctor</div>
          ${a.doctor_advice}
        </div>`;
    }
  }

  function renderSummaryMode(a, filename) {
    document.getElementById('patientBar').innerHTML = `<div class="patient-bar-item"><span class="patient-bar-label">File</span><span class="patient-bar-value">${filename}</span></div>`;
    document.getElementById('oneLiner').textContent = a.one_line_summary || 'Summary extracted successfully.';
    document.getElementById('resultsGrid').innerHTML = buildSummaryCard(a);
    document.getElementById('adviceSection').innerHTML = '';
  }

  function renderLabsMode(a, filename) {
    document.getElementById('patientBar').innerHTML = `<div class="patient-bar-item"><span class="patient-bar-label">File</span><span class="patient-bar-value">${filename}</span></div>`;
    const overall = (a.overall_severity || 'Normal').toLowerCase();
    document.getElementById('oneLiner').innerHTML = `${a.overall_emoji || '🟢'} Lab Analysis Complete — Overall: <strong>${a.overall_severity || 'Normal'}</strong>`;
    document.getElementById('resultsGrid').innerHTML = buildLabCard(a);
    document.getElementById('adviceSection').innerHTML = '';
  }

  function renderRiskMode(a, filename) {
    document.getElementById('patientBar').innerHTML = `<div class="patient-bar-item"><span class="patient-bar-label">File</span><span class="patient-bar-value">${filename}</span></div>`;
    const risk = a.readmission_risk_percent !== undefined ? a : {};
    const bed  = a.bed_management || {};
    document.getElementById('oneLiner').textContent = a.priority_message || 'Risk assessment complete.';
    let html = '';
    if (Object.keys(risk).length) html += buildRiskCard(risk);
    if (bed.recommended_ward) html += buildBedCard(bed);
    document.getElementById('resultsGrid').innerHTML = html;
    document.getElementById('adviceSection').innerHTML = '';
  }

  // ── Card Builders ──────────────────────────────────────────

  function buildSummaryCard(s) {
    const rows = [
      ['Chief Complaint', s.chief_complaint],
      ['History',         s.history],
      ['Examination',     s.examination],
      ['Diagnosis',       s.diagnosis],
      ['Treatment',       s.treatment],
      ['Recommendations', s.recommendations],
    ].filter(([k,v]) => v && v !== 'Not mentioned').map(([k,v]) => `
      <div class="summary-row">
        <div class="row-label">${k}</div>
        <div class="row-value">${v}</div>
      </div>`).join('');

    return `
      <div class="card">
        <div class="card-header">
          <div class="card-icon" style="background:rgba(59,130,246,0.15)">📋</div>
          <div>
            <div class="card-title">Patient Summary</div>
            <div class="card-subtitle">Clinical overview</div>
          </div>
        </div>
        ${rows}
      </div>`;
  }

  function buildLabCard(lab) {
    const sev = (lab.overall_severity || 'Normal').toLowerCase();
    const findings = (lab.findings || []).map(f => {
      const s = (f.status || f.severity || 'Normal').toLowerCase();
      const flag = (f.flag || 'NORMAL').toUpperCase();
      return `<tr>
        <td><strong>${f.parameter}</strong></td>
        <td>${f.value ?? '—'} <span style="color:var(--muted)">${f.unit || ''}</span></td>
        <td style="color:var(--muted)">${f.normal_range || '—'}</td>
        <td><span class="flag-${flag.toLowerCase()}">${flag}</span></td>
        <td><span class="sev-badge sev-${s}">${f.emoji || ''} ${f.status || f.severity || 'Normal'}</span></td>
      </tr>`;
    }).join('');

    const alerts = (lab.alerts || []).map(a => `<div>${a}</div>`).join('');

    return `
      <div class="card">
        <div class="card-header">
          <div class="card-icon" style="background:rgba(6,182,212,0.15)">🔬</div>
          <div>
            <div class="card-title">Lab Analysis</div>
            <div class="card-subtitle">Abnormality detection</div>
          </div>
        </div>

        <div class="severity-banner sev-banner-${sev}">
          <span class="sev-banner-text">${lab.overall_emoji || ''} Overall: ${lab.overall_severity || 'Normal'}</span>
          <span class="sev-banner-counts">
            🔴 ${lab.critical_count||0} Critical &nbsp;
            🟠 ${lab.moderate_count||0} Moderate &nbsp;
            🟡 ${lab.mild_count||0} Mild &nbsp;
            🟢 ${lab.normal_count||0} Normal
          </span>
        </div>

        ${findings ? `
        <table class="lab-table">
          <thead><tr>
            <th>Parameter</th><th>Value</th><th>Normal Range</th><th>Flag</th><th>Status</th>
          </tr></thead>
          <tbody>${findings}</tbody>
        </table>` : '<div style="color:var(--muted);font-size:13px">No lab values detected in this report.</div>'}

        ${alerts ? `<div class="alert-box">${alerts}</div>` : ''}
      </div>`;
  }

  function buildRiskCard(risk) {
    const r = risk.readmission_risk_percent || 0;
    const c = risk.complication_risk_percent || 0;
    const priority = (risk.appointment_priority || 'NORMAL').toUpperCase();
    const pClass   = 'priority-' + priority.toLowerCase().replace(/\s.*/, '');

    const rColor = r > 70 ? '#ef4444' : r > 50 ? '#f97316' : r > 30 ? '#f59e0b' : '#10b981';
    const cColor = c > 70 ? '#ef4444' : c > 50 ? '#f97316' : c > 30 ? '#f59e0b' : '#10b981';

    const factors = (risk.key_risk_factors || []).map(f =>
      `<span class="risk-tag">${f}</span>`).join('');

    return `
      <div class="card">
        <div class="card-header">
          <div class="card-icon" style="background:rgba(239,68,68,0.12)">📊</div>
          <div>
            <div class="card-title">Risk Assessment</div>
            <div class="card-subtitle">ML-powered prediction</div>
          </div>
        </div>

        <div class="risk-grid">
          <div class="risk-card">
            <div class="risk-percent" style="color:${rColor}">${r}%</div>
            <div class="risk-label">Readmission Risk (30d)</div>
            <div class="risk-bar-wrap">
              <div class="risk-bar" style="width:${r}%;background:${rColor}"></div>
            </div>
          </div>
          <div class="risk-card">
            <div class="risk-percent" style="color:${cColor}">${c}%</div>
            <div class="risk-label">Complication Risk</div>
            <div class="risk-bar-wrap">
              <div class="risk-bar" style="width:${c}%;background:${cColor}"></div>
            </div>
          </div>
        </div>

        <div class="priority-badge ${pClass}">
          <span>${priority === 'URGENT' ? '🚨' : priority === 'HIGH' ? '⚠️' : priority === 'MEDIUM' ? '📌' : '✅'}</span>
          <span>${priority}</span>
          <span style="font-size:12px;font-weight:400">${risk.priority_message || ''}</span>
        </div>

        ${factors ? `<div style="margin-top:8px"><div style="font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:0.5px;margin-bottom:8px">Key Risk Factors</div><div class="risk-factors">${factors}</div></div>` : ''}
      </div>`;
  }

  function buildBedCard(bed) {
    return `
      <div class="card">
        <div class="card-header">
          <div class="card-icon" style="background:rgba(139,92,246,0.15)">🛏️</div>
          <div>
            <div class="card-title">Bed Management</div>
            <div class="card-subtitle">Ward assignment & discharge planning</div>
          </div>
        </div>
        <div class="bed-grid">
          <div class="bed-stat">
            <div class="bed-value">${bed.recommended_ward || '—'}</div>
            <div class="bed-label">Recommended Ward</div>
          </div>
          <div class="bed-stat">
            <div class="bed-value">${bed.estimated_stay_days ?? '—'}</div>
            <div class="bed-label">Est. Days</div>
          </div>
        </div>
        ${bed.discharge_note ? `<div style="margin-top:16px;color:var(--muted);font-size:13px">${bed.discharge_note}</div>` : ''}
      </div>`;
  }

  // ── Chat ───────────────────────────────────────────────────
  async function chat() {
    const q = document.getElementById('chatInput').value.trim();
    if (!q) return;

    const box = document.getElementById('chatResponse');
    box.textContent = 'Thinking...';
    box.classList.add('visible');

    try {
      const res  = await fetch(`/agent/chat?message=${encodeURIComponent(q)}`);
      const data = await res.json();
      const ans  = data.response?.answer || JSON.stringify(data.response, null, 2);
      box.textContent = ans;
    } catch(e) {
      box.textContent = 'Error: ' + e.message;
    }
  }
</script>
</body>
</html>"""

