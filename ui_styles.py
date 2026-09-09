"""
ui_styles.py - מערכת העיצוב המלאה של GetAJob
תומכת באופן מלא ב-Dark Mode (ערכת הנושא המקורית והרשמית של האפיון - PRD סעיף 1.4)
וב-Light Mode (לפי בחירת המשתמש באמצעות מתג מהיר).
כולל רכיב תצוגת קוד/Markdown מקצועי עבור שלד ה-README.md, התאמת ניגודיות מלאה,
ומעקב התקדמות מקצועי בחיפוש עבודה ל-UX/UI.
"""

import os
import base64
import textwrap


def get_custom_css(theme: str = "light") -> str:
    """
    מחזיר את קובץ ה-CSS המלא עבור GetAJob המוטמע לפי עקרונות Google Material Design 3 (Material You).
    כולל מערכת טוקנים רשמית, Tonal Elevation, קצוות מעוגלים לפי M3 Shape Scale, וכפתורי קפסולה מלאים.
    """
    css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

    :root {
        /* ==========================================================================
           1. פלטת צבעים — GetAJob Design Handoff v1.0 (8 בספטמבר 2026)
           ========================================================================== */
        /* 1.1 רקעים ומשטחים */
        --bg-base: #FBF9F4;
        --surface: linear-gradient(180deg, #FFFFFF, #FDFCF9);
        --surface-sunken: linear-gradient(180deg, #FCFAF6, #F5F1E7);
        --surface-glass: rgba(255, 255, 255, 0.72);
        --surface-dark: #111114;
        --border: #EEE8DA;
        --border-input: #E4DED0;
        --border-hairline: #F2EDE1;

        /* 1.3 אקסנט */
        --accent: #4F46E5;
        --accent-light: #6C63FF;
        --accent-deep: #4338CA;
        --accent-tint: linear-gradient(180deg, #F4F2FF, #EAE6FF);
        --accent-ring: rgba(79, 70, 229, 0.14);

        /* 1.4 טקסט */
        --text: #17171C;
        --text-body: #4A4A55;
        --text-muted: #6B6B74;
        --text-on-dark: #FBF9F4;
        --text-on-dark-body: #A9A9B4;
        --text-placeholder: #9A9AA4;

        /* 1.5 סמנטיים (נתונים ומצבי מערכת בלבד — לא לכפתורים!) */
        --semantic-error: #B42318;
        --semantic-error-bg: #FEE2E2;
        --semantic-warning: #92400E;
        --semantic-warning-bg: #FEF3C7;
        --semantic-success: #166534;
        --semantic-success-bg: #DCFCE7;
        --state-dot: #16A34A;

        /* 4. צללים ואפקטים מדויקים */
        --sh-card: 0 1px 2px rgba(23, 23, 28, 0.035), 0 18px 40px -30px rgba(23, 23, 28, 0.4);
        --sh-panel: 0 1px 2px rgba(23, 23, 28, 0.035), 0 24px 50px -32px rgba(23, 23, 28, 0.45);
        --sh-nav: 0 1px 2px rgba(23, 23, 28, 0.04), 0 18px 40px -28px rgba(23, 23, 28, 0.45);
        --sh-accent: 0 1px 0 rgba(255, 255, 255, 0.28) inset, 0 14px 30px -12px rgba(79, 70, 229, 0.75);
        --sh-selected: 0 0 0 4px rgba(79, 70, 229, 0.13), 0 22px 46px -30px rgba(79, 70, 229, 0.85);
        --sh-inset: 0 1px 2px rgba(23, 23, 28, 0.06) inset;
        --sh-dark: 0 40px 90px -50px rgba(23, 23, 28, 0.85);

        /* טיפוגרפיה — Heebo בלבד בממשק */
        --font-sans: 'Heebo', -apple-system, BlinkMacSystemFont, sans-serif;
        --font-mono: 'JetBrains Mono', monospace;

        /* תאימות למערכת הכללית */
        --md-sys-color-primary: var(--accent);
        --md-sys-color-on-primary: #FFFFFF;
        --md-sys-color-surface: var(--bg-base);
        --md-sys-color-on-surface: var(--text);
        --md-sys-color-on-surface-variant: var(--text-body);
        --md-sys-color-outline: var(--border-input);
        --md-sys-color-outline-variant: var(--border);
    }

    /* 1.2 שכבת ה-Gradient (חתימה ויזואלית — חובה) על ה-body והמכולה הראשית */
    html, body, [data-testid="stAppViewContainer"], .main {
        background-color: #FBF9F4 !important;
        background-image:
            radial-gradient(1100px 620px at 78% -8%, #E9E6FF 0%, rgba(233, 230, 255, 0) 62%),
            radial-gradient(900px 520px at 8% 4%, #FFF3E4 0%, rgba(255, 243, 228, 0) 58%) !important;
        background-attachment: fixed !important;
        background-repeat: no-repeat !important;
        color: #4A4A55 !important;
        font-family: 'Heebo', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
        -webkit-font-smoothing: antialiased;
    }

    body, [data-testid="stAppViewContainer"],
    [data-testid="stMarkdownContainer"],
    .stMarkdown, .stText, p, label {
        font-family: 'Heebo', sans-serif !important;
    }

    span:not([data-testid="stIconMaterial"]):not([class*="material-symbols"]) {
        font-family: 'Heebo', sans-serif !important;
    }

    span[data-testid="stIconMaterial"], .material-symbols-rounded, .material-symbols-outlined, .material-icons {
        font-family: "Material Symbols Rounded", "Material Symbols Outlined", "Material Icons" !important;
    }

    bdi, [dir="rtl"] {
        unicode-bidi: isolate !important;
    }

    [dir="ltr"], [dir="ltr"] * {
        direction: ltr !important;
        unicode-bidi: isolate !important;
    }

    /* הסתרת סרגל צד */
    [data-testid="stSidebar"],
    [data-testid="collapsedControl"],
    section[data-testid="stSidebar"] {
        display: none !important;
        visibility: hidden !important;
        width: 0 !important;
    }

    /* החלקת גלילה וסרגל גלילה בצד ימין מותאם לצבעי הממשק */
    html, body {
        scroll-behavior: smooth !important;
    }

    section[data-testid="stMain"],
    .stMain {
        direction: ltr !important;
        overflow-y: auto !important;
        overflow-x: hidden !important;
        scrollbar-width: thin !important;
        scrollbar-color: #C7D2FE transparent !important;
        scroll-behavior: smooth !important;
    }

    section[data-testid="stMain"] > *,
    .stMain > * {
        direction: rtl !important;
    }

    section[data-testid="stMain"]::-webkit-scrollbar,
    .stMain::-webkit-scrollbar,
    ::-webkit-scrollbar {
        width: 8px !important;
        height: 8px !important;
    }

    section[data-testid="stMain"]::-webkit-scrollbar-track,
    .stMain::-webkit-scrollbar-track,
    ::-webkit-scrollbar-track {
        background: transparent !important;
    }

    section[data-testid="stMain"]::-webkit-scrollbar-thumb,
    .stMain::-webkit-scrollbar-thumb,
    ::-webkit-scrollbar-thumb {
        background: #C7D2FE !important;
        border-radius: 9999px !important;
    }

    section[data-testid="stMain"]::-webkit-scrollbar-thumb:hover,
    .stMain::-webkit-scrollbar-thumb:hover,
    ::-webkit-scrollbar-thumb:hover {
        background: #4F46E5 !important;
    }

    /* הסתרת אייקוני עוגן של כותרות Streamlit בלבד */
    a.anchorjs-link,
    [data-testid="stMarkdownContainer"] :is(h1, h2, h3, h4, h5, h6) > a,
    h1 a, h2 a, h3 a, h4 a, h5 a, h6 a,
    h1:hover a, h2:hover a, h3:hover a, h4:hover a {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        pointer-events: none !important;
    }

    /* הסרת כפתורי מסך מלא על תמונות */
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
        display: none !important;
        height: 0 !important;
        min-height: 0 !important;
        pointer-events: none !important;
        visibility: hidden !important;
    }

    /* 5.6 ניווט צף — Floating Frosted Glass Navbar */
    .m3-landing-navbar {
        position: fixed !important;
        top: 14px !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        width: min(1180px, calc(100% - 36px)) !important;
        z-index: 99999 !important;
        display: grid !important;
        grid-template-columns: 1fr auto 1fr !important;
        align-items: center !important;
        padding: 12px 24px !important;
        background: rgba(255, 255, 255, 0.72) !important;
        backdrop-filter: blur(14px) !important;
        -webkit-backdrop-filter: blur(14px) !important;
        border: 1px solid rgba(23, 23, 28, 0.07) !important;
        border-radius: 16px !important;
        box-shadow: 0 1px 2px rgba(23, 23, 28, 0.04), 0 18px 40px -28px rgba(23, 23, 28, 0.45) !important;
        transition: box-shadow 0.18s ease, border-color 0.18s ease, transform 0.18s ease !important;
    }

    /* כפתור חזרה לראש העמוד — סעיף 5.6 */
    #back-to-top-btn {
        position: fixed !important;
        left: 24px !important;
        bottom: 28px !important;
        width: 48px !important;
        height: 48px !important;
        border-radius: 14px !important;
        background: #FFFFFF !important;
        border: 1px solid #EEE8DA !important;
        box-shadow: 0 1px 2px rgba(23, 23, 28, 0.035), 0 18px 40px -30px rgba(23, 23, 28, 0.4) !important;
        color: #4A4A55 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        cursor: pointer !important;
        z-index: 99999 !important;
        opacity: 0;
        pointer-events: none;
        transition: all 0.2s ease !important;
    }
    #back-to-top-btn:hover {
        background: linear-gradient(180deg, #6C63FF, #4F46E5) !important;
        border-color: #4338CA !important;
        color: #FFFFFF !important;
        box-shadow: 0 1px 0 rgba(255, 255, 255, 0.28) inset, 0 14px 30px -12px rgba(79, 70, 229, 0.75) !important;
        transform: translateY(-2px) !important;
    }

    /* סקשן איך זה עובד — גריד 2 טורים זה לצד זה */
    .m3-how-it-works-grid {
        display: grid !important;
        grid-template-columns: 1fr 1.08fr !important;
        gap: 44px !important;
        align-items: center !important;
    }
    @media (max-width: 860px) {
        .m3-how-it-works-grid {
            grid-template-columns: 1fr !important;
        }
    }

    /* סקשן שאלות נפוצות — 2 שורות של כרטיסיות, 2 בכל שורה */
    .m3-faq-cards-grid {
        display: grid !important;
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 18px !important;
        direction: rtl !important;
        text-align: right !important;
    }
    @media (max-width: 768px) {
        .m3-faq-cards-grid {
            grid-template-columns: 1fr !important;
        }
    }
    .m3-faq-card {
        background: #FFFFFF !important;
        border: 1px solid #EEE8DA !important;
        border-radius: 18px !important;
        padding: 22px 20px !important;
        box-shadow: 0 1px 2px rgba(23, 23, 28, 0.035), 0 8px 20px -16px rgba(23, 23, 28, 0.08) !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: flex-start !important;
        text-align: right !important;
        direction: rtl !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease !important;
    }
    .m3-faq-card:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 12px 28px -10px rgba(79, 70, 229, 0.14) !important;
        border-color: #DDD6FE !important;
    }

    /* מרכוז כותרות ותיאורים ייעודיים בכל הסקשנים */
    .m3-hero-title-container,
    .m3-hero-title-container h1,
    .m3-hero-title-container .m3-hero-title-1,
    .m3-hero-title-container .m3-hero-title-2,
    .m3-hero-subtitle-container,
    .m3-hero-subtitle-container p,
    .m3-hero-subtitle,
    #how-it-works .m3-section-header,
    #how-it-works h2,
    #sample-output .m3-section-header,
    #sample-output h2,
    #sample-output p.m3-section-subtitle,
    #faq .m3-section-header,
    #faq h2,
    #faq p.m3-section-subtitle {
        text-align: center !important;
    }

    /* תיקון צבע, משקל וגודל בבאנר הכהה התחתון */
    #bottom-cta {
        max-width: 900px !important;
        margin-inline: auto !important;
        text-align: center !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
    }
    #bottom-cta h2,
    #bottom-cta .m3-bottom-cta-title {
        color: #FBF9F4 !important;
        text-align: center !important;
        font-weight: 800 !important;
        margin-top: 0 !important;
        margin-bottom: 0 !important;
        line-height: 1.15 !important;
        width: 100% !important;
    }
    #bottom-cta p,
    #bottom-cta .m3-bottom-cta-desc {
        color: #A9A9B4 !important;
        text-align: center !important;
        font-weight: 400 !important;
        margin-top: -3px !important;
        margin-bottom: 0 !important;
        font-size: 15px !important;
        line-height: 1.35 !important;
        width: 100% !important;
    }

    /* הכנסת כפתור ה-CTA התחתון לתוך מלבן הבאנר הכהה בריווח מדויק ומכולה קומפקטית */
    div:has(#bottom-cta) ~ div [data-testid="stHorizontalBlock"]:has(.stButton) {
        max-width: 900px !important;
        margin-inline: auto !important;
        margin-top: -76px !important;
        margin-bottom: 45px !important;
        position: relative !important;
        z-index: 10 !important;
    }
    div:has(#bottom-cta) ~ div [data-testid="stHorizontalBlock"] [data-testid="stButton"] {
        display: flex !important;
        justify-content: center !important;
    }
    div:has(#bottom-cta) ~ div [data-testid="stHorizontalBlock"] button {
        max-width: 210px !important;
        width: 100% !important;
        margin-inline: auto !important;
        font-weight: 800 !important;
        padding: 12px 20px !important;
    }
    div:has(#bottom-cta) ~ div [data-testid="stHorizontalBlock"] button p,
    div:has(#bottom-cta) ~ div [data-testid="stHorizontalBlock"] button span {
        font-weight: 800 !important;
    }

    /* היסט עוגן גלילה עבור ניווט קבוע */
    #how-it-works, #sample-output, #faq, #bottom-cta {
        scroll-margin-top: 96px !important;
    }

    /* מכולה ראשית — סעיף 3 (max-width: 1180px, padding-inline: 32px) */
    .block-container {
        max-width: 1180px !important;
        padding-inline: 32px !important;
        margin-inline: auto !important;
        padding-top: 96px !important;
        padding-bottom: 64px !important;
        direction: rtl !important;
        text-align: right !important;
    }

    [data-testid="stHorizontalBlock"] {
        direction: rtl !important;
        text-align: right !important;
    }

    /* 2. טיפוגרפיה — Heebo בלבד, text-wrap: pretty על כל הכותרות */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Heebo', sans-serif !important;
        color: #17171C !important;
        font-weight: 800 !important;
        text-wrap: pretty !important;
        text-align: right !important;
        direction: rtl !important;
    }
    h1 {
        font-size: clamp(28px, 3.7vw, 44px) !important;
        line-height: 1.1 !important;
        letter-spacing: -0.03em !important;
    }
    h2 {
        font-size: clamp(28px, 3.4vw, 42px) !important;
        line-height: 1.14 !important;
        letter-spacing: -0.025em !important;
    }
    h3 {
        font-size: 18px !important;
        line-height: 1.3 !important;
        letter-spacing: -0.01em !important;
    }

    /* 5.1 כפתורים */
    .stButton > button,
    [data-testid="baseButton-primary"],
    [data-testid="baseButton-secondary"],
    div.stButton > button {
        font-family: 'Heebo', sans-serif !important;
        font-weight: 700 !important;
        transition: box-shadow 0.18s ease, border-color 0.18s ease, transform 0.18s ease !important;
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        cursor: pointer !important;
        min-height: 44px !important;
    }

    .stButton > button p,
    .stButton > button span,
    [data-testid="baseButton-primary"] p,
    [data-testid="baseButton-primary"] span,
    [data-testid="baseButton-secondary"] p,
    [data-testid="baseButton-secondary"] span {
        background: transparent !important;
        color: inherit !important;
    }

    /* כפתור ראשי (Primary) — גרדיאנט אינדיגו, מסגרת 4338CA, רדיוס 12px */
    [data-testid="baseButton-primary"],
    div.stButton > button[kind="primary"] {
        background: linear-gradient(180deg, #6C63FF, #4F46E5) !important;
        border: 1px solid #4338CA !important;
        color: #FFFFFF !important;
        box-shadow: 0 1px 0 rgba(255, 255, 255, 0.28) inset, 0 14px 30px -12px rgba(79, 70, 229, 0.75) !important;
        border-radius: 12px !important;
        padding: 16px 30px !important;
        font-size: 16.5px !important;
    }
    [data-testid="baseButton-primary"]:hover,
    div.stButton > button[kind="primary"]:hover {
        background: linear-gradient(180deg, #5F56FF, #4338CA) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 1px 0 rgba(255, 255, 255, 0.35) inset, 0 16px 34px -10px rgba(79, 70, 229, 0.85) !important;
    }

    /* כפתור משני (Secondary) — רקע לבן, מסגרת EEE8DA, רדיוס 12px */
    [data-testid="baseButton-secondary"],
    div.stButton > button[kind="secondary"],
    div.stButton > button:not([kind="primary"]) {
        background: #FFFFFF !important;
        border: 1px solid #EEE8DA !important;
        color: #17171C !important;
        border-radius: 12px !important;
        padding: 14px 22px !important;
        font-size: 15.5px !important;
    }
    [data-testid="baseButton-secondary"]:hover,
    div.stButton > button:not([kind="primary"]):hover {
        border-color: #17171C !important;
        transform: translateY(-1px) !important;
    }

    /* focus-visible חובה על כל שדה וכפתור */
    button:focus-visible, input:focus-visible, textarea:focus-visible, a:focus-visible {
        outline: none !important;
        border-color: #4F46E5 !important;
        box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.14) !important;
    }

    /* 5.2 כרטיסים ופנלים */
    .custom-card,
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: linear-gradient(180deg, #FFFFFF 0%, #FDFCF9 100%) !important;
        border: 1px solid #EEE8DA !important;
        border-radius: 18px !important;
        padding: 22px !important;
        box-shadow: 0 1px 2px rgba(23, 23, 28, 0.035), 0 18px 40px -30px rgba(23, 23, 28, 0.4) !important;
        transition: box-shadow 0.18s ease, border-color 0.18s ease, transform 0.18s ease !important;
        direction: rtl !important;
        text-align: right !important;
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


def render_landing_navbar(current_user: dict | None = None) -> str:
    """
    סרגל ניווט עליון מודרני מותאם לפי מפרט מערכת עיצוב GetAJob v1.0 (סעיף 5.6):
    - מקובע בראש הדף עם אפקט זכוכית מטושטשת (surface-glass: blur 14px + rgba(255,255,255,.72)).
    - מרכוז מושלם באמצעות CSS Grid (1fr auto 1fr) ללא space-between (סעיף 5.6).
    - כולל לוגו מותג, קישורי עוגן, אינדיקטור פעילות חי, וכפתורי כניסה והרשמה.
    """
    if current_user:
        user_first = current_user.get("name", "משתמש/ת").split()[0]
        action_buttons_html = f"""
        <a href="?step=auth&mode=account" onclick="window.location.href='?step=auth&mode=account'; return false;" target="_self" style="color: #4F46E5; font-size: 14.5px; font-weight: 700; padding: 6px 12px; text-decoration: none; transition: color 0.18s ease; font-family: 'Heebo', sans-serif;">
            שלום, {user_first}
        </a>
        <a href="?step=auth&mode=account" onclick="window.location.href='?step=auth&mode=account'; return false;" target="_self" style="background: #111114; color: #FFFFFF; font-size: 14px; font-weight: 700; padding: 9px 20px; border-radius: 11px; text-decoration: none; transition: all 0.18s ease; font-family: 'Heebo', sans-serif; border: none;">
            האזור האישי
        </a>
        """
    else:
        action_buttons_html = """
        <a href="?step=auth&mode=signup" onclick="window.location.href='?step=auth&mode=signup'; return false;" target="_self" style="color: #4F46E5; font-size: 14.5px; font-weight: 700; padding: 6px 12px; text-decoration: none; transition: color 0.18s ease; font-family: 'Heebo', sans-serif;">
            הירשם
        </a>
        <a href="?step=auth&mode=login" onclick="window.location.href='?step=auth&mode=login'; return false;" target="_self" style="background: #111114; color: #FFFFFF; font-size: 14px; font-weight: 700; padding: 9px 20px; border-radius: 11px; text-decoration: none; transition: all 0.18s ease; font-family: 'Heebo', sans-serif; border: none;">
            היכנס
        </a>
        """

    html = """
    <div class="m3-landing-navbar" style="direction: rtl;">
        <!-- צד ימין: לוגו מותג עם ריבוע G אינדיגו בצד שמאל של הטקסט GetAJob -->
        <a href="?step=1" onclick="window.location.href='?step=1'; return false;" target="_self" style="display: inline-flex; direction: ltr; align-items: center; gap: 10px; text-decoration: none; justify-self: start;">
            <div style="width: 32px; height: 32px; background: linear-gradient(180deg, #6C63FF, #4F46E5); border: 1px solid #4338CA; border-radius: 10px; display: flex; align-items: center; justify-content: center; color: #FFFFFF; font-weight: 800; font-size: 16.5px; font-family: 'Heebo', sans-serif;">
                G
            </div>
            <span style="font-size: 19px; font-weight: 800; color: #17171C; font-family: 'Heebo', sans-serif; letter-spacing: -0.02em;"><bdi dir="ltr">GetAJob</bdi></span>
        </a>

        <!-- מרכז: קישורי ניווט עדינים בגלילה מונפשת חלקה (justify-self: center) -->
        <div style="display: flex; align-items: center; gap: 28px; justify-self: center;">
            <a href="#how-it-works" onclick="const el = document.getElementById('how-it-works'); if (el) { el.scrollIntoView({ behavior: 'smooth', block: 'start' }); } return false;" style="color: #4A4A55; font-size: 14.5px; font-weight: 600; text-decoration: none; transition: color 0.18s ease; font-family: 'Heebo', sans-serif; cursor: pointer;">איך זה עובד</a>
            <a href="#sample-output" onclick="const el = document.getElementById('sample-output'); if (el) { el.scrollIntoView({ behavior: 'smooth', block: 'start' }); } return false;" style="color: #4A4A55; font-size: 14.5px; font-weight: 600; text-decoration: none; transition: color 0.18s ease; font-family: 'Heebo', sans-serif; cursor: pointer;">דוגמת ניתוח</a>
            <a href="#faq" onclick="const el = document.getElementById('faq'); if (el) { el.scrollIntoView({ behavior: 'smooth', block: 'start' }); } return false;" style="color: #4A4A55; font-size: 14.5px; font-weight: 600; text-decoration: none; transition: color 0.18s ease; font-family: 'Heebo', sans-serif; cursor: pointer;">שאלות</a>
        </div>

        <!-- צד שמאל: כפתורי פעולה (justify-self: end) -->
        <div style="display: flex; align-items: center; gap: 14px; justify-self: end;">
            {{ACTION_BUTTONS}}
        </div>
    </div>

    <!-- כפתור חזרה לראש העמוד (סעיף 5.6) — מופיע מעל 320px גלילה -->
    <button id="back-to-top-btn" onclick="const m = document.querySelector('section[data-testid=\\'stMain\\']') || window; m.scrollTo({top: 0, behavior: 'smooth'});" aria-label="חזרה לראש העמוד">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="18 15 12 9 6 15"></polyline>
        </svg>
    </button>
    <script>
    (function() {
        function checkScroll() {
            var btn = document.getElementById('back-to-top-btn');
            var scrollEl = document.querySelector('section[data-testid="stMain"]') || window;
            var currentY = scrollEl.scrollTop !== undefined ? scrollEl.scrollTop : window.scrollY;
            if (btn) {
                if (currentY > 320) {
                    btn.style.opacity = '1';
                    btn.style.pointerEvents = 'auto';
                } else {
                    btn.style.opacity = '0';
                    btn.style.pointerEvents = 'none';
                }
            }
        }
        var scrollEl = document.querySelector('section[data-testid="stMain"]') || window;
        scrollEl.addEventListener('scroll', checkScroll, { passive: true });
        window.addEventListener('scroll', checkScroll, { passive: true });
        window.addEventListener('DOMContentLoaded', checkScroll);
        setTimeout(checkScroll, 500);
    })();
    </script>
    """.replace("{{ACTION_BUTTONS}}", action_buttons_html)
    return textwrap.dedent(html).strip()


def render_how_it_works() -> str:
    """
    סקשן 'איך זה עובד' לפי מפרט מערכת עיצוב GetAJob v1.0:
    - מרווח סקשן: 96px (סעיף 3)
    - ריווחים מותאמים וצפופים ללא שטחים מתים מיותרים
    - היררכיה ברורה בין כותרת, תיאור ושלבים ממוספרים
    """
    # טעינת איור המערכת והטמעתו בסקשן 'איך זה עובד' במקום ה-placeholder
    img_b64_html = ""
    hero_img_path = os.path.join(os.path.dirname(__file__), "assets", "hero_illustration.jpg")
    if not os.path.exists(hero_img_path):
        hero_img_path = "assets/hero_illustration.jpg"

    if os.path.exists(hero_img_path):
        try:
            with open(hero_img_path, "rb") as f:
                b64_data = base64.b64encode(f.read()).decode("utf-8")
            img_b64_html = f'''
            <div style="flex: 1 1 380px; min-width: 0; max-width: 440px; display: flex; align-items: center; justify-content: center;">
                <img src="data:image/jpeg;base64,{b64_data}" alt="איור מערכת GetAJob" style="width: 100%; height: auto; max-height: 270px; object-fit: contain; border-radius: 18px; border: 1px solid #EEE8DA; box-shadow: 0 1px 2px rgba(23, 23, 28, 0.035), 0 18px 40px -30px rgba(23, 23, 28, 0.4); display: block;" />
            </div>
            '''
        except Exception:
            img_b64_html = ""

    if not img_b64_html:
        img_b64_html = '''
        <div style="flex: 1 1 380px; min-width: 0; max-width: 440px; background: linear-gradient(180deg, #FCFAF6, #F5F1E7); border: 1px solid #EEE8DA; border-radius: 22px; min-height: 260px; display: flex; align-items: center; justify-content: center; padding: 28px;">
            <div style="background: #FFFFFF; border: 1px solid #EEE8DA; border-radius: 12px; padding: 10px 22px; font-family: 'JetBrains Mono', monospace; font-size: 13px; color: #4A4A55; font-weight: 600; direction: ltr; display: inline-flex; align-items: center; gap: 8px;">
                <span>product shot — analysis flow</span>
            </div>
        </div>
        '''

    html = f"""
    <div id="how-it-works" style="direction: rtl; text-align: center; margin-top: 80px; margin-bottom: 0;">
        <!-- כותרת ראשית וקטגוריה ממורכזת מעל שני הטורים -->
        <div class="m3-section-header" style="margin-bottom: 28px; text-align: center;">
            <span style="color: #4F46E5; font-size: 13px; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; display: inline-block; margin-bottom: 4px; font-family: 'Heebo', sans-serif;">
                איך זה עובד
            </span>
            <h2 style="margin: 0; font-size: clamp(26px, 3.2vw, 38px); font-weight: 800; color: #17171C; line-height: 1.15; letter-spacing: -0.025em; font-family: 'Heebo', sans-serif; text-wrap: pretty; text-align: center !important;">
                שלוש פעולות בין קורות החיים שלך לראיון
            </h2>
        </div>

        <div style="display: flex; flex-wrap: wrap; gap: 32px; align-items: center; justify-content: center; direction: rtl; text-align: right;">
            <!-- טור ימין: 3 השלבים הממוספרים -->
            <div style="flex: 1 1 440px; min-width: 0; display: flex; flex-direction: column; gap: 16px;">
                <!-- שלב 1 -->
                <div style="display: flex; align-items: flex-start; gap: 14px; direction: rtl; text-align: right;">
                    <div style="width: 32px; height: 32px; border-radius: 10px; background: linear-gradient(180deg, #F4F2FF, #EAE6FF); border: 1px solid #EEE8DA; color: #4F46E5; font-size: 15px; font-weight: 800; display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 2px; font-family: 'Heebo', sans-serif;">
                        1
                    </div>
                    <div>
                        <h3 style="margin: 0 0 2px 0; font-size: 16.5px; font-weight: 700; color: #17171C; font-family: 'Heebo', sans-serif; letter-spacing: -0.01em; line-height: 1.25;">
                            איתור פערי מיומנויות
                        </h3>
                        <p style="margin: 0; color: #4A4A55; font-size: 14.5px; line-height: 1.45; font-family: 'Heebo', sans-serif;">
                            סריקה קפדנית של דרישות המשרה מול קורות החיים, ודירוג כל פער לפי חומרה.
                        </p>
                    </div>
                </div>

                <!-- שלב 2 -->
                <div style="display: flex; align-items: flex-start; gap: 14px; direction: rtl; text-align: right;">
                    <div style="width: 32px; height: 32px; border-radius: 10px; background: linear-gradient(180deg, #F4F2FF, #EAE6FF); border: 1px solid #EEE8DA; color: #4F46E5; font-size: 15px; font-weight: 800; display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 2px; font-family: 'Heebo', sans-serif;">
                        2
                    </div>
                    <div>
                        <h3 style="margin: 0 0 2px 0; font-size: 16.5px; font-weight: 700; color: #17171C; font-family: 'Heebo', sans-serif; letter-spacing: -0.01em; line-height: 1.25;">
                            שכתוב סעיפים למדידים
                        </h3>
                        <p style="margin: 0; color: #4A4A55; font-size: 14.5px; line-height: 1.45; font-family: 'Heebo', sans-serif;">
                            כל סעיף גנרי הופך לפעולה, היקף ותוצאה — בניסוח שעובר גם סינון אוטומטי.
                        </p>
                    </div>
                </div>

                <!-- שלב 3 (הסרת README והדגשת בניית פרויקט לפורטפוליו) -->
                <div style="display: flex; align-items: flex-start; gap: 14px; direction: rtl; text-align: right;">
                    <div style="width: 32px; height: 32px; border-radius: 10px; background: linear-gradient(180deg, #F4F2FF, #EAE6FF); border: 1px solid #EEE8DA; color: #4F46E5; font-size: 15px; font-weight: 800; display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 2px; font-family: 'Heebo', sans-serif;">
                        3
                    </div>
                    <div>
                        <h3 style="margin: 0 0 2px 0; font-size: 16.5px; font-weight: 700; color: #17171C; font-family: 'Heebo', sans-serif; letter-spacing: -0.01em; line-height: 1.25;">
                            בניית פרויקט לפורטפוליו
                        </h3>
                        <p style="margin: 0; color: #4A4A55; font-size: 14.5px; line-height: 1.45; font-family: 'Heebo', sans-serif;">
                            מפרט פרויקט מעשי שסוגר בדיוק את הפער שנמצא, עם דגש על הצגת תוצרים מוכחים בתיק העבודות למגייסים.
                        </p>
                    </div>
                </div>
            </div>

            <!-- טור שמאל: איור המערכת המחליף את ה-placeholder -->
            {img_b64_html}
        </div>
    </div>
    """
    return textwrap.dedent(html).strip()


def render_sample_showcase() -> str:
    """
    סקשן 'דוגמת פלט לניתוח אמיתי' לפי מפרט מערכת עיצוב GetAJob v1.0:
    - טור ימין (ב-RTL): מד התאמה למשרה (סעיף 5.4)
    - טור שמאל (ב-RTL): כרטיסי פערים עם Badges מדויקים (חוסם: #B42318/#FEE2E2, חשוב: #92400E/#FEF3C7, קיים: #166534/#DCFCE7) (סעיף 1.5, 5.3)
    - כרטיס תחתון מלא: השוואת שכתוב סעיף (לפני בצד ימין / אחרי בצד שמאל) (סעיף 5.2)
    """
    html = """
    <div id="sample-output" style="direction: rtl; text-align: right; margin-top: 80px; margin-bottom: 0;">
        <!-- כותרת ראשית וקטגוריה ממורכזת עם ריווח מהודק -->
        <div class="m3-section-header" style="margin-bottom: 18px; text-align: center;">
            <span style="color: #4F46E5; font-size: 13px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; display: inline-block; margin-bottom: 3px; font-family: 'Heebo', sans-serif;">
                דוגמת פלט
            </span>
            <h2 style="margin: 0 0 4px 0; font-size: clamp(26px, 3.2vw, 38px); font-weight: 800; color: #17171C; letter-spacing: -0.025em; font-family: 'Heebo', sans-serif; text-wrap: pretty; line-height: 1.12; text-align: center !important;">
                ככה נראה ניתוח אמיתי
            </h2>
            <p class="m3-section-subtitle" style="margin: 0; color: #4A4A55; font-size: 15.5px; font-weight: 400; line-height: 1.45; font-family: 'Heebo', sans-serif; text-align: center !important;">
                משרת Junior UX/UI Designer מול קורות חיים של בוגר בוטקאמפ.
            </p>
        </div>

        <!-- גריד עליון: ימין (מדדים ללא שטח מת), שמאל (פערים) -->
        <div style="display: flex; flex-wrap: wrap; gap: 20px; align-items: stretch; margin-bottom: 20px;">
            <!-- טור ימין (RTL): מדדים — סעיף 5.4 ללא שטח מת (flex: 1 1 300px) -->
            <div style="flex: 1 1 300px; min-width: 0; background: linear-gradient(180deg, #FFFFFF, #FDFCF9); border: 1px solid #EEE8DA; border-radius: 20px; padding: 22px 24px; box-shadow: 0 1px 2px rgba(23, 23, 28, 0.035), 0 18px 40px -30px rgba(23, 23, 28, 0.4); display: flex; flex-direction: column; gap: 14px;">
                <div>
                    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 8px;">
                        <span style="font-size: 15.5px; font-weight: 700; color: #17171C; font-family: 'Heebo', sans-serif;">
                            מד התאמה למשרה
                        </span>
                        <div dir="ltr" style="display: inline-flex; align-items: baseline; gap: 2px;">
                            <span style="font-size: 36px; font-weight: 800; color: #17171C; font-family: 'Heebo', sans-serif; line-height: 1; letter-spacing: -0.035em;">64</span>
                            <span style="font-size: 18px; color: #6B6B74; font-weight: 600; font-family: 'Heebo', sans-serif;">%</span>
                        </div>
                    </div>

                    <!-- פס התקדמות אופקי — Track & Fill לפי סעיף 5.4 -->
                    <div role="progressbar" aria-valuenow="64" aria-valuemin="0" aria-valuemax="100" aria-label="מד התאמה למשרה" style="background: linear-gradient(180deg, #E7E2D2, #F1EDE1); border-radius: 999px; height: 10px; overflow: hidden; margin-bottom: 4px; box-shadow: 0 1px 2px rgba(23, 23, 28, 0.06) inset; direction: rtl;">
                        <div style="background: linear-gradient(270deg, #8B84FF, #4F46E5); width: 64%; height: 100%; border-radius: 999px; box-shadow: 0 0 0 1px rgba(79, 70, 229, 0.2), 0 6px 14px -6px rgba(79, 70, 229, 0.7);"></div>
                    </div>
                    <div style="display: flex; justify-content: space-between; font-size: 12px; color: #6B6B74; font-weight: 500; margin-bottom: 12px; direction: rtl; font-family: 'Heebo', sans-serif;">
                        <span>0</span>
                        <span>100</span>
                    </div>

                    <!-- תגית סטטוס מוכנות ממצה -->
                    <div style="display: inline-flex; align-items: center; gap: 7px; background: #FEF3C7; border: 1px solid #FDE68A; border-radius: 8px; padding: 4px 10px;">
                        <span style="width: 6px; height: 6px; border-radius: 50%; background: #D97706;"></span>
                        <span style="font-size: 12.5px; font-weight: 700; color: #92400E; font-family: 'Heebo', sans-serif;">מוכנות בינונית — נדרש פרויקט תיק עבודות</span>
                    </div>
                </div>

                <!-- מדדי סיכום בבלוקים שקועים אלגנטיים למניעת שטחים מתים -->
                <div style="display: flex; flex-direction: column; gap: 8px; border-top: 1px solid #F2EDE1; padding-top: 14px;">
                    <div style="background: linear-gradient(180deg, #FCFAF6, #F5F1E7); border: 1px solid #EEE8DA; border-radius: 12px; padding: 9px 14px; display: flex; justify-content: space-between; align-items: center;">
                        <span style="color: #4A4A55; font-size: 13.5px; font-weight: 600; font-family: 'Heebo', sans-serif;">כישורים שקיימים בקורות החיים</span>
                        <span style="background: #DCFCE7; color: #166534; font-size: 13.5px; font-weight: 800; padding: 2px 10px; border-radius: 8px; font-family: 'Heebo', sans-serif;">7</span>
                    </div>
                    <div style="background: linear-gradient(180deg, #FCFAF6, #F5F1E7); border: 1px solid #EEE8DA; border-radius: 12px; padding: 9px 14px; display: flex; justify-content: space-between; align-items: center;">
                        <span style="color: #4A4A55; font-size: 13.5px; font-weight: 600; font-family: 'Heebo', sans-serif;">פערים טכנולוגיים שזוהו</span>
                        <span style="background: #FEE2E2; color: #B42318; font-size: 13.5px; font-weight: 800; padding: 2px 10px; border-radius: 8px; font-family: 'Heebo', sans-serif;">4</span>
                    </div>
                    <div style="background: linear-gradient(180deg, #FCFAF6, #F5F1E7); border: 1px solid #EEE8DA; border-radius: 12px; padding: 9px 14px; display: flex; justify-content: space-between; align-items: center;">
                        <span style="color: #4A4A55; font-size: 13.5px; font-weight: 600; font-family: 'Heebo', sans-serif;">סעיפים שדורשים שכתוב</span>
                        <span style="background: #FEF3C7; color: #92400E; font-size: 13.5px; font-weight: 800; padding: 2px 10px; border-radius: 8px; font-family: 'Heebo', sans-serif;">5</span>
                    </div>
                </div>
            </div>

            <!-- טור שמאל (RTL): כרטיסי פערים — סעיף 5.3 (flex: 1 1 340px) -->
            <div style="flex: 1 1 340px; min-width: 0; display: flex; flex-direction: column; gap: 10px;">
                <!-- כרטיס חוסם (#B42318 על #FEE2E2) -->
                <div style="background: linear-gradient(180deg, #FFFFFF, #FDFCF9); border: 1px solid #EEE8DA; border-radius: 18px; padding: 15px 20px; box-shadow: 0 1px 2px rgba(23, 23, 28, 0.035), 0 18px 40px -30px rgba(23, 23, 28, 0.4);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                        <h3 style="margin: 0; font-size: 15.5px; font-weight: 700; color: #17171C; font-family: 'Heebo', sans-serif;">
                            אין תיק עבודות עם תהליך מלא
                        </h3>
                        <span style="background: #FEE2E2; color: #B42318; border-radius: 8px; padding: 4px 10px; font-size: 12px; font-weight: 800; flex: 0 0 auto; font-family: 'Heebo', sans-serif;">
                            חוסם
                        </span>
                    </div>
                    <p style="margin: 0; color: #4A4A55; font-size: 13.5px; line-height: 1.45; font-family: 'Heebo', sans-serif;">
                        המשרה דורשת הצגת end-to-end case study. בקורות החיים מופיעים רק מסכים סופיים.
                    </p>
                </div>

                <!-- כרטיס חשוב (#92400E על #FEF3C7) -->
                <div style="background: linear-gradient(180deg, #FFFFFF, #FDFCF9); border: 1px solid #EEE8DA; border-radius: 18px; padding: 15px 20px; box-shadow: 0 1px 2px rgba(23, 23, 28, 0.035), 0 18px 40px -30px rgba(23, 23, 28, 0.4);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                        <h3 style="margin: 0; font-size: 15.5px; font-weight: 700; color: #17171C; font-family: 'Heebo', sans-serif;">
                            ניסוח ללא מדידה
                        </h3>
                        <span style="background: #FEF3C7; color: #92400E; border-radius: 8px; padding: 4px 10px; font-size: 12px; font-weight: 800; flex: 0 0 auto; font-family: 'Heebo', sans-serif;">
                            חשוב
                        </span>
                    </div>
                    <p style="margin: 0; color: #4A4A55; font-size: 13.5px; line-height: 1.45; font-family: 'Heebo', sans-serif;">
                        כל הסעיפים מתארים מה עשית, אף אחד לא מתאר מה זה שינה.
                    </p>
                </div>

                <!-- כרטיס קיים (#166534 על #DCFCE7) -->
                <div style="background: linear-gradient(180deg, #FFFFFF, #FDFCF9); border: 1px solid #EEE8DA; border-radius: 18px; padding: 15px 20px; box-shadow: 0 1px 2px rgba(23, 23, 28, 0.035), 0 18px 40px -30px rgba(23, 23, 28, 0.4);">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                        <h3 style="margin: 0; font-size: 15.5px; font-weight: 700; color: #17171C; font-family: 'Heebo', sans-serif;">
                            שליטה בכלי העבודה
                        </h3>
                        <span style="background: #DCFCE7; color: #166534; border-radius: 8px; padding: 4px 10px; font-size: 12px; font-weight: 800; flex: 0 0 auto; font-family: 'Heebo', sans-serif;">
                            קיים
                        </span>
                    </div>
                    <p style="margin: 0; color: #4A4A55; font-size: 13.5px; line-height: 1.45; font-family: 'Heebo', sans-serif;">
                        Figma, מערכות עיצוב ופרוטוטייפינג — כולם מכוסים ומופיעים בבירור.
                    </p>
                </div>
            </div>
        </div>

        <!-- כרטיס שכתוב סעיף רוחבי מלא (Before / After) לפי סעיף 5.2 -->
        <div style="background: linear-gradient(180deg, #FFFFFF, #FDFCF9); border: 1px solid #EEE8DA; border-radius: 18px; padding: 20px 24px; box-shadow: 0 1px 2px rgba(23, 23, 28, 0.035), 0 18px 40px -30px rgba(23, 23, 28, 0.4);">
            <div style="margin-bottom: 12px;">
                <span style="font-size: 13.5px; font-weight: 800; color: #6B6B74; font-family: 'Heebo', sans-serif;">
                    שכתוב סעיף
                </span>
            </div>
            <div style="display: flex; flex-wrap: wrap; gap: 16px;">
                <!-- לפני — צד ימין ב-RTL (כרטיס פנימי surface-sunken) -->
                <div style="flex: 1 1 260px; min-width: 0; background: linear-gradient(180deg, #FCFAF6, #F5F1E7); border: 1px solid #EFEADD; border-radius: 14px; padding: 16px 18px;">
                    <span style="color: #B42318; font-size: 12px; font-weight: 800; display: inline-block; margin-bottom: 6px; font-family: 'Heebo', sans-serif; background: #FEE2E2; padding: 3px 8px; border-radius: 6px;">
                        לפני
                    </span>
                    <p style="margin: 0; color: #4A4A55; font-size: 14.5px; line-height: 1.45; font-family: 'Heebo', sans-serif;">
                        עיצבתי מסכים לאפליקציית מסחר בקורס.
                    </p>
                </div>

                <!-- אחרי — צד שמאל ב-RTL (כרטיס פנימי accent-tint) -->
                <div style="flex: 1 1 260px; min-width: 0; background: linear-gradient(180deg, #F4F2FF, #EAE6FF); border: 1px solid #E0D9FF; border-radius: 14px; padding: 16px 18px;">
                    <span style="color: #4338CA; font-size: 12px; font-weight: 800; display: inline-block; margin-bottom: 6px; font-family: 'Heebo', sans-serif; background: #E0D9FF; padding: 3px 8px; border-radius: 6px;">
                        אחרי
                    </span>
                    <p style="margin: 0; color: #17171C; font-size: 14.5px; line-height: 1.45; font-weight: 500; font-family: 'Heebo', sans-serif;">
                        עיצבתי מחדש תהליך צ'קאאוט ב-4 מסכים, וקיצרתי אותו מ-6 שלבים ל-3 בבדיקת שימושיות עם 8 משתתפים.
                    </p>
                </div>
        </div>
    </div>
    """
    return textwrap.dedent(html).strip()


def render_faq_section() -> str:
    """
    סקשן שאלות נפוצות (FAQ) לפי מפרט מערכת עיצוב GetAJob v1.0:
    - 2 שורות של כרטיסיות, 2 בכל שורה (גריד 2x2).
    - סגנון כרטיסייה תואם לחלק העליון של הדף עם אייקון מותאם.
    - ללא אימוג'י (כלל איסור סעיף 7).
    """
    html = """
    <div id="faq" style="direction: rtl; text-align: center; margin-top: 80px; margin-bottom: 0;">
        <div class="m3-section-header" style="margin-bottom: 28px; text-align: center;">
            <span style="color: #4F46E5; font-size: 13px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; display: inline-block; margin-bottom: 4px; font-family: 'Heebo', sans-serif;">
                שאלות נפוצות
            </span>
            <h2 style="margin: 0 0 4px 0; font-size: clamp(26px, 3.2vw, 38px); font-weight: 800; color: #17171C; letter-spacing: -0.025em; font-family: 'Heebo', sans-serif; text-wrap: pretty; line-height: 1.12; text-align: center !important;">
                שאלות שאולי יש לכם
            </h2>
            <p class="m3-section-subtitle" style="margin: 0; color: #4A4A55; font-size: 15.5px; font-weight: 400; line-height: 1.45; font-family: 'Heebo', sans-serif; text-align: center !important;">
                כל מה שחשוב לדעת על הפלטפורמה ואיך היא מכינה אותך לגיוס.
            </p>
        </div>

        <div class="m3-faq-cards-grid">
            <!-- שאלה 1 -->
            <div class="m3-faq-card">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px; width: 100%;">
                    <div style="width: 34px; height: 34px; border-radius: 9px; background: linear-gradient(180deg, #F4F2FF, #EAE6FF); border: 1px solid #E0D9FF; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                        <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#4F46E5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                            <circle cx="9" cy="7" r="4"></circle>
                            <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                            <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                        </svg>
                    </div>
                    <h3 style="margin: 0; font-size: 16px; font-weight: 700; color: #17171C; font-family: 'Heebo', sans-serif; line-height: 1.25;">
                        למי GetAJob מיועדת?
                    </h3>
                </div>
                <p style="margin: 0; color: #4A4A55; font-size: 13px; line-height: 1.5; font-family: 'Heebo', sans-serif;">
                    הפלטפורמה נבנתה במיוחד עבור ג'וניורים, בוגרי בוטקאמפים וקורסים מקצועיים, ומועמדים שנתקעים בשלב הסינון הראשוני ללא משוב ברור.
                </p>
            </div>

            <!-- שאלה 2 -->
            <div class="m3-faq-card">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px; width: 100%;">
                    <div style="width: 34px; height: 34px; border-radius: 9px; background: linear-gradient(180deg, #F4F2FF, #EAE6FF); border: 1px solid #E0D9FF; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                        <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#4F46E5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="11" cy="11" r="8"></circle>
                            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                            <circle cx="11" cy="11" r="3"></circle>
                        </svg>
                    </div>
                    <h3 style="margin: 0; font-size: 16px; font-weight: 700; color: #17171C; font-family: 'Heebo', sans-serif; line-height: 1.25;">
                        איך המערכת מזהה פערי מיומנויות?
                    </h3>
                </div>
                <p style="margin: 0; color: #4A4A55; font-size: 13px; line-height: 1.5; font-family: 'Heebo', sans-serif;">
                    מנוע המערכת מנתח את הדרישות הספציפיות של משרת היעד שלך מול קורות החיים שהעלית, ומסווג את החוסרים לרמות חומרה (חוסם, חשוב או קיים) כדי שתדע על מה לעבוד.
                </p>
            </div>

            <!-- שאלה 3 (שאלה חדשה) -->
            <div class="m3-faq-card">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px; width: 100%;">
                    <div style="width: 34px; height: 34px; border-radius: 9px; background: linear-gradient(180deg, #F4F2FF, #EAE6FF); border: 1px solid #E0D9FF; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                        <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#4F46E5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                            <polyline points="14 2 14 8 20 8"></polyline>
                            <path d="M9 15l2 2 4-4"></path>
                        </svg>
                    </div>
                    <h3 style="margin: 0; font-size: 16px; font-weight: 700; color: #17171C; font-family: 'Heebo', sans-serif; line-height: 1.25;">
                        איך המערכת מסייעת לעבור סינון ATS?
                    </h3>
                </div>
                <p style="margin: 0; color: #4A4A55; font-size: 13px; line-height: 1.5; font-family: 'Heebo', sans-serif;">
                    המערכת ממירה ניסוחים כלליים לסעיפי הישגים מדידים בפורמט Action-Impact, ומטמיעה מילות מפתח הכרחיות מהמשרה שאלגוריתמי הסינון ומנהלי הגיוס מחפשים.
                </p>
            </div>

            <!-- שאלה 4 -->
            <div class="m3-faq-card">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px; width: 100%;">
                    <div style="width: 34px; height: 34px; border-radius: 9px; background: linear-gradient(180deg, #F4F2FF, #EAE6FF); border: 1px solid #E0D9FF; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                        <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#4F46E5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="12" cy="12" r="10"></circle>
                            <path d="M12 6v6l4 2"></path>
                        </svg>
                    </div>
                    <h3 style="margin: 0; font-size: 16px; font-weight: 700; color: #17171C; font-family: 'Heebo', sans-serif; line-height: 1.25;">
                        האם השימוש במערכת כרוך בתשלום?
                    </h3>
                </div>
                <p style="margin: 0; color: #4A4A55; font-size: 13px; line-height: 1.5; font-family: 'Heebo', sans-serif;">
                    לא. GetAJob פתוחה לשימוש חופשי כחלק מפרויקט הגמר, במטרה לסייע למועמדים לסגור פערי ידע ולהשתלב בהצלחה בתעשיית ההייטק.
                </p>
            </div>
        </div>
    </div>
    """
    return textwrap.dedent(html).strip()


def render_bottom_cta_banner() -> str:
    """
    באנר כהה יוקרתי בתחתית העמוד לפי סעיף 5.7 במפרט:
    background-color: #111114;
    radial-gradient(700px 340px at 50% -10%, rgba(108,99,255,.42) 0%, rgba(108,99,255,0) 70%),
    linear-gradient(180deg, #1B1B22 0%, #101014 100%);
    border-radius: 26px; padding: clamp(40px, 6vw, 72px);
    box-shadow: 0 40px 90px -50px rgba(23,23,28,.85);
    title: #FBF9F4 · body: #A9A9B4
    """
    html = """
    <div id="bottom-cta" style="background-color: #111114; background-image: radial-gradient(700px 340px at 50% -10%, rgba(108, 99, 255, 0.42) 0%, rgba(108, 99, 255, 0) 70%), linear-gradient(180deg, #1B1B22 0%, #101014 100%); border-radius: 26px; max-width: 900px; margin-inline: auto; padding: 36px 28px 84px 28px; text-align: center; color: #FBF9F4; margin-top: 80px; margin-bottom: 0; box-shadow: 0 40px 90px -50px rgba(23, 23, 28, 0.85); direction: rtl; display: flex; flex-direction: column; align-items: center; justify-content: center;">
        <div role="heading" aria-level="2" class="m3-bottom-cta-title" style="margin: 0 0 2px 0 !important; font-size: clamp(26px, 3.2vw, 38px); font-weight: 800; color: #FBF9F4 !important; font-family: 'Heebo', sans-serif; letter-spacing: -0.025em; text-wrap: pretty; text-align: center !important; line-height: 1.15 !important; width: 100%;">
            תגלו מה חסר לפני שהמגייס יגלה
        </div>
        <p class="m3-bottom-cta-desc" style="margin: -2px auto 0 auto !important; color: #A9A9B4 !important; font-size: 15px; font-weight: 400 !important; max-width: 580px; line-height: 1.35 !important; font-family: 'Heebo', sans-serif; text-align: center !important; width: 100%;">
            העלו קורות חיים ומשרה אחת. הניתוח הראשון לוקח פחות מדקה.
        </p>
    </div>
    """
    return textwrap.dedent(html).strip()

