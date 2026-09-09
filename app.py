"""
GetAJob - פלטפורמת הדרכה ומעבר לתפקידי הייטק
זרימת משתמש מובנית, מזמינה וקלה לשימוש:
מסך 1: ברוכים הבאים וערך מוסף (3 כרטיסי יכולות מרכזיות למעבר לקריירה בהייטק).
מסך 2: בחירת תפקיד יעד (Pills מהירים / מאגר תפקידים) והזנת קורות חיים (דמו מהיר / קובץ).
מסך 3: לוח תוצאות (חיווי עליון רוחבי + 3 לשוניות: פערים ומסלולים, שדרוג קו"ח ל-ATS, צ'קליסט ומעקב התקדמות ליעד).
"""

import os
import json
import textwrap
import streamlit as st

from schemas import JobMatchAnalysis
from extractor import extract_text_from_file, DocumentExtractionError
from sanitizer import sanitize_pii, truncate_job_description
from cache_manager import global_cache
from llm_engine import analyze_job_match, load_mock_response
from career_catalog import (
    get_all_roles,
    get_role_data,
    get_learning_paths_for_skills,
)
import importlib
import ui_styles
importlib.reload(ui_styles)
import auth_view
importlib.reload(auth_view)
from ui_styles import (
    get_custom_css,
    render_score_gauge,
    render_bullet_comparison,
    render_learning_paths,
    render_ats_tip,
    render_landing_navbar,
    render_how_it_works,
    render_sample_showcase,
    render_faq_section,
    render_bottom_cta_banner,
)
from auth_view import render_auth_page, render_auth_navbar


# הגדרות עמוד ראשיות
st.set_page_config(
    page_title="GetAJob | מקפצת הקריירה להייטק",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# הזרקת מערכת העיצוב (מצב בהיר קבוע ומודרני)
st.markdown(get_custom_css(theme="light"), unsafe_allow_html=True)


def render_clean_html(html_str: str) -> None:
    """מרנדר HTML ב-Streamlit ללא רווחים מובילים או שורות ריקות שגורמות ל-Markdown לפרש כקוד."""
    cleaned = "\n".join(line.strip() for line in html_str.splitlines() if line.strip())
    st.markdown(cleaned, unsafe_allow_html=True)


# טעינת נתוני דמו מוכנים
@st.cache_data
def load_all_presets():
    presets_path = os.path.join(os.path.dirname(__file__), "data", "demo_presets.json")
    try:
        with open(presets_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


PRESETS = load_all_presets()

# מיפוי 3 התפקידים הפופולריים לשמות במאגר
POPULAR_ROLES_MAP = {
    "🎨 מעצב/ת UX/UI": "UX/UI Designer",
    "💻 מפתח/ת Frontend": "Frontend Developer",
    "📊 אנליסט/ית נתונים": "Data Analyst",
}


def map_role_to_preset(role_name: str) -> str:
    """התאמת תפקיד לתרחיש הדמו המתאים ביותר"""
    r = role_name.lower()
    if any(k in r for k in ["ux", "ui", "design", "product"]):
        return "ux_ui_preset"
    if any(k in r for k in ["soc", "security", "penetration", "network", "noc"]):
        return "soc_analyst"
    if any(k in r for k in ["data", "bi ", "analyst", "scientist"]):
        return "data_analyst"
    if any(k in r for k in ["devops", "cloud", "sre", "kubernetes"]):
        return "devops_cloud"
    if any(k in r for k in ["qa", "test"]):
        return "qa_automation"
    return "fullstack_dev"


def generate_role_milestones(target_role: str, missing_skills: list, project=None) -> list:
    """
    מחולל צ'קליסט אבני דרך אינטראקטיבי ומותאם אישית לתפקיד היעד ולפערי המועמד.
    מתאים לכל קשת התפקידים: עיצוב חוויית משתמש (UX/UI), ניתוח נתונים (Data), ותכנות/הנדסת תוכנה.
    """
    role_lower = target_role.lower()
    milestones = []
    high_skills = [s.skill for s in missing_skills if getattr(s, "importance", "") == "High"]
    med_skills = [s.skill for s in missing_skills if getattr(s, "importance", "") == "Medium"]

    # 1. UX/UI Designer
    if any(k in role_lower for k in ["ux", "ui", "design", "מעצב", "אפיון"]):
        proj_name = project.project_name if project else "אפיון ועיצוב מערכת SaaS מקצה לקצה"
        primary_skill = high_skills[0] if high_skills else (med_skills[0] if med_skills else "Figma & Design Systems")

        milestones.append({
            "id": "ms_ux_case_study",
            "category": "🎨 תיק עבודות ומקרה בוחן",
            "title": f"בניית מקרה בוחן מעמיק (Case Study) ב-Figma: {proj_name}",
            "desc": f"אפיון ועיצוב פרויקט דגל מלא הכולל: הגדרת הבעיה העסקית, מחקר מתחרים, מסעות לקוח (User Journey), אפיון מסכים ב-Wireframes ועיצוב Visual UI מלא ב-Figma.",
            "action_hint": "💡 טיפ למעצבי ג'וניור: מגייסים בוחנים את תהליך החשיבה והפתרון של הבעיה (Problem Solving) ולא רק תמונות של מסכים יפים.",
        })

        milestones.append({
            "id": "ms_ux_primary_skill",
            "category": "🛠️ סגירת פער מיומנות חובה",
            "title": f"שליטה ותרגול מעשי בכלי החובה: {primary_skill}",
            "desc": f"הטמעת עבודה מקצועית ב-{primary_skill}, כולל שימוש במערכות עיצוב (Design Systems), רכיבי Auto-Layout, משתנים (Variables) ו-Tokens.",
            "action_hint": f"💡 עיין בלשונית 'ניתוח פערים ומסלולי למידה' לסילבוס ההסמכה הרשמי ב-{primary_skill}.",
        })

        if len(high_skills) > 1:
            second_skill = high_skills[1]
            milestones.append({
                "id": "ms_ux_second_skill",
                "category": "🛠️ סגירת פער מיומנות קריטי",
                "title": f"שליטה במיומנות ליבה נוספת: {second_skill}",
                "desc": f"סגירת פער המיומנות ב-{second_skill} על ידי יישום תרגיל מעשי ייעודי והוספתו לתיק העבודות.",
                "action_hint": "💡 הוכחת שליטה במיומנויות החובה תאפשר לך לעבור את שלב המיון המקצועי של ה-Design Lead.",
            })

        milestones.append({
            "id": "ms_ux_usability",
            "category": "🧪 מחקר ובדיקות שמישות",
            "title": "ביצוע בדיקות שמישות (Usability Testing) עם 3-5 משתמשים",
            "desc": "העברת משתמשים אמיתיים באב-טיפוס אינטראקטיבי (Clickable Prototype), זיהוי חסמים בחוויית המשתמש (Friction Points) ותיעוד האיטרציות העיצוביות שבוצעו במקרה הבוחן.",
            "action_hint": "💡 תיעוד של 'מה לא עבד וכיצד תיקנו את זה' על בסיס משתמשים מוכיח בשלות מקצועית יוצאת דופן.",
        })

        milestones.append({
            "id": "ms_ux_cv_ats",
            "category": "✍️ שדרוג קורות חיים ל-ATS",
            "title": "שדרוג סעיפי הניסיון בקו\"ח לנוסחת Action + Scale + Impact",
            "desc": "המרת ניסוחים כלליים להישגים מדידים (למשל: 'עיצוב מחדש של תהליך ההרשמה שהפחית נטישה ב-34% והעלה שביעות רצון משתמשים').",
            "action_hint": "💡 העתק ישירות את הסעיפים המשודרגים מתוך לשונית 'שדרוג קורות חיים'.",
        })

        milestones.append({
            "id": "ms_ux_certification",
            "category": "🎓 הסמכה מקצועית מהקטלוג",
            "title": "השלמת הסמכה מוכרת ב-UX/UI Design",
            "desc": "סיום קורס מעשי מוביל מהקטלוג (כגון Google UX Design Professional Certificate או Figma Academy) להוספת תעודה רשמית לפרופיל ה-LinkedIn.",
            "action_hint": "💡 תעודות רשמיות עוזרות לצלוח את סינון ה-ATS הראשוני של מחלקות הגיוס.",
        })

        milestones.append({
            "id": "ms_ux_launch_outreach",
            "category": "🚀 פרסום ונטוורקינג",
            "title": "העלאת תיק העבודות לרשת ופנייה יזומה ל-5 מגייסים ומעצבים בכירים",
            "desc": "פרסום מקרי הבוחן באתר אישי (Webflow / Framer / Notion / Behance), אופטימיזציה של פרופיל ה-LinkedIn ופנייה אישית ל-5 חברות מתאימות.",
            "action_hint": "💡 צרף קישור ישיר למקרה הבוחן המתאים ביותר לדרישות החברה בכל פנייה.",
        })

    # 2. Data Analyst / BI
    elif any(k in role_lower for k in ["data", "analyst", "bi", "נתונים", "דאטה"]):
        proj_name = project.project_name if project else "לוח מחוונים עסקי לניתוח מדדי פעילות"
        primary_skill = high_skills[0] if high_skills else (med_skills[0] if med_skills else "SQL מתקדם & Power BI")

        milestones.append({
            "id": "ms_data_dashboard",
            "category": "📊 לוח מחוונים ו-BI אינטראקטיבי",
            "title": f"בניית לוח מחוונים עסקי אינטראקטיבי: {proj_name}",
            "desc": f"פיתוח דשבורד מקיף ב-PowerBI / Tableau / Python עבור {proj_name}, הכולל ויזואליזציות מתקדמות, מדדי ביצוע (KPIs) עסקיים ופילוחים דינמיים.",
            "action_hint": "💡 הדגש תובנות עסקיות מניעות לפעולה (Actionable Insights) ולא רק גרפים יפים.",
        })

        milestones.append({
            "id": "ms_data_primary_skill",
            "category": "🛠️ סגירת פער מיומנות חובה",
            "title": f"סגירת פער טכנולוגי: שליטה מעשית ב-{primary_skill}",
            "desc": f"תרגול שאילתות מורכבות, ניקוי והכנת נתונים (Data Wrangling) ושימוש מעשי ב-{primary_skill} על גבי מערכי נתונים אמיתיים.",
            "action_hint": f"💡 עיין במסלולי הלמידה המומלצים בלשונית ניתוח הפערים עבור {primary_skill}.",
        })

        if len(high_skills) > 1:
            second_skill = high_skills[1]
            milestones.append({
                "id": "ms_data_second_skill",
                "category": "🛠️ סגירת פער מיומנות קריטי",
                "title": f"שליטה במיומנות ליבה נוספת: {second_skill}",
                "desc": f"ביצוע מודול מעשי ב-{second_skill} להוכחת היכולת הטכנולוגית מול דרישות המשרה.",
                "action_hint": "💡 חברות דורשות שילוב של SQL, כלי BI ושפת ניתוח כמו Python/R.",
            })

        milestones.append({
            "id": "ms_data_eda",
            "category": "🧹 חקר נתונים ו-Storytelling",
            "title": "ביצוע ניתוח נתונים חקרני ותיעוד ממצאים (Data Storytelling)",
            "desc": "חקירת קורלציות, זיהוי חריגים, הסקת מסקנות עסקיות מנומקות והצגתן כמסמך תובנות עסקיות.",
            "action_hint": "💡 מראיינים מחפשים מועמדים שיודעים להסביר מספרים בשפה עסקית פשוטה שמנהלים מבינים.",
        })

        milestones.append({
            "id": "ms_data_cv_ats",
            "category": "✍️ שדרוג קורות חיים ל-ATS",
            "title": "שכתוב סעיפי קורות החיים בדגש על השפעה עסקית ומדדים",
            "desc": "הבלטת חיסכון בשעות עבודה, אופטימיזציה של תהליכים, גילוי צווארי בקבוק וקבלת החלטות מבוססות נתונים.",
            "action_hint": "💡 השתמש בסעיפים המוכנים מתוך לשונית 'שדרוג קורות חיים'.",
        })

        milestones.append({
            "id": "ms_data_certification",
            "category": "🎓 הסמכה מקצועית מהקטלוג",
            "title": "השלמת הסמכה רשמית ב-Data Analytics / BI",
            "desc": "קבלת תעודת Google Data Analytics Professional Certificate או Microsoft Power BI Data Analyst Associate.",
            "action_hint": "💡 הוספת תג ההסמכה הרשמי מעלה משמעותית את שיעור הפניות היזומות ממגייסים ב-LinkedIn.",
        })

        milestones.append({
            "id": "ms_data_launch",
            "category": "🚀 פרסום ונטוורקינג",
            "title": "פרסום ניתוח הדאטה ב-LinkedIn ופנייה יזומה למנהלי צוותי אנליטיקס",
            "desc": "שיתוף תובנות מהדשבורד בפוסט מקצועי ופנייה ממוקדת ל-5 מגייסים ומובילי תחום ה-Data בחברות היעד.",
            "action_hint": "💡 צרף קישור ללוח המחוונים החי (Interactive Dashboard) בכל פנייה.",
        })

    # 3. Developer / Frontend / Fullstack / DevOps / Cyber / QA
    else:
        proj_name = project.project_name if project else "מערכת תוכנה מתקדמת מקצה לקצה"
        primary_skill = high_skills[0] if high_skills else (med_skills[0] if med_skills else "כלי/ספריית חובה")

        milestones.append({
            "id": "ms_dev_repo",
            "category": "💻 פרויקט קוד מלא ל-GitHub",
            "title": f"פיתוח והעלאת פרויקט קצה-לקצה ל-GitHub: {proj_name}",
            "desc": "מימוש ארכיטקטורת המערכת בקוד נקי, מודולרי ומתועד, כולל בדיקות יחידה (Unit Tests) והוראות התקנה ברורות.",
            "action_hint": "💡 מגייסים ומראיינים טכניים בודקים את היסטוריית הקומיטים (Commit History) ואיכות הארכיטקטורה.",
        })

        milestones.append({
            "id": "ms_dev_primary_skill",
            "category": "🛠️ סגירת פער טכנולוגי קריטי",
            "title": f"הטמעה מעשית של כלי/שפת החובה: {primary_skill}",
            "desc": f"שילוב מודול מעשי הממחיש שליטה ב-{primary_skill} כחלק מליבת הארכיטקטורה של הפרויקט.",
            "action_hint": f"💡 ראה מסלול למידה והסמכה מותאם בלשונית ניתוח הפערים עבור {primary_skill}.",
        })

        if len(high_skills) > 1:
            second_skill = high_skills[1]
            milestones.append({
                "id": "ms_dev_second_skill",
                "category": "🛠️ סגירת פער טכנולוגי נוסף",
                "title": f"שליטה במיומנות ליבה נוספת: {second_skill}",
                "desc": f"אינטגרציה של {second_skill} במערכת או פיתוח שירות ייעודי המשתמש בה.",
                "action_hint": "💡 סגירת פערי ה-High מאפשרת לעבור את שלב הסינון הראשוני של הטק-ליד.",
            })

        milestones.append({
            "id": "ms_dev_deploy_readme",
            "category": "☁️ פריסה לענן ותיעוד מקצועי",
            "title": "פריסה לסביבת ענן חיה (Live Demo) והעלאת קובץ README.md מושלם",
            "desc": "פריסת האפליקציה לענן (Vercel / AWS / Render / Docker) עם קישור פעיל להדגמה וקובץ README מקצועי עם דיאגרמת ארכיטקטורה.",
            "action_hint": "💡 שלד קובץ ה-README המלא זמין להורדה מטה בלשונית זו.",
        })

        milestones.append({
            "id": "ms_dev_cv_ats",
            "category": "✍️ אופטימיזציה של קורות החיים ל-ATS",
            "title": "המרת סעיפי הניסיון בקו\"ח לנוסחת Action-Impact הנדסית",
            "desc": "שדרוג סעיפי הפיתוח עם מדדי ביצוע טכנולוגיים (שיפור מהירות טעינה, צמצום זמני ריצה, חיסכון במשאבים).",
            "action_hint": "💡 היעזר בסעיפים המנוסחים בלשונית 'שדרוג קורות חיים'.",
        })

        milestones.append({
            "id": "ms_dev_certification",
            "category": "🎓 הסמכה טכנולוגית מובילה מהקטלוג",
            "title": "השלמת מסלול הסמכה טכנולוגי מוכר",
            "desc": "סיום קורס רשמי מחברות טכנולוגיה מובילות (כגון AWS Certified Cloud Practitioner או Meta Frontend Developer).",
            "action_hint": "💡 הסמכה רשמית מאשררת את הידע התאורטי מול מסנני ה-ATS.",
        })

        milestones.append({
            "id": "ms_dev_launch",
            "category": "🚀 הגשות ממוקדות ונטוורקינג פעיל",
            "title": "הגשת מועמדות ל-10 משרות מתאימות ופנייה ישירה לראשי צוותים",
            "desc": "שליחת קורות החיים המותאמים וקישור ישיר לפרויקט הפורטפוליו ו-GitHub לפרופילים של מנהלי פיתוח רלוונטיים.",
            "action_hint": "💡 פנייה ישירה למנהל מגייס עם הצגת פרויקט מעשי מגדילה משמעותית את הסיכוי לראיון ראשון.",
        })

    return milestones


# אתחול Session State
if "app_step" not in st.session_state:
    st.session_state.app_step = 1  # 1 = ברוכים הבאים וערך, 2 = בחירת תפקיד וקלט, 3 = לוח תוצאות, "auth" = הרשמה והתחברות

if "current_user" not in st.session_state:
    st.session_state.current_user = None

# תמיכה במעבר שלבים מקישורי Navbar (הירשם / היכנס) או Query Params
step_param = st.query_params.get("step")
page_param = st.query_params.get("page")

if step_param == "auth" or page_param == "auth":
    st.session_state.app_step = "auth"
    if st.query_params.get("mode"):
        st.session_state.auth_mode = st.query_params.get("mode")
    try:
        del st.query_params["step"]
    except Exception:
        pass
    try:
        del st.query_params["page"]
    except Exception:
        pass
    try:
        del st.query_params["mode"]
    except Exception:
        pass
elif step_param == "1":
    st.session_state.app_step = 1
    try:
        del st.query_params["step"]
    except Exception:
        pass
elif step_param == "2":
    st.session_state.app_step = 2
    try:
        del st.query_params["step"]
    except Exception:
        pass


if "target_role" not in st.session_state:
    st.session_state.target_role = "UX/UI Designer"

if "quick_role_choice" not in st.session_state:
    st.session_state.quick_role_choice = "🎨 מעצב/ת UX/UI"

if "data_source" not in st.session_state:
    st.session_state.data_source = "demo"  # "demo" | "upload"

if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

if "job_text" not in st.session_state:
    st.session_state.job_text = ""

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

if "cache_hit" not in st.session_state:
    st.session_state.cache_hit = False

if "gemini_api_key" not in st.session_state:
    st.session_state.gemini_api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY", "")

if "force_mock_mode" not in st.session_state:
    st.session_state.force_mock_mode = False

if "completed_milestones" not in st.session_state:
    st.session_state.completed_milestones = set()

if "balloons_shown" not in st.session_state:
    st.session_state.balloons_shown = False


# ==============================================================================
# מסך 1: ברוכים הבאים וערך מוסף (WELCOME & VALUE PROPOSITION - SLACK HERO STYLE)
# ==============================================================================
if st.session_state.app_step == 1:
    # ביטול כפתור הגדלת תמונה בעת ריחוף והגדרת מרווחי עמוד עליונים מותאמים
    st.markdown(
        """
        <style>
        .block-container {
            padding-top: 96px !important;
            padding-bottom: 4rem !important;
        }
        /* ביטול כפתור הגדלת תמונה למסך מלא בעת ריחוף */
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
        /* כפתור ה-CTA התחתון — סעיף 5.1 במפרט העיצוב */
        div.stButton > button[kind="primary"] {
            font-family: 'Heebo', sans-serif !important;
            font-size: 16.5px !important;
            font-weight: 700 !important;
            padding: 16px 30px !important;
            border-radius: 12px !important;
            background: linear-gradient(180deg, #6C63FF, #4F46E5) !important;
            border: 1px solid #4338CA !important;
            color: #FFFFFF !important;
            box-shadow: 0 1px 0 rgba(255, 255, 255, 0.28) inset, 0 14px 30px -12px rgba(79, 70, 229, 0.75) !important;
            transition: box-shadow 0.18s ease, border-color 0.18s ease, transform 0.18s ease !important;
            min-height: 48px !important;
        }
        div.stButton > button[kind="primary"]:hover {
            background: linear-gradient(180deg, #5F56FF, #4338CA) !important;
            box-shadow: 0 1px 0 rgba(255, 255, 255, 0.35) inset, 0 16px 34px -10px rgba(79, 70, 229, 0.85) !important;
            transform: translateY(-1px) !important;
        }
        /* כרטיסיות ה-Value Props בסקשן ה-Hero */
        .m3-hero-cards-grid {
            display: grid !important;
            grid-template-columns: repeat(4, 1fr) !important;
            gap: 16px !important;
            direction: rtl !important;
            text-align: right !important;
        }
        @media (max-width: 960px) {
            .m3-hero-cards-grid {
                grid-template-columns: repeat(2, 1fr) !important;
            }
        }
        @media (max-width: 520px) {
            .m3-hero-cards-grid {
                grid-template-columns: 1fr !important;
            }
        }
        .m3-hero-card {
            background: #FFFFFF !important;
            border: 1px solid #EEE8DA !important;
            border-radius: 18px !important;
            padding: 20px 18px !important;
            box-shadow: 0 1px 2px rgba(23, 23, 28, 0.035), 0 8px 20px -16px rgba(23, 23, 28, 0.08) !important;
            display: flex !important;
            flex-direction: column !important;
            align-items: flex-start !important;
            text-align: right !important;
            direction: rtl !important;
            transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease !important;
        }
        /* מרכוז כותרות ותת-כותרות בסקשן ה-Hero */
        .m3-hero-title-container,
        .m3-hero-title-1,
        .m3-hero-title-2,
        .m3-hero-subtitle-container,
        .m3-hero-subtitle,
        .m3-hero-subtitle-container p {
            text-align: center !important;
            margin-left: auto !important;
            margin-right: auto !important;
        }

        /* העברת סליידר הגלילה לצד ימין, הצגה אוטומטית רק כשיש גלילה, והתאמה לפלטת המערכת */
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
        .stMain::-webkit-scrollbar {
            width: 8px !important;
            height: 8px !important;
        }
        section[data-testid="stMain"]::-webkit-scrollbar-track,
        .stMain::-webkit-scrollbar-track {
            background: transparent !important;
        }
        section[data-testid="stMain"]::-webkit-scrollbar-thumb,
        .stMain::-webkit-scrollbar-thumb {
            background: #C7D2FE !important;
            border-radius: 9999px !important;
        }
        section[data-testid="stMain"]::-webkit-scrollbar-thumb:hover,
        .stMain::-webkit-scrollbar-thumb:hover {
            background: #4F46E5 !important;
        }

        /* מרווחי גלילה עבור עוגני ה-Navbar עם סרגל ניווט קבוע */
        html, body {
            scroll-behavior: smooth !important;
        }
        #how-it-works,
        #sample-output,
        #faq {
            scroll-margin-top: 88px !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # ----------------------------------------------------
    # 1. סרגל ניווט עליון קבוע עם אפקט טשטוש (Fixed Frosted Navbar - סעיף 5.6)
    # ----------------------------------------------------
    render_clean_html(render_landing_navbar(st.session_state.get("current_user")))


    # ----------------------------------------------------
    # 2. סקשן מרכזי (Hero Section: Centered Title, Right Subtitle, 4 Value Cards)
    # ----------------------------------------------------
    render_clean_html(
        """
        <div style="direction: rtl; margin-top: 10px; margin-bottom: 0;">
            <!-- תגית מותג עליונה ממורכזת — בנוי לג'וניורים -->
            <div style="text-align: center; margin-bottom: 16px;">
                <div style="display: inline-flex; align-items: center; gap: 7px; background: linear-gradient(180deg, #F4F2FF, #EAE6FF); border: 1px solid #E0D9FF; border-radius: 999px; padding: 5px 16px;">
                    <svg width="13" height="13" viewBox="0 0 24 24" fill="#4F46E5" stroke="#4F46E5" stroke-width="1">
                        <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
                    </svg>
                    <span style="font-size: 13px; font-weight: 700; color: #4338CA; font-family: 'Heebo', sans-serif;">בנוי לג'וניורים שנתקעו בשלב הסינון</span>
                </div>
            </div>

            <!-- כותרת ראשית ממורכזת בדומה לתמונה מקלוד דיזיין -->
            <div class="m3-hero-title-container" style="text-align: center !important; margin-bottom: 16px;">
                <div role="heading" aria-level="1" class="m3-hero-title-1" style="margin: 0 0 4px 0; text-align: center !important; font-family: 'Heebo', sans-serif; font-size: clamp(32px, 4.4vw, 52px); font-weight: 800; line-height: 1.12; color: #17171C; letter-spacing: -0.035em; text-wrap: pretty;">
                    זהה את פערי הידע שלך.
                </div>
                <div class="m3-hero-title-2" style="text-align: center !important; font-family: 'Heebo', sans-serif; font-size: clamp(32px, 4.4vw, 52px); font-weight: 800; line-height: 1.12; background: linear-gradient(180deg, #6C63FF 0%, #4F46E5 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: -0.035em; text-wrap: pretty;">
                    ובנה בדיוק את מה שחסר לך.
                </div>
            </div>

            <!-- תיאור מתחת לכותרת במרכז (Center Aligned) -->
            <div class="m3-hero-subtitle-container" style="text-align: center !important; margin-bottom: 32px; direction: rtl;">
                <p class="m3-hero-subtitle" style="margin: 0 auto; text-align: center !important; color: #4A4A55; font-size: 16.5px; line-height: 1.6; font-weight: 400; font-family: 'Heebo', sans-serif; max-width: 680px;">
                    העלו קורות חיים ותיאור משרה — ותקבלו מפת פערים מדויקת, סעיפים משוכתבים, ופרויקט פורטפוליו שסוגר את החסר.
                </p>
            </div>

            <!-- 4 כרטיסיות מותאמות בפרופורציות מוקפדות לפי מפרט העיצוב -->
            <div class="m3-hero-cards-grid">
                <!-- כרטיסייה 1: איתור פערי מיומנויות -->
                <div class="m3-hero-card">
                    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px; width: 100%;">
                        <div style="width: 34px; height: 34px; border-radius: 9px; background: linear-gradient(180deg, #F4F2FF, #EAE6FF); border: 1px solid #E0D9FF; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                            <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#4F46E5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <circle cx="12" cy="12" r="10"></circle>
                                <circle cx="12" cy="12" r="6"></circle>
                                <circle cx="12" cy="12" r="2"></circle>
                            </svg>
                        </div>
                        <div style="font-size: 15.5px; font-weight: 700; color: #17171C; font-family: 'Heebo', sans-serif; line-height: 1.25;">
                            איתור פערי מיומנויות
                        </div>
                    </div>
                    <div style="font-size: 13px; color: #4A4A55; line-height: 1.5; font-family: 'Heebo', sans-serif;">
                        מיפוי מדויק של הטכנולוגיות וכלי החובה שחסרים לך מול דרישות השוק.
                    </div>
                </div>

                <!-- כרטיסייה 2: שדרוג קורות חיים ל-ATS -->
                <div class="m3-hero-card">
                    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px; width: 100%;">
                        <div style="width: 34px; height: 34px; border-radius: 9px; background: linear-gradient(180deg, #F4F2FF, #EAE6FF); border: 1px solid #E0D9FF; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                            <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#4F46E5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                                <polyline points="14 2 14 8 20 8"></polyline>
                                <line x1="16" y1="13" x2="8" y2="13"></line>
                                <line x1="16" y1="17" x2="8" y2="17"></line>
                                <polyline points="10 9 9 9 8 9"></polyline>
                            </svg>
                        </div>
                        <div style="font-size: 15.5px; font-weight: 700; color: #17171C; font-family: 'Heebo', sans-serif; line-height: 1.25;">
                            שדרוג קורות חיים ל-<bdi>ATS</bdi>
                        </div>
                    </div>
                    <div style="font-size: 13px; color: #4A4A55; line-height: 1.5; font-family: 'Heebo', sans-serif;">
                        המרת ניסוחים לסעיפי הישגים מדידים בפורמט <bdi dir="ltr" style="font-weight: 600; color: #4338CA;">Action-Impact</bdi>.
                    </div>
                </div>

                <!-- כרטיסייה 3: צ'קליסט אינטראקטיבי ומעקב -->
                <div class="m3-hero-card">
                    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px; width: 100%;">
                        <div style="width: 34px; height: 34px; border-radius: 9px; background: linear-gradient(180deg, #F4F2FF, #EAE6FF); border: 1px solid #E0D9FF; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                            <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#4F46E5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M9 11l3 3L22 4"></path>
                                <path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path>
                            </svg>
                        </div>
                        <div style="font-size: 15.5px; font-weight: 700; color: #17171C; font-family: 'Heebo', sans-serif; line-height: 1.25;">
                            צ'קליסט אינטראקטיבי ומעקב
                        </div>
                    </div>
                    <div style="font-size: 13px; color: #4A4A55; line-height: 1.5; font-family: 'Heebo', sans-serif;">
                        זיהוי החוסרים לקראת תפקיד היעד והצגתם כרשימת משימות לסימון, עם מעקב שוטף ומד מוכנות לגיוס.
                    </div>
                </div>

                <!-- כרטיסייה 4: מסלולי למידה והסמכות -->
                <div class="m3-hero-card">
                    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px; width: 100%;">
                        <div style="width: 34px; height: 34px; border-radius: 9px; background: linear-gradient(180deg, #F4F2FF, #EAE6FF); border: 1px solid #E0D9FF; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                            <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#4F46E5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M22 10v6M2 10l10-5 10 5-10 5z"></path>
                                <path d="M6 12v5c3 3 9 3 12 0v-5"></path>
                            </svg>
                        </div>
                        <div style="font-size: 15.5px; font-weight: 700; color: #17171C; font-family: 'Heebo', sans-serif; line-height: 1.25;">
                            מסלולי למידה והסמכות
                        </div>
                    </div>
                    <div style="font-size: 13px; color: #4A4A55; line-height: 1.5; font-family: 'Heebo', sans-serif;">
                        קורסים מומלצים מחברות טכנולוגיה מובילות <span dir="ltr" style="font-weight: 600; color: #17171C;">(Google, AWS, Meta, Figma)</span>.
                    </div>
                </div>
            </div>
        </div>
        """
    )

    # ----------------------------------------------------
    # 3. סקשן "איך זה עובד" (How It Works - סעיף 3, 5)
    # ----------------------------------------------------
    render_clean_html(render_how_it_works())

    # ----------------------------------------------------
    # 4. סקשן "דוגמת פלט לניתוח אמיתי" (Real Analysis Showcase - סעיף 1.5, 5.3, 5.4)
    # ----------------------------------------------------
    render_clean_html(render_sample_showcase())

    # ----------------------------------------------------
    # 5. סקשן שאלות נפוצות (FAQ - סעיף 3, 7)
    # ----------------------------------------------------
    render_clean_html(render_faq_section())

    # ----------------------------------------------------
    # 6. באנר הנעה לפעולה תחתון (Dark CTA Band - סעיף 5.7)
    # ----------------------------------------------------
    render_clean_html(render_bottom_cta_banner())

    col_bot_sp1, col_bot_run, col_bot_sp2 = st.columns([1.8, 1.0, 1.8], vertical_alignment="center")
    with col_bot_run:
        if st.button("הריצו ניתוח להדגמה", type="primary", use_container_width=True, key="btn_bottom_run"):
            st.session_state.app_step = 2
            st.rerun()


# ==============================================================================
# מסך הרשמה והתחברות (AUTH SCREEN - CLAUDE DESIGN HANDOFF v1.0)
# ==============================================================================
elif st.session_state.app_step == "auth":
    render_auth_navbar()
    render_auth_page()


# ==============================================================================
# מסך 2: בחירת תפקיד והזנת נתוני מועמד (ROLE SELECTION & INPUT)
# ==============================================================================
elif st.session_state.app_step == 2:
    # ----------------------------------------------------
    # 1. Header עליון צף ומטושטש (מפרט סעיף 5.6)
    # ----------------------------------------------------
    render_auth_navbar()

    st.markdown(
        """
        <style>
        .auth-custom-navbar {
            margin-bottom: 24px !important;
        }
        div[data-testid="stHorizontalBlock"]:has(.step2-role-card) {
            align-items: stretch !important;
        }
        div[data-testid="stColumn"]:has(.step2-role-card),
        div[data-testid="column"]:has(.step2-role-card) {
            background: #FFFFFF !important;
            border: 1.5px solid #EEE8DA !important;
            border-radius: 16px !important;
            padding: 16px 15px 14px 15px !important;
            box-shadow: 0 1px 3px rgba(23, 23, 28, 0.035), 0 8px 20px -16px rgba(23, 23, 28, 0.08) !important;
            transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease, background 0.2s ease !important;
            display: flex !important;
            flex-direction: column !important;
            justify-content: space-between !important;
            height: 100% !important;
            direction: rtl !important;
            text-align: right !important;
            cursor: pointer !important;
            box-sizing: border-box !important;
        }
        div[data-testid="stColumn"]:has(.step2-role-card:not(.active)):hover,
        div[data-testid="column"]:has(.step2-role-card:not(.active)):hover {
            transform: translateY(-2px) !important;
            border-color: #C7D2FE !important;
            box-shadow: 0 10px 24px -10px rgba(79, 70, 229, 0.16) !important;
        }
        div[data-testid="stColumn"]:has(.step2-role-card.active),
        div[data-testid="column"]:has(.step2-role-card.active) {
            background: linear-gradient(180deg, #FFFFFF 0%, #F8F7FF 100%) !important;
            border: 2px solid #4F46E5 !important;
            box-shadow: 0 0 0 1px #4F46E5, 0 10px 24px -8px rgba(79, 70, 229, 0.22) !important;
        }
        div[data-testid="stColumn"]:has(.step2-role-card) > div[data-testid="stVerticalBlock"],
        div[data-testid="column"]:has(.step2-role-card) > div[data-testid="stVerticalBlock"] {
            height: 100% !important;
            display: flex !important;
            flex-direction: column !important;
            justify-content: space-between !important;
            gap: 0 !important;
        }
        .step2-role-card {
            background: transparent !important;
            border: none !important;
            border-radius: 0 !important;
            padding: 0 !important;
            box-shadow: none !important;
            min-height: auto !important;
            cursor: pointer !important;
            display: flex !important;
            flex-direction: column !important;
            flex-grow: 1 !important;
            margin-bottom: 0 !important;
            direction: rtl !important;
            text-align: right !important;
        }
        .step2-role-card-header {
            display: flex !important;
            align-items: center !important;
            gap: 10px !important;
            margin-bottom: 8px !important;
            width: 100% !important;
        }
        .step2-role-icon-box {
            width: 34px !important;
            height: 34px !important;
            border-radius: 9px !important;
            background: linear-gradient(180deg, #F4F2FF, #EAE6FF) !important;
            border: 1px solid #E0D9FF !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            flex-shrink: 0 !important;
        }
        .step2-role-title {
            font-size: 15px !important;
            font-weight: 700 !important;
            color: #17171C !important;
            font-family: 'Heebo', sans-serif !important;
            line-height: 1.25 !important;
        }
        .step2-role-desc {
            font-size: 12.5px !important;
            color: #4A4A55 !important;
            line-height: 1.5 !important;
            font-family: 'Heebo', sans-serif !important;
            margin-bottom: 4px !important;
            flex-grow: 1 !important;
        }
        div[data-testid="stColumn"]:has(.step2-role-card) div[data-testid="stElementContainer"]:has(button),
        div[data-testid="column"]:has(.step2-role-card) div[data-testid="stElementContainer"]:has(button) {
            margin-top: 12px !important;
            margin-bottom: 0 !important;
            width: 100% !important;
        }
        div[data-testid="stColumn"]:has(.step2-role-card) button,
        div[data-testid="column"]:has(.step2-role-card) button {
            height: 34px !important;
            min-height: 34px !important;
            max-height: 34px !important;
            line-height: 34px !important;
            padding: 0 10px !important;
            font-size: 13px !important;
            font-weight: 600 !important;
            border-radius: 8px !important;
            font-family: 'Heebo', sans-serif !important;
            width: 100% !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            transition: all 0.16s ease !important;
        }
        div[data-testid="stColumn"]:has(.step2-role-card) button[kind="secondary"],
        div[data-testid="column"]:has(.step2-role-card) button[kind="secondary"] {
            background: #F8F7F4 !important;
            border: 1px solid #E6DFCE !important;
            color: #4A4A55 !important;
            box-shadow: none !important;
        }
        div[data-testid="stColumn"]:has(.step2-role-card) button[kind="secondary"]:hover,
        div[data-testid="column"]:has(.step2-role-card) button[kind="secondary"]:hover {
            background: #EEF2FF !important;
            border-color: #C7D2FE !important;
            color: #4F46E5 !important;
        }
        div[data-testid="stColumn"]:has(.step2-role-card) button[kind="primary"],
        div[data-testid="column"]:has(.step2-role-card) button[kind="primary"] {
            background: #4F46E5 !important;
            border: 1px solid #4338CA !important;
            color: #FFFFFF !important;
            box-shadow: 0 2px 6px rgba(79, 70, 229, 0.25) !important;
        }
        div[data-testid="stColumn"]:has(.step2-role-card) button[kind="primary"]:hover,
        div[data-testid="column"]:has(.step2-role-card) button[kind="primary"]:hover {
            background: #4338CA !important;
            border-color: #3730A3 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # ----------------------------------------------------
    # 2. בחירת תפקיד יעד (כרטיסיות מעוצבות לפי מפרט העיצוב)
    # ----------------------------------------------------
    render_clean_html(
        """
        <div style="direction: rtl; text-align: right; margin-bottom: 14px; margin-top: 6px;">
            <h3 style="color: #17171C; font-size: 19px; font-weight: 800; margin: 0; font-family: 'Heebo', sans-serif; display: flex; align-items: center; gap: 8px;">
                <span style="display: inline-flex; width: 24px; height: 24px; border-radius: 7px; background: #EDE9FE; color: #4F46E5; align-items: center; justify-content: center; font-size: 13px; font-weight: 800;">1</span>
                בחר תפקיד יעד בהייטק
            </h3>
        </div>
        """
    )

    if "selected_role_category" not in st.session_state:
        if st.session_state.target_role == "UX/UI Designer":
            st.session_state.selected_role_category = "ux_ui"
        elif st.session_state.target_role == "Frontend Developer":
            st.session_state.selected_role_category = "frontend"
        elif st.session_state.target_role == "Data Analyst":
            st.session_state.selected_role_category = "data"
        else:
            st.session_state.selected_role_category = "other"

    role_cards_data = [
        {
            "id": "ux_ui",
            "title": "מעצב/ת UX/UI",
            "role_name": "UX/UI Designer",
            "desc": "אפיון מסעות משתמש, עיצוב ממשקים ב-Figma, בניית Design Systems ומחקר שימושיות.",
            "svg": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#4F46E5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>',
        },
        {
            "id": "frontend",
            "title": "מפתח/ת Frontend",
            "role_name": "Frontend Developer",
            "desc": "פיתוח ממשקי Web מודרניים, שימוש ב-React ו-TypeScript, ארכיטקטורת רכיבים וביצועים.",
            "svg": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#4F46E5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>',
        },
        {
            "id": "data",
            "title": "אנליסט/ית נתונים",
            "role_name": "Data Analyst",
            "desc": "ניתוח תובנות עסקיות מורכבות, שאילתות SQL מתקדמות, ניתוח דאטה וויזואליזציה ב-BI.",
            "svg": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#4F46E5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>',
        },
        {
            "id": "other",
            "title": "תפקיד נוסף מהמאגר",
            "role_name": None,
            "desc": "בחירה חופשית מתוך 21 תפקידי הייטק נוספים (DevOps, QA, Cyber, Fullstack ועוד).",
            "svg": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#4F46E5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>',
        },
    ]

    col_ux, col_fe, col_da, col_ot = st.columns(4)
    cols = [col_ux, col_fe, col_da, col_ot]

    for col, rdata in zip(cols, role_cards_data):
        with col:
            is_active = (st.session_state.selected_role_category == rdata["id"])
            active_cls = "active" if is_active else ""
            card_html = f"""
            <div class="step2-role-card {active_cls}" onclick="const btn = this.closest('[data-testid*=\\'olumn\\']').querySelector('button'); if(btn) btn.click();">
                <div class="step2-role-card-header">
                    <div class="step2-role-icon-box">{rdata['svg']}</div>
                    <div class="step2-role-title">{rdata['title']}</div>
                </div>
                <div class="step2-role-desc">{rdata['desc']}</div>
            </div>
            """
            render_clean_html(card_html)
            btn_label = "✓ נבחר" if is_active else "בחר תפקיד"
            btn_type = "primary" if is_active else "secondary"
            if st.button(btn_label, key=f"btn_role_card_{rdata['id']}", type=btn_type, use_container_width=True):
                st.session_state.selected_role_category = rdata["id"]
                if rdata["role_name"]:
                    st.session_state.target_role = rdata["role_name"]
                st.rerun()

    if st.session_state.selected_role_category == "other":
        all_catalog_roles = get_all_roles()
        popular_catalog_names = ["UX/UI Designer", "Frontend Developer", "Data Analyst"]
        other_catalog_roles = [r for r in all_catalog_roles if r not in popular_catalog_names]
        selected_from_catalog = st.selectbox(
            "בחר תפקיד מתוך מאגר 21 התפקידים:",
            options=other_catalog_roles,
            index=0 if st.session_state.target_role not in other_catalog_roles else other_catalog_roles.index(st.session_state.target_role),
            key="select_other_catalog_role",
        )
        st.session_state.target_role = selected_from_catalog

    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

    # ----------------------------------------------------
    # 3. מקור נתוני המועמד (דמו מהיר / העלאת קורות חיים)
    # ----------------------------------------------------
    render_clean_html(
        """
        <div style="direction: rtl; text-align: right; margin-bottom: 14px;">
            <h3 style="color: #17171C; font-size: 19px; font-weight: 800; margin: 0; font-family: 'Heebo', sans-serif; display: flex; align-items: center; gap: 8px;">
                <span style="display: inline-flex; width: 24px; height: 24px; border-radius: 7px; background: #EDE9FE; color: #4F46E5; align-items: center; justify-content: center; font-size: 13px; font-weight: 800;">2</span>
                מקור נתוני המועמד
            </h3>
        </div>
        """
    )

    source_selection = st.radio(
        "בחר כיצד להזין את נתוני המועמד:",
        options=["פרופיל דמו מהיר (הדגמה בקליק אחד)", "העלאת קורות חיים (קובץ PDF או DOCX)"],
        index=0 if st.session_state.data_source == "demo" else 1,
        horizontal=True,
        key="radio_source_selection",
        label_visibility="collapsed",
    )

    matched_preset_id = map_role_to_preset(st.session_state.target_role)
    matched_preset = next((p for p in PRESETS if p["id"] == matched_preset_id), PRESETS[0] if PRESETS else None)

    if "פרופיל דמו מהיר" in source_selection:
        st.session_state.data_source = "demo"
        with st.container(border=True):
            if matched_preset:
                render_clean_html(
                    f"""
                    <div style="direction: rtl; text-align: right; padding: 4px 2px;">
                        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 8px;">
                            <span style="font-size: 22px;">⚡</span>
                            <strong style="color: #0F172A; font-size: 16px; font-weight: 800;">{matched_preset['title']}</strong>
                        </div>
                        <p style="color: #475569; font-size: 14px; margin: 0 0 12px 0; line-height: 1.6;">
                            {matched_preset['description']}
                        </p>
                        <div style="display: inline-flex; align-items: center; gap: 8px; background: #EDE9FE; color: #3730A3; border-radius: 9999px; padding: 5px 16px; font-size: 13px; font-weight: 700; border: 1px solid #C7D2FE;">
                            ✔ נתוני קורות החיים ודרישות המשרה מוכנים לניתוח מיידי בלחיצה אחת
                        </div>
                    </div>
                    """
                )
    else:
        st.session_state.data_source = "upload"
        with st.container(border=True):
            uploaded_file = st.file_uploader(
                "העלה קובץ קורות חיים בפורמט PDF או Word (.docx)",
                type=["pdf", "docx"],
                help="הטקסט יחולץ ישירות בזיכרון. הפרטים המזהים יטוהרו אוטומטית.",
                key="cv_file_uploader_input",
            )
            if uploaded_file is not None:
                try:
                    file_bytes = uploaded_file.read()
                    extracted_text, _ = extract_text_from_file(file_bytes, uploaded_file.name)
                    st.session_state.resume_text = extracted_text
                    st.success(f"✔ הקובץ '{uploaded_file.name}' נטען בהצלחה ({len(extracted_text)} תווים).")
                except DocumentExtractionError as err:
                    st.error(f"שגיאה בטעינת הקובץ: {err}")

            with st.expander("צפייה ועריכה של טקסט קורות החיים ותיאור המשרה (אופציונלי)", expanded=False):
                col_c1, col_c2 = st.columns(2)
                with col_c1:
                    cv_val = st.text_area(
                        "טקסט קורות החיים:",
                        value=st.session_state.resume_text,
                        height=160,
                        placeholder="הדבק כאן את טקסט קורות החיים אם לא העלית קובץ...",
                        key="direct_cv_text_area",
                    )
                    st.session_state.resume_text = cv_val
                with col_c2:
                    default_job_desc = ""
                    role_info = get_role_data(st.session_state.target_role)
                    if role_info:
                        default_job_desc = (
                            f"דרוש/ה {role_info.get('role_name', st.session_state.target_role)}.\n"
                            f"דרישות חובה: {', '.join(role_info.get('main_skills', []))}.\n"
                            f"כלים וטכנולוגיות: {', '.join(role_info.get('common_tools', []))}."
                        )
                    job_val = st.text_area(
                        "דרישות משרת היעד:",
                        value=st.session_state.job_text or default_job_desc,
                        height=160,
                        placeholder="הדבק כאן את דרישות המשרה...",
                        key="direct_job_text_area",
                    )
                    st.session_state.job_text = job_val

    st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)

    # ----------------------------------------------------
    # 3. פעולה יחידה: כפתור בולט ברוחב מלא
    # ----------------------------------------------------
    analyze_clicked = st.button(
        "נתח התאמה לתפקיד",
        type="primary",
        use_container_width=True,
        key="btn_main_analyze_role",
    )

    if analyze_clicked:
        if st.session_state.data_source == "demo":
            if matched_preset:
                st.session_state.resume_text = matched_preset["cv_text"]
                st.session_state.job_text = matched_preset["job_text"]
                st.session_state.analysis_result = JobMatchAnalysis.model_validate(matched_preset["result"])
                st.session_state.cache_hit = True
                st.session_state.app_step = 3
                st.rerun()
            else:
                st.error("לא נמצא תרחיש דמו מתאים.")
        else:
            # מצב העלאה עצמאית
            if not st.session_state.resume_text.strip():
                st.warning("⚠️ יש להעלות קובץ קורות חיים או להדביק טקסט לפני ביצוע הניתוח.")
            else:
                # מילוי דרישות משרה ברירת מחדל אם ריק
                if not st.session_state.job_text.strip():
                    role_info = get_role_data(st.session_state.target_role)
                    if role_info:
                        st.session_state.job_text = (
                            f"דרוש/ה {role_info.get('role_name', st.session_state.target_role)}.\n"
                            f"דרישות חובה: {', '.join(role_info.get('main_skills', []))}.\n"
                            f"כלים וטכנולוגיות: {', '.join(role_info.get('common_tools', []))}."
                        )
                    else:
                        st.session_state.job_text = f"דרוש/ה {st.session_state.target_role} עם מיומנויות תעשייתיות רלוונטיות."

                with st.spinner("מבצע טיהור פרטים מזהים (PII) וניתוח התאמה מול דרישות השוק..."):
                    clean_cv, _ = sanitize_pii(st.session_state.resume_text)
                    clean_job = truncate_job_description(st.session_state.job_text)

                    if st.session_state.force_mock_mode:
                        st.session_state.analysis_result = load_mock_response()
                        st.session_state.cache_hit = False
                    else:
                        cached = global_cache.get(clean_cv, clean_job)
                        if cached:
                            st.session_state.analysis_result = cached
                            st.session_state.cache_hit = True
                        else:
                            res = analyze_job_match(clean_cv, clean_job, api_key=st.session_state.gemini_api_key)
                            global_cache.set(clean_cv, clean_job, res)
                            st.session_state.analysis_result = res
                            st.session_state.cache_hit = False

                    st.session_state.app_step = 3
                    st.rerun()


# ==============================================================================
# מסך 3: לוח תוצאות (RESULTS DASHBOARD)
# ==============================================================================
elif st.session_state.app_step == 3:
    res: JobMatchAnalysis = st.session_state.analysis_result
    if not res:
        st.warning("לא נמצאו תוצאות ניתוח. חוזר לבחירת תפקיד...")
        st.session_state.app_step = 2
        st.rerun()

    # סרגל ניווט עליון
    top_col_back, top_col_role = st.columns([1.2, 3], vertical_alignment="center")
    with top_col_back:
        if st.button("⬅ חזור לבחירת תפקיד", use_container_width=True, key="btn_back_to_role_selection"):
            st.session_state.app_step = 2
            st.rerun()
    with top_col_role:
        render_clean_html(
            f"""
            <div style="direction: rtl; text-align: left; display: flex; align-items: center; justify-content: flex-end; gap: 10px;">
                <span style="font-size: 13.5px; color: #64748B; font-weight: 600;">תפקיד היעד:</span>
                <span style="background: #EDE9FE; color: #3730A3; border: 1.5px solid #C7D2FE; border-radius: 9999px; padding: 5px 18px; font-weight: 800; font-size: 14px; box-shadow: var(--md-sys-elevation-1);">
                    🎯 {st.session_state.target_role}
                </span>
            </div>
            """
        )

    st.markdown("<div style='margin-top: 14px;'></div>", unsafe_allow_html=True)

    # ----------------------------------------------------
    # 1. חיווי עליון רוחבי (KPI Header)
    # ----------------------------------------------------
    st.markdown(render_score_gauge(res.match_score, res.match_summary, theme="light"), unsafe_allow_html=True)

    if st.session_state.cache_hit:
        render_clean_html(
            """
            <div style="background: #ECFDF5; border: 1.5px solid #6EE7B7; border-radius: 9999px; padding: 5px 18px; margin-bottom: 20px; display: inline-flex; align-items: center; gap: 8px; font-size: 13px; color: #065F46; font-weight: 800; box-shadow: var(--md-sys-elevation-1);">
                ⚡ נשלף מיידית משכבת המטמון (Cache Hit)
            </div>
            """
        )

    # ----------------------------------------------------
    # 2. חלוקה ל-3 לשוניות עבודה בלבד
    # ----------------------------------------------------
    tab_gaps, tab_cv, tab_checklist = st.tabs([
        "🎯 ניתוח פערים ומסלולי למידה",
        "✍️ שדרוג קורות חיים (ATS Optimizer)",
        "📋 צ'קליסט ומעקב התקדמות ליעד (Career Progress Tracker)",
    ])

    # ----------------------------------------------------
    # לשונית א': ניתוח פערים ומסלולי למידה
    # ----------------------------------------------------
    with tab_gaps:
        col_missing, col_paths = st.columns([1, 1], gap="large")

        with col_missing:
            render_clean_html(
                """
                <div style="border-bottom: 2px solid #E2E8F0; padding-bottom: 10px; margin-bottom: 18px;">
                    <h3 style="margin: 0; color: #0F172A; font-weight: 800; font-size: 19px;">
                        🎯 מיומנויות חסרות לפי רמת חומרה
                    </h3>
                    <p style="margin: 4px 0 0 0; color: #64748B; font-size: 13.5px;">
                        הפערים הקריטיים שמונעים מקורות החיים שלך לעבור את סינון המגייסים
                    </p>
                </div>
                """
            )

            # פילוח מיומנויות חסרות לפי High, Medium, Low
            high_list = [s for s in res.missing_skills if s.importance == "High"]
            med_list = [s for s in res.missing_skills if s.importance == "Medium"]
            low_list = [s for s in res.missing_skills if s.importance == "Low"]

            if high_list:
                render_clean_html(
                    """
                    <div style="margin-bottom: 14px;">
                        <span style="font-size: 14.5px; font-weight: 800; color: #EF4444; display: flex; align-items: center; gap: 6px;">
                            🔴 פערי חובה קריטיים (Must-Have)
                        </span>
                    </div>
                    """
                )
                for s in high_list:
                    render_clean_html(
                        f"""
                        <div style="background: #FEF2F2; border: 1px solid #FECACA; border-radius: 14px; padding: 12px 18px; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center; direction: rtl; box-shadow: var(--md-sys-elevation-1);">
                            <strong style="color: #991B1B; font-size: 14.5px;">{s.skill}</strong>
                            <span style="background: #EF4444; color: #FFFFFF; padding: 3px 12px; border-radius: 9999px; font-size: 11px; font-weight: 800;">HIGH</span>
                        </div>
                        """
                    )

            if med_list:
                render_clean_html(
                    """
                    <div style="margin-top: 20px; margin-bottom: 14px;">
                        <span style="font-size: 14.5px; font-weight: 800; color: #F59E0B; display: flex; align-items: center; gap: 6px;">
                            🟡 פערים מהותיים שכדאי לגשר (Medium)
                        </span>
                    </div>
                    """
                )
                for s in med_list:
                    render_clean_html(
                        f"""
                        <div style="background: #FFFBEB; border: 1px solid #FDE68A; border-radius: 14px; padding: 12px 18px; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center; direction: rtl; box-shadow: var(--md-sys-elevation-1);">
                            <strong style="color: #92400E; font-size: 14.5px;">{s.skill}</strong>
                            <span style="background: #F59E0B; color: #FFFFFF; padding: 3px 12px; border-radius: 9999px; font-size: 11px; font-weight: 800;">MEDIUM</span>
                        </div>
                        """
                    )

            if low_list:
                render_clean_html(
                    """
                    <div style="margin-top: 20px; margin-bottom: 14px;">
                        <span style="font-size: 14.5px; font-weight: 800; color: #0284C7; display: flex; align-items: center; gap: 6px;">
                            🔵 מיומנויות יתרון ובונוס (Low)
                        </span>
                    </div>
                    """
                )
                for s in low_list:
                    render_clean_html(
                        f"""
                        <div style="background: #F0F9FF; border: 1px solid #BAE6FD; border-radius: 14px; padding: 12px 18px; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center; direction: rtl; box-shadow: var(--md-sys-elevation-1);">
                            <strong style="color: #0369A1; font-size: 14.5px;">{s.skill}</strong>
                            <span style="background: #0284C7; color: #FFFFFF; padding: 3px 12px; border-radius: 9999px; font-size: 11px; font-weight: 800;">LOW</span>
                        </div>
                        """
                    )

        with col_paths:
            render_clean_html(
                """
                <div style="border-bottom: 2px solid #E2E8F0; padding-bottom: 10px; margin-bottom: 18px;">
                    <h3 style="margin: 0; color: #0F172A; font-weight: 800; font-size: 19px;">
                        🎓 מסלולי למידה והסמכות מותאמים
                    </h3>
                    <p style="margin: 4px 0 0 0; color: #64748B; font-size: 13.5px;">
                        הסמכות וקורסים מובילים מהקטלוג לסגירת הפערים שזוהו
                    </p>
                </div>
                """
            )

            missing_skill_names = [s.skill for s in res.missing_skills]
            matched_lps = get_learning_paths_for_skills(missing_skill_names)
            st.markdown(render_learning_paths(matched_lps, theme="light"), unsafe_allow_html=True)

    # ----------------------------------------------------
    # לשונית ב': שדרוג קורות חיים (ATS Optimizer)
    # ----------------------------------------------------
    with tab_cv:
        render_clean_html(
            """
            <div style="border-bottom: 2px solid #E2E8F0; padding-bottom: 10px; margin-bottom: 18px;">
                <h3 style="margin: 0; color: #0F172A; font-weight: 800; font-size: 19px;">
                    ✍️ שדרוג סעיפי הישגים בקורות החיים (Before / After)
                </h3>
                <p style="margin: 4px 0 0 0; color: #64748B; font-size: 13.5px;">
                    הפיכת ניסוחים פסיביים לסעיפי הישגים מנצחים בשיטת Action + Scale + Impact המותאמים למסנני ה-ATS
                </p>
            </div>
            """
        )

        with st.expander("💡 טיפים קריטיים למעבר מערכות סינון ATS", expanded=False):
            st.markdown(render_ats_tip(theme="light"), unsafe_allow_html=True)

        st.markdown(render_bullet_comparison([b.model_dump() for b in res.cv_bullet_improvements], theme="light"), unsafe_allow_html=True)

    # ----------------------------------------------------
    # לשונית ג': צ'קליסט ומעקב התקדמות ליעד (Career Progress Tracker)
    # ----------------------------------------------------
    with tab_checklist:
        proj = res.portfolio_project
        milestones = generate_role_milestones(st.session_state.target_role, res.missing_skills, proj)
        total_milestones = len(milestones)

        # עדכון סטטוס המשימות שהושלמו
        completed_ids = set()
        for m in milestones:
            if st.session_state.get(f"chk_{m['id']}", False):
                completed_ids.add(m["id"])
        st.session_state.completed_milestones = completed_ids
        completed_count = len(completed_ids)

        progress_pct = int((completed_count / total_milestones) * 100) if total_milestones > 0 else 0
        base_score = res.match_score
        current_readiness = min(100, int(base_score + (100 - base_score) * (completed_count / total_milestones))) if total_milestones > 0 else base_score
        score_delta = current_readiness - base_score

        # חיווי שלב המוכנות
        if current_readiness >= 100:
            stage_label = "🎉 מוכן/ה לגיוס והגשות לשוק!"
            stage_badge_style = "background: #ECFDF5; color: #065F46; border: 1.5px solid #10B981;"
            bar_gradient = "linear-gradient(90deg, #10B981 0%, #059669 100%)"
        elif current_readiness >= 80:
            stage_label = "🔥 כמעט שם - ליטושים אחרונים"
            stage_badge_style = "background: #F0FDF4; color: #15803D; border: 1.5px solid #86EFAC;"
            bar_gradient = "linear-gradient(90deg, #34D399 0%, #10B981 100%)"
        elif current_readiness >= 65:
            stage_label = "⚡ בתהליך בנייה מתקדם"
            stage_badge_style = "background: #EDE9FE; color: #3730A3; border: 1.5px solid #C7D2FE;"
            bar_gradient = "linear-gradient(90deg, #5A45FF 0%, #4F46E5 100%)"
        else:
            stage_label = "🌱 שלב גישור פערים ראשוני"
            stage_badge_style = "background: #FFFBEB; color: #92400E; border: 1.5px solid #FCD34D;"
            bar_gradient = "linear-gradient(90deg, #F59E0B 0%, #D97706 100%)"

        # בלון חגיגי בעת הגעה ל-100%
        if current_readiness >= 100:
            if not st.session_state.get("balloons_shown", False):
                st.balloons()
                st.session_state.balloons_shown = True
        else:
            st.session_state.balloons_shown = False

        # כרטיס מד התקדמות עליון (Live Tracker Header)
        delta_pill = f'<span style="background: #ECFDF5; color: #065F46; font-size: 12px; font-weight: 800; padding: 2px 10px; border-radius: 9999px; border: 1px solid #6EE7B7; margin-right: 8px;">+{score_delta}% שיפור</span>' if score_delta > 0 else ''
        render_clean_html(
            f"""
            <div style="background: var(--md-sys-color-surface-container-lowest); border: 1px solid var(--md-sys-color-outline-variant); border-radius: var(--md-sys-shape-corner-extra-large); padding: 26px 32px; margin-bottom: 22px; box-shadow: var(--md-sys-elevation-1); direction: rtl; text-align: right;">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px; margin-bottom: 18px;">
                    <div>
                        <div style="display: flex; align-items: center; gap: 10px;">
                            <span style="font-size: 26px;">📋</span>
                            <h3 style="margin: 0; font-size: 20px; font-weight: 900; color: #0F172A;">
                                צ'קליסט ומעקב התקדמות אישי: בדרך למשרת {st.session_state.target_role}
                            </h3>
                        </div>
                        <p style="margin: 6px 0 0 0; color: #64748B; font-size: 14px; line-height: 1.5;">
                            סמן/י את אבני הדרך שהשלמת כדי לגשר על פערי המיומנויות ולהעלות את מד המוכנות לגיוס בזמן אמת.
                        </p>
                    </div>
                    <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
                        <span style="padding: 6px 18px; border-radius: 9999px; font-size: 13.5px; font-weight: 800; {stage_badge_style}">
                            {stage_label}
                        </span>
                        <span style="background: #F8FAFC; color: #0F172A; padding: 6px 18px; border-radius: 9999px; font-size: 14px; font-weight: 800; border: 1.5px solid #CBD5E1;">
                            {completed_count} מתוך {total_milestones} הושלמו ({progress_pct}%)
                        </span>
                    </div>
                </div>

                <!-- סרגל התקדמות גרפי רספונסיבי M3 Linear Indicator -->
                <div style="background: #F1F5F9; border-radius: 9999px; height: 16px; overflow: hidden; margin-bottom: 16px; border: 1px solid #E2E8F0;">
                    <div style="background: {bar_gradient}; width: {progress_pct}%; height: 100%; border-radius: 9999px; transition: width 0.6s cubic-bezier(0.2, 0.0, 0, 1.0);"></div>
                </div>

                <!-- חיווי מד מוכנות לגיוס -->
                <div style="display: flex; justify-content: space-between; align-items: center; font-size: 14px; color: #475569; flex-wrap: wrap; gap: 10px;">
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <span>מד מוכנות לגיוס מעודכן:</span>
                        <strong style="font-size: 18px; color: #0F172A;">{current_readiness}%</strong>
                        {delta_pill}
                    </div>
                    <div style="font-size: 13px; color: #94A3B8;">
                        ציון בסיס מקורי מקורות החיים: {base_score}%
                    </div>
                </div>
            </div>
            """
        )

        # באנר הצלחה וחגיגה בעת השלמת 100%
        if current_readiness >= 100:
            render_clean_html(
                f"""
                <div style="background: linear-gradient(135deg, #ECFDF5 0%, #D1FAE5 100%); border: 2px solid #34D399; border-radius: 20px; padding: 20px 26px; margin-bottom: 22px; direction: rtl; text-align: right; box-shadow: var(--md-sys-elevation-2);">
                    <div style="display: flex; align-items: center; gap: 14px;">
                        <span style="font-size: 34px;">🏆</span>
                        <div>
                            <h4 style="margin: 0; color: #065F46; font-weight: 900; font-size: 17px;">
                                כל הכבוד! הגעת ל-100% מוכנות לתפקיד {st.session_state.target_role}!
                            </h4>
                            <p style="margin: 4px 0 0 0; color: #047857; font-size: 13.5px; line-height: 1.55;">
                                סגרת בהצלחה את פערי הידע הקריטיים, שדרגת את קורות החיים ל-ATS והכנת תיק עבודות מרשים. הפרופיל שלך עומד כעת ברף הגבוה ביותר של המגייסים.
                            </p>
                        </div>
                    </div>
                </div>
                """
            )

        # כפתורי פעולה מהירים (איפוס והדגמה)
        col_act_space, col_act_demo, col_act_reset = st.columns([2, 1.5, 1], vertical_alignment="center")
        with col_act_demo:
            if st.button("✨ סמן הכל (הדגמת 100% מוכנות)", use_container_width=True, key="btn_check_all_demo"):
                for m in milestones:
                    st.session_state[f"chk_{m['id']}"] = True
                st.session_state.completed_milestones = {m["id"] for m in milestones}
                st.rerun()
        with col_act_reset:
            if st.button("🔄 אפס צ'קליסט", use_container_width=True, key="btn_reset_milestones"):
                for m in milestones:
                    st.session_state[f"chk_{m['id']}"] = False
                st.session_state.completed_milestones = set()
                st.rerun()

        st.markdown("<div style='margin-top: 16px;'></div>", unsafe_allow_html=True)

        # הצגת כרטיסי המשימות
        for idx, m in enumerate(milestones, 1):
            is_done = m["id"] in st.session_state.completed_milestones

            with st.container(border=True):
                col_chk, col_info = st.columns([0.05, 0.95], gap="small", vertical_alignment="top")

                with col_chk:
                    checked = st.checkbox(
                        label=f"סימון משימה: {m['title']}",
                        value=is_done,
                        key=f"chk_{m['id']}",
                        label_visibility="collapsed",
                    )
                    if checked != is_done:
                        if checked:
                            st.session_state.completed_milestones.add(m["id"])
                        else:
                            st.session_state.completed_milestones.discard(m["id"])
                        st.rerun()

                with col_info:
                    if is_done:
                        status_badge = '<span style="background: #ECFDF5; color: #065F46; border: 1px solid #6EE7B7; border-radius: 9999px; padding: 3px 12px; font-size: 11.5px; font-weight: 800;">✅ הושלם בהצלחה</span>'
                        title_color = "#15803D"
                    else:
                        status_badge = f'<span style="background: #F1F5F9; color: #475569; border: 1px solid #CBD5E1; border-radius: 9999px; padding: 3px 12px; font-size: 11.5px; font-weight: 700;">משימה {idx} מתוך {total_milestones}</span>'
                        title_color = "#0F172A"

                    render_clean_html(
                        f"""
                        <div style="direction: rtl; text-align: right; padding: 2px 0;">
                            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 8px;">
                                <div style="font-size: 16px; font-weight: 800; color: {title_color};">
                                    {m['title']}
                                </div>
                                <div style="display: flex; align-items: center; gap: 8px;">
                                    <span style="background: #EDE9FE; color: #3730A3; border-radius: 9999px; padding: 3px 14px; font-size: 12px; font-weight: 800; border: 1px solid #C7D2FE;">
                                        {m['category']}
                                    </span>
                                    {status_badge}
                                </div>
                            </div>
                            <p style="margin: 0 0 10px 0; color: #334155; font-size: 14px; line-height: 1.6;">
                                {m['desc']}
                            </p>
                            <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 10px; padding: 8px 16px; font-size: 13px; color: #475569; display: inline-block;">
                                {m['action_hint']}
                            </div>
                        </div>
                        """
                    )


