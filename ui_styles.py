"""
ui_styles.py - מערכת העיצוב המלאה של GetAJob
תומכת באופן מלא ב-Dark Mode (ערכת הנושא המקורית והרשמית של האפיון - PRD סעיף 1.4)
וב-Light Mode (לפי בחירת המשתמש באמצעות מתג מהיר).
כולל רכיב תצוגת קוד/Markdown מקצועי עבור שלד ה-README.md, התאמת ניגודיות מלאה,
ומעקב התקדמות מקצועי בחיפוש עבודה ל-UX/UI.
"""

import textwrap


def get_custom_css(theme: str = "dark") -> str:
    """
    מחזיר את קובץ ה-CSS המלא עבור GetAJob.
    theme: 'dark' (ברירת מחדל רשמית של האפיון) או 'light'
    """
    is_dark = (theme == "dark")

    if is_dark:
        bg_main = "#0B0F19"
        surface_card = "#131A2A"
        surface_secondary = "#1B2436"
        surface_elevated = "#222C42"
        primary_accent = "#6C63FF"
        primary_hover = "#5A52E0"
        primary_glow = "rgba(108, 99, 255, 0.35)"
        text_primary = "#F8FAFC"
        text_secondary = "#94A3B8"
        text_muted = "#64748B"
        border_color = "#232D42"
        border_focus = "#6C63FF"
        card_shadow = "0 4px 20px rgba(0, 0, 0, 0.45)"
        code_bg = "#0d1117"
        code_border = "#30363d"
        tag_bg = "#1e293b"
        tag_border = "#334155"
        input_bg = "#131A2A"
        input_text = "#F8FAFC"
    else:
        bg_main = "#f8faff"
        surface_card = "#ffffff"
        surface_secondary = "#f1f5f9"
        surface_elevated = "#ffffff"
        primary_accent = "#4f46e5"
        primary_hover = "#4338ca"
        primary_glow = "rgba(79, 70, 229, 0.25)"
        text_primary = "#0f172a"
        text_secondary = "#334155"
        text_muted = "#64748b"
        border_color = "#cbd5e1"
        border_focus = "#4f46e5"
        card_shadow = "0 4px 20px rgba(15, 23, 42, 0.05)"
        code_bg = "#f6f8fa"
        code_border = "#d0d7de"
        tag_bg = "#f1f5f9"
        tag_border = "#cbd5e1"
        input_bg = "#ffffff"
        input_text = "#0f172a"

    css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;500;600;700;800&family=Heebo:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap');

    :root {{
        --bg-main: {bg_main};
        --surface-card: {surface_card};
        --surface-secondary: {surface_secondary};
        --surface-elevated: {surface_elevated};
        --primary-accent: {primary_accent};
        --primary-hover: {primary_hover};
        --primary-glow: {primary_glow};
        --text-primary: {text_primary};
        --text-secondary: {text_secondary};
        --text-muted: {text_muted};
        --border-color: {border_color};
        --border-focus: {border_focus};
        --card-shadow: {card_shadow};
        --code-bg: {code_bg};
        --code-border: {code_border};
        --tag-bg: {tag_bg};
        --tag-border: {tag_border};
        --input-bg: {input_bg};
        --input-text: {input_text};
        --color-success: #10b981;
        --color-warning: #f59e0b;
        --color-critical: #ef4444;
        --font-sans: 'Assistant', 'Heebo', -apple-system, sans-serif;
        --font-mono: 'JetBrains Mono', monospace;
    }}

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
    .stMarkdown, .stText {{
        background-color: var(--bg-main);
        color: var(--text-primary);
        font-family: var(--font-sans) !important;
        direction: rtl !important;
        text-align: right !important;
    }}

    bdi, [dir="rtl"] {{
        unicode-bidi: isolate !important;
    }}

    [data-testid="stHeader"] {{
        background: transparent !important;
    }}

    /* Container Spacing & Maximum Width */
    .block-container {{
        padding-top: 1.2rem !important;
        padding-bottom: 3.5rem !important;
        max-width: 1200px !important;
        direction: rtl !important;
        text-align: right !important;
    }}

    /* Typography Hierarchy */
    h1, h2, h3 {{
        font-family: var(--font-sans) !important;
        color: var(--text-primary) !important;
        font-weight: 800 !important;
        letter-spacing: -0.02em;
        text-align: right !important;
        direction: rtl !important;
    }}
    h1 {{ font-size: 30px !important; }}
    h2 {{ font-size: 24px !important; }}
    h3 {{ font-size: 18px !important; }}
    h4, h5, h6 {{
        color: var(--text-primary) !important;
        font-weight: 700 !important;
        text-align: right !important;
        direction: rtl !important;
    }}

    /* Header Bar & Server Status */
    .app-header-bar {{
        background: var(--surface-card);
        border: 1.5px solid var(--border-color);
        border-radius: 20px;
        padding: 16px 24px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 22px;
        box-shadow: var(--card-shadow);
    }}
    .status-server-online {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: {'rgba(16, 185, 129, 0.15)' if is_dark else '#ecfdf5'};
        border: 1.5px solid {'rgba(16, 185, 129, 0.4)' if is_dark else '#a7f3d0'};
        color: {'#6ee7b7' if is_dark else '#065f46'};
        font-weight: 700;
        font-size: 13px;
        padding: 5px 14px;
        border-radius: 9999px;
    }}
    .status-dot-pulse {{
        width: 8px;
        height: 8px;
        background: #10b981;
        border-radius: 50%;
        box-shadow: 0 0 10px #10b981;
        animation: pulseDot 2s infinite;
    }}
    @keyframes pulseDot {{
        0% {{ transform: scale(0.95); opacity: 0.8; }}
        50% {{ transform: scale(1.25); opacity: 1; }}
        100% {{ transform: scale(0.95); opacity: 0.8; }}
    }}

    /* Material 3 Expressive & Cards */
    .custom-card {{
        background: var(--surface-card);
        border: 1.5px solid var(--border-color);
        border-radius: 20px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: var(--card-shadow);
        transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), border-color 0.2s ease;
        direction: rtl;
        text-align: right;
    }}
    .custom-card:hover {{
        border-color: var(--border-focus);
    }}

    /* Form Inputs, Textarea, File Uploader */
    textarea, input, [data-baseweb="textarea"], [data-baseweb="input"] {{
        background-color: var(--input-bg) !important;
        color: var(--input-text) !important;
        border-color: var(--border-color) !important;
        border-radius: 14px !important;
        font-family: var(--font-sans) !important;
        direction: rtl !important;
        text-align: right !important;
    }}
    [data-baseweb="textarea"]:focus-within, [data-baseweb="input"]:focus-within {{
        border-color: var(--border-focus) !important;
        box-shadow: 0 0 0 2px var(--primary-glow) !important;
    }}

    /* Streamlit File Uploader */
    [data-testid="stFileUploader"] {{
        background: var(--surface-secondary);
        border: 1.5px dashed var(--border-color);
        border-radius: 16px;
        padding: 10px 14px;
        transition: all 0.25s ease;
    }}
    [data-testid="stFileUploader"]:hover {{
        border-color: var(--primary-accent);
    }}

    /* Primary Buttons & Interactive Elements */
    .stButton > button {{
        background: linear-gradient(135deg, var(--primary-accent) 0%, var(--primary-hover) 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 9999px !important;
        padding: 10px 24px !important;
        font-weight: 700 !important;
        font-size: 15px !important;
        box-shadow: 0 4px 14px var(--primary-glow) !important;
        transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
    }}
    .stButton > button:hover {{
        transform: translateY(-2px) scale(1.02) !important;
        box-shadow: 0 6px 20px var(--primary-glow) !important;
    }}

    /* Secondary / Download Buttons */
    [data-testid="stDownloadButton"] > button {{
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 9999px !important;
        padding: 10px 24px !important;
        font-weight: 800 !important;
        box-shadow: 0 4px 14px rgba(16, 185, 129, 0.3) !important;
        transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
    }}
    [data-testid="stDownloadButton"] > button:hover {{
        transform: translateY(-2px) scale(1.02) !important;
        box-shadow: 0 6px 20px rgba(16, 185, 129, 0.45) !important;
    }}

    /* Tabs Styling - Clean and unclamped */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px !important;
        background-color: var(--surface-card) !important;
        padding: 8px 12px !important;
        border-radius: 18px !important;
        border: 1.5px solid var(--border-color) !important;
        direction: rtl !important;
    }}
    .stTabs [data-baseweb="tab"] {{
        border-radius: 12px !important;
        padding: 8px 16px !important;
        color: var(--text-secondary) !important;
        font-weight: 700 !important;
        background: transparent !important;
        border: none !important;
        transition: all 0.2s ease !important;
    }}
    .stTabs [aria-selected="true"] {{
        background-color: var(--surface-elevated) !important;
        color: var(--primary-accent) !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15) !important;
        border: 1.5px solid var(--border-focus) !important;
    }}

    /* Expander styling */
    [data-testid="stExpander"] {{
        background: var(--surface-card) !important;
        border: 1.5px solid var(--border-color) !important;
        border-radius: 16px !important;
        overflow: hidden;
    }}

    /* Score Hero Gauge */
    .score-hero-container {{
        background: var(--surface-card);
        border: 1.5px solid var(--border-color);
        border-radius: 24px;
        padding: 24px 30px;
        margin-bottom: 24px;
        box-shadow: var(--card-shadow);
        display: flex;
        align-items: center;
        gap: 26px;
        flex-wrap: wrap;
    }}
    .score-circle-badge {{
        width: 100px;
        height: 100px;
        border-radius: 50%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        font-family: 'Outfit', sans-serif;
    }}
    .score-circle-high {{
        background: {'rgba(16, 185, 129, 0.15)' if is_dark else '#ecfdf5'};
        border: 3px solid #10b981;
        color: {'#34d399' if is_dark else '#065f46'};
        box-shadow: 0 0 16px rgba(16, 185, 129, 0.3);
    }}
    .score-circle-med {{
        background: {'rgba(245, 158, 11, 0.15)' if is_dark else '#fffbeb'};
        border: 3px solid #f59e0b;
        color: {'#fbbf24' if is_dark else '#92400e'};
        box-shadow: 0 0 16px rgba(245, 158, 11, 0.3);
    }}
    .score-circle-low {{
        background: {'rgba(239, 68, 68, 0.15)' if is_dark else '#fef2f2'};
        border: 3px solid #ef4444;
        color: {'#f87171' if is_dark else '#991b1b'};
        box-shadow: 0 0 16px rgba(239, 68, 68, 0.3);
    }}

    /* Skill Badges */
    .skill-badge {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 5px 14px;
        border-radius: 9999px;
        font-size: 13px;
        font-weight: 700;
        margin: 3px;
    }}
    .badge-high {{
        background: {'rgba(239, 68, 68, 0.18)' if is_dark else '#fef2f2'};
        color: {'#fca5a5' if is_dark else '#991b1b'};
        border: 1.5px solid {'rgba(239, 68, 68, 0.4)' if is_dark else '#fca5a5'};
    }}
    .badge-med {{
        background: {'rgba(245, 158, 11, 0.18)' if is_dark else '#fffbeb'};
        color: {'#fcd34d' if is_dark else '#92400e'};
        border: 1.5px solid {'rgba(245, 158, 11, 0.4)' if is_dark else '#fcd34d'};
    }}
    .badge-low {{
        background: {'rgba(56, 189, 248, 0.18)' if is_dark else '#f0f9ff'};
        color: {'#7dd3fc' if is_dark else '#0369a1'};
        border: 1.5px solid {'rgba(56, 189, 248, 0.4)' if is_dark else '#7dd3fc'};
    }}

    /* Bullet Comparison Cards */
    .compare-card-container {{
        background: var(--surface-card);
        border: 1.5px solid var(--border-color);
        border-radius: 18px;
        padding: 20px 24px;
        margin-bottom: 16px;
        box-shadow: var(--card-shadow);
        direction: rtl;
        text-align: right;
    }}
    .compare-side {{
        border-radius: 14px;
        padding: 14px 18px;
        margin: 8px 0;
        font-size: 14.5px;
        line-height: 1.6;
    }}
    .compare-original-side {{
        background: {'rgba(239, 68, 68, 0.1)' if is_dark else '#fff5f5'};
        border: 1px solid {'rgba(239, 68, 68, 0.25)' if is_dark else '#fed7d7'};
        color: {'#fca5a5' if is_dark else '#991b1b'};
    }}
    .compare-improved-side {{
        background: {'rgba(16, 185, 129, 0.1)' if is_dark else '#f0fdf4'};
        border: 1px solid {'rgba(16, 185, 129, 0.25)' if is_dark else '#bbf7d0'};
        color: {'#6ee7b7' if is_dark else '#14532d'};
    }}

    /* Dedicated README Code Viewer Block */
    .readme-ide-block {{
        background: var(--code-bg);
        border: 1.5px solid var(--code-border);
        border-radius: 18px;
        overflow: hidden;
        margin: 18px 0;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35);
        direction: ltr !important;
        text-align: left !important;
    }}
    .readme-ide-header {{
        background: {'#161b22' if is_dark else '#eaeef2'};
        padding: 10px 18px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 1px solid var(--code-border);
    }}
    .readme-code-pre {{
        margin: 0;
        padding: 18px 20px;
        font-family: var(--font-mono) !important;
        font-size: 13.5px;
        line-height: 1.65;
        color: {'#e6edf3' if is_dark else '#24292f'};
        white-space: pre-wrap;
        word-break: break-word;
        max-height: 520px;
        overflow-y: auto;
        direction: ltr !important;
        text-align: left !important;
    }}

    /* Onboarding styles */
    .onboarding-container {{
        background: var(--surface-card);
        border: 1.5px solid var(--border-color);
        border-radius: 28px;
        padding: 36px;
        margin: 10px auto 30px auto;
        box-shadow: var(--card-shadow);
        max-width: 900px;
        direction: rtl;
        text-align: right;
    }}
    .onboarding-dots {{
        display: flex;
        justify-content: center;
        gap: 8px;
        margin-top: 24px;
    }}
    .onboarding-dot {{
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: var(--border-color);
        transition: all 0.3s ease;
    }}
    .onboarding-dot.active {{
        width: 32px;
        border-radius: 9999px;
        background: var(--primary-accent);
        box-shadow: 0 0 10px var(--primary-glow);
    }}
    </style>
    """
    return textwrap.dedent(css).strip()


def render_step_bar(current_step: int = 1, theme: str = "dark") -> str:
    """סרגל שלבים מעוצב למסך הראשי עם תמיכה מלאה במצב כהה ובהיר"""
    is_dark = (theme == "dark")
    steps = [
        (1, "טעינת קורות חיים ומשרה"),
        (2, "ניתוח פערים ושכתוב"),
        (3, "מפרט פרויקט ו-README"),
    ]
    items = []
    for num, title in steps:
        if num <= current_step:
            border_color = "var(--primary-accent)"
            bg_color = "rgba(108, 99, 255, 0.18)" if is_dark else "#ede9fe"
            text_color = "#c7d2fe" if is_dark else "#3730a3"
            num_bg = "var(--primary-accent)"
            num_text = "#ffffff"
        else:
            border_color = "var(--border-color)"
            bg_color = "var(--surface-card)"
            text_color = "var(--text-muted)"
            num_bg = "rgba(100, 116, 139, 0.3)" if is_dark else "#94a3b8"
            num_text = "#94a3b8" if is_dark else "#ffffff"

        item_html = (
            f'<div style="flex: 1; min-width: 170px; background: {bg_color}; '
            f'border: 1.5px solid {border_color}; border-radius: 9999px; padding: 8px 18px; '
            f'display: flex; align-items: center; gap: 10px; color: {text_color}; '
            f'font-weight: 700; font-size: 14px; direction: rtl;">'
            f'<span style="background: {num_bg}; color: {num_text}; width: 24px; height: 24px; '
            f'border-radius: 50%; display: flex; align-items: center; justify-content: center; '
            f'font-size: 12px; font-weight: 800;">{num}</span>'
            f'<span>{title}</span></div>'
        )
        items.append(item_html)
    return f'<div style="display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 22px; direction: rtl;">{"".join(items)}</div>'


def render_ats_tip(theme: str = "dark") -> str:
    """כרטיס טיפ מקצועי לעמידה ב-ATS"""
    is_dark = (theme == "dark")
    bg = "rgba(108, 99, 255, 0.12)" if is_dark else "#f5f3ff"
    border = "rgba(108, 99, 255, 0.35)" if is_dark else "#c7d2fe"
    title_col = "#c7d2fe" if is_dark else "#3730a3"
    text_col = "#cbd5e1" if is_dark else "#334155"
    formula_col = "#a5b4fc" if is_dark else "#4338ca"

    html = f"""
    <div style="background: {bg}; border: 1.5px solid {border}; border-radius: 18px; padding: 18px 24px; margin-bottom: 22px; display: flex; align-items: flex-start; gap: 14px; direction: rtl; text-align: right;">
    <div style="width: 38px; height: 38px; border-radius: 12px; background: {'rgba(108, 99, 255, 0.2)' if is_dark else '#ede9fe'}; color: var(--primary-accent); display: flex; align-items: center; justify-content: center; font-size: 20px; flex-shrink: 0; border: 1px solid {border};">💡</div>
    <div style="flex: 1;">
    <strong style="color: {title_col}; font-size: 15.5px; display: block; margin-bottom: 4px;">
    טיפ מקצועי למעבר סינון ראשוני (Strict ATS):
    </strong>
    <p style="margin: 0; color: {text_col}; font-size: 14.5px; line-height: 1.6;">
    מערכות גיוס מודרניות (Greenhouse, Workday, Lever) בודקות מילות מפתח בהקשר מעשי. 
    הנוסחה המנצחת של Google לקורות חיים היא: 
    <span style="color: {formula_col}; font-weight: 700; direction: ltr; display: inline-block;">"Accomplished [X] as measured by [Y], by doing [Z]"</span>
    (השגת יעד מדיד באמצעות טכנולוגיה ספציפית).
    </p>
    </div>
    </div>
    """
    return textwrap.dedent(html).strip()


def render_score_gauge(score: int, summary: str, theme: str = "dark") -> str:
    """מד ציון התאמה הנדסי בעיצוב Material 3 Expressive מותאם Dark/Light"""
    is_dark = (theme == "dark")
    if score >= 75:
        circle_class = "score-circle-high"
        status_text = "התאמה גבוהה (מוכן להגשה)"
        subtext = "קורות החיים מציגים את רוב דרישות הסף המרכזיות."
        badge_style = "background: rgba(16, 185, 129, 0.2); color: #6ee7b7; border: 1.5px solid #10b981;" if is_dark else "background: #ecfdf5; color: #065f46; border: 1.5px solid #6ee7b7;"
    elif score >= 50:
        circle_class = "score-circle-med"
        status_text = "התאמה בינונית (דורשת שדרוג)"
        subtext = "קיימת תשתית טובה, אך חסרות טכנולוגיות מפתח להבטחת מעבר סינון."
        badge_style = "background: rgba(245, 158, 11, 0.2); color: #fcd34d; border: 1.5px solid #f59e0b;" if is_dark else "background: #fffbeb; color: #92400e; border: 1.5px solid #fcd34d;"
    else:
        circle_class = "score-circle-low"
        status_text = "פער הנדסי משמעותי"
        subtext = "מומלץ לבנות פרויקט ממוקד בפורטפוליו לפני הגשת מועמדות."
        badge_style = "background: rgba(239, 68, 68, 0.2); color: #fca5a5; border: 1.5px solid #ef4444;" if is_dark else "background: #fef2f2; color: #991b1b; border: 1.5px solid #fca5a5;"

    html = f"""
    <div class="score-hero-container">
    <div class="score-circle-badge {circle_class}">
    <div style="font-size: 32px; line-height: 1; font-weight: 800;">{score}%</div>
    <div style="font-size: 11px; font-weight: 700; opacity: 0.8; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">MATCH</div>
    </div>
    <div style="flex: 1; direction: rtl; text-align: right;">
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px; flex-wrap: wrap;">
    <h3 style="margin: 0; font-size: 20px; font-weight: 800; color: var(--text-primary);">ציון התאמה הנדסי משוקלל</h3>
    <span style="font-size: 13px; font-weight: 700; padding: 4px 14px; border-radius: 9999px; {badge_style}">
    {status_text}
    </span>
    </div>
    <div style="color: var(--text-secondary); font-size: 15px; line-height: 1.6; font-weight: 500;">{summary}</div>
    <div style="margin-top: 8px; color: var(--text-muted); font-size: 13.5px;">{subtext}</div>
    </div>
    </div>
    """
    return textwrap.dedent(html).strip()


def render_skill_badges(missing_skills: list, theme: str = "dark") -> str:
    """תגיות מיומנויות חסרות מחולקות לחומרה עם צבעי התראה ברורים"""
    high_skills = [s for s in missing_skills if s.get("importance") == "High"]
    med_skills = [s for s in missing_skills if s.get("importance") == "Medium"]
    low_skills = [s for s in missing_skills if s.get("importance") == "Low"]

    parts = ['<div style="direction: rtl; text-align: right; margin-bottom: 20px;">']

    if high_skills:
        badges = "".join([
            f'<div class="skill-badge badge-high"><strong>{s.get("skill")}</strong> <span style="font-size: 11px; opacity: 0.9;">• HIGH</span></div>'
            for s in high_skills
        ])
        parts.append(f'<div style="margin-bottom: 14px;"><span style="font-size: 14.5px; font-weight: 800; color: #ef4444;">🔴 פערי חובה קריטיים (Must-Have):</span><div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px;">{badges}</div></div>')

    if med_skills:
        badges = "".join([
            f'<div class="skill-badge badge-med"><strong>{s.get("skill")}</strong> <span style="font-size: 11px; opacity: 0.9;">• MEDIUM</span></div>'
            for s in med_skills
        ])
        parts.append(f'<div style="margin-bottom: 14px;"><span style="font-size: 14.5px; font-weight: 800; color: #f59e0b;">🟡 פערים מהותיים שכדאי לגשר:</span><div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px;">{badges}</div></div>')

    if low_skills:
        badges = "".join([
            f'<div class="skill-badge badge-low"><strong>{s.get("skill")}</strong> <span style="font-size: 11px; opacity: 0.9;">• LOW</span></div>'
            for s in low_skills
        ])
        parts.append(f'<div style="margin-bottom: 14px;"><span style="font-size: 14.5px; font-weight: 800; color: #38bdf8;">🔵 מיומנויות יתרון (Nice-to-Have):</span><div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px;">{badges}</div></div>')

    parts.append('</div>')
    return "".join(parts)


def render_bullet_comparison(improvements: list, theme: str = "dark") -> str:
    """שדרוג סעיפי קורות חיים Before / After"""
    is_dark = (theme == "dark")
    cards = []
    for i, item in enumerate(improvements, 1):
        orig = item.get("original", "")
        imp = item.get("improved", "")
        reason = item.get("reason", "")
        
        card = f"""
        <div class="compare-card-container">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
        <span style="font-weight: 800; color: {'#c7d2fe' if is_dark else '#3730a3'}; font-size: 15.5px;">
        📌 סעיף {i}: שדרוג מבוסס Action-Impact (מוכן להעתקה לקורות החיים)
        </span>
        <span style="font-size: 12px; background: {'rgba(16, 185, 129, 0.18)' if is_dark else '#ecfdf5'}; color: {'#6ee7b7' if is_dark else '#065f46'}; padding: 4px 14px; border-radius: 9999px; font-weight: 700; border: 1px solid {'rgba(16, 185, 129, 0.35)' if is_dark else '#6ee7b7'};">
        ATS Optimized ✔
        </span>
        </div>
        <div class="compare-side compare-original-side">
        <span style="font-size: 13px; font-weight: 800; display: block; color: #ef4444; margin-bottom: 4px;">
        ✖ נוסח מקורי בקורות החיים (פסיבי / חסר נתונים):
        </span>
        {orig}
        </div>
        <div class="compare-side compare-improved-side">
        <span style="font-size: 13px; font-weight: 800; display: block; color: #10b981; margin-bottom: 4px;">
        ✔ נוסח משודרג וממוקד משרה (Action + Scale + Impact):
        </span>
        {imp}
        </div>
        <div style="margin-top: 10px; display: flex; align-items: center; gap: 8px;">
        <span style="color: {'#a5b4fc' if is_dark else '#4338ca'}; font-size: 13.5px; font-weight: 600;">💡 למה זה מקפיץ את הסיכוי? {reason}</span>
        </div>
        </div>
        """
        cards.append(textwrap.dedent(card).strip())
    return "".join(cards)


def render_onboarding_progress(current_step: int, total_steps: int = 3, theme: str = "dark") -> str:
    """מחוון נקודות מעוצב"""
    dots = []
    for i in range(1, total_steps + 1):
        active_cls = "active" if i == current_step else ""
        dots.append(f'<div class="onboarding-dot {active_cls}"></div>')
    return f'<div class="onboarding-dots">{"".join(dots)}</div>'


def render_career_intel(domain: dict, theme: str = "dark") -> str:
    """כרטיס סקירה מקצועית מעמיקה עבור התחום שנבחר"""
    is_dark = (theme == "dark")
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

    inner_bg = "var(--surface-secondary)"
    inner_border = "var(--border-color)"

    html = f"""
    <div style="direction: rtl !important; text-align: right !important; background: var(--surface-card); border: 1.5px solid var(--border-color); border-radius: 24px; padding: 26px 30px; box-shadow: var(--card-shadow); margin-bottom: 24px;">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; margin-bottom: 18px; border-bottom: 1.5px solid {inner_border}; padding-bottom: 16px; direction: rtl !important;">
    <div style="display: flex; align-items: center; gap: 14px; direction: rtl !important; text-align: right !important;">
    <div style="width: 52px; height: 52px; border-radius: 16px; background: {'rgba(108, 99, 255, 0.18)' if is_dark else '#ede9fe'}; color: var(--primary-accent); display: flex; align-items: center; justify-content: center; font-size: 26px; border: 1.5px solid {'rgba(108, 99, 255, 0.35)' if is_dark else '#c7d2fe'}; flex-shrink: 0;">
    {icon}
    </div>
    <div style="text-align: right !important; direction: rtl !important;">
    <h2 style="margin: 0; font-size: 22px; font-weight: 800; color: var(--text-primary); text-align: right !important; direction: rtl !important;"><bdi>{title}</bdi></h2>
    <p style="margin: 4px 0 0 0; color: var(--text-muted); font-size: 14.5px; font-weight: 500; text-align: right !important; direction: rtl !important;"><bdi>{desc}</bdi></p>
    </div>
    </div>
    <div style="display: flex; gap: 8px; flex-wrap: wrap; direction: rtl !important;">
    <span style="background: {'rgba(16, 185, 129, 0.15)' if is_dark else '#ecfdf5'}; color: {'#6ee7b7' if is_dark else '#065f46'}; border: 1px solid {'rgba(16, 185, 129, 0.35)' if is_dark else '#6ee7b7'}; border-radius: 9999px; padding: 5px 14px; font-size: 13px; font-weight: 700; direction: rtl !important;"><bdi>{demand}</bdi></span>
    <span style="background: {'rgba(108, 99, 255, 0.15)' if is_dark else '#ede9fe'}; color: {'#c7d2fe' if is_dark else '#3730a3'}; border: 1px solid {'rgba(108, 99, 255, 0.35)' if is_dark else '#c7d2fe'}; border-radius: 9999px; padding: 5px 14px; font-size: 13px; font-weight: 700; direction: rtl !important;"><bdi>💰 {salary}</bdi></span>
    </div>
    </div>
    <div style="margin-bottom: 18px; text-align: right !important; direction: rtl !important;">
    <h4 style="color: var(--text-primary); font-weight: 800; margin-bottom: 8px; text-align: right !important; direction: rtl !important;">📌 מה השוק והמגייסים באמת מחפשים כיום?</h4>
    <p style="color: var(--text-secondary); font-size: 14.5px; line-height: 1.65; margin: 0; background: {inner_bg}; border: 1.5px solid {inner_border}; border-radius: 14px; padding: 14px 18px; text-align: right !important; direction: rtl !important;"><bdi>{reality}</bdi></p>
    </div>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 20px; direction: rtl !important;">
    <div style="background: {inner_bg}; border: 1.5px solid {inner_border}; border-radius: 16px; padding: 16px 18px; text-align: right !important; direction: rtl !important;">
    <strong style="color: {'#fbbf24' if is_dark else '#b45309'}; font-size: 14px; display: block; margin-bottom: 8px; text-align: right !important;">🔥 סטאק טכנולוגי חובה (דרישות סף):</strong>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; direction: ltr; justify-content: flex-end;">{must_html}</div>
    </div>
    <div style="background: {inner_bg}; border: 1.5px solid {inner_border}; border-radius: 16px; padding: 16px 18px; text-align: right !important; direction: rtl !important;">
    <strong style="color: {'#38bdf8' if is_dark else '#0369a1'}; font-size: 14px; display: block; margin-bottom: 8px; text-align: right !important;">⚡ טכנולוגיות יתרון שיבדילו אותך:</strong>
    <div style="display: flex; flex-wrap: wrap; gap: 6px; direction: ltr; justify-content: flex-end;">{good_html}</div>
    </div>
    </div>
    <div style="background: {inner_bg}; border: 1.5px solid {inner_border}; border-radius: 16px; padding: 16px 20px; text-align: right !important; direction: rtl !important;">
    <strong style="color: {'#a5b4fc' if is_dark else '#4338ca'}; font-size: 14px; display: block; margin-bottom: 6px; text-align: right !important;">🚀 סוג הפרויקט המומלץ לפורטפוליו שלך:</strong>
    <p style="margin: 0; color: var(--text-secondary); font-size: 14px; line-height: 1.6; text-align: right !important; direction: rtl !important;"><bdi>{project}</bdi></p>
    </div>
    </div>
    """
    return textwrap.dedent(html).strip()


def render_learning_paths(paths: list, theme: str = "dark") -> str:
    """מחולל כרטיסי מסלולי לימוד והסמכות מתוך מאגר ה-49 מסלולים"""
    is_dark = (theme == "dark")
    if not paths:
        return """
        <div style="background: var(--surface-card); border: 1.5px solid var(--border-color); border-radius: 16px; padding: 20px; text-align: center; color: var(--text-muted);">
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

        inner_bg = "var(--surface-secondary)"
        inner_border = "var(--border-color)"

        card_html = f"""
        <div style="background: var(--surface-card); border: 1.5px solid var(--border-color); border-radius: 18px; padding: 20px 24px; margin-bottom: 16px; direction: rtl; text-align: right; box-shadow: var(--card-shadow);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px; margin-bottom: 10px;">
        <div>
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
        <span style="background: {'rgba(108, 99, 255, 0.18)' if is_dark else '#ede9fe'}; color: {'#c7d2fe' if is_dark else '#3730a3'}; border: 1px solid {'rgba(108, 99, 255, 0.35)' if is_dark else '#c7d2fe'}; border-radius: 9999px; padding: 3px 12px; font-size: 12px; font-weight: 700;">{domain} • {lp_type}</span>
        <span style="font-size: 12.5px; color: var(--text-muted); font-weight: 600;">רמה: {level}</span>
        </div>
        <h4 style="margin: 0; font-size: 18px; font-weight: 800; color: var(--text-primary);">{name}</h4>
        </div>
        <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;">
        <span style="background: {'rgba(16, 185, 129, 0.15)' if is_dark else '#ecfdf5'}; color: {'#6ee7b7' if is_dark else '#065f46'}; border: 1px solid {'rgba(16, 185, 129, 0.35)' if is_dark else '#6ee7b7'}; border-radius: 9999px; padding: 4px 12px; font-size: 12.5px; font-weight: 700;">⏱ משך: {duration}</span>
        <span style="background: {'rgba(245, 158, 11, 0.15)' if is_dark else '#fffbeb'}; color: {'#fcd34d' if is_dark else '#92400e'}; border: 1px solid {'rgba(245, 158, 11, 0.35)' if is_dark else '#fcd34d'}; border-radius: 9999px; padding: 4px 12px; font-size: 12.5px; font-weight: 700;">חוזק הוכחה: {stars}</span>
        </div>
        </div>
        <div style="background: {inner_bg}; border: 1px solid {inner_border}; border-radius: 12px; padding: 12px 16px; margin: 12px 0;">
        <strong style="color: {'#c7d2fe' if is_dark else '#3730a3'}; font-size: 13.5px; display: block; margin-bottom: 3px;">🎯 מתי מומלץ על פי המודל?</strong>
        <p style="margin: 0; color: var(--text-secondary); font-size: 13.5px; line-height: 1.5;">{when_to}</p>
        </div>
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-top: 14px;">
        <div style="flex: 1; min-width: 260px;">
        <span style="color: {'#a5b4fc' if is_dark else '#4338ca'}; font-size: 13px; font-weight: 700;">🛠 פרויקט הוכחה מומלץ:</span>
        <span style="color: var(--text-secondary); font-size: 13px;"> {project}</span>
        </div>
        <a href="{url}" target="_blank" style="background: var(--primary-accent); color: #ffffff; text-decoration: none; padding: 7px 18px; border-radius: 9999px; font-size: 12.5px; font-weight: 700; display: inline-flex; align-items: center; gap: 6px; box-shadow: 0 2px 8px var(--primary-glow);">
        סילבוס ומקור רשמי ↗
        </a>
        </div>
        </div>
        """
        cards.append(textwrap.dedent(card_html).strip())
    return "".join(cards)


def render_job_search_tracker(milestones: list, progress_pct: int, theme: str = "dark") -> str:
    """
    רכיב מעקב התקדמות בחיפוש עבודה (UX/UI Job Search Roadmap & Progress Tracker)
    מציג גרף התקדמות, מד מוכנות לגיוס, וצ'קליסט אבני דרך אינטראקטיבי.
    """
    is_dark = (theme == "dark")
    if progress_pct >= 80:
        bar_color = "linear-gradient(90deg, #10b981 0%, #059669 100%)"
        status_label = "🚀 מוכן לגיוס והגשות לשוק!"
        status_badge = "background: rgba(16, 185, 129, 0.2); color: #6ee7b7; border: 1.5px solid #10b981;" if is_dark else "background: #ecfdf5; color: #065f46; border: 1.5px solid #6ee7b7;"
    elif progress_pct >= 50:
        bar_color = "linear-gradient(90deg, #6C63FF 0%, #5A52E0 100%)" if is_dark else "linear-gradient(90deg, #4f46e5 0%, #4338ca 100%)"
        status_label = "⚡ בתהליך בנייה מתקדם"
        status_badge = "background: rgba(108, 99, 255, 0.2); color: #c7d2fe; border: 1.5px solid #6C63FF;" if is_dark else "background: #ede9fe; color: #3730a3; border: 1.5px solid #c7d2fe;"
    else:
        bar_color = "linear-gradient(90deg, #f59e0b 0%, #d97706 100%)"
        status_label = "🌱 שלב ההכנה הראשוני"
        status_badge = "background: rgba(245, 158, 11, 0.2); color: #fcd34d; border: 1.5px solid #f59e0b;" if is_dark else "background: #fffbeb; color: #92400e; border: 1.5px solid #fcd34d;"

    html = f"""
    <div style="background: var(--surface-card); border: 1.5px solid var(--border-color); border-radius: 24px; padding: 26px 30px; margin-bottom: 24px; box-shadow: var(--card-shadow); direction: rtl; text-align: right;">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px;">
    <div>
    <div style="display: flex; align-items: center; gap: 10px;">
    <span style="font-size: 26px;">📈</span>
    <h3 style="margin: 0; font-size: 22px; font-weight: 800; color: var(--text-primary);">מעקב התקדמות אישי: בדרך למשרת מעצב/ת UX/UI</h3>
    </div>
    <p style="margin: 4px 0 0 0; color: var(--text-muted); font-size: 14.5px;">עקוב אחרי השלמת אבני הדרך להבטחת ראיון טכני ראשון</p>
    </div>
    <div style="display: flex; align-items: center; gap: 10px;">
    <span style="padding: 6px 16px; border-radius: 9999px; font-size: 13.5px; font-weight: 800; {status_badge}">
    {status_label}
    </span>
    <span style="background: var(--surface-secondary); color: var(--text-primary); padding: 6px 14px; border-radius: 9999px; font-size: 15px; font-weight: 800; border: 1.5px solid var(--border-color);">
    {progress_pct}% הושלמו
    </span>
    </div>
    </div>

    <!-- סרגל גרף התקדמות ויזואלי -->
    <div style="background: var(--surface-secondary); border-radius: 9999px; height: 14px; overflow: hidden; margin-bottom: 20px; border: 1px solid var(--border-color);">
    <div style="background: {bar_color}; width: {progress_pct}%; height: 100%; border-radius: 9999px; transition: width 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);"></div>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 12px; margin-top: 14px;">
    """

    milestone_cards = []
    for m in milestones:
        is_done = m.get("completed", False)
        icon = "✔" if is_done else "○"
        if is_done:
            box_bg = "rgba(16, 185, 129, 0.12)" if is_dark else "#f0fdf4"
            box_border = "rgba(16, 185, 129, 0.35)" if is_dark else "#86efac"
            title_color = "#6ee7b7" if is_dark else "#14532d"
            badge_bg = "rgba(16, 185, 129, 0.2)" if is_dark else "#ecfdf5"
            badge_color = "#34d399" if is_dark else "#16a34a"
        else:
            box_bg = "var(--surface-secondary)"
            box_border = "var(--border-color)"
            title_color = "var(--text-primary)"
            badge_bg = "var(--surface-elevated)"
            badge_color = "var(--text-muted)"

        m_card = (
            f'<div style="background: {box_bg}; border: 1.5px solid {box_border}; border-radius: 16px; padding: 14px 18px; display: flex; align-items: flex-start; gap: 12px; box-shadow: 0 1px 4px rgba(0, 0, 0, 0.1);">'
            f'<span style="background: {badge_bg}; color: {badge_color}; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 800; flex-shrink: 0;">{icon}</span>'
            f'<div style="flex: 1;">'
            f'<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 3px;">'
            f'<strong style="color: {title_color}; font-size: 14.5px;">{m.get("title")}</strong>'
            f'<span style="font-size: 11.5px; font-weight: 700; color: {badge_color};">{m.get("category")}</span>'
            f'</div>'
            f'<p style="margin: 0; color: var(--text-muted); font-size: 13px; line-height: 1.45;">{m.get("desc")}</p>'
            f'</div></div>'
        )
        milestone_cards.append(m_card)

    html += "".join(milestone_cards)
    html += "</div></div>"
    return textwrap.dedent(html).strip()


def render_readme_block(readme_content: str, project_name: str, theme: str = "dark") -> str:
    """
    רכיב תצוגת קוד/Markdown מקצועי (IDE Style Code Block) עבור שלד README.md.
    כולל חלון עליון עם כותרת, תגיות פורמט, ומסך קוד LTR מלא לצפייה לפני ההורדה (TC-07).
    """
    is_dark = (theme == "dark")
    header_bg = "#161b22" if is_dark else "#eaeef2"
    border_col = "#30363d" if is_dark else "#cbd5e1"
    code_bg = "#0d1117" if is_dark else "#f8fafc"
    text_col = "#e6edf3" if is_dark else "#0f172a"
    file_title = f"README_{project_name.replace(' ', '_')}.md"

    html = f"""
    <div class="readme-ide-block" style="background: {code_bg}; border: 1.5px solid {border_col}; border-radius: 18px; overflow: hidden; margin: 18px 0; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35); direction: ltr !important; text-align: left !important;">
      <div class="readme-ide-header" style="background: {header_bg}; padding: 12px 18px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid {border_col};">
        <div style="display: flex; align-items: center; gap: 8px;">
          <span style="width: 12px; height: 12px; border-radius: 50%; background: #ff5f56; display: inline-block;"></span>
          <span style="width: 12px; height: 12px; border-radius: 50%; background: #ffbd2e; display: inline-block;"></span>
          <span style="width: 12px; height: 12px; border-radius: 50%; background: #27c93f; display: inline-block;"></span>
          <span style="margin-left: 10px; font-family: 'JetBrains Mono', monospace; font-size: 13.5px; font-weight: 700; color: {text_col};">📄 {file_title}</span>
        </div>
        <div style="display: flex; gap: 8px; align-items: center;">
          <span style="font-size: 11.5px; font-weight: 700; background: {'rgba(108, 99, 255, 0.2)' if is_dark else '#ede9fe'}; color: {'#c7d2fe' if is_dark else '#3730a3'}; padding: 3px 12px; border-radius: 9999px; border: 1px solid {'rgba(108, 99, 255, 0.4)' if is_dark else '#c7d2fe'};">Markdown (LTR)</span>
          <span style="font-size: 11.5px; font-weight: 700; background: {'rgba(16, 185, 129, 0.2)' if is_dark else '#ecfdf5'}; color: {'#6ee7b7' if is_dark else '#065f46'}; padding: 3px 12px; border-radius: 9999px; border: 1px solid {'rgba(16, 185, 129, 0.4)' if is_dark else '#6ee7b7'};">GitHub Ready ✔</span>
        </div>
      </div>
      <pre class="readme-code-pre" style="margin: 0; padding: 20px 22px; font-family: 'JetBrains Mono', monospace; font-size: 13.5px; line-height: 1.65; color: {text_col}; white-space: pre-wrap; word-break: break-word; max-height: 520px; overflow-y: auto; direction: ltr !important; text-align: left !important;">{readme_content}</pre>
    </div>
    """
    return textwrap.dedent(html).strip()
