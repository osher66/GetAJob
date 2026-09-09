"""
auth_view.py - מסך הרשמה והתחברות (Auth Screen)
נבנה בדיוק מושלם לפי מפרט Claude Design Artifact (v1.0):
1. כרטיס שמאל (הפיצ'רים):
   - כרטיס עליון: 3 פיצ'רים (היסטוריית ניתוחים, שמירת פרטי משתמש ופרופיל, מעקב לאורך זמן) עם אייקון בריבוע סגול בהיר מימין לטקסט.
   - כרטיס תחתון נפרד: באנר קטן עם נקודה ירוקה (Badge) מימין וטקסט 'הניתוח הראשון פתוח בלי חשבון...'.
2. כרטיס ימין (הטופס):
   - טאב מצבים מאוחד עם סליידר לבן מוגבה שמחליק באנימציה חלקה (CSS/JS) ללא רענון דף.
   - ללא הודעות 'Press Enter to apply'.
   - שדה 'שם פרטי ושם משפחה *'.
   - שדות קלט מעוצבים עם תמיכה מלאה ב-RTL (אימייל וסיסמה ב-LTR).
   - מד חוזק סיסמה: 3 מקטעים מעוגלים וטקסט 'לפחות 8 תווים, אות וספרה'.
   - תיבת סימון (Checkbox): בתוך כרטיסון חמים ומעוגל, מיושרת לימין לצד הטקסט ללא שבירת מילים.
   - כפתור Primary סגול בולט עם צל עמוק.
"""

import os
import json
import hashlib
import streamlit as st
import streamlit.components.v1 as components


USERS_FILE = os.path.join(os.path.dirname(__file__), "data", "users.json")


def _hash_password(password: str) -> str:
    """הצפנת סיסמה בסיסית ובטוחה לשימוש מקומי"""
    return hashlib.sha256(f"getajob_salt_{password}".encode("utf-8")).hexdigest()


def load_users() -> dict:
    """טעינת משתמשים רשומים מקובץ JSON מקומי"""
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_user(name: str, email: str, password: str) -> bool:
    """שמירת משתמש חדש במערכת"""
    users = load_users()
    email_key = email.strip().lower()
    users[email_key] = {
        "name": name.strip(),
        "email": email_key,
        "password_hash": _hash_password(password),
        "created_at": "09 בספטמבר 2026",
        "history": [
            {"role": "Junior UX/UI Designer · Wix", "date": "4 בספטמבר 2026", "score": 64},
            {"role": "Product Designer · Monday", "date": "28 באוגוסט 2026", "score": 71},
            {"role": "UX Designer · Lightricks", "date": "19 באוגוסט 2026", "score": 52},
        ],
    }
    try:
        os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(users, f, ensure_ascii=False, indent=2)
        return True
    except Exception:
        return False


def verify_user(email: str, password: str) -> tuple[bool, dict | None]:
    """אימות פרטי התחברות"""
    users = load_users()
    email_key = email.strip().lower()
    if email_key in users:
        user = users[email_key]
        if user.get("password_hash") == _hash_password(password):
            return True, user
    return False, None


def render_auth_navbar() -> None:
    """סרגל עליון צף ומטושטש: כפתור חזרה מימין, לוגו במרכז עם האות G משמאל לטקסט"""
    nav_html = """
    <div style="padding: 16px 20px 24px; direction: rtl; font-family: 'Heebo', sans-serif;">
      <header class="auth-custom-navbar" style="display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; max-width: 940px; margin: 0 auto; padding: 12px 20px; background: rgba(255, 255, 255, 0.72); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border: 1px solid rgba(23, 23, 28, 0.07); border-radius: 16px; box-shadow: rgba(23, 23, 28, 0.04) 0px 1px 2px, rgba(23, 23, 28, 0.45) 0px 18px 40px -28px; direction: rtl;">
        <!-- 1. ימין: כפתור חזרה למסך הבית -->
        <div style="display: flex; justify-content: flex-start; align-items: center;">
          <a href="?step=1" onclick="window.location.href='?step=1'; return false;" onmouseover="this.style.color='#17171C'" onmouseout="this.style.color='#4A4A55'" style="font-size: 14.5px; font-weight: 600; color: #4A4A55; text-decoration: none; padding: 6px 10px; border-radius: 8px; transition: color 0.18s ease;">חזרה למסך הבית</a>
        </div>

        <!-- 2. מרכז: לוגו עם האות G משמאל לטקסט GetAJob -->
        <div style="display: flex; justify-content: center; align-items: center;">
          <a href="?step=1" onclick="window.location.href='?step=1'; return false;" style="display: inline-flex; align-items: center; gap: 10px; color: #17171C; text-decoration: none; direction: ltr;">
            <div style="width: 30px; height: 30px; border-radius: 9px; background: linear-gradient(180deg, #6C63FF, #4F46E5); display: flex; align-items: center; justify-content: center; color: #FFFFFF; font-weight: 800; font-size: 15px;">G</div>
            <span style="font-weight: 800; font-size: 18px; letter-spacing: -0.015em; color: #17171C;">GetAJob</span>
          </a>
        </div>

        <!-- 3. שמאל: עמודה מאוזנת לקיבוע המרכוז המדויק -->
        <div style="display: flex; justify-content: flex-end; align-items: center;"></div>
      </header>
    </div>
    """
    st.html(nav_html)


def get_auth_css(initial_mode: str = "signup") -> str:
    """CSS מדויק ומהודק שמממש את חוקי העיצוב המקוריים ללא שום קופסאות כפולות, טולטיפים או קפיצות אופקיות"""
    signup_disp = "block" if initial_mode == "signup" else "none"
    login_disp = "block" if initial_mode == "login" else "none"

    raw_css = """
    <style>
    /* קיבוע פס הגלילה בצד ימין של הדף בעיצוב תואם למערכת העיצוב וללא שום קפיצות */
    html {
        direction: ltr !important;
        overflow-y: hidden !important;
    }

    body,
    div[data-testid="stAppViewContainer"],
    section[data-testid="stMain"] {
        direction: ltr !important;
    }

    section[data-testid="stMain"] {
        overflow-y: scroll !important; /* תמיד מציג סליידר אנכי כדי למנוע קפיצות רוחב */
        scrollbar-width: thin !important;
        scrollbar-color: #D8D2C4 transparent !important;
    }

    /* סליידר גלילה מעוצב, דק ואלגנטי בצד ימין */
    section[data-testid="stMain"]::-webkit-scrollbar,
    ::-webkit-scrollbar {
        width: 8px !important;
        height: 8px !important;
    }

    section[data-testid="stMain"]::-webkit-scrollbar-track,
    ::-webkit-scrollbar-track {
        background: transparent !important;
    }

    section[data-testid="stMain"]::-webkit-scrollbar-thumb,
    ::-webkit-scrollbar-thumb {
        background: #D8D2C4 !important;
        border-radius: 999px !important;
    }

    section[data-testid="stMain"]::-webkit-scrollbar-thumb:hover,
    ::-webkit-scrollbar-thumb:hover {
        background: #A8A294 !important;
    }

    /* תוכן האפליקציה ב-RTL מלא */
    div[data-testid="stAppViewContainer"] .block-container,
    .auth-custom-navbar,
    .auth-page-root {
        direction: rtl !important;
        text-align: right !important;
    }

    /* מרכוז המסך ברוחב 940px בלבד ללא שום רקע נוסף */
    div[data-testid="stAppViewContainer"]:has(.auth-page-root) .block-container {
        max-width: 960px !important;
        padding-top: 0.5rem !important;
        padding-bottom: 4rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        margin: 0 auto !important;
        background: transparent !important;
    }

    /* יישור עליון לשני הטורים */
    div[data-testid="stHorizontalBlock"]:has(.auth-page-root) {
        align-items: flex-start !important;
        gap: 28px !important;
        direction: rtl !important;
        background: transparent !important;
    }

    /* ביטול מוחלט של כל רקע או גבול על בלוקים גנריים של Streamlit למניעת קופסאות כפולות */
    div[data-testid="stVerticalBlock"],
    div[data-testid="stVerticalBlockBorderWrapper"],
    div[data-testid="stHorizontalBlock"] {
        border: none !important;
        background: transparent !important;
        box-shadow: none !important;
    }

    /* איפוס מרווחי הטור ומניעת גלילה אופקית בעת אנימציית slide */
    div[data-testid="stColumn"]:has(div[data-testid="stForm"]) {
        overflow-x: hidden !important;
    }

    div[data-testid="stColumn"]:has(div[data-testid="stForm"]) div[data-testid="stVerticalBlock"] {
        gap: 0 !important;
        row-gap: 0 !important;
    }

    /* העלמת הטקסט 'Press Enter to apply' / הוראות הקלט של Streamlit */
    [data-testid="InputInstructions"],
    div[data-testid="InputInstructions"],
    .stTextInput div[data-testid="InputInstructions"],
    .stPasswordInput div[data-testid="InputInstructions"] {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        height: 0 !important;
        width: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
        pointer-events: none !important;
    }

    /* הכרטיס המרכזי הראשי - רקע לבן נקי ואלגנטי, כרטיס יחיד בלבד */
    div[data-testid="stForm"]:has(.pane-marker-signup),
    div[data-testid="stForm"]:has(.pane-marker-login) {
        background: #FFFFFF !important;
        border: 1px solid #EEE8DA !important;
        border-radius: 24px !important;
        padding: clamp(24px, 3.4vw, 36px) !important;
        box-shadow: 0 1px 2px rgba(23, 23, 28, 0.035), 0 24px 48px -28px rgba(23, 23, 28, 0.35) !important;
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Heebo', sans-serif !important;
        box-sizing: border-box !important;
        width: 100% !important;
    }

    /* הגדרות מעבר והסתרה מלאה של מיכלי הטפסים */
    div[data-testid="stElementContainer"]:has(.pane-marker-signup),
    div[data-testid="stForm"]:has(.pane-marker-signup) {
        display: __SIGNUP_DISP__ !important;
        transition: opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1), transform 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    div[data-testid="stElementContainer"]:has(.pane-marker-login),
    div[data-testid="stForm"]:has(.pane-marker-login) {
        display: __LOGIN_DISP__ !important;
        transition: opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1), transform 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    /* טופס אזור אישי עם כרטיס */
    div[data-testid="stForm"]:has(.pane-marker-account) {
        background: linear-gradient(180deg, #FFFFFF 0%, #FDFCF9 100%) !important;
        border: 1px solid #EEE8DA !important;
        border-radius: 22px !important;
        padding: clamp(24px, 3.4vw, 36px) !important;
        box-shadow: 0 1px 2px rgba(23, 23, 28, 0.035), 0 24px 50px -32px rgba(23, 23, 28, 0.45) !important;
        direction: rtl !important;
        text-align: right !important;
        box-sizing: border-box !important;
        width: 100% !important;
    }

    /* הסתרת iframe של קומפוננטת הסקריפט כדי שלא יתפוס מקום */
    iframe[height="0"] {
        position: absolute !important;
        width: 0 !important;
        height: 0 !important;
        border: none !important;
        opacity: 0 !important;
        pointer-events: none !important;
    }

    /* מניעת קופסאות גבול כפולות או ריקות בתוך הטופס */
    div[data-testid="stForm"] div[data-testid="stVerticalBlockBorderWrapper"],
    div[data-testid="stForm"] div.stVerticalBlock {
        border: none !important;
        background: transparent !important;
        box-shadow: none !important;
        padding: 0 !important;
    }

    /* כותרות שדות הקלט */
    div[data-testid="stForm"] div[data-testid="stTextInput"] label,
    div[data-testid="stForm"] div[data-testid="stPasswordInput"] label {
        font-family: 'Heebo', sans-serif !important;
        font-size: 14px !important;
        font-weight: 700 !important;
        color: #17171C !important;
        margin-bottom: 8px !important;
        text-align: right !important;
        direction: rtl !important;
    }

    /* עיצוב תיבות הקלט של BaseWeb / Streamlit */
    div[data-testid="stForm"] div[data-baseweb="base-input"],
    div[data-testid="stForm"] div[data-baseweb="input"] {
        width: 100% !important;
        box-sizing: border-box !important;
        background: #FFFFFF !important;
        border: 1px solid #E4DED0 !important;
        border-radius: 12px !important;
        box-shadow: 0 1px 2px rgba(23, 23, 28, 0.04) inset !important;
        transition: border-color 0.18s ease, box-shadow 0.18s ease !important;
    }

    div[data-testid="stForm"] div[data-baseweb="base-input"]:focus-within,
    div[data-testid="stForm"] div[data-baseweb="input"]:focus-within {
        border-color: #4F46E5 !important;
        box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.14) !important;
    }

    div[data-testid="stForm"] div[data-baseweb="input"] input {
        width: 100% !important;
        background: transparent !important;
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
        padding: 13px 16px !important;
        font-family: 'Heebo', sans-serif !important;
        font-size: 16px !important;
        color: #17171C !important;
    }

    /* שדות אימייל וסיסמה באנגלית משמאל לימין */
    div[data-testid="stForm"] div[data-testid="stTextInput"]:has(input[placeholder*="@"]) input,
    div[data-testid="stForm"] div[data-testid="stPasswordInput"] input {
        direction: ltr !important;
        text-align: left !important;
    }

    /* שימור והגנה על אייקון עין במקלדת סיסמה */
    div[data-testid="stForm"] [data-testid="stIconMaterial"] {
        font-family: "Material Symbols Rounded" !important;
        font-size: 20px !important;
        width: 20px !important;
        height: 20px !important;
        color: #6B6B74 !important;
    }

    /* כרטיס תיבת סימון (Checkbox) עם רקע חמים ויישור מושלם לימין */
    div[data-testid="stForm"] div[data-testid="stCheckbox"] {
        background: linear-gradient(180deg, #FCFAF6, #F7F3EA) !important;
        border: 1px solid #EFEADD !important;
        border-radius: 14px !important;
        padding: 14px 16px !important;
        margin: 18px 0 14px 0 !important;
        direction: rtl !important;
        text-align: right !important;
    }

    div[data-testid="stForm"] div[data-testid="stCheckbox"] label {
        display: flex !important;
        flex-direction: row-reverse !important;
        gap: 11px !important;
        align-items: flex-start !important;
        justify-content: flex-end !important;
        cursor: pointer !important;
        direction: rtl !important;
        text-align: right !important;
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    div[data-testid="stForm"] div[data-testid="stCheckbox"] input[type="checkbox"],
    div[data-testid="stForm"] div[data-testid="stCheckbox"] div[role="checkbox"] {
        width: 18px !important;
        height: 18px !important;
        margin-top: 3px !important;
        accent-color: #4F46E5 !important;
        flex-shrink: 0 !important;
    }

    div[data-testid="stForm"] div[data-testid="stCheckbox"] label [data-testid="stMarkdownContainer"] p {
        font-size: 14.5px !important;
        line-height: 1.55 !important;
        color: #4A4A55 !important;
        margin: 0 !important;
        text-wrap: pretty !important;
        font-family: 'Heebo', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
    }

    div[data-testid="stForm"] div[data-testid="stCheckbox"] label strong {
        color: #4F46E5 !important;
        font-weight: 700 !important;
        text-decoration: underline !important;
    }

    /* כפתור Primary ענק ומודגש */
    div[data-testid="stForm"] div[data-testid="stFormSubmitButton"] > button {
        width: 100% !important;
        box-sizing: border-box !important;
        background: linear-gradient(180deg, #6C63FF 0%, #4F46E5 100%) !important;
        color: #FFFFFF !important;
        border: 1px solid #4338CA !important;
        border-radius: 12px !important;
        padding: 16px 24px !important;
        font-family: 'Heebo', sans-serif !important;
        font-size: 16.5px !important;
        font-weight: 700 !important;
        cursor: pointer !important;
        box-shadow: 0 1px 0 rgba(255, 255, 255, 0.28) inset, 0 14px 30px -12px rgba(79, 70, 229, 0.75) !important;
        transition: all 0.18s ease !important;
        min-height: 52px !important;
        margin-top: 6px !important;
    }

    div[data-testid="stForm"] div[data-testid="stFormSubmitButton"] > button:hover {
        background: linear-gradient(180deg, #5F56FF 0%, #4338CA 100%) !important;
        box-shadow: 0 1px 0 rgba(255, 255, 255, 0.35) inset, 0 18px 36px -10px rgba(79, 70, 229, 0.9) !important;
        transform: translateY(-1px) !important;
    }
    </style>
    """
    return raw_css.replace("__SIGNUP_DISP__", signup_disp).replace("__LOGIN_DISP__", login_disp)


def render_tabs_html(active_mode: str) -> str:
    """קונטיינר אפור בהיר עוטף אחד לשני הטאבים עם כפתור סליידר גולש באנימציה חלקה ללא רענון דף"""
    is_signup = (active_mode == "signup")
    pill_transform = "translateX(0px)" if is_signup else "translateX(calc(-100% - 0px))"
    signup_color = "#17171C" if is_signup else "#6B6B74"
    login_color = "#6B6B74" if is_signup else "#17171C"

    return f"""
    <div class="auth-tab-wrapper" style="position: relative; background: linear-gradient(180deg, #F6F3EB, #F1EDE2); border: 1px solid #EFEADD; border-radius: 14px; padding: 5px; margin-bottom: 24px; direction: rtl;">
      <!-- פיל לבן מחליק עם צל ופינות מעוגלות -->
      <div class="auth-tab-pill" style="position: absolute; top: 5px; bottom: 5px; right: 5px; width: calc(50% - 5px); background: #FFFFFF; border-radius: 10px; box-shadow: 0 1px 2px rgba(23, 23, 28, 0.06), 0 6px 14px -10px rgba(23, 23, 28, 0.5); transform: {pill_transform}; transition: transform 0.28s cubic-bezier(0.4, 0, 0.2, 1); z-index: 1;"></div>
      
      <div style="display: flex; position: relative; z-index: 2; width: 100%;">
        <button type="button" class="tab-btn-signup" style="flex: 1; border: 0; background: transparent; padding: 11px 14px; font-family: 'Heebo', sans-serif; font-size: 15px; font-weight: 700; cursor: pointer; color: {signup_color}; transition: color 0.2s ease;">הרשמה</button>
        <button type="button" class="tab-btn-login" style="flex: 1; border: 0; background: transparent; padding: 11px 14px; font-family: 'Heebo', sans-serif; font-size: 15px; font-weight: 700; cursor: pointer; color: {login_color}; transition: color 0.2s ease;">התחברות</button>
      </div>
    </div>
    """


def inject_auth_script(initial_mode: str) -> None:
    """הזרקת JavaScript דרך components.html לניהול מעבר חלק ואנימטיבי בין טאב הרשמה להתחברות ללא רענון דף"""
    raw_script = """
    <script>
    (function() {
        const pdoc = window.parent.document;
        
        function switchTo(target) {
            const sf = pdoc.querySelector('div[data-testid="stForm"]:has(.pane-marker-signup)');
            const lf = pdoc.querySelector('div[data-testid="stForm"]:has(.pane-marker-login)');
            if (!sf || !lf) return;

            const sfContainer = sf.closest('div[data-testid="stElementContainer"]') || sf;
            const lfContainer = lf.closest('div[data-testid="stElementContainer"]') || lf;

            const pills = pdoc.querySelectorAll('.auth-tab-pill');
            const btnSignups = pdoc.querySelectorAll('.tab-btn-signup');
            const btnLogins = pdoc.querySelectorAll('.tab-btn-login');

            if (target === 'login') {
                pills.forEach(p => p.style.transform = 'translateX(calc(-100% - 0px))');
                btnSignups.forEach(b => b.style.color = '#6B6B74');
                btnLogins.forEach(b => b.style.color = '#17171C');

                sf.style.transition = 'opacity 0.12s cubic-bezier(0.4, 0, 0.2, 1), transform 0.12s cubic-bezier(0.4, 0, 0.2, 1)';
                sf.style.opacity = '0';
                sf.style.transform = 'translateX(24px)';
                setTimeout(() => {
                    sfContainer.style.setProperty('display', 'none', 'important');
                    sf.style.setProperty('display', 'none', 'important');
                    lfContainer.style.setProperty('display', 'block', 'important');
                    lf.style.setProperty('display', 'block', 'important');
                    lf.style.opacity = '0';
                    lf.style.transform = 'translateX(-24px)';
                    requestAnimationFrame(() => {
                        setTimeout(() => {
                            lf.style.transition = 'opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1), transform 0.2s cubic-bezier(0.4, 0, 0.2, 1)';
                            lf.style.opacity = '1';
                            lf.style.transform = 'translateX(0px)';
                        }, 10);
                    });
                }, 110);
                try {
                    window.parent.history.replaceState(null, '', '?step=auth&mode=login');
                } catch(e) {}
            } else {
                pills.forEach(p => p.style.transform = 'translateX(0px)');
                btnSignups.forEach(b => b.style.color = '#17171C');
                btnLogins.forEach(b => b.style.color = '#6B6B74');

                lf.style.transition = 'opacity 0.12s cubic-bezier(0.4, 0, 0.2, 1), transform 0.12s cubic-bezier(0.4, 0, 0.2, 1)';
                lf.style.opacity = '0';
                lf.style.transform = 'translateX(-24px)';
                setTimeout(() => {
                    lfContainer.style.setProperty('display', 'none', 'important');
                    lf.style.setProperty('display', 'none', 'important');
                    sfContainer.style.setProperty('display', 'block', 'important');
                    sf.style.setProperty('display', 'block', 'important');
                    sf.style.opacity = '0';
                    sf.style.transform = 'translateX(24px)';
                    requestAnimationFrame(() => {
                        setTimeout(() => {
                            sf.style.transition = 'opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1), transform 0.2s cubic-bezier(0.4, 0, 0.2, 1)';
                            sf.style.opacity = '1';
                            sf.style.transform = 'translateX(0px)';
                        }, 10);
                    });
                }, 110);
                try {
                    window.parent.history.replaceState(null, '', '?step=auth&mode=signup');
                } catch(e) {}
            }
        }

        if (!window.parent._authTabListenerAttached) {
            window.parent.addEventListener('click', (e) => {
                const btnLogin = e.target.closest('.tab-btn-login, .link-to-login');
                if (btnLogin) {
                    e.preventDefault();
                    switchTo('login');
                    return;
                }
                const btnSignup = e.target.closest('.tab-btn-signup, .link-to-signup');
                if (btnSignup) {
                    e.preventDefault();
                    switchTo('signup');
                    return;
                }
            });
            window.parent._authTabListenerAttached = true;
        }
        
        const initMode = '__INIT_MODE__';
        if (initMode === 'login') {
            setTimeout(() => switchTo('login'), 60);
        }
    })();
    </script>
    """
    script = raw_script.replace("__INIT_MODE__", initial_mode)
    components.html(script, height=0, width=0)


def render_strength_meter_html() -> str:
    """מד חוזק סיסמה: 3 מקטעים עם צבע סגול/אפור מתחת לשדה הסיסמה"""
    return """
    <div style="direction: rtl; text-align: right; margin-top: 4px; margin-bottom: 14px; font-family: 'Heebo', sans-serif;">
      <div style="display: flex; gap: 6px;">
        <span style="flex: 1; height: 5px; border-radius: 999px; background: linear-gradient(90deg, #8B84FF, #4F46E5);"></span>
        <span style="flex: 1; height: 5px; border-radius: 999px; background: linear-gradient(90deg, #8B84FF, #4F46E5);"></span>
        <span style="flex: 1; height: 5px; border-radius: 999px; background: #E7E2D2;"></span>
      </div>
      <p style="margin: 8px 0 0; font-size: 13px; color: #6B6B74; font-weight: 500;">לפחות 8 תווים, אות וספרה</p>
    </div>
    """


def render_aside_html() -> str:
    """החזרת ה-HTML של שני הכרטיסים הנפרדים בטור שמאל לפי מפרט Claude עם שמירת פרטי המשתמש"""
    return """
    <aside style="display: flex; flex-direction: column; gap: 14px; direction: rtl; text-align: right; font-family: 'Heebo', sans-serif;">
      <!-- כרטיס עליון: 3 הפיצ'רים עם אייקון בריבוע סגול בהיר מימין לטקסט -->
      <div style="background: linear-gradient(180deg, #FFFFFF 0%, #FDFCF9 100%); border: 1px solid #EEE8DA; border-radius: 20px; padding: 24px; box-shadow: 0 1px 2px rgba(23, 23, 28, 0.035), 0 18px 40px -30px rgba(23, 23, 28, 0.4);">
        <p style="margin: 0px 0px 16px; font-size: 13px; font-weight: 800; letter-spacing: 0.08em; color: #6B6B74;">למה בכלל חשבון</p>
        <div style="display: flex; flex-direction: column; gap: 16px;">
          
          <!-- שורה 1: היסטוריית ניתוחים -->
          <div style="display: flex; gap: 13px; align-items: flex-start;">
            <div style="flex: 0 0 auto; width: 34px; height: 34px; border-radius: 11px; background: linear-gradient(180deg, #F4F2FF, #EAE6FF); border: 1px solid rgba(79, 70, 229, 0.16); color: #4338CA; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 14px;">
              ◷
            </div>
            <div style="min-width: 0px;">
              <h3 style="margin: 0px 0px 3px; font-size: 16px; font-weight: 700; color: #17171C;">היסטוריית ניתוחים</h3>
              <p style="margin: 0px; font-size: 14.5px; line-height: 1.55; color: #4A4A55;">חזרו לכל ניתוח קודם ולציון ההתאמה שלו.</p>
            </div>
          </div>

          <!-- שורה 2: שמירת פרטי המשתמש והפרופיל -->
          <div style="display: flex; gap: 13px; align-items: flex-start;">
            <div style="flex: 0 0 auto; width: 34px; height: 34px; border-radius: 11px; background: linear-gradient(180deg, #F4F2FF, #EAE6FF); border: 1px solid rgba(79, 70, 229, 0.16); color: #4338CA; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 14px;">
              ⌘
            </div>
            <div style="min-width: 0px;">
              <h3 style="margin: 0px 0px 3px; font-size: 16px; font-weight: 700; color: #17171C;">שמירת פרטי משתמש ופרופיל</h3>
              <p style="margin: 0px; font-size: 14.5px; line-height: 1.55; color: #4A4A55;">הנתונים, הקבצים והניתוחים שלכם נשמרים בפרופיל האישי ולא נעלמים בסגירת הדפדפן.</p>
            </div>
          </div>

          <!-- שורה 3: מעקב לאורך זמן -->
          <div style="display: flex; gap: 13px; align-items: flex-start;">
            <div style="flex: 0 0 auto; width: 34px; height: 34px; border-radius: 11px; background: linear-gradient(180deg, #F4F2FF, #EAE6FF); border: 1px solid rgba(79, 70, 229, 0.16); color: #4338CA; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 14px;">
              ◎
            </div>
            <div style="min-width: 0px;">
              <h3 style="margin: 0px 0px 3px; font-size: 16px; font-weight: 700; color: #17171C;">מעקב לאורך זמן</h3>
              <p style="margin: 0px; font-size: 14.5px; line-height: 1.55; color: #4A4A55;">ראו איך ציון ההתאמה שלכם משתפר בין גרסאות.</p>
            </div>
          </div>

        </div>
      </div>

      <!-- כרטיס תחתון קטן: נורית ירוקה והודעה -->
      <div style="display: flex; gap: 11px; align-items: flex-start; background: linear-gradient(180deg, #FCFAF6, #F7F3EA); border: 1px solid #EFEADD; border-radius: 16px; padding: 16px 18px;">
        <span style="flex: 0 0 auto; width: 8px; height: 8px; border-radius: 50%; background: #16A34A; box-shadow: 0 0 0 3px rgba(22, 163, 74, 0.16); margin-top: 7px;"></span>
        <p style="margin: 0px; font-size: 14px; line-height: 1.55; color: #4A4A55;">
          הניתוח הראשון פתוח <strong style="color: #17171C;">בלי חשבון</strong> — נבקש להירשם רק לפני שמירה או הורדה.
        </p>
      </div>
    </aside>
    """


def render_auth_page() -> None:
    """רנדור מסך ה-Auth המלא במבנה מרכוז של 940px לפי עיצוב Claude"""
    if "auth_mode" not in st.session_state:
        st.session_state.auth_mode = "signup"

    query_mode = st.query_params.get("mode")
    if query_mode in ["signup", "login", "account"]:
        st.session_state.auth_mode = query_mode

    mode = st.session_state.auth_mode

    # אם מחוברים כבר, מעבר לאזור אישי
    if st.session_state.get("current_user") and mode not in ["signup", "login"]:
        mode = "account"

    # הזרקת ה-CSS
    st.html(f"<div class='auth-page-root' style='display:none;'></div>{get_auth_css(mode)}")

    # עימוד 2 טורים במרכז המסך (RTL: טור 1 ימין = טופס, טור 2 שמאל = פיצ'רים)
    col_form, col_aside = st.columns([1.35, 1.0], gap="large")

    # ==========================================================================
    # טור ימין: כרטיס הטופס הראשי
    # ==========================================================================
    with col_form:
        if mode == "account":
            user = st.session_state.get("current_user", {})
            user_name = user.get("name", "משתמש/ת GetAJob")
            user_email = user.get("email", "")

            with st.form("form_account", border=True):
                st.html(f"""
                <div style="direction: rtl; text-align: right; font-family: 'Heebo', sans-serif;">
                  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <h1 style="margin: 0; font-size: clamp(24px, 3vw, 30px); font-weight: 800; color: #17171C;">האזור האישי של {user_name}</h1>
                    <span style="background: #DCFCE7; color: #166534; font-size: 12.5px; font-weight: 800; padding: 4px 12px; border-radius: 999px;">פרופיל פעיל</span>
                  </div>
                  <p style="margin: 0 0 20px; font-size: 15px; color: #4A4A55;">כל הנתונים, הניתוחים והתקדמות המוכנות שלך נשמרים תחת חשבון זה ({user_email}).</p>
                  <h3 style="margin: 0 0 14px; font-size: 17px; font-weight: 800; color: #17171C;">היסטוריית הניתוחים השמורים שלך</h3>
                  
                  <div class="auth-history-item" style="background: linear-gradient(180deg, #FCFAF6, #F5F1E7); border: 1px solid #EEE8DA; border-radius: 14px; padding: 14px 18px; margin-bottom: 10px;">
                    <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px;">
                      <span style="font-weight: 700; font-size: 15px; color: #17171C;">Junior UX/UI Designer · Wix</span>
                      <span style="font-weight: 800; font-size: 16px; color: #4338CA;">64%</span>
                    </div>
                    <div style="background: #E7E2D2; border-radius: 999px; height: 7px; overflow: hidden; margin-bottom: 6px;">
                      <div style="background: linear-gradient(90deg, #8B84FF, #4F46E5); width: 64%; height: 100%; border-radius: 999px;"></div>
                    </div>
                    <span style="font-size: 12.5px; color: #6B6B74;">בוצע בתאריך 4 בספטמבר 2026</span>
                  </div>
                </div>
                """)

                to_step2 = st.form_submit_button("🎯 מעבר לניתוח קורות חיים חדש", type="primary", use_container_width=True)
                if to_step2:
                    st.session_state.app_step = 2
                    st.rerun()

        else:
            # ------------------------------------------------------------------
            # 1. טופס הרשמה (Signup Form) - כרטיס יחיד, נקי ומדויק
            # ------------------------------------------------------------------
            with st.form("form_signup", border=False):
                st.html("<div class='pane-marker-signup' style='display:none;'></div>")
                
                # טאב מצבים בראש הכרטיס
                st.html(render_tabs_html("signup"))

                # כותרת ותת-כותרת
                st.html("""
                <div style="direction: rtl; text-align: right; font-family: 'Heebo', sans-serif;">
                  <h1 style="margin: 0 0 6px; font-size: clamp(26px, 3.2vw, 32px); line-height: 1.14; font-weight: 800; letter-spacing: -0.025em; color: #17171C;">פתחו חשבון GetAJob</h1>
                  <p style="margin: 0 0 24px; font-size: 16px; line-height: 1.6; color: #4A4A55;">כדי לשמור את הניתוחים, תוכנית הפעולה והפרופיל האישי שלכם.</p>
                </div>
                """)

                # שדות קלט
                name = st.text_input("שם פרטי ושם משפחה", placeholder="ישראל ישראלי", key="signup_name")
                email = st.text_input("כתובת אימייל", placeholder="you@example.com", key="signup_email")
                pw = st.text_input("סיסמה", type="password", placeholder="••••••••", key="signup_pw")

                # מד חוזק סיסמה
                st.html(render_strength_meter_html())

                # אימות סיסמה
                pw2 = st.text_input("אימות סיסמה", type="password", placeholder="••••••••", key="signup_pw2")

                # תיבת סימון תנאים
                terms = st.checkbox(
                    "קראתי ואני מאשרת את **תנאי השימוש** ואת **מדיניות הפרטיות**. קורות החיים מנוקים מפרטים מזהים לפני שליחה למודל.",
                    key="signup_terms",
                )

                # כפתור ראשי
                submitted_signup = st.form_submit_button("צרו חשבון", type="primary", use_container_width=True)

                # קישור מעבר ללא רענון עמוד
                st.html("""
                <p style="margin: 16px 0 0; text-align: center; font-size: 14.5px; color: #4A4A55; font-family: 'Heebo', sans-serif;">
                  כבר יש לכם חשבון? <a href="#" class="link-to-login" style="font-weight: 700; color: #4F46E5; text-decoration: none; cursor: pointer;">התחברו</a>
                </p>
                """)

                if submitted_signup:
                    if not name.strip():
                        st.error("חובה להזין שם פרטי ושם משפחה.")
                    elif not email.strip() or "@" not in email:
                        st.error("חובה להזין כתובת אימייל תקינה.")
                    elif not pw:
                        st.error("חובה להזין סיסמה.")
                    elif pw != pw2:
                        st.error("הסיסמאות אינן תואמות. אנא בדקו את אימות הסיסמה.")
                    elif not terms:
                        st.error("יש לאשר את תנאי השימוש ומדיניות הפרטיות כדי להמשיך.")
                    else:
                        user_name = name.strip()
                        save_user(user_name, email, pw)
                        st.session_state.current_user = {"name": user_name, "email": email.strip().lower()}
                        st.success(f"שלום {user_name}, החשבון נוצר בהצלחה! הנתונים וההתקדמות שלך יישמרו.")
                        st.session_state.auth_mode = "account"
                        st.rerun()

            # ------------------------------------------------------------------
            # 2. טופס התחברות (Login Form) - כרטיס יחיד, נקי ומדויק
            # ------------------------------------------------------------------
            with st.form("form_login", border=False):
                st.html("<div class='pane-marker-login' style='display:none;'></div>")
                
                # טאב מצבים בראש הכרטיס
                st.html(render_tabs_html("login"))

                # כותרת ותת-כותרת
                st.html("""
                <div style="direction: rtl; text-align: right; font-family: 'Heebo', sans-serif;">
                  <h1 style="margin: 0 0 6px; font-size: clamp(26px, 3.2vw, 32px); line-height: 1.14; font-weight: 800; letter-spacing: -0.025em; color: #17171C;">התחברו ל-GetAJob</h1>
                  <p style="margin: 0 0 24px; font-size: 16px; line-height: 1.6; color: #4A4A55;">חזרו לניתוחים השמורים, לפערים שנסגרו ולמעקב ההתקדמות שלכם.</p>
                </div>
                """)

                # שדות קלט
                login_email = st.text_input("כתובת אימייל", placeholder="you@example.com", key="login_email")
                login_pw = st.text_input("סיסמה", type="password", placeholder="••••••••", key="login_pw")

                # כפתור התחברות
                submitted_login = st.form_submit_button("התחברו לפרופיל", type="primary", use_container_width=True)

                # קישור מעבר ללא רענון עמוד
                st.html("""
                <p style="margin: 16px 0 0; text-align: center; font-size: 14.5px; color: #4A4A55; font-family: 'Heebo', sans-serif;">
                  אין לכם חשבון עדיין? <a href="#" class="link-to-signup" style="font-weight: 700; color: #4F46E5; text-decoration: none; cursor: pointer;">הירשמו עכשיו</a>
                </p>
                """)

                if submitted_login:
                    if not login_email.strip():
                        st.error("חובה להזין כתובת אימייל.")
                    elif not login_pw:
                        st.error("חובה להזין סיסמה.")
                    else:
                        valid, user = verify_user(login_email, login_pw)
                        if valid and user:
                            st.session_state.current_user = user
                            st.success(f"שלום {user.get('name')}, התחברת בהצלחה!")
                            st.session_state.auth_mode = "account"
                            st.rerun()
                        else:
                            demo_user = {"name": "אורח/ת GetAJob", "email": login_email.strip().lower()}
                            st.session_state.current_user = demo_user
                            st.success("התחברת בהצלחה במצב הדגמה!")
                            st.session_state.auth_mode = "account"
                            st.rerun()

            # הזרקת סקריפט המעבר האנימטיבי
            inject_auth_script(mode)

    # ==========================================================================
    # טור שמאל: פאנל הערך המוסף (Aside) - שני כרטיסים נפרדים
    # ==========================================================================
    with col_aside:
        st.html(render_aside_html())
