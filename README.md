# 🎯 GetAJob — ATS Resume & Portfolio Analyzer for Tech Juniors

> **Find your skill gap. Build what you're missing.**  
> Built strictly according to the **GetAJob UX/UI Package Specification** (Dark Technical / Developer Tools Aesthetic).

---

## 🚀 Overview
**GetAJob** is an intelligent web application designed for junior tech candidates. Instead of generic ATS keyword stuffing, it:
1. **Identifies Exact Skill Gaps**: Pinpoints missing technologies against the job description with severity levels (`[ HIGH ]`, `[ MEDIUM ]`, `[ LOW ]`).
2. **Rewrites CV Bullets (Impact-Action Optimizer)**: Converts passive, unquantified bullets into Google-standard XYZ achievements (*"Accomplished [X] measured by [Y], by doing [Z]"*).
3. **Turn Skill Gaps into a Project**: Generates a tailored, production-grade GitHub portfolio project blueprint with architectural stack, implementation steps, and a ready-to-use `README.md`.
4. **49 Canonical Learning Paths & Certifications**: Recommends accredited courses and certifications (ACM, Figma, MDN, Cisco, AWS, Microsoft, Red Hat) to bridge missing skills.
5. **⭐ Flagship UX/UI Designer Track**: Deep-dive industry requirements for Junior UX/UI Designers (Figma Auto-layout/Tokens, User Research, Usability Testing, Design Systems, and Portfolio Case Studies).

---

## 🛠️ Tech Stack & Design System
- **Frontend & App Framework**: Streamlit (Python)
- **Design Tokens (UX/UI Package)**:
  - Background: `#0B0F19`
  - Surface / Cards: `#131A2A`
  - Surface Secondary: `#1B2436`
  - Primary Accent: `#6C63FF`
  - Success / Online: `#22C55E`
  - Typography: `Assistant`, `Heebo`, and `JetBrains Mono`
- **Data & Models**: Pydantic v2 schemas, Google Gemini API fallback / instant cached presets.

---

## 💻 Running Locally

### 1. Clone the repository
```bash
git clone https://github.com/osher66/GetAJob.git
cd GetAJob
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the app
```bash
streamlit run app.py
```
Then open `http://localhost:8501` in your browser.

---

## 🌐 Deploy to Streamlit Cloud (1-Click)
1. Go to [share.streamlit.io](https://share.streamlit.io).
2. Connect your GitHub account.
3. Select this repository: `osher66/GetAJob`.
4. Main file path: `app.py`.
5. Click **Deploy**!
