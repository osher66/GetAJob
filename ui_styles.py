"""
ui_styles.py - מערכת העיצוב המלאה של GetAJob
עיצוב בהיר מונגש (Accessible Light Mode - WCAG AAA Contrast)
כולל תיקון מלא של גליץ' הטאבים (הסרת פסים שחורים), פיצ'ר מעקב התקדמות ל-UX/UI,
ופרופורציות מדויקות של כפתורים, מרווחים וכרטיסים.
"""

import textwrap

def get_custom_css() -> str:
    """
    מחזיר את קובץ ה-CSS המלא לעיצוב בהיר מונגש עם ניגודיות מלאה.
    """
    css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;500;600;700;800&family=Heebo:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

    :root {
        --bg-main: #f8faff;
        --surface-card: #ffffff;
        --surface-secondary: #f1f5f9;
        --surface-elevated: #ffffff;
        --primary-accent: #4f46e5;
        --primary-hover: #4338ca;
        --primary-glow: rgba(79, 70, 229, 0.25);
        --text-primary: #0f172a;
        --text-secondary: #334155;
        --text-muted: #64748b;
        --border-color: #cbd5e1;
        --border-focus: #4f46e5;
        --color-success: #16a34a;
        --color-warning: #d97706;
        --color-critical: #dc2626;
        --font-sans: 'Assistant', 'Heebo', -apple-system, sans-serif;
        --font-mono: 'JetBrains Mono', monospace;
    }

    /* Base Body & App View - Full RTL Enforcement */
    html, body, [data-testid="stAppViewContainer"], .main,
    [data-testid="stMarkdownContainer"],
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] span,
    [data-testid="stMarkdownContainer"] div,
    [data-testid="stMarkdownContainer"] h1,
    [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMarkdownContainer"] h3,
    [data-testid="stMarkdownContainer"] h4,
    [data-testid="stMarkdownContainer"] label,
    .stMarkdown, .stText {
        background-color: var(--bg-main);
        color: var(--text-primary);
        font-family: var(--font-sans) !important;
        direction: rtl !important;
        text-align: right !important;
    }

    bdi, [dir="rtl"] {
        unicode-bidi: isolate !important;
    }

    [data-testid="stHeader"] {
        background: transparent !important;
    }

    /* Container Spacing & Maximum Width */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3.5rem !important;
        max-width: 1200px !important;
        direction: rtl !important;
        text-align: right !important;
    }

    /* Typography Hierarchy */
    h1, h2, h3 {
        font-family: var(--font-sans) !important;
        color: var(--text-primary) !important;
        font-weight: 800 !important;
        letter-spacing: -0.02em;
        text-align: right !important;
        direction: rtl !important;
    }
    h1 { font-size: 30px !important; }
    h2 { font-size: 24px !important; }
    h3 { font-size: 18px !important; }
    h4, h5, h6 {
        color: var(--text-primary) !important;
        font-weight: 700 !important;
        text-align: right !important;
        direction: rtl !important;
    }

    /* Header Bar & Server Status */
    .app-header-bar {
        background: var(--surface-card);
        border: 1.5px solid var(--border-color);
        border-radius: 20px;
        padding: 16px 24px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 24px;
        box-shadow: 0 4px 18px rgba(15, 23, 42, 0.05);
    }
    .status-server-online {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: #ecfdf5;
        border: 1.5px solid #a7f3d0;
        color: #065f46;
        font-weight: 700;
        font-size: 13px;
        padding: 5px 14px;
        border-radius: 9999px;
    }
    .status-dot-pulse {
        width: 8px;
        height: 8px;
        background: #10b981;
        border-radius: 50%;
        box-shadow: 0 0 8px #10b981;
        display: inline-block;
        animation: pulse-glow 2s infinite ease-in-out;
    }
    @keyframes pulse-glow {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.5; transform: scale(0.85); }
    }

    /* Cards & Containers */
    .custom-card, .onboarding-card {
        background-color: var(--surface-card) !important;
        border: 1.5px solid var(--border-color) !important;
        border-radius: 20px !important;
        padding: 24px 28px !important;
        box-shadow: 0 4px 18px rgba(15, 23, 42, 0.06) !important;
        margin-bottom: 20px !important;
        direction: rtl !important;
        text-align: right !important;
    }

    /* Form Labels */
    .stWidgetLabel, label[data-testid="stWidgetLabel"] {
        direction: rtl !important;
        text-align: right !important;
        font-weight: 700 !important;
        color: var(--text-primary) !important;
        margin-bottom: 8px !important;
        font-size: 15px !important;
        display: block !important;
    }

    /* Inputs & Textareas */
    .stTextInput input, .stTextArea textarea {
        direction: rtl !important;
        text-align: right !important;
        background-color: #ffffff !important;
        border: 1.5px solid var(--border-color) !important;
        color: var(--text-primary) !important;
        border-radius: 14px !important;
        font-size: 15px !important;
        line-height: 1.6 !important;
        padding: 12px 16px !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04) !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: var(--primary-accent) !important;
        box-shadow: 0 0 0 3px var(--primary-glow) !important;
        background-color: #ffffff !important;
    }
    .stTextInput input::placeholder, .stTextArea textarea::placeholder {
        color: #94a3b8 !important;
    }

    /* Primary & Secondary Buttons - Proportional & Accessible */
    button[kind="primary"], .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #4f46e5 0%, #4338ca 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        font-size: 15.5px !important;
        padding: 10px 24px !important;
        box-shadow: 0 3px 12px rgba(79, 70, 229, 0.25) !important;
        transition: all 0.2s ease !important;
    }
    button[kind="primary"]:hover, .stButton > button[kind="primary"]:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 5px 16px rgba(79, 70, 229, 0.35) !important;
    }
    button[kind="secondary"], .stButton > button[kind="secondary"], .stButton > button:not([kind="primary"]) {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1.5px solid var(--border-color) !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        padding: 9px 20px !important;
        box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04) !important;
        transition: all 0.2s ease !important;
    }
    button[kind="secondary"]:hover, .stButton > button:not([kind="primary"]):hover {
        background-color: #f8fafc !important;
        border-color: #94a3b8 !important;
        color: #4f46e5 !important;
        transform: translateY(-1px) !important;
    }

    /* TABS FIX - Completely eliminate BaseWeb horizontal lines and clipping */
    .stTabs [data-baseweb="tab-highlight"],
    .stTabs [data-baseweb="tab-border"] {
        display: none !important;
        height: 0 !important;
        background: transparent !important;
    }
    .stTabs [data-baseweb="tab-list"] {
        background-color: #f1f5f9 !important;
        border: 1.5px solid #cbd5e1 !important;
        border-radius: 16px !important;
        padding: 6px !important;
        gap: 8px !important;
        direction: rtl !important;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 12px !important;
        color: #334155 !important;
        font-weight: 700 !important;
        font-size: 14.5px !important;
        padding: 10px 20px !important;
        border: none !important;
        background: transparent !important;
        transition: all 0.2s ease !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #e2e8f0 !important;
        color: #0f172a !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: #4f46e5 !important;
        color: #ffffff !important;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3) !important;
    }

    /* Match Score Container (Light Mode) */
    .score-hero-container {
        background: #ffffff;
        border: 1.5px solid #cbd5e1;
        border-radius: 24px;
        padding: 26px 30px;
        display: flex;
        align-items: center;
        gap: 28px;
        margin-bottom: 24px;
        box-shadow: 0 4px 20px rgba(15, 23, 42, 0.06);
        direction: rtl;
        text-align: right;
    }
    .score-circle-badge {
        width: 105px;
        height: 105px;
        border-radius: 50%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        font-family: var(--font-sans);
        font-weight: 800;
        font-size: 32px;
        flex-shrink: 0;
        background: #ffffff;
        border: 4px solid var(--primary-accent);
        color: #0f172a;
        box-shadow: 0 4px 16px rgba(79, 70, 229, 0.15);
    }
    .score-circle-high {
        border-color: #16a34a;
        color: #16a34a;
        box-shadow: 0 4px 16px rgba(22, 163, 74, 0.2);
    }
    .score-circle-med {
        border-color: #d97706;
        color: #d97706;
        box-shadow: 0 4px 16px rgba(217, 119, 6, 0.2);
    }
    .score-circle-low {
        border-color: #dc2626;
        color: #dc2626;
        box-shadow: 0 4px 16px rgba(220, 38, 38, 0.2);
    }

    /* Severity Badges (Light Mode) */
    .badge-high {
        background: #fef2f2 !important;
        border: 1.5px solid #f87171 !important;
        color: #991b1b !important;
    }
    .badge-med {
        background: #fffbeb !important;
        border: 1.5px solid #fcd34d !important;
        color: #92400e !important;
    }
    .badge-low {
        background: #f0f9ff !important;
        border: 1.5px solid #7dd3fc !important;
        color: #075985 !important;
    }
    .skill-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 6px 14px;
        border-radius: 9999px;
        font-size: 13.5px;
        font-weight: 700;
        margin: 4px;
        direction: ltr;
    }

    /* Before / After Compare Container (Light Mode) */
    .compare-card-container {
        background: #ffffff;
        border: 1.5px solid #cbd5e1;
        border-radius: 18px;
        padding: 20px 24px;
        margin-bottom: 16px;
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
        direction: rtl;
        text-align: right;
    }
    .compare-side {
        padding: 14px 18px;
        border-radius: 14px;
        margin-bottom: 10px;
        font-size: 14.5px;
        line-height: 1.6;
        direction: rtl;
        text-align: right;
    }
    .compare-original-side {
        background: #fef2f2;
        border: 1.5px solid #fca5a5;
        color: #7f1d1d;
    }
    .compare-improved-side {
        background: #f0fdf4;
        border: 1.5px solid #86efac;
        color: #14532d;
        font-weight: 600;
    }

    /* README Container */
    .readme-dark-editor {
        background: #0f172a;
        border: 1.5px solid #334155;
        border-radius: 18px;
        padding: 22px 26px;
        direction: ltr;
        text-align: left;
        font-family: var(--font-mono);
        font-size: 13.5px;
        color: #f8fafc;
        line-height: 1.65;
        overflow-x: auto;
    }

    /* Onboarding Flow Pagination Dots */
    .onboarding-dots {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        margin: 20px 0;
    }
    .onboarding-dot {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: #cbd5e1;
        transition: all 0.3s ease;
    }
    .onboarding-dot.active {
        width: 34px;
        border-radius: 9999px;
        background: var(--primary-accent);
        box-shadow: 0 0 10px var(--primary-glow);
    }
    </style>
    """
    return textwrap.dedent(css).strip()


def render_step_bar(current_step: int = 1) -> str:
    """סרגל שלבים מעוצב למסך הראשי בעיצוב בהיר"""
    steps = [
        (1, "טעינת קו\"ח ומשרה"),
        (2, "ניתוח פערים ושכתוב"),
        (3, "מפרט פרויקט ו-README"),
    ]
    items = []
    for num, title in steps:
        if num <= current_step:
            border_color = "#4f46e5"
            bg_color = "#ede9fe"
            text_color = "#3730a3"
            num_bg = "#4f46e5"
        else:
            border_color = "#cbd5e1"
            bg_color = "#ffffff"
            text_color = "#64748b"
            num_bg = "#94a3b8"
        
        items.append(f"""
        <div style="flex: 1; min-width: 170px; background: {bg_color}; border: 1.5px solid {border_color}; border-radius: 9999px; padding: 8px 18px; display: flex; align-items: center; gap: 10px; color: {text_color}; font-weight: 700; font-size: 14px; direction: rtl;">
        <span style="background: {num_bg}; color: #ffffff; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 800;">{num}</span>
        <span>{title}</span>
        </div>
        """)
    return f"""<div style="display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 22px; direction: rtl;">{"".join(items)}</div>"""


def render_ats_tip() -> str:
    """כרטיס טיפ מקצועי לעמידה ב-ATS בעיצוב בהיר"""
    html = """
    <div style="background: #f5f3ff; border: 1.5px solid #c7d2fe; border-radius: 18px; padding: 18px 24px; margin-bottom: 22px; display: flex; align-items: flex-start; gap: 14px; direction: rtl; text-align: right;">
    <div style="width: 38px; height: 38px; border-radius: 12px; background: #ede9fe; color: #4f46e5; display: flex; align-items: center; justify-content: center; font-size: 20px; flex-shrink: 0; border: 1px solid #c7d2fe;">💡</div>
    <div style="flex: 1;">
    <strong style="color: #3730a3; font-size: 15.5px; display: block; margin-bottom: 4px;">
    טיפ מקצועי למעבר סינון ראשוני (Strict ATS):
    </strong>
    <p style="margin: 0; color: #334155; font-size: 14.5px; line-height: 1.6;">
    מערכות גיוס מודרניות (Greenhouse, Workday, Lever) בודקות מילות מפתח בהקשר מעשי. 
    הנוסחה המנצחת של Google לקורות חיים היא: 
    <span style="color: #4338ca; font-weight: 700; direction: ltr; display: inline-block;">"Accomplished [X] as measured by [Y], by doing [Z]"</span>
    (השגת יעד מדיד באמצעות טכנולוגיה ספציפית).
    </p>
    </div>
    </div>
    """
    return textwrap.dedent(html).strip()


def render_score_gauge(score: int, summary: str) -> str:
    """מד ציון התאמה הנדסי בעיצוב בהיר מונגש"""
    if score >= 75:
        circle_class = "score-circle-high"
        status_text = "התאמה גבוהה (מוכן להגשה)"
        subtext = "קורות החיים מציגים את רוב דרישות הסף המרכזיות."
        badge_style = "background: #ecfdf5; color: #065f46; border: 1.5px solid #6ee7b7;"
    elif score >= 50:
        circle_class = "score-circle-med"
        status_text = "התאמה בינונית (דורשת שדרוג)"
        subtext = "קיימת תשתית טובה, אך חסרות טכנולוגיות מפתח להבטחת מעבר סינון."
        badge_style = "background: #fffbeb; color: #92400e; border: 1.5px solid #fcd34d;"
    else:
        circle_class = "score-circle-low"
        status_text = "פער הנדסי משמעותי"
        subtext = "מומלץ לבנות פרויקט ממוקד בפורטפוליו לפני הגשת מועמדות."
        badge_style = "background: #fef2f2; color: #991b1b; border: 1.5px solid #fca5a5;"

    html = f"""
    <div class="score-hero-container">
    <div class="score-circle-badge {circle_class}">
    <div style="font-size: 32px; line-height: 1; font-weight: 800;">{score}%</div>
    <div style="font-size: 11px; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">MATCH</div>
    </div>
    <div style="flex: 1; direction: rtl; text-align: right;">
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px; flex-wrap: wrap;">
    <h3 style="margin: 0; font-size: 20px; font-weight: 800; color: #0f172a;">ציון התאמה הנדסי משוקלל</h3>
    <span style="font-size: 13px; font-weight: 700; padding: 4px 14px; border-radius: 9999px; {badge_style}">
    {status_text}
    </span>
    </div>
    <div style="color: #334155; font-size: 15px; line-height: 1.6; font-weight: 500;">{summary}</div>
    <div style="margin-top: 8px; color: #64748b; font-size: 13.5px;">{subtext}</div>
    </div>
    </div>
    """
    return textwrap.dedent(html).strip()


def render_skill_badges(missing_skills: list) -> str:
    """תגיות מיומנויות חסרות בעיצוב בהיר קריא ומונגש"""
    high_skills = [s for s in missing_skills if s.get("importance") == "High"]
    med_skills = [s for s in missing_skills if s.get("importance") == "Medium"]
    low_skills = [s for s in missing_skills if s.get("importance") == "Low"]

    parts = ['<div style="direction: rtl; text-align: right; margin-bottom: 20px;">']

    if high_skills:
        badges = "".join([
            f'<div class="skill-badge badge-high"><strong>{s.get("skill")}</strong> <span style="font-size: 11px; opacity: 0.9;">• HIGH</span></div>'
            for s in high_skills
        ])
        parts.append(f'<div style="margin-bottom: 14px;"><span style="font-size: 14.5px; font-weight: 800; color: #dc2626;">🔴 פערי חובה קריטיים (Must-Have):</span><div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px;">{badges}</div></div>')

    if med_skills:
        badges = "".join([
            f'<div class="skill-badge badge-med"><strong>{s.get("skill")}</strong> <span style="font-size: 11px; opacity: 0.9;">• MEDIUM</span></div>'
            for s in med_skills
        ])
        parts.append(f'<div style="margin-bottom: 14px;"><span style="font-size: 14.5px; font-weight: 800; color: #d97706;">🟡 פערים מהותיים שכדאי לגשר:</span><div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px;">{badges}</div></div>')

    if low_skills:
        badges = "".join([
            f'<div class="skill-badge badge-low"><strong>{s.get("skill")}</strong> <span style="font-size: 11px; opacity: 0.9;">• LOW</span></div>'
            for s in low_skills
        ])
        parts.append(f'<div style="margin-bottom: 14px;"><span style="font-size: 14.5px; font-weight: 800; color: #0284c7;">🔵 מיומנויות יתרון (Nice-to-Have):</span><div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px;">{badges}</div></div>')

    parts.append('</div>')
    return "".join(parts)


def render_bullet_comparison(improvements: list) -> str:
    """שדרוג סעיפי קורות חיים Before / After בעיצוב בהיר מונגש"""
    cards = []
    for i, item in enumerate(improvements, 1):
        orig = item.get("original", "")
        imp = item.get("improved", "")
        reason = item.get("reason", "")
        
        card = f"""
        <div class="compare-card-container">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
        <span style="font-weight: 800; color: #3730a3; font-size: 15.5px;">
        📌 סעיף {i}: שדרוג מבוסס Action-Impact (מוכן להעתקה לקו"ח)
        </span>
        <span style="font-size: 12px; background: #ecfdf5; color: #065f46; padding: 4px 14px; border-radius: 9999px; font-weight: 700; border: 1px solid #6ee7b7;">
        ATS Optimized ✔
        </span>
        </div>
        <div class="compare-side compare-original-side">
        <span style="font-size: 13px; font-weight: 800; display: block; color: #dc2626; margin-bottom: 4px;">
        ✖ נוסח מקורי בקו"ח (פסיבי / חסר נתונים):
        </span>
        {orig}
        </div>
        <div class="compare-side compare-improved-side">
        <span style="font-size: 13px; font-weight: 800; display: block; color: #16a34a; margin-bottom: 4px;">
        ✔ נוסח משודרג וממוקד משרה (Action + Scale + Impact):
        </span>
        {imp}
        </div>
        <div style="margin-top: 10px; display: flex; align-items: center; gap: 8px;">
        <span style="color: #4338ca; font-size: 13.5px; font-weight: 600;">💡 למה זה מקפיץ את הסיכוי? {reason}</span>
        </div>
        </div>
        """
        cards.append(textwrap.dedent(card).strip())
    return "".join(cards)


def render_onboarding_progress(current_step: int, total_steps: int = 3) -> str:
    """מחוון נקודות מובייל מעוצב"""
    dots = []
    for i in range(1, total_steps + 1):
        active_cls = "active" if i == current_step else ""
        dots.append(f'<div class="onboarding-dot {active_cls}"></div>')
    return f'<div class="onboarding-dots">{"".join(dots)}</div>'


def render_career_intel(domain: dict) -> str:
    """כרטיס סקירה מקצועית מעמיקה עבור התחום שנבחר בעיצוב בהיר מונגש"""
    title = domain["title"]
    icon = domain["icon"]
    desc = domain["short_desc"]
    demand = domain["demand_level"]
    salary = domain["salary_range"]
    reality = domain["market_reality"]
    project = domain["recommended_project_type"]
    must_skills = domain["must_have_skills"]
    good_skills = domain["good_to_have_skills"]

    must_html = "".join([f'<span class="skill-badge badge-med" style="font-size: 13px;">{s}</span>' for s in must_skills])
    good_html = "".join([f'<span class="skill-badge badge-low" style="font-size: 13px;">{s}</span>' for s in good_skills])

    html = f"""
    <div style="direction: rtl !important; text-align: right !important; background: var(--surface-card); border: 1.5px solid var(--border-color); border-radius: 24px; padding: 26px 30px; box-shadow: 0 4px 20px rgba(15, 23, 42, 0.05); margin-bottom: 24px;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; margin-bottom: 18px; border-bottom: 1.5px solid #e2e8f0; padding-bottom: 16px; direction: rtl !important;">
    <div style="display: flex; align-items: center; gap: 14px; direction: rtl !important; text-align: right !important;">
    <div style="width: 52px; height: 52px; border-radius: 16px; background: #ede9fe; color: #4f46e5; display: flex; align-items: center; justify-content: center; font-size: 26px; border: 1.5px solid #c7d2fe; flex-shrink: 0;">
    {icon}
    </div>
    <div style="text-align: right !important; direction: rtl !important;">
    <h2 style="margin: 0; font-size: 22px; font-weight: 800; color: #0f172a; text-align: right !important; direction: rtl !important;"><bdi>{title}</bdi></h2>
    <p style="margin: 4px 0 0 0; color: #475569; font-size: 14.5px; font-weight: 500; text-align: right !important; direction: rtl !important;"><bdi>{desc}</bdi></p>
    </div>
    </div>
    <div style="display: flex; gap: 8px; flex-wrap: wrap; direction: rtl !important;">
    <span style="background: #ecfdf5; color: #065f46; border: 1px solid #6ee7b7; border-radius: 9999px; padding: 5px 14px; font-size: 13px; font-weight: 700; direction: rtl !important;"><bdi>{demand}</bdi></span>
    <span style="background: #ede9fe; color: #3730a3; border: 1px solid #c7d2fe; border-radius: 9999px; padding: 5px 14px; font-size: 13px; font-weight: 700; direction: rtl !important;"><bdi>💰 {salary}</bdi></span>
    </div>
    </div>
    <div style="margin-bottom: 18px; text-align: right !important; direction: rtl !important;">
    <h4 style="color: #0f172a; font-weight: 800; margin-bottom: 8px; text-align: right !important; direction: rtl !important;">📌 מה השוק והמגייסים באמת מחפשים כיום?</h4>
    <p style="color: #334155; font-size: 14.5px; line-height: 1.65; margin: 0; background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 14px 18px; text-align: right !important; direction: rtl !important;"><bdi>{reality}</bdi></p>
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 20px; direction: rtl !important;">
    <div style="background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 16px; padding: 16px 18px; text-align: right !important; direction: rtl !important;">
    <strong style="color: #b45309; font-size: 14px; display: block; margin-bottom: 8px; text-align: right !important;">🔥 סטאק טכנולוגי חובה (דרישות סף):</strong>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; direction: ltr; justify-content: flex-end;">{must_html}</div>
    </div>
    <div style="background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 16px; padding: 16px 18px; text-align: right !important; direction: rtl !important;">
    <strong style="color: #0369a1; font-size: 14px; display: block; margin-bottom: 8px; text-align: right !important;">⚡ טכנולוגיות יתרון שיבדילו אותך:</strong>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; direction: ltr; justify-content: flex-end;">{good_html}</div>
    </div>
    </div>
    <div style="background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 16px; padding: 16px 20px; text-align: right !important; direction: rtl !important;">
    <strong style="color: #4338ca; font-size: 14px; display: block; margin-bottom: 6px; text-align: right !important;">🚀 סוג הפרויקט המומלץ לפורטפוליו שלך:</strong>
    <p style="margin: 0; color: #334155; font-size: 14px; line-height: 1.6; text-align: right !important; direction: rtl !important;"><bdi>{project}</bdi></p>
    </div>
    </div>
    """
    return textwrap.dedent(html).strip()


def render_learning_paths(paths: list) -> str:
    """מחולל כרטיסי מסלולי לימוד והסמכות מתוך מאגר ה-49 מסלולים בעיצוב בהיר"""
    if not paths:
        return """
        <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 16px; padding: 20px; text-align: center; color: #64748b;">
        לא נמצאו מסלולי לימוד ישירים עבור מיומנויות אלו במאגר המסלולים.
        </div>
        """

    cards = []
    for lp in paths:
        name = lp.get("name", "")
        domain = lp.get("domain", "")
        lp_type = lp.get("type", "")
        level = lp.get("level", "")
        duration = lp.get("duration", "")
        proof = lp.get("proof_strength", "3")
        url = lp.get("official_url", "#")
        project = lp.get("recommended_project", "")
        when_to = lp.get("when_to_recommend", "")

        try:
            p_val = int(float(proof))
        except Exception:
            p_val = 3
        stars = "★" * p_val + "☆" * (5 - p_val)

        card_html = f"""
        <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 18px; padding: 20px 24px; margin-bottom: 16px; direction: rtl; text-align: right; box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px; margin-bottom: 10px;">
        <div>
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
        <span style="background: #ede9fe; color: #3730a3; border: 1px solid #c7d2fe; border-radius: 9999px; padding: 3px 12px; font-size: 12px; font-weight: 700;">{domain} • {lp_type}</span>
        <span style="font-size: 12.5px; color: #64748b; font-weight: 600;">רמה: {level}</span>
        </div>
        <h4 style="margin: 0; font-size: 18px; font-weight: 800; color: #0f172a;">{name}</h4>
        </div>
        <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;">
        <span style="background: #ecfdf5; color: #065f46; border: 1px solid #6ee7b7; border-radius: 9999px; padding: 4px 12px; font-size: 12.5px; font-weight: 700;">⏱ משך: {duration}</span>
        <span style="background: #fffbeb; color: #92400e; border: 1px solid #fcd34d; border-radius: 9999px; padding: 4px 12px; font-size: 12.5px; font-weight: 700;">חוזק הוכחה: {stars}</span>
        </div>
        </div>
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 12px 16px; margin: 12px 0;">
        <strong style="color: #3730a3; font-size: 13.5px; display: block; margin-bottom: 3px;">🎯 מתי מומלץ על פי המודל?</strong>
        <p style="margin: 0; color: #475569; font-size: 13.5px; line-height: 1.5;">{when_to}</p>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-top: 14px;">
        <div style="flex: 1; min-width: 260px;">
        <span style="color: #4338ca; font-size: 13px; font-weight: 700;">🛠 פרויקט הוכחה מומלץ:</span>
        <span style="color: #334155; font-size: 13px;"> {project}</span>
        </div>
        <a href="{url}" target="_blank" style="background: #4f46e5; color: #ffffff; text-decoration: none; padding: 7px 18px; border-radius: 9999px; font-size: 12.5px; font-weight: 700; display: inline-flex; align-items: center; gap: 6px; box-shadow: 0 2px 8px rgba(79, 70, 229, 0.25);">
        סילבוס ומקור רשמי ↗
        </a>
        </div>
        </div>
        """
        cards.append(textwrap.dedent(card_html).strip())
    return "".join(cards)


def render_job_search_tracker(milestones: list, progress_pct: int) -> str:
    """
    רכיב מעקב התקדמות בחיפוש עבודה (UX/UI Job Search Roadmap & Progress Tracker)
    מציג גרף התקדמות, מד מוכנות לגיוס, וצ'קליסט אבני דרך אינטראקטיבי.
    """
    if progress_pct >= 80:
        bar_color = "linear-gradient(90deg, #10b981 0%, #059669 100%)"
        status_label = "🚀 מוכן לגיוס והגשות לשוק!"
        status_badge = "background: #ecfdf5; color: #065f46; border: 1.5px solid #6ee7b7;"
    elif progress_pct >= 50:
        bar_color = "linear-gradient(90deg, #4f46e5 0%, #4338ca 100%)"
        status_label = "⚡ בתהליך בנייה מתקדם"
        status_badge = "background: #ede9fe; color: #3730a3; border: 1.5px solid #c7d2fe;"
    else:
        bar_color = "linear-gradient(90deg, #f59e0b 0%, #d97706 100%)"
        status_label = "🌱 שלב ההכנה הראשוני"
        status_badge = "background: #fffbeb; color: #92400e; border: 1.5px solid #fcd34d;"

    html = f"""
    <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 24px; padding: 26px 30px; margin-bottom: 24px; box-shadow: 0 4px 20px rgba(15, 23, 42, 0.05); direction: rtl; text-align: right;">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px;">
    <div>
    <div style="display: flex; align-items: center; gap: 10px;">
    <span style="font-size: 26px;">📈</span>
    <h3 style="margin: 0; font-size: 22px; font-weight: 800; color: #0f172a;">מעקב התקדמות אישי: בדרך למשרת מעצב/ת UX/UI</h3>
    </div>
    <p style="margin: 4px 0 0 0; color: #64748b; font-size: 14.5px;">עקוב אחרי השלמת אבני הדרך להבטחת ראיון טכני ראשון</p>
    </div>
    <div style="display: flex; align-items: center; gap: 10px;">
    <span style="padding: 6px 16px; border-radius: 9999px; font-size: 13.5px; font-weight: 800; {status_badge}">
    {status_label}
    </span>
    <span style="background: #f1f5f9; color: #0f172a; padding: 6px 14px; border-radius: 9999px; font-size: 15px; font-weight: 800; border: 1px solid #cbd5e1;">
    {progress_pct}% הושלמו
    </span>
    </div>
    </div>

    <!-- סרגל גרף התקדמות ויזואלי -->
    <div style="background: #f1f5f9; border-radius: 9999px; height: 14px; overflow: hidden; margin-bottom: 20px; border: 1px solid #e2e8f0;">
    <div style="background: {bar_color}; width: {progress_pct}%; height: 100%; border-radius: 9999px; transition: width 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);"></div>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 12px; margin-top: 14px;">
    """

    for m in milestones:
        is_done = m.get("completed", False)
        icon = "✔" if is_done else "○"
        box_bg = "#f0fdf4" if is_done else "#ffffff"
        box_border = "#86efac" if is_done else "#e2e8f0"
        title_color = "#14532d" if is_done else "#0f172a"
        badge_bg = "#ecfdf5" if is_done else "#f1f5f9"
        badge_color = "#16a34a" if is_done else "#64748b"

        html += f"""
        <div style="background: {box_bg}; border: 1.5px solid {box_border}; border-radius: 16px; padding: 14px 18px; display: flex; align-items: flex-start; gap: 12px; box-shadow: 0 1px 3px rgba(15, 23, 42, 0.03);">
        <span style="background: {badge_bg}; color: {badge_color}; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 800; flex-shrink: 0;">{icon}</span>
        <div style="flex: 1;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px;">
        <strong style="color: {title_color}; font-size: 14.5px;">{m.get('title')}</strong>
        <span style="font-size: 11.5px; font-weight: 700; color: {badge_color};">{m.get('category')}</span>
        </div>
        <p style="margin: 0; color: #475569; font-size: 13px; line-height: 1.45;">{m.get('desc')}</p>
        </div>
        </div>
        """

    html += """
    </div>
    </div>
    """
    return textwrap.dedent(html).strip()
