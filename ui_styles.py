"""
ui_styles.py - מערכת העיצוב המלאה של GetAJob
מותאמת במדויק לחבילת העיצוב הרשמית: GetAJob UX/UI Package (Handoff for Developer).
פלטת צבעים (Dark Technical / Developer Tools):
- Background: #0B0F19
- Surface / Cards: #131A2A
- Surface Secondary: #1B2436
- Primary Accent: #6C63FF
- Primary Text: #F8FAFC
- Secondary Text: #94A3B8
- Status: Success (#22C55E), Warning (#F59E0B), Critical (#EF4444)
- Typography: Assistant / Heebo & JetBrains Mono
"""

import textwrap

def get_custom_css() -> str:
    """
    מחזיר את קובץ ה-CSS המותאם אישית ל-GetAJob בהתאם למסמך ה-UX/UI Package.
    כולל התאמה ל-RTL, טיפוגרפיה, פלטת צבעים מדויקת, כרטיסים ואפקטי אינטראקציה.
    """
    css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;500;600;700;800&family=Heebo:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

    :root {
        --bg-main: #0B0F19;
        --surface-card: #131A2A;
        --surface-secondary: #1B2436;
        --surface-elevated: #222C42;
        --primary-accent: #6C63FF;
        --primary-hover: #5A52E0;
        --primary-glow: rgba(108, 99, 255, 0.35);
        --text-primary: #F8FAFC;
        --text-secondary: #94A3B8;
        --text-muted: #64748B;
        --border-color: #232D42;
        --border-focus: #6C63FF;
        --color-success: #22C55E;
        --color-warning: #F59E0B;
        --color-critical: #EF4444;
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

    /* Prevent mixed Hebrew/English from flipping parentheses or trailing punctuation */
    bdi, [dir="rtl"] {
        unicode-bidi: isolate !important;
    }

    [data-testid="stHeader"] {
        background: transparent !important;
    }

    /* Container Spacing */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3.5rem !important;
        max-width: 1200px !important;
        direction: rtl !important;
        text-align: right !important;
    }

    /* Typography Hierarchy (UX/UI Package Page 13) */
    h1, h2, h3 {
        font-family: var(--font-sans) !important;
        color: var(--text-primary) !important;
        font-weight: 800 !important;
        letter-spacing: -0.02em;
        text-align: right !important;
        direction: rtl !important;
    }
    h1 { font-size: 32px !important; }
    h2 { font-size: 24px !important; }
    h3 { font-size: 18px !important; }
    h4, h5, h6 {
        color: var(--text-primary) !important;
        font-weight: 700 !important;
        text-align: right !important;
        direction: rtl !important;
    }

    /* Header Bar & Server Status (Page 5 & 9) */
    .app-header-bar {
        background: var(--surface-card);
        border: 1.5px solid var(--border-color);
        border-radius: 20px;
        padding: 16px 24px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 24px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    }
    .status-server-online {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(34, 197, 94, 0.12);
        border: 1.5px solid rgba(34, 197, 94, 0.35);
        color: var(--color-success);
        font-weight: 700;
        font-size: 13px;
        padding: 5px 14px;
        border-radius: 9999px;
    }
    .status-dot-pulse {
        width: 8px;
        height: 8px;
        background: var(--color-success);
        border-radius: 50%;
        box-shadow: 0 0 8px var(--color-success);
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
        box-shadow: 0 4px 24px rgba(0, 0, 0, 0.3) !important;
        margin-bottom: 20px !important;
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

    /* Inputs & Textareas (Page 14) */
    .stTextInput input, .stTextArea textarea {
        direction: rtl !important;
        text-align: right !important;
        background-color: var(--surface-secondary) !important;
        border: 1.5px solid var(--border-color) !important;
        color: var(--text-primary) !important;
        border-radius: 14px !important;
        font-size: 15px !important;
        line-height: 1.6 !important;
        padding: 14px 18px !important;
        transition: all 0.25s ease !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: var(--primary-accent) !important;
        box-shadow: 0 0 0 3px var(--primary-glow), 0 2px 8px rgba(0,0,0,0.4) !important;
        background-color: var(--surface-elevated) !important;
    }
    .stTextInput input::placeholder, .stTextArea textarea::placeholder {
        color: var(--text-muted) !important;
    }

    /* Primary & Secondary Buttons (Page 14) */
    button[kind="primary"], .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, var(--primary-accent) 0%, #5345EB 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 9999px !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        padding: 12px 28px !important;
        box-shadow: 0 4px 18px var(--primary-glow) !important;
        transition: all 0.25s ease !important;
    }
    button[kind="primary"]:hover, .stButton > button[kind="primary"]:hover {
        transform: translateY(-2px) scale(1.01) !important;
        box-shadow: 0 6px 24px rgba(108, 99, 255, 0.5) !important;
    }
    button[kind="secondary"], .stButton > button[kind="secondary"], .stButton > button:not([kind="primary"]) {
        background-color: var(--surface-secondary) !important;
        color: var(--text-primary) !important;
        border: 1.5px solid var(--border-color) !important;
        border-radius: 9999px !important;
        font-weight: 600 !important;
        font-size: 14.5px !important;
        padding: 10px 22px !important;
        transition: all 0.25s ease !important;
    }
    button[kind="secondary"]:hover, .stButton > button:not([kind="primary"]):hover {
        background-color: var(--surface-elevated) !important;
        border-color: #384661 !important;
        color: #ffffff !important;
        transform: translateY(-1px) !important;
    }

    /* Tabs (Page 6 & 14) */
    .stTabs [data-baseweb="tab-list"] {
        background-color: var(--surface-secondary);
        border: 1.5px solid var(--border-color);
        border-radius: 9999px;
        padding: 6px;
        gap: 6px;
        direction: rtl;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 9999px !important;
        color: var(--text-secondary) !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        padding: 8px 18px !important;
        border: none !important;
        background: transparent !important;
        transition: all 0.2s ease !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: var(--primary-accent) !important;
        color: #ffffff !important;
        box-shadow: 0 2px 10px var(--primary-glow) !important;
    }

    /* Match Score Container (Page 6 & 9) */
    .score-hero-container {
        background: linear-gradient(135deg, #131A2A 0%, #172136 100%);
        border: 1.5px solid var(--border-color);
        border-radius: 24px;
        padding: 28px 32px;
        display: flex;
        align-items: center;
        gap: 32px;
        margin-bottom: 24px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.35);
    }
    .score-circle-badge {
        width: 110px;
        height: 110px;
        border-radius: 50%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        font-family: var(--font-sans);
        font-weight: 800;
        font-size: 32px;
        flex-shrink: 0;
        box-shadow: 0 0 24px rgba(108, 99, 255, 0.3);
        border: 3px solid var(--primary-accent);
        background: #1B2436;
        color: #ffffff;
    }
    .score-circle-high {
        border-color: var(--color-success);
        box-shadow: 0 0 24px rgba(34, 197, 94, 0.35);
        color: #4ade80;
    }
    .score-circle-med {
        border-color: var(--color-warning);
        box-shadow: 0 0 24px rgba(245, 158, 11, 0.35);
        color: #fcd34d;
    }
    .score-circle-low {
        border-color: var(--color-critical);
        box-shadow: 0 0 24px rgba(239, 68, 68, 0.35);
        color: #fca5a5;
    }

    /* Severity Badges (Page 6 & 14) */
    .badge-high {
        background: rgba(239, 68, 68, 0.15) !important;
        border: 1.5px solid var(--color-critical) !important;
        color: #fca5a5 !important;
    }
    .badge-med {
        background: rgba(245, 158, 11, 0.15) !important;
        border: 1.5px solid var(--color-warning) !important;
        color: #fde047 !important;
    }
    .badge-low {
        background: rgba(56, 189, 248, 0.15) !important;
        border: 1.5px solid #38BDF8 !important;
        color: #7dd3fc !important;
    }
    .skill-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 7px 16px;
        border-radius: 9999px;
        font-size: 13.5px;
        font-weight: 700;
        margin: 4px;
        direction: ltr;
    }

    /* Before / After Compare Container (Page 6) */
    .compare-card-container {
        background: var(--surface-secondary);
        border: 1.5px solid var(--border-color);
        border-radius: 18px;
        padding: 20px 24px;
        margin-bottom: 16px;
    }
    .compare-side {
        padding: 14px 18px;
        border-radius: 14px;
        margin-bottom: 10px;
        font-size: 14.5px;
        line-height: 1.6;
    }
    .compare-original-side {
        background: rgba(239, 68, 68, 0.08);
        border: 1.5px solid rgba(239, 68, 68, 0.25);
        color: #cbd5e1;
    }
    .compare-improved-side {
        background: rgba(34, 197, 94, 0.08);
        border: 1.5px solid rgba(34, 197, 94, 0.3);
        color: #f8fafc;
        font-weight: 500;
    }

    /* Project Blueprint & Implementation Steps (Page 7 & 10) */
    .step-counter-box {
        width: 32px;
        height: 32px;
        border-radius: 10px;
        background: rgba(108, 99, 255, 0.2);
        color: #a5b4fc;
        border: 1px solid var(--primary-accent);
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: var(--font-mono);
        font-weight: 700;
        font-size: 14px;
        flex-shrink: 0;
    }

    /* README Container (Page 8 & 10) */
    .readme-dark-editor {
        background: #070A12;
        border: 1.5px solid var(--border-color);
        border-radius: 18px;
        padding: 22px 26px;
        direction: ltr;
        text-align: left;
        font-family: var(--font-mono);
        font-size: 13.5px;
        color: #e2e8f0;
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
        background: #334155;
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
    """סרגל שלבים מעוצב למסך הראשי לפי חבילת העיצוב"""
    steps = [
        (1, "טעינת קו\"ח ומשרה"),
        (2, "ניתוח פערים ושכתוב"),
        (3, "מפרט פרויקט ו-README"),
    ]
    items = []
    for num, title in steps:
        active = "active" if num <= current_step else ""
        border_color = "var(--primary-accent)" if num <= current_step else "var(--border-color)"
        bg_color = "rgba(108, 99, 255, 0.15)" if num <= current_step else "var(--surface-secondary)"
        text_color = "#ffffff" if num <= current_step else "var(--text-secondary)"
        num_bg = "var(--primary-accent)" if num <= current_step else "#334155"
        
        items.append(f"""
        <div style="flex: 1; min-width: 170px; background: {bg_color}; border: 1.5px solid {border_color}; border-radius: 9999px; padding: 8px 18px; display: flex; align-items: center; gap: 10px; color: {text_color}; font-weight: 700; font-size: 14px;">
        <span style="background: {num_bg}; color: #ffffff; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 800;">{num}</span>
        <span>{title}</span>
        </div>
        """)
    return f"""<div style="display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 22px; direction: rtl;">{"".join(items)}</div>"""


def render_ats_tip() -> str:
    """כרטיס טיפ מקצועי לעמידה ב-ATS לפי שפת העיצוב הכהה"""
    html = """
    <div style="background: rgba(108, 99, 255, 0.08); border: 1.5px solid rgba(108, 99, 255, 0.3); border-radius: 18px; padding: 18px 24px; margin-bottom: 22px; display: flex; align-items: flex-start; gap: 14px; direction: rtl; text-align: right;">
    <div style="width: 36px; height: 36px; border-radius: 12px; background: rgba(108, 99, 255, 0.25); color: #a5b4fc; display: flex; align-items: center; justify-content: center; font-size: 20px; flex-shrink: 0; border: 1px solid var(--primary-accent);">💡</div>
    <div style="flex: 1;">
    <strong style="color: #c7d2fe; font-size: 15.5px; display: block; margin-bottom: 4px;">
    טיפ מקצועי למעבר סינון ראשוני (Strict ATS):
    </strong>
    <p style="margin: 0; color: #94a3b8; font-size: 14.5px; line-height: 1.6;">
    מערכות גיוס מודרניות (Greenhouse, Workday, Lever) בודקות מילות מפתח בהקשר מעשי. 
    הנוסחה המנצחת של Google לקורות חיים היא: 
    <span style="color: #38bdf8; font-weight: 700; direction: ltr; display: inline-block;">"Accomplished [X] as measured by [Y], by doing [Z]"</span>
    (השגת יעד מדיד באמצעות טכנולוגיה ספציפית).
    </p>
    </div>
    </div>
    """
    return textwrap.dedent(html).strip()


def render_score_gauge(score: int, summary: str) -> str:
    """מד ציון התאמה הנדסי לפי עמוד 6 ב-UX/UI Package"""
    if score >= 75:
        circle_class = "score-circle-high"
        status_text = "התאמה גבוהה (מוכן להגשה)"
        subtext = "קורות החיים מציגים את רוב דרישות הסף המרכזיות."
        badge_style = "background: rgba(34, 197, 94, 0.15); color: #4ade80; border: 1.5px solid #22c55e;"
    elif score >= 50:
        circle_class = "score-circle-med"
        status_text = "התאמה בינונית (דורשת שדרוג)"
        subtext = "קיימת תשתית טובה, אך חסרות טכנולוגיות מפתח להבטחת מעבר סינון."
        badge_style = "background: rgba(245, 158, 11, 0.15); color: #fcd34d; border: 1.5px solid #f59e0b;"
    else:
        circle_class = "score-circle-low"
        status_text = "פער הנדסי משמעותי"
        subtext = "מומלץ לבנות פרויקט ממוקד בפורטפוליו לפני הגשת מועמדות."
        badge_style = "background: rgba(239, 68, 68, 0.15); color: #fca5a5; border: 1.5px solid #ef4444;"

    html = f"""
    <div class="score-hero-container">
    <div class="score-circle-badge {circle_class}">
    <div style="font-size: 32px; line-height: 1;">{score}%</div>
    <div style="font-size: 11px; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">MATCH</div>
    </div>
    <div style="flex: 1; direction: rtl; text-align: right;">
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px; flex-wrap: wrap;">
    <h3 style="margin: 0; font-size: 20px; font-weight: 800; color: #ffffff;">ציון התאמה הנדסי משוקלל</h3>
    <span style="font-size: 13px; font-weight: 700; padding: 4px 14px; border-radius: 9999px; {badge_style}">
    {status_text}
    </span>
    </div>
    <div style="color: #cbd5e1; font-size: 15px; line-height: 1.6; font-weight: 500;">{summary}</div>
    <div style="margin-top: 8px; color: #94a3b8; font-size: 13.5px;">{subtext}</div>
    </div>
    </div>
    """
    return textwrap.dedent(html).strip()


def render_skill_badges(missing_skills: list) -> str:
    """תגיות מיומנויות חסרות לפי חלוקת רמות חומרה (High / Medium / Low) בעמוד 6"""
    high_skills = [s for s in missing_skills if s.get("importance") == "High"]
    med_skills = [s for s in missing_skills if s.get("importance") == "Medium"]
    low_skills = [s for s in missing_skills if s.get("importance") == "Low"]

    parts = ['<div style="direction: rtl; text-align: right; margin-bottom: 20px;">']

    if high_skills:
        badges = "".join([
            f'<div class="skill-badge badge-high"><strong>{s.get("skill")}</strong> <span style="font-size: 11px; opacity: 0.9;">• HIGH</span></div>'
            for s in high_skills
        ])
        parts.append(f'<div style="margin-bottom: 14px;"><span style="font-size: 14.5px; font-weight: 800; color: #fca5a5;">🔴 פערי חובה קריטיים (Must-Have):</span><div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px;">{badges}</div></div>')

    if med_skills:
        badges = "".join([
            f'<div class="skill-badge badge-med"><strong>{s.get("skill")}</strong> <span style="font-size: 11px; opacity: 0.9;">• MEDIUM</span></div>'
            for s in med_skills
        ])
        parts.append(f'<div style="margin-bottom: 14px;"><span style="font-size: 14.5px; font-weight: 800; color: #fde047;">🟡 פערים מהותיים שכדאי לגשר:</span><div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px;">{badges}</div></div>')

    if low_skills:
        badges = "".join([
            f'<div class="skill-badge badge-low"><strong>{s.get("skill")}</strong> <span style="font-size: 11px; opacity: 0.9;">• LOW</span></div>'
            for s in low_skills
        ])
        parts.append(f'<div style="margin-bottom: 14px;"><span style="font-size: 14.5px; font-weight: 800; color: #7dd3fc;">🔵 מיומנויות יתרון (Nice-to-Have):</span><div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px;">{badges}</div></div>')

    parts.append('</div>')
    return "".join(parts)


def render_bullet_comparison(improvements: list) -> str:
    """שדרוג סעיפי קורות חיים Before / After לפי עמוד 6 ב-UX/UI Package"""
    cards = []
    for i, item in enumerate(improvements, 1):
        orig = item.get("original", "")
        imp = item.get("improved", "")
        reason = item.get("reason", "")
        
        card = f"""
        <div class="compare-card-container">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
        <span style="font-weight: 800; color: #a5b4fc; font-size: 15.5px;">
        📌 סעיף {i}: שדרוג מבוסס Action-Impact (מוכן להעתקה לקו"ח)
        </span>
        <span style="font-size: 12px; background: rgba(34, 197, 94, 0.15); color: #4ade80; padding: 4px 14px; border-radius: 9999px; font-weight: 700; border: 1px solid #22c55e;">
        ATS Optimized ✔
        </span>
        </div>
        <div class="compare-side compare-original-side">
        <span style="font-size: 13px; font-weight: 800; display: block; color: #f87171; margin-bottom: 4px;">
        ✖ נוסח מקורי בקו"ח (פסיבי / חסר נתונים):
        </span>
        {orig}
        </div>
        <div class="compare-side compare-improved-side">
        <span style="font-size: 13px; font-weight: 800; display: block; color: #4ade80; margin-bottom: 4px;">
        ✔ נוסח משודרג וממוקד משרה (Action + Scale + Impact):
        </span>
        {imp}
        </div>
        <div style="margin-top: 10px; display: flex; align-items: center; gap: 8px;">
        <span style="color: #a5b4fc; font-size: 13.5px; font-weight: 600;">💡 למה זה מקפיץ את הסיכוי? {reason}</span>
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
    """כרטיס סקירה מקצועית מעמיקה עבור התחום שנבחר - מיושר 100% ל-RTL ללא תיבות טקסט שבורות או מיותרות"""
    title = domain["title"]
    icon = domain["icon"]
    desc = domain["short_desc"]
    demand = domain["demand_level"]
    salary = domain["salary_range"]
    reality = domain["market_reality"]
    project = domain["recommended_project_type"]
    must_skills = domain["must_have_skills"]
    good_skills = domain["good_to_have_skills"]

    must_html = "".join([f'<span class="skill-badge badge-med" style="color: #fde047; font-size: 13px;">{s}</span>' for s in must_skills])
    good_html = "".join([f'<span class="skill-badge badge-low" style="color: #7dd3fc; font-size: 13px;">{s}</span>' for s in good_skills])

    html = f"""
    <div style="direction: rtl !important; text-align: right !important; background: var(--surface-card); border: 1.5px solid var(--border-color); border-radius: 24px; padding: 26px 30px; box-shadow: 0 4px 24px rgba(0,0,0,0.35); margin-bottom: 24px;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; margin-bottom: 18px; border-bottom: 1.5px solid var(--border-color); padding-bottom: 16px; direction: rtl !important;">
    <div style="display: flex; align-items: center; gap: 14px; direction: rtl !important; text-align: right !important;">
    <div style="width: 50px; height: 50px; border-radius: 16px; background: var(--surface-secondary); color: var(--primary-accent); display: flex; align-items: center; justify-content: center; font-size: 26px; border: 1.5px solid rgba(108, 99, 255, 0.4); flex-shrink: 0;">
    {icon}
    </div>
    <div style="text-align: right !important; direction: rtl !important;">
    <h2 style="margin: 0; font-size: 22px; font-weight: 800; color: #ffffff; text-align: right !important; direction: rtl !important;"><bdi>{title}</bdi></h2>
    <p style="margin: 4px 0 0 0; color: #94a3b8; font-size: 14.5px; font-weight: 500; text-align: right !important; direction: rtl !important;"><bdi>{desc}</bdi></p>
    </div>
    </div>
    <div style="display: flex; gap: 8px; flex-wrap: wrap; direction: rtl !important;">
    <span style="background: rgba(34, 197, 94, 0.15); color: #4ade80; border: 1px solid #22c55e; border-radius: 9999px; padding: 5px 14px; font-size: 13px; font-weight: 700; direction: rtl !important;"><bdi>{demand}</bdi></span>
    <span style="background: rgba(245, 158, 11, 0.15); color: #fcd34d; border: 1px solid #f59e0b; border-radius: 9999px; padding: 5px 14px; font-size: 13px; font-weight: 700; direction: rtl !important;"><bdi>💰 {salary}</bdi></span>
    </div>
    </div>
    <div style="margin-bottom: 18px; text-align: right !important; direction: rtl !important;">
    <h4 style="color: #ffffff; font-weight: 800; margin-bottom: 8px; text-align: right !important; direction: rtl !important;">📌 מה השוק והמגייסים באמת מחפשים כיום?</h4>
    <p style="color: #cbd5e1; font-size: 14.5px; line-height: 1.65; margin: 0; background: var(--surface-secondary); border: 1px solid var(--border-color); border-radius: 14px; padding: 14px 18px; text-align: right !important; direction: rtl !important;"><bdi>{reality}</bdi></p>
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 20px; direction: rtl !important;">
    <div style="background: var(--surface-secondary); border: 1.5px solid var(--border-color); border-radius: 16px; padding: 16px 18px; text-align: right !important; direction: rtl !important;">
    <strong style="color: #fde047; font-size: 14px; display: block; margin-bottom: 8px; text-align: right !important;">🔥 סטאק טכנולוגי חובה (דרישות סף):</strong>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; direction: ltr; justify-content: flex-end;">{must_html}</div>
    </div>
    <div style="background: var(--surface-secondary); border: 1.5px solid var(--border-color); border-radius: 16px; padding: 16px 18px; text-align: right !important; direction: rtl !important;">
    <strong style="color: #7dd3fc; font-size: 14px; display: block; margin-bottom: 8px; text-align: right !important;">⚡ טכנולוגיות יתרון שיבדילו אותך:</strong>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; direction: ltr; justify-content: flex-end;">{good_html}</div>
    </div>
    </div>
    <div style="background: var(--surface-secondary); border: 1.5px solid var(--border-color); border-radius: 16px; padding: 16px 20px; text-align: right !important; direction: rtl !important;">
    <strong style="color: #fcd34d; font-size: 14px; display: block; margin-bottom: 6px; text-align: right !important;">🚀 סוג הפרויקט המומלץ לפורטפוליו שלך:</strong>
    <p style="margin: 0; color: #cbd5e1; font-size: 14.5px; line-height: 1.6; text-align: right !important; direction: rtl !important;"><bdi>{project}</bdi></p>
    </div>
    </div>
    """
    return textwrap.dedent(html).strip()


def render_learning_paths(paths: list) -> str:
    """מחולל כרטיסי מסלולי לימוד והסמכות מתוך מאגר ה-49 מסלולים"""
    if not paths:
        return """
        <div style="background: var(--surface-secondary); border: 1.5px solid var(--border-color); border-radius: 16px; padding: 20px; text-align: center; color: var(--text-secondary);">
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
        <div style="background: var(--surface-secondary); border: 1.5px solid var(--border-color); border-radius: 18px; padding: 20px 24px; margin-bottom: 16px; direction: rtl; text-align: right;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px; margin-bottom: 10px;">
        <div>
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
        <span style="background: rgba(108, 99, 255, 0.2); color: #c7d2fe; border: 1px solid var(--primary-accent); border-radius: 9999px; padding: 3px 12px; font-size: 12px; font-weight: 700;">{domain} • {lp_type}</span>
        <span style="font-size: 12.5px; color: #94a3b8; font-weight: 600;">רמה: {level}</span>
        </div>
        <h4 style="margin: 0; font-size: 18px; font-weight: 800; color: #ffffff;">{name}</h4>
        </div>
        <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;">
        <span style="background: rgba(34, 197, 94, 0.15); color: #4ade80; border: 1px solid #22c55e; border-radius: 9999px; padding: 4px 12px; font-size: 12.5px; font-weight: 700;">⏱ משך: {duration}</span>
        <span style="background: rgba(245, 158, 11, 0.15); color: #fcd34d; border: 1px solid #f59e0b; border-radius: 9999px; padding: 4px 12px; font-size: 12.5px; font-weight: 700;">חוזק הוכחה: {stars}</span>
        </div>
        </div>
        <div style="background: #0D1322; border: 1px solid var(--border-color); border-radius: 12px; padding: 12px 16px; margin: 12px 0;">
        <strong style="color: #c7d2fe; font-size: 13.5px; display: block; margin-bottom: 3px;">🎯 מתי מומלץ על פי המודל?</strong>
        <p style="margin: 0; color: #94a3b8; font-size: 13.5px; line-height: 1.5;">{when_to}</p>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-top: 14px;">
        <div style="flex: 1; min-width: 260px;">
        <span style="color: #a5b4fc; font-size: 13px; font-weight: 700;">🛠 פרויקט הוכחה מומלץ:</span>
        <span style="color: #cbd5e1; font-size: 13px;"> {project}</span>
        </div>
        <a href="{url}" target="_blank" style="background: var(--primary-accent); color: #ffffff; text-decoration: none; padding: 7px 18px; border-radius: 9999px; font-size: 12.5px; font-weight: 700; display: inline-flex; align-items: center; gap: 6px; box-shadow: 0 2px 8px var(--primary-glow);">
        סילבוס ומקור רשמי ↗
        </a>
        </div>
        </div>
        """
        cards.append(textwrap.dedent(card_html).strip())
    return "".join(cards)
