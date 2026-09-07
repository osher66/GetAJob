"""
ui_styles.py - מערכת העיצוב המלאה של GetAJob
תומכת באופן מלא ב-Dark Mode (ערכת הנושא המקורית והרשמית של האפיון - PRD סעיף 1.4)
וב-Light Mode (לפי בחירת המשתמש באמצעות מתג מהיר).
כולל רכיב תצוגת קוד/Markdown מקצועי עבור שלד ה-README.md, התאמת ניגודיות מלאה,
ומעקב התקדמות מקצועי בחיפוש עבודה ל-UX/UI.
"""

import textwrap


def get_custom_css(theme: str = "light") -> str:
    """
    מחזיר את קובץ ה-CSS המלא עבור GetAJob המוטמע לפי עקרונות Google Material Design 3 (Material You).
    כולל מערכת טוקנים רשמית, Tonal Elevation, קצוות מעוגלים לפי M3 Shape Scale, וכפתורי קפסולה מלאים.
    """
    css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&family=Outfit:wght@500;600;700;800;900&family=Rubik:wght@300;400;500;600;700;800;900&display=swap');

    :root {
        /* ==========================================================================
           1. Google Material Design 3 (M3) Color Roles (Light Theme)
           ========================================================================== */
        --md-sys-color-primary: #5A45FF;
        --md-sys-color-on-primary: #FFFFFF;
        --md-sys-color-primary-container: #EDE9FE;
        --md-sys-color-on-primary-container: #3730A3;
        --md-sys-color-primary-hover: #4C37F5;

        --md-sys-color-secondary: #4F46E5;
        --md-sys-color-on-secondary: #FFFFFF;
        --md-sys-color-secondary-container: #F3F0FF;
        --md-sys-color-on-secondary-container: #312E81;

        --md-sys-color-tertiary: #0284C7;
        --md-sys-color-tertiary-container: #E0F2FE;
        --md-sys-color-on-tertiary-container: #0369A1;

        --md-sys-color-surface: #F8FAFC;
        --md-sys-color-on-surface: #0F172A;
        --md-sys-color-on-surface-variant: #475569;

        --md-sys-color-surface-container-lowest: #FFFFFF;
        --md-sys-color-surface-container-low: #F8FAFC;
        --md-sys-color-surface-container: #F1F5F9;
        --md-sys-color-surface-container-high: #E2E8F0;
        --md-sys-color-surface-container-highest: #CBD5E1;

        --md-sys-color-outline: #94A3B8;
        --md-sys-color-outline-variant: #E2E8F0;

        --md-sys-color-success: #006C4C;
        --md-sys-color-success-container: #ECFDF5;
        --md-sys-color-on-success-container: #065F46;

        --md-sys-color-warning: #B45309;
        --md-sys-color-warning-container: #FFFBEB;
        --md-sys-color-on-warning-container: #92400E;

        --md-sys-color-error: #BA1A1A;
        --md-sys-color-error-container: #FEF2F2;
        --md-sys-color-on-error-container: #991B1B;

        /* Legacy mapping for backward compatibility */
        --bg-main: var(--md-sys-color-surface);
        --surface-card: var(--md-sys-color-surface-container-lowest);
        --surface-secondary: var(--md-sys-color-surface-container);
        --surface-elevated: var(--md-sys-color-surface-container-lowest);
        --primary-accent: var(--md-sys-color-primary);
        --primary-hover: var(--md-sys-color-primary-hover);
        --primary-glow: rgba(90, 69, 255, 0.22);
        --text-primary: var(--md-sys-color-on-surface);
        --text-secondary: var(--md-sys-color-on-surface-variant);
        --text-muted: #64748B;
        --border-color: var(--md-sys-color-outline-variant);
        --border-focus: var(--md-sys-color-primary);
        --card-shadow: 0 2px 8px rgba(15, 23, 42, 0.05);

        /* ==========================================================================
           2. M3 Tonal Elevation System (Soft ambient shadows + surface separation)
           ========================================================================== */
        --md-sys-elevation-0: none;
        --md-sys-elevation-1: 0 1px 3px 1px rgba(15, 23, 42, 0.05), 0 1px 2px 0 rgba(15, 23, 42, 0.08);
        --md-sys-elevation-2: 0 2px 6px 2px rgba(15, 23, 42, 0.06), 0 1px 2px 0 rgba(15, 23, 42, 0.10);
        --md-sys-elevation-3: 0 4px 12px 3px rgba(15, 23, 42, 0.08), 0 1px 3px 0 rgba(15, 23, 42, 0.12);
        --md-sys-elevation-4: 0 6px 16px 4px rgba(15, 23, 42, 0.08), 0 2px 4px 0 rgba(15, 23, 42, 0.12);

        /* ==========================================================================
           3. M3 Shape Scale (Distinct rounded corners)
           ========================================================================== */
        --md-sys-shape-corner-full: 9999px;
        --md-sys-shape-corner-extra-large: 28px;
        --md-sys-shape-corner-large: 18px;
        --md-sys-shape-corner-medium: 12px;
        --md-sys-shape-corner-small: 8px;

        /* ==========================================================================
           4. M3 Motion & State Layers
           ========================================================================== */
        --md-sys-motion-easing-standard: cubic-bezier(0.2, 0.0, 0, 1.0);
        --md-sys-motion-duration-short: 0.2s;
        --md-sys-motion-duration-medium: 0.35s;

        /* ==========================================================================
           5. Typography Hierarchy
           ========================================================================== */
        --font-sans: 'Rubik', 'Heebo', -apple-system, BlinkMacSystemFont, sans-serif;
        --font-brand: 'Outfit', sans-serif;
        --font-mono: 'JetBrains Mono', monospace;
    }

    /* Base Body & App View - Full RTL Enforcement */
    html, body, [data-testid="stAppViewContainer"], .main {
        background-color: var(--md-sys-color-surface) !important;
        color: var(--md-sys-color-on-surface);
        font-family: var(--font-sans) !important;
        direction: rtl !important;
        text-align: right !important;
        -webkit-font-smoothing: antialiased;
    }

    [data-testid="stMarkdownContainer"],
    .stMarkdown, .stText {
        color: var(--md-sys-color-on-surface);
        font-family: var(--font-sans) !important;
        direction: rtl !important;
        text-align: right !important;
    }

    bdi, [dir="rtl"] {
        unicode-bidi: isolate !important;
    }

    /* Hide Sidebar completely */
    [data-testid="stSidebar"],
    [data-testid="collapsedControl"],
    section[data-testid="stSidebar"] {
        display: none !important;
        visibility: hidden !important;
        width: 0 !important;
    }

    /* Remove hover anchor link icons on headers */
    [data-testid="stHeaderActionElements"],
    [data-testid="stHeaderActionElements"] *,
    .st-emotion-cache-15zrgzn,
    .st-emotion-cache-gi04ae,
    a.anchorjs-link,
    [data-testid="stMarkdownContainer"] a[href^="#"],
    h1 a, h2 a, h3 a, h4 a, h5 a, h6 a,
    h1:hover a, h2:hover a, h3:hover a, h4:hover a {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        pointer-events: none !important;
    }

    /* Suppress image fullscreen/zoom button and element toolbars on hover */
    [data-testid="stImage"] button,
    [data-testid="StyledFullScreenButton"],
    [data-testid="stElementToolbar"],
    button[title*="fullscreen" i],
    button[title*="Fullscreen" i],
    button[title*="מסך מלא" i],
    button[title*="הגדלה" i] {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        pointer-events: none !important;
    }

    [data-testid="stHeader"] {
        background: transparent !important;
    }

    /* Container Spacing & Maximum Width */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3.5rem !important;
        max-width: 1200px !important;
        margin-left: auto !important;
        margin-right: auto !important;
        direction: rtl !important;
        text-align: right !important;
    }

    /* Horizontal layout (st.columns) - Enforce RTL row ordering */
    [data-testid="stHorizontalBlock"] {
        direction: rtl !important;
        text-align: right !important;
    }

    /* Typography Hierarchy */
    h1, h2, h3 {
        font-family: var(--font-sans) !important;
        color: var(--md-sys-color-on-surface) !important;
        font-weight: 800 !important;
        letter-spacing: -0.02em;
        text-align: right !important;
        direction: rtl !important;
    }
    h1 { font-size: 30px !important; }
    h2 { font-size: 24px !important; }
    h3 { font-size: 19px !important; }
    h4, h5, h6 {
        color: var(--md-sys-color-on-surface) !important;
        font-weight: 700 !important;
        text-align: right !important;
        direction: rtl !important;
    }

    /* ==========================================================================
       6. Material Design 3 Buttons (Filled, Tonal, Outlined & Download)
       ========================================================================== */
    /* Button base reset & typography */
    .stButton > button,
    [data-testid="baseButton-primary"],
    [data-testid="baseButton-secondary"],
    div.stButton > button {
        border-radius: var(--md-sys-shape-corner-full) !important;
        font-family: var(--font-sans) !important;
        font-weight: 700 !important;
        font-size: 14.5px !important;
        transition: all var(--md-sys-motion-duration-short) var(--md-sys-motion-easing-standard) !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        cursor: pointer !important;
        letter-spacing: -0.2px !important;
    }

    /* Remove text wrapper artifacts inside buttons */
    .stButton > button p,
    .stButton > button span,
    .stButton > button div,
    [data-testid="baseButton-primary"] p,
    [data-testid="baseButton-primary"] span,
    [data-testid="baseButton-secondary"] p,
    [data-testid="baseButton-secondary"] span {
        background: transparent !important;
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
        margin: 0 !important;
        color: inherit !important;
    }

    /* M3 Filled Button (Primary CTA) */
    [data-testid="baseButton-primary"],
    div.stButton > button[kind="primary"] {
        background-color: var(--md-sys-color-primary) !important;
        background: var(--md-sys-color-primary) !important;
        color: var(--md-sys-color-on-primary) !important;
        border: none !important;
        border-radius: var(--md-sys-shape-corner-full) !important;
        padding: 10px 28px !important;
        min-height: 46px !important;
        box-shadow: var(--md-sys-elevation-1) !important;
    }
    [data-testid="baseButton-primary"]:hover,
    div.stButton > button[kind="primary"]:hover {
        background-color: var(--md-sys-color-primary-hover) !important;
        background: var(--md-sys-color-primary-hover) !important;
        color: var(--md-sys-color-on-primary) !important;
        box-shadow: var(--md-sys-elevation-2) !important;
        transform: translateY(-1px) !important;
    }
    [data-testid="baseButton-primary"]:active,
    div.stButton > button[kind="primary"]:active {
        box-shadow: var(--md-sys-elevation-1) !important;
        transform: scale(0.98) !important;
    }
    [data-testid="baseButton-primary"] p,
    div.stButton > button[kind="primary"] p {
        color: #FFFFFF !important;
    }

    /* M3 Tonal / Outlined Button (Secondary) */
    [data-testid="baseButton-secondary"],
    div.stButton > button[kind="secondary"] {
        background-color: var(--md-sys-color-surface-container-lowest) !important;
        background: var(--md-sys-color-surface-container-lowest) !important;
        color: var(--md-sys-color-on-surface-variant) !important;
        border: 1.5px solid var(--md-sys-color-outline-variant) !important;
        border-radius: var(--md-sys-shape-corner-full) !important;
        padding: 8px 22px !important;
        min-height: 42px !important;
        box-shadow: var(--md-sys-elevation-1) !important;
    }
    [data-testid="baseButton-secondary"]:hover,
    div.stButton > button[kind="secondary"]:hover {
        background-color: var(--md-sys-color-surface-container-low) !important;
        background: var(--md-sys-color-surface-container-low) !important;
        border-color: var(--md-sys-color-primary) !important;
        color: var(--md-sys-color-primary) !important;
        box-shadow: var(--md-sys-elevation-2) !important;
        transform: translateY(-1px) !important;
    }
    [data-testid="baseButton-secondary"]:active,
    div.stButton > button[kind="secondary"]:active {
        box-shadow: var(--md-sys-elevation-0) !important;
        transform: scale(0.98) !important;
    }

    /* M3 Download Button */
    [data-testid="stDownloadButton"] > button {
        background: linear-gradient(135deg, #10B981 0%, #059669 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: var(--md-sys-shape-corner-full) !important;
        padding: 10px 26px !important;
        font-weight: 800 !important;
        box-shadow: var(--md-sys-elevation-1) !important;
        transition: all var(--md-sys-motion-duration-short) var(--md-sys-motion-easing-standard) !important;
    }
    [data-testid="stDownloadButton"] > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: var(--md-sys-elevation-2) !important;
    }

    /* ==========================================================================
       7. M3 Elevated Cards & Streamlit Containers
       ========================================================================== */
    [data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: var(--md-sys-shape-corner-large) !important;
        border: 1px solid var(--md-sys-color-outline-variant) !important;
        background-color: var(--md-sys-color-surface-container-lowest) !important;
        box-shadow: var(--md-sys-elevation-1) !important;
        transition: all var(--md-sys-motion-duration-short) var(--md-sys-motion-easing-standard) !important;
        padding: 16px 22px !important;
        margin-bottom: 16px !important;
    }
    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: #CBD5E1 !important;
        box-shadow: var(--md-sys-elevation-2) !important;
    }

    .custom-card {
        background: var(--md-sys-color-surface-container-lowest);
        border: 1px solid var(--md-sys-color-outline-variant);
        border-radius: var(--md-sys-shape-corner-extra-large);
        padding: 24px 28px;
        margin-bottom: 20px;
        box-shadow: var(--md-sys-elevation-1);
        transition: all var(--md-sys-motion-duration-short) var(--md-sys-motion-easing-standard);
        direction: rtl;
        text-align: right;
    }
    .custom-card:hover {
        border-color: var(--md-sys-color-primary);
        box-shadow: var(--md-sys-elevation-2);
    }

    /* ==========================================================================
       8. M3 Primary Navigation Tabs (Segmented Pill Container)
       ========================================================================== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px !important;
        background-color: var(--md-sys-color-surface-container) !important;
        padding: 6px 8px !important;
        border-radius: var(--md-sys-shape-corner-full) !important;
        border: 1px solid var(--md-sys-color-outline-variant) !important;
        direction: rtl !important;
        margin-bottom: 18px !important;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: var(--md-sys-shape-corner-full) !important;
        padding: 10px 22px !important;
        color: var(--md-sys-color-on-surface-variant) !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        background: transparent !important;
        border: none !important;
        transition: all var(--md-sys-motion-duration-short) var(--md-sys-motion-easing-standard) !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: var(--md-sys-color-primary) !important;
        background: rgba(255, 255, 255, 0.6) !important;
    }
    .stTabs [aria-selected="true"] {
        background-color: var(--md-sys-color-surface-container-lowest) !important;
        color: var(--md-sys-color-primary) !important;
        box-shadow: var(--md-sys-elevation-1) !important;
        font-weight: 800 !important;
    }
    .stTabs [data-baseweb="tab-highlight"],
    .stTabs [data-baseweb="tab-border"] {
        display: none !important;
    }

    /* ==========================================================================
       9. M3 Filter Chips (st.pills) & Radio Buttons
       ========================================================================== */
    [data-testid="stPills"] {
        gap: 10px !important;
        margin-bottom: 12px !important;
    }
    [data-testid="stPills"] button {
        border-radius: var(--md-sys-shape-corner-full) !important;
        padding: 8px 20px !important;
        font-family: var(--font-sans) !important;
        font-weight: 700 !important;
        font-size: 14px !important;
        border: 1.5px solid var(--md-sys-color-outline-variant) !important;
        background: var(--md-sys-color-surface-container-lowest) !important;
        color: var(--md-sys-color-on-surface-variant) !important;
        transition: all var(--md-sys-motion-duration-short) var(--md-sys-motion-easing-standard) !important;
        box-shadow: var(--md-sys-elevation-0) !important;
    }
    [data-testid="stPills"] button:hover {
        border-color: var(--md-sys-color-primary) !important;
        background: var(--md-sys-color-surface-container-low) !important;
        color: var(--md-sys-color-primary) !important;
    }
    [data-testid="stPills"] button[aria-pressed="true"],
    [data-testid="stPills"] button[data-selected="true"] {
        background: var(--md-sys-color-primary-container) !important;
        color: var(--md-sys-color-on-primary-container) !important;
        border: 1.5px solid #C7D2FE !important;
        box-shadow: var(--md-sys-elevation-1) !important;
        font-weight: 800 !important;
    }

    /* Radio buttons styled as M3 selection cards */
    [data-testid="stRadio"] > div {
        gap: 12px !important;
    }
    [data-testid="stRadio"] label {
        background: var(--md-sys-color-surface-container-lowest) !important;
        border: 1.5px solid var(--md-sys-color-outline-variant) !important;
        border-radius: var(--md-sys-shape-corner-large) !important;
        padding: 10px 18px !important;
        transition: all var(--md-sys-motion-duration-short) var(--md-sys-motion-easing-standard) !important;
        box-shadow: var(--md-sys-elevation-1) !important;
        cursor: pointer !important;
    }
    [data-testid="stRadio"] label:hover {
        border-color: var(--md-sys-color-primary) !important;
        background: var(--md-sys-color-surface-container-low) !important;
    }

    /* ==========================================================================
       10. M3 Outlined Text Fields, Selectbox & File Uploader
       ========================================================================== */
    textarea, input, [data-baseweb="textarea"], [data-baseweb="input"] {
        background-color: var(--md-sys-color-surface-container-lowest) !important;
        color: var(--md-sys-color-on-surface) !important;
        border: 1.5px solid var(--md-sys-color-outline) !important;
        border-radius: var(--md-sys-shape-corner-medium) !important;
        font-family: var(--font-sans) !important;
        direction: rtl !important;
        text-align: right !important;
        transition: border-color var(--md-sys-motion-duration-short) ease, box-shadow var(--md-sys-motion-duration-short) ease !important;
    }
    [data-baseweb="textarea"]:focus-within, [data-baseweb="input"]:focus-within {
        border-color: var(--md-sys-color-primary) !important;
        box-shadow: 0 0 0 3px rgba(90, 69, 255, 0.14) !important;
    }

    [data-baseweb="select"] > div {
        border-radius: var(--md-sys-shape-corner-medium) !important;
        border: 1.5px solid var(--md-sys-color-outline) !important;
        background: var(--md-sys-color-surface-container-lowest) !important;
    }

    [data-testid="stFileUploader"] {
        background: var(--md-sys-color-surface-container-low);
        border: 1.5px dashed var(--md-sys-color-outline);
        border-radius: var(--md-sys-shape-corner-large);
        padding: 16px 20px;
        transition: all var(--md-sys-motion-duration-short) ease;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: var(--md-sys-color-primary);
        background: var(--md-sys-color-surface-container);
    }

    /* ==========================================================================
       11. M3 Checkbox Styling
       ========================================================================== */
    [data-testid="stCheckbox"] {
        display: flex !important;
        align-items: center !important;
    }
    [data-testid="stCheckbox"] div[role="checkbox"] {
        border-radius: 6px !important;
        border: 2px solid var(--md-sys-color-outline) !important;
        transition: all var(--md-sys-motion-duration-short) ease !important;
    }
    [data-testid="stCheckbox"] div[role="checkbox"][aria-checked="true"] {
        background-color: var(--md-sys-color-primary) !important;
        border-color: var(--md-sys-color-primary) !important;
    }

    /* Clean Expander */
    [data-testid="stExpander"] {
        background: var(--md-sys-color-surface-container-lowest) !important;
        border: 1.5px solid var(--md-sys-color-outline-variant) !important;
        border-radius: var(--md-sys-shape-corner-large) !important;
        overflow: hidden;
        margin-bottom: 16px;
    }

    /* Code Block resets */
    .stMarkdown code, [data-testid="stMarkdownContainer"] code {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
        color: inherit !important;
    }
    </style>
    """
    return textwrap.dedent(css).strip()


def render_step_bar(current_step: int = 1, theme: str = "light") -> str:
    """סרגל שלבים מעוצב למסך הראשי עם תמיכה מלאה במצב כהה ובהיר"""
    is_dark = False
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


def render_ats_tip(theme: str = "light") -> str:
    """כרטיס טיפ מקצועי לעמידה ב-ATS לפי מפרט M3 Tonal Assist Card"""
    html = """
    <div style="background: #F5F3FF; border: 1.5px solid #DDD6FE; border-radius: 18px; padding: 20px 26px; margin-bottom: 22px; display: flex; align-items: flex-start; gap: 14px; direction: rtl; text-align: right; box-shadow: var(--md-sys-elevation-1);">
        <div style="width: 40px; height: 40px; border-radius: 12px; background: #EDE9FE; color: #5A45FF; display: flex; align-items: center; justify-content: center; font-size: 20px; flex-shrink: 0; border: 1px solid #C7D2FE;">💡</div>
        <div style="flex: 1;">
            <strong style="color: #3730A3; font-size: 15.5px; display: block; margin-bottom: 4px;">
                טיפ מקצועי למעבר סינון ראשוני (Strict ATS):
            </strong>
            <p style="margin: 0; color: #334155; font-size: 14px; line-height: 1.6;">
                מערכות גיוס מודרניות (Greenhouse, Workday, Lever) בודקות מילות מפתח בהקשר מעשי. 
                הנוסחה המנצחת של Google לקורות חיים היא: 
                <span style="color: #4338CA; font-weight: 700; direction: ltr; display: inline-block;">"Accomplished [X] as measured by [Y], by doing [Z]"</span>
                (השגת יעד מדיד באמצעות טכנולוגיה ספציפית).
            </p>
        </div>
    </div>
    """
    return textwrap.dedent(html).strip()


def render_score_gauge(score: int, summary: str, theme: str = "light") -> str:
    """מד ציון התאמה הנדסי בעיצוב Material Design 3 Elevated Card"""
    if score >= 75:
        circle_bg = "#ECFDF5"
        circle_border = "#10B981"
        circle_color = "#065F46"
        circle_shadow = "0 0 16px rgba(16, 185, 129, 0.22)"
        status_text = "התאמה גבוהה (מוכן להגשה)"
        subtext = "קורות החיים מציגים את רוב דרישות הסף המרכזיות."
        badge_style = "background: #ECFDF5; color: #065F46; border: 1.5px solid #6EE7B7;"
    elif score >= 50:
        circle_bg = "#FFFBEB"
        circle_border = "#F59E0B"
        circle_color = "#92400E"
        circle_shadow = "0 0 16px rgba(245, 158, 11, 0.22)"
        status_text = "התאמה בינונית (דורשת שדרוג)"
        subtext = "קיימת תשתית טובה, אך חסרות טכנולוגיות מפתח להבטחת מעבר סינון."
        badge_style = "background: #FFFBEB; color: #92400E; border: 1.5px solid #FCD34D;"
    else:
        circle_bg = "#FEF2F2"
        circle_border = "#EF4444"
        circle_color = "#991B1B"
        circle_shadow = "0 0 16px rgba(239, 68, 68, 0.22)"
        status_text = "פער הנדסי משמעותי"
        subtext = "מומלץ לבנות פרויקט ממוקד בפורטפוליו לפני הגשת מועמדות."
        badge_style = "background: #FEF2F2; color: #991B1B; border: 1.5px solid #FCA5A5;"

    html = f"""
    <div style="background: var(--md-sys-color-surface-container-lowest); border: 1px solid var(--md-sys-color-outline-variant); border-radius: var(--md-sys-shape-corner-extra-large); padding: 26px 32px; margin-bottom: 22px; box-shadow: var(--md-sys-elevation-1); display: flex; align-items: center; gap: 28px; flex-wrap: wrap; direction: rtl; text-align: right;">
        <div style="width: 100px; height: 100px; border-radius: 50%; background: {circle_bg}; border: 3.5px solid {circle_border}; color: {circle_color}; box-shadow: {circle_shadow}; display: flex; flex-direction: column; align-items: center; justify-content: center; flex-shrink: 0; font-family: 'Outfit', sans-serif;">
            <div style="font-size: 32px; line-height: 1; font-weight: 900;">{score}%</div>
            <div style="font-size: 11px; font-weight: 800; opacity: 0.85; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">MATCH</div>
        </div>
        <div style="flex: 1; direction: rtl; text-align: right;">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px; flex-wrap: wrap;">
                <h3 style="margin: 0; font-size: 20px; font-weight: 800; color: #0F172A;">ציון התאמה הנדסי משוקלל</h3>
                <span style="font-size: 13px; font-weight: 800; padding: 4px 16px; border-radius: 9999px; {badge_style}">
                    {status_text}
                </span>
            </div>
            <div style="color: #334155; font-size: 15px; line-height: 1.6; font-weight: 500;">{summary}</div>
            <div style="margin-top: 8px; color: #64748B; font-size: 13.5px;">{subtext}</div>
        </div>
    </div>
    """
    return textwrap.dedent(html).strip()


def render_skill_badges(missing_skills: list, theme: str = "light") -> str:
    """תגיות מיומנויות חסרות מחולקות לחומרה עם צבעי M3 Assist Chips"""
    high_skills = [s for s in missing_skills if s.get("importance") == "High"]
    med_skills = [s for s in missing_skills if s.get("importance") == "Medium"]
    low_skills = [s for s in missing_skills if s.get("importance") == "Low"]

    parts = ['<div style="direction: rtl; text-align: right; margin-bottom: 20px;">']

    if high_skills:
        badges = "".join([
            f'<div style="display: inline-flex; align-items: center; gap: 6px; padding: 5px 14px; border-radius: 9999px; font-size: 13px; font-weight: 700; margin: 3px; background: #FEF2F2; color: #991B1B; border: 1.5px solid #FCA5A5;"><strong>{s.get("skill")}</strong> <span style="font-size: 11px; opacity: 0.9;">• HIGH</span></div>'
            for s in high_skills
        ])
        parts.append(f'<div style="margin-bottom: 14px;"><span style="font-size: 14.5px; font-weight: 800; color: #EF4444;">🔴 פערי חובה קריטיים (Must-Have):</span><div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px;">{badges}</div></div>')

    if med_skills:
        badges = "".join([
            f'<div style="display: inline-flex; align-items: center; gap: 6px; padding: 5px 14px; border-radius: 9999px; font-size: 13px; font-weight: 700; margin: 3px; background: #FFFBEB; color: #92400E; border: 1.5px solid #FCD34D;"><strong>{s.get("skill")}</strong> <span style="font-size: 11px; opacity: 0.9;">• MEDIUM</span></div>'
            for s in med_skills
        ])
        parts.append(f'<div style="margin-bottom: 14px;"><span style="font-size: 14.5px; font-weight: 800; color: #F59E0B;">🟡 פערים מהותיים שכדאי לגשר:</span><div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px;">{badges}</div></div>')

    if low_skills:
        badges = "".join([
            f'<div style="display: inline-flex; align-items: center; gap: 6px; padding: 5px 14px; border-radius: 9999px; font-size: 13px; font-weight: 700; margin: 3px; background: #F0F9FF; color: #0369A1; border: 1.5px solid #7DD3FC;"><strong>{s.get("skill")}</strong> <span style="font-size: 11px; opacity: 0.9;">• LOW</span></div>'
            for s in low_skills
        ])
        parts.append(f'<div style="margin-bottom: 14px;"><span style="font-size: 14.5px; font-weight: 800; color: #0284C7;">🔵 מיומנויות יתרון (Nice-to-Have):</span><div style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px;">{badges}</div></div>')

    parts.append('</div>')
    return "".join(parts)


def render_bullet_comparison(improvements: list, theme: str = "light") -> str:
    """שדרוג סעיפי קורות חיים Before / After לפי עיצוב M3 Elevated Cards"""
    cards = []
    for i, item in enumerate(improvements, 1):
        orig = item.get("original", "")
        imp = item.get("improved", "")
        reason = item.get("reason", "")
        
        card = f"""
        <div style="background: var(--md-sys-color-surface-container-lowest); border: 1px solid var(--md-sys-color-outline-variant); border-radius: 20px; padding: 22px 26px; margin-bottom: 18px; box-shadow: var(--md-sys-elevation-1); direction: rtl; text-align: right;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; flex-wrap: wrap; gap: 8px;">
                <span style="font-weight: 800; color: #3730A3; font-size: 15.5px;">
                    📌 סעיף {i}: שדרוג מבוסס Action-Impact (מוכן להעתקה לקורות החיים)
                </span>
                <span style="font-size: 12px; background: #ECFDF5; color: #065F46; padding: 4px 14px; border-radius: 9999px; font-weight: 800; border: 1px solid #6EE7B7;">
                    ATS Optimized ✔
                </span>
            </div>
            <div style="background: #FEF2F2; border: 1px solid #FECACA; border-radius: 14px; padding: 14px 18px; margin: 8px 0; font-size: 14.5px; line-height: 1.6; color: #991B1B;">
                <span style="font-size: 13px; font-weight: 800; display: block; color: #EF4444; margin-bottom: 4px;">
                    ✖ נוסח מקורי בקורות החיים (פסיבי / חסר נתונים):
                </span>
                {orig}
            </div>
            <div style="background: #F0FDF4; border: 1px solid #BBF7D0; border-radius: 14px; padding: 14px 18px; margin: 8px 0; font-size: 14.5px; line-height: 1.6; color: #14532D;">
                <span style="font-size: 13px; font-weight: 800; display: block; color: #10B981; margin-bottom: 4px;">
                    ✔ נוסח משודרג וממוקד משרה (Action + Scale + Impact):
                </span>
                {imp}
            </div>
            <div style="margin-top: 12px; background: #EDE9FE; border: 1px solid #DDD6FE; border-radius: 10px; padding: 10px 16px; display: flex; align-items: center; gap: 8px;">
                <span style="color: #3730A3; font-size: 13.5px; font-weight: 700;">💡 למה זה מקפיץ את הסיכוי? {reason}</span>
            </div>
        </div>
        """
        cards.append(textwrap.dedent(card).strip())
    return "".join(cards)


def render_onboarding_progress(current_step: int, total_steps: int = 3, theme: str = "light") -> str:
    """מחוון נקודות מעוצב"""
    dots = []
    for i in range(1, total_steps + 1):
        active_cls = "active" if i == current_step else ""
        dots.append(f'<div class="onboarding-dot {active_cls}"></div>')
    return f'<div class="onboarding-dots">{"".join(dots)}</div>'


def render_career_intel(domain: dict, theme: str = "light") -> str:
    """כרטיס סקירה מקצועית מעמיקה עבור התחום שנבחר"""
    is_dark = False
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


def render_learning_paths(paths: list, theme: str = "light") -> str:
    """מחולל כרטיסי מסלולי לימוד והסמכות לפי עיצוב M3 Elevated Cards"""
    if not paths:
        return """
        <div style="background: var(--md-sys-color-surface-container-lowest); border: 1px solid var(--md-sys-color-outline-variant); border-radius: 16px; padding: 20px; text-align: center; color: var(--text-muted);">
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
        <div style="background: var(--md-sys-color-surface-container-lowest); border: 1px solid var(--md-sys-color-outline-variant); border-radius: 18px; padding: 20px 24px; margin-bottom: 16px; direction: rtl; text-align: right; box-shadow: var(--md-sys-elevation-1);">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px; margin-bottom: 12px;">
                <div>
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
                        <span style="background: #EDE9FE; color: #3730A3; border: 1px solid #C7D2FE; border-radius: 9999px; padding: 3px 12px; font-size: 12px; font-weight: 800;">{domain} • {lp_type}</span>
                        <span style="font-size: 12.5px; color: #64748B; font-weight: 600;">רמה: {level}</span>
                    </div>
                    <h4 style="margin: 0; font-size: 18px; font-weight: 800; color: #0F172A;">{name}</h4>
                </div>
                <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;">
                    <span style="background: #ECFDF5; color: #065F46; border: 1px solid #6EE7B7; border-radius: 9999px; padding: 4px 12px; font-size: 12.5px; font-weight: 800;">⏱ משך: {duration}</span>
                    <span style="background: #FFFBEB; color: #92400E; border: 1px solid #FCD34D; border-radius: 9999px; padding: 4px 12px; font-size: 12.5px; font-weight: 800;">חוזק הוכחה: {stars}</span>
                </div>
            </div>
            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px 16px; margin: 12px 0;">
                <strong style="color: #3730A3; font-size: 13.5px; display: block; margin-bottom: 3px;">🎯 מתי מומלץ על פי המודל?</strong>
                <p style="margin: 0; color: #334155; font-size: 13.5px; line-height: 1.5;">{when_to}</p>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-top: 14px;">
                <div style="flex: 1; min-width: 260px;">
                    <span style="color: #4338CA; font-size: 13px; font-weight: 700;">🛠 פרויקט הוכחה מומלץ:</span>
                    <span style="color: #334155; font-size: 13px;"> {project}</span>
                </div>
                <a href="{url}" target="_blank" style="background: #5A45FF; color: #FFFFFF; text-decoration: none; padding: 7px 20px; border-radius: 9999px; font-size: 12.5px; font-weight: 800; display: inline-flex; align-items: center; gap: 6px; box-shadow: var(--md-sys-elevation-1); transition: all 0.2s ease;">
                    סילבוס ומקור רשמי ↗
                </a>
            </div>
        </div>
        """
        cards.append(textwrap.dedent(card_html).strip())
    return "".join(cards)


def render_job_search_tracker(milestones: list, progress_pct: int, theme: str = "light") -> str:
    """
    רכיב מעקב התקדמות בחיפוש עבודה (UX/UI Job Search Roadmap & Progress Tracker)
    מציג גרף התקדמות, מד מוכנות לגיוס, וצ'קליסט אבני דרך אינטראקטיבי.
    """
    is_dark = False
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


def render_readme_block(readme_content: str, project_name: str, theme: str = "light") -> str:
    """
    רכיב תצוגת קוד/Markdown מקצועי (IDE Style Code Block) עבור שלד README.md.
    כולל חלון עליון עם כותרת, תגיות פורמט, ומסך קוד LTR מלא לצפייה לפני ההורדה (TC-07).
    """
    is_dark = False
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
