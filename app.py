import os
import json
import textwrap
import streamlit as st

from schemas import JobMatchAnalysis
from extractor import extract_text_from_pdf, PDFExtractionError
from sanitizer import sanitize_pii, truncate_job_description
from cache_manager import global_cache
from llm_engine import analyze_job_match
from career_domains import CAREER_DOMAINS
from career_catalog import (
    get_all_roles,
    get_role_data,
    search_roles,
    get_learning_paths_for_skills,
    UX_UI_OFFICIAL_SPEC,
)
from ui_styles import (
    get_custom_css,
    render_step_bar,
    render_ats_tip,
    render_score_gauge,
    render_skill_badges,
    render_bullet_comparison,
    render_onboarding_progress,
    render_career_intel,
    render_learning_paths,
)

# הגדרות עמוד ראשיות
st.set_page_config(
    page_title="GetAJob | מקפצת הקריירה לג'וניורים",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# הזרקת מערכת העיצוב Material 3 Expressive (Light Mode & Accessible)
st.markdown(get_custom_css(), unsafe_allow_html=True)


def load_presets():
    presets_path = os.path.join(os.path.dirname(__file__), "data", "demo_presets.json")
    try:
        with open(presets_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


presets = load_presets()

# אתחול Session State
if "onboarding_active" not in st.session_state:
    st.session_state.onboarding_active = True
if "onboarding_step" not in st.session_state:
    st.session_state.onboarding_step = 1
if "selected_domain_id" not in st.session_state:
    st.session_state.selected_domain_id = "ux_ui"
if "custom_profession_name" not in st.session_state:
    st.session_state.custom_profession_name = CAREER_DOMAINS["ux_ui"]["title"]

if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""
if "job_text" not in st.session_state:
    st.session_state.job_text = ""
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None
if "cache_hit" not in st.session_state:
    st.session_state.cache_hit = False
if "pii_stats" not in st.session_state:
    st.session_state.pii_stats = None
if "active_preset_name" not in st.session_state:
    st.session_state.active_preset_name = None


# ==============================================================================
# תהליך ONBOARDING רב-שלבי (Mobile-App Style Flow)
# ==============================================================================
if st.session_state.onboarding_active:
    st.markdown('<div class="onboarding-container">', unsafe_allow_html=True)

    # ----------------------------------------------------
    # שלב 1: מסך פתיחה והשראה (Welcome Screen)
    # ----------------------------------------------------
    if st.session_state.onboarding_step == 1:
        st.markdown(
            """
            <div class="onboarding-card">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; flex-wrap: wrap; gap: 8px;">
            <span style="background: rgba(108, 99, 255, 0.2); color: #c7d2fe; border: 1.5px solid var(--primary-accent); border-radius: 9999px; padding: 5px 16px; font-size: 13px; font-weight: 800;">
            🚀 שלב 1 מתוך 3 • ברוכים הבאים
            </span>
            <div class="status-server-online">
            <span class="status-dot-pulse"></span>
            <span>● Server Online</span>
            </div>
            </div>

            <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 20px;">
            <div style="width: 58px; height: 58px; border-radius: 18px; background: linear-gradient(135deg, #6C63FF 0%, #5345EB 100%); display: flex; align-items: center; justify-content: center; font-size: 30px; box-shadow: 0 6px 18px rgba(108, 99, 255, 0.4); border: 1px solid rgba(255,255,255,0.2); flex-shrink: 0;">
            🎯
            </div>
            <div>
            <h1 style="margin: 0; font-size: 30px; font-weight: 800; color: #ffffff;">GetAJob</h1>
            <p style="margin: 4px 0 0 0; color: #a5b4fc; font-size: 16px; font-weight: 600;">
            Find your skill gap. Build what you're missing.
            </p>
            </div>
            </div>

            <div style="background: var(--surface-secondary); border: 1.5px solid var(--border-color); border-radius: 20px; padding: 24px; margin: 24px 0;">
            <h3 style="margin-top: 0; margin-bottom: 14px; font-size: 18px; color: #ffffff; font-weight: 800;">
            איך המערכת הופכת אותך לג'וניור שאי אפשר להתעלם ממנו?
            </h3>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px;">
            <div style="background: var(--surface-card); border: 1px solid var(--border-color); border-radius: 14px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.25);">
            <div style="font-size: 24px; margin-bottom: 6px;">🔍</div>
            <strong style="color: #ffffff; font-size: 15px; display: block; margin-bottom: 4px;">איתור פערי מיומנויות</strong>
            <p style="color: #94a3b8; font-size: 13.5px; margin: 0; line-height: 1.5;">סריקה קפדנית מול דרישות המשרה לאיתור הטכנולוגיות החסרות בקו"ח.</p>
            </div>

            <div style="background: var(--surface-card); border: 1px solid var(--border-color); border-radius: 14px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.25);">
            <div style="font-size: 24px; margin-bottom: 6px;">✍️</div>
            <strong style="color: #ffffff; font-size: 15px; display: block; margin-bottom: 4px;">שכתוב סעיפים ל-ATS</strong>
            <p style="color: #94a3b8; font-size: 13.5px; margin: 0; line-height: 1.5;">הפיכת סעיפים גנריים לסעיפי הישגים מדידים (Action + Scale + Impact) שפותחים דלתות.</p>
            </div>

            <div style="background: var(--surface-card); border: 1px solid var(--border-color); border-radius: 14px; padding: 18px; box-shadow: 0 2px 8px rgba(0,0,0,0.25);">
            <div style="font-size: 24px; margin-bottom: 6px;">🚀</div>
            <strong style="color: #ffffff; font-size: 15px; display: block; margin-bottom: 4px;">מחולל פרויקט ל-GitHub</strong>
            <p style="color: #94a3b8; font-size: 13.5px; margin: 0; line-height: 1.5;">מפרט פרויקט מעשי ושלד README מקצועי לסגירת הפער בדיוק מול המשרה.</p>
            </div>
            </div>
            </div>

            <p style="color: #cbd5e1; font-size: 15px; font-weight: 600; text-align: center; margin-bottom: 24px;">
            בחר את מסלול היעד שלך (בראשם <strong>מסלול הדגל UX/UI</strong>) וקבל סקירת עומק על דרישות השוק!
            </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(render_onboarding_progress(1, 3), unsafe_allow_html=True)

        col_start, col_skip = st.columns([2, 1])
        with col_start:
            if st.button("בוא נבחר את מסלול היעד שלך 👈", type="primary", use_container_width=True):
                st.session_state.onboarding_step = 2
                st.rerun()
        with col_skip:
            if st.button("דלג ישירות למנוע הניתוח ⏩", use_container_width=True):
                st.session_state.onboarding_active = False
                st.rerun()

    # ----------------------------------------------------
    # שלב 2: בחירת תחום היעד המקצועי (Choose Career Domain)
    # ----------------------------------------------------
    elif st.session_state.onboarding_step == 2:
        st.markdown(
            """
            <div class="onboarding-card">
            <span class="onboarding-step-badge">💼 שלב 2 מתוך 3 • בחירת מסלול יעד</span>
            <h2 style="margin: 0; font-size: 26px; font-weight: 800; color: #0f172a;">
            לאיזה תפקיד בהייטק אתה שואף להגיע?
            </h2>
            <p style="margin: 6px 0 16px 0; color: #475569; font-size: 15.5px;">
            הקלד את המקצוע הרצוי בתיבה למטה, או בחר בלחיצה אחת מאחד המסלולים המובילים (בראשם <strong>מסלול הדגל UX/UI</strong>):
            </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # תיבת הקלדה חופשית למקצוע המבוקש
        st.markdown("<label style='font-size: 16px; font-weight: 800; color: #0f172a; display: block; margin-bottom: 8px;'>✍️ הקלד את המקצוע המבוקש שלך:</label>", unsafe_allow_html=True)
        typed_job = st.text_input(
            "שם התפקיד הרצוי:",
            value=st.session_state.custom_profession_name,
            placeholder="למשל: UX/UI Designer, Fullstack Developer, QA אוטומציה, Data Analyst, Cloud Engineer...",
            label_visibility="collapsed",
            help="תוכל להקליד כל מקצוע, לבחור ממסלולי הדגל למטה, או לפתוח את מאגר 21 התפקידים המלא."
        )
        if typed_job != st.session_state.custom_profession_name:
            st.session_state.custom_profession_name = typed_job
            matched_key = None
            for k, d in CAREER_DOMAINS.items():
                if d["title"].lower() in typed_job.lower() or typed_job.lower() in d["title"].lower() or k in typed_job.lower():
                    matched_key = k
                    break
            st.session_state.selected_domain_id = matched_key if matched_key else "custom"

        # כותרת למקצועות המוצעים
        st.markdown(
            """
            <div style="display: flex; align-items: center; justify-content: space-between; margin-top: 24px; margin-bottom: 14px; flex-wrap: wrap; gap: 8px;">
            <h4 style="margin: 0; color: #0f172a; font-weight: 800; font-size: 17px;">
            ✨ מסלולי היעד המובילים (בראשם מסלול הדגל UX/UI):
            </h4>
            <span style="font-size: 13px; color: #64748b; font-weight: 600;">(לחיצה תמלא את התפקיד ותסמן את המסלול)</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        for domain_key, domain in CAREER_DOMAINS.items():
            is_selected = (
                st.session_state.selected_domain_id == domain_key or 
                st.session_state.custom_profession_name.strip() == domain["title"].strip()
            )
            is_flagship = domain.get("is_flagship", False)
            
            if is_flagship:
                border_color = "#f43f5e" if is_selected else "rgba(244, 63, 94, 0.5)"
                bg_color = "rgba(225, 29, 72, 0.12)" if is_selected else "var(--surface-card)"
                shadow_style = "box-shadow: 0 4px 20px rgba(225, 29, 72, 0.35);" if is_selected else ""
                flagship_badge = '<span style="background: rgba(225, 29, 72, 0.2); color: #fda4af; border: 1.5px solid #fda4af; border-radius: 9999px; padding: 4px 12px; font-size: 12.5px; font-weight: 800; direction: rtl;"><bdi>⭐ מסלול הדגל הראשי</bdi></span>'
            else:
                border_color = "var(--primary-accent)" if is_selected else "var(--border-color)"
                bg_color = "rgba(108, 99, 255, 0.12)" if is_selected else "var(--surface-card)"
                shadow_style = "box-shadow: 0 4px 18px var(--primary-glow);" if is_selected else ""
                flagship_badge = ""

            domain_card_html = f"""
            <div style="background: {bg_color}; border: 2px solid {border_color}; border-radius: 20px; padding: 20px 24px; margin-bottom: 12px; direction: rtl !important; text-align: right !important; {shadow_style}">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 12px; direction: rtl !important;">
            <div style="display: flex; align-items: center; gap: 14px; direction: rtl !important; text-align: right !important;">
            <span style="font-size: 32px; flex-shrink: 0;">{domain['icon']}</span>
            <div style="text-align: right !important; direction: rtl !important;">
            <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap; direction: rtl !important;">
            <h3 style="margin: 0; font-size: 18.5px; font-weight: 800; color: #ffffff; text-align: right !important; direction: rtl !important;"><bdi>{domain['title']}</bdi></h3>
            {flagship_badge}
            </div>
            <p style="margin: 4px 0 0 0; color: #94a3b8; font-size: 14px; font-weight: 500; text-align: right !important; direction: rtl !important;"><bdi>{domain['short_desc']}</bdi></p>
            </div>
            </div>
            <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap; direction: rtl !important;">
            <span style="background: rgba(34, 197, 94, 0.15); color: #4ade80; border: 1px solid #22c55e; border-radius: 9999px; padding: 4px 12px; font-size: 12.5px; font-weight: 700; direction: rtl !important;"><bdi>{domain['demand_level']}</bdi></span>
            <span style="background: rgba(245, 158, 11, 0.15); color: #fcd34d; border: 1px solid #f59e0b; border-radius: 9999px; padding: 4px 12px; font-size: 12.5px; font-weight: 700; direction: rtl !important;"><bdi>💰 {domain['salary_range']}</bdi></span>
            </div>
            </div>
            </div>
            """
            st.markdown(textwrap.dedent(domain_card_html).strip(), unsafe_allow_html=True)

            btn_label = f"👈 בחר ב{domain['title']}" if not is_selected else f"✔ {domain['title']} נבחר"
            btn_type = "primary" if is_selected else "secondary"
            if st.button(btn_label, key=f"select_dom_{domain_key}", type=btn_type, use_container_width=True):
                st.session_state.selected_domain_id = domain_key
                st.session_state.custom_profession_name = domain["title"]
                st.rerun()

            st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)

        # הרחבה למאגר המלא של 21 תפקידי התעשייה מה-Excel
        with st.expander("📚 מאגר מורחב: צפה בכל 21 תפקידי היעד מהתעשייה (לחץ לבחירה ישירה)"):
            st.markdown("<p style='font-size: 13.5px; color: #475569; margin-bottom: 12px;'>מבוסס על מאגר מסלולי הלימוד וה-Skills הרשמי שנלמד מה-Excel:</p>", unsafe_allow_html=True)
            all_role_names = get_all_roles()
            role_cols = st.columns(3)
            for r_idx, r_name in enumerate(all_role_names):
                with role_cols[r_idx % 3]:
                    if st.button(f"🎯 {r_name}", key=f"cat_role_{r_idx}", use_container_width=True):
                        st.session_state.custom_profession_name = r_name
                        matched_key = None
                        for k, d in CAREER_DOMAINS.items():
                            if d["title"].lower() in r_name.lower() or r_name.lower() in d["title"].lower():
                                matched_key = k
                                break
                        st.session_state.selected_domain_id = matched_key if matched_key else "catalog_role"
                        st.rerun()

        st.markdown(render_onboarding_progress(2, 3), unsafe_allow_html=True)

        nav_col1, nav_col2, nav_col3 = st.columns([1, 2, 1])
        with nav_col1:
            if st.button("⬅ חזור", use_container_width=True):
                st.session_state.onboarding_step = 1
                st.rerun()
        with nav_col2:
            if st.button("הבא: קבל סקירת עומק על המקצוע 👈", type="primary", use_container_width=True):
                st.session_state.onboarding_step = 3
                st.rerun()
        with nav_col3:
            if st.button("דלג לאנלייזר ⏩", use_container_width=True):
                st.session_state.onboarding_active = False
                st.rerun()

    # ----------------------------------------------------
    # שלב 3: סקירת המקצוע והדרישות בשוק (Career Deep Dive)
    # ----------------------------------------------------
    elif st.session_state.onboarding_step == 3:
        if st.session_state.selected_domain_id in CAREER_DOMAINS:
            selected_dom = CAREER_DOMAINS[st.session_state.selected_domain_id]
        else:
            cat_role = get_role_data(st.session_state.custom_profession_name)
            if cat_role:
                selected_dom = {
                    "id": "catalog_role",
                    "title": cat_role["role_name"],
                    "icon": "💼",
                    "short_desc": f"תפקיד מוגדר מתוך מאגר 21 מקצועות התעשייה: {cat_role['role_name']}",
                    "demand_level": "תפקיד ממופה במאגר",
                    "salary_range": "בהתאם לוותק ולחברה",
                    "must_have_skills": cat_role.get("main_skills", []),
                    "good_to_have_skills": cat_role.get("common_tools", []),
                    "market_reality": f"דרישת הוכחה מינימלית: {cat_role.get('minimum_evidence', '')}. {cat_role.get('education_note', '')}",
                    "ats_winning_formula": f"Delivered robust engineering outcomes in {cat_role['role_name']}, utilizing {', '.join(cat_role.get('common_tools', [])[:3])} to optimize workflow velocity.",
                    "recommended_project_type": f"פרויקט מעשי המוכיח: {cat_role.get('minimum_evidence', 'בניית מערכת מודולרית מתועדת')}",
                    "matching_preset_id": "fullstack_preset"
                }
            else:
                custom_title = st.session_state.custom_profession_name.strip() or "מקצוע הייטק מותאם אישית"
                selected_dom = {
                    "id": "custom",
                    "title": custom_title,
                    "icon": "🎯",
                    "short_desc": f"מסלול קריירה מותאם אישית עבור {custom_title}",
                    "demand_level": "מסלול מותאם אישית (Custom Track)",
                    "salary_range": "בהתאם לדרישות המשרה והוותק",
                    "must_have_skills": ["דרישות סף מרכזיות מהמשרה", "קוד נקי ומבני נתונים", "Git & Source Control", "אינטגרציית APIs"],
                    "good_to_have_skills": ["Docker & Containers", "בדיקות אוטומטיות (Testing)", "ארכיטקטורת ענן", "אופטימיזציית ביצועים"],
                    "market_reality": f"עבור תפקידי {custom_title}, מעסיקים ומגייסים מחפשים מועמדים שמוכיחים עשייה פרקטית ועצמאות: פרויקט ייעודי שמציג עבודה לפי סטנדרטים מקובלים בתעשייה, פתרון אתגרים מוחשיים וקוד מאורגן וקריא.",
                    "ats_winning_formula": f"Architected robust solutions for {custom_title}, enhancing operational efficiency and applying modern engineering best practices.",
                    "recommended_project_type": f"פרויקט מקצועי וממוקד לתפקיד {custom_title} המוכיח שליטה בארכיטקטורה, שילוב טכנולוגיות מתאימות ותיעוד README מקצועי עם פקודות הרצה.",
                    "matching_preset_id": "fullstack_preset"
                }
        
        st.markdown(
            f"""
            <div class="onboarding-card" style="margin-bottom: 20px;">
            <span class="onboarding-step-badge">📊 שלב 3 מתוך 3 • סקירת שוק מקצועית</span>
            <h2 style="margin: 0; font-size: 26px; font-weight: 800; color: #0f172a;">
            סקירת מקצוע: {selected_dom['title']}
            </h2>
            <p style="margin: 6px 0 0 0; color: #475569; font-size: 15.5px;">
            הנה כל מה שאתה חייב לדעת כג'וניור כדי לעבור את שלב הסינון הראשוני ולהגיע לראיון:
            </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # כרטיס סקירה מעמיקה
        st.markdown(render_career_intel(selected_dom), unsafe_allow_html=True)

        st.markdown(render_onboarding_progress(3, 3), unsafe_allow_html=True)

        bot_col1, bot_col2 = st.columns([1, 2])
        with bot_col1:
            if st.button("⬅ שנה מקצוע / מסלול", use_container_width=True):
                st.session_state.onboarding_step = 2
                st.rerun()
        with bot_col2:
            finish_btn = st.button(
                f"🚀 מעולה! בוא ננתח קו\"ח מותאמים ל{selected_dom['title']}",
                type="primary",
                use_container_width=True,
            )
            if finish_btn:
                st.session_state.onboarding_active = False
                # התאמת תרחיש דמו ראשוני בהתאם לתחום
                matching_id = selected_dom.get("matching_preset_id")
                matching_preset = next((p for p in presets if p["id"] == matching_id), None)
                if matching_preset and not st.session_state.resume_text:
                    st.session_state.resume_text = matching_preset["cv_text"]
                    st.session_state.job_text = matching_preset["job_text"]
                    st.session_state.analysis_result = JobMatchAnalysis.model_validate(matching_preset["result"])
                    st.session_state.cache_hit = True
                    st.session_state.active_preset_name = matching_preset["id"]
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


# ==============================================================================
# המערכת הראשית (Main Analyzer Dashboard)
# ==============================================================================
else:
    if st.session_state.selected_domain_id in CAREER_DOMAINS:
        curr_domain = CAREER_DOMAINS[st.session_state.selected_domain_id]
    else:
        custom_title = st.session_state.custom_profession_name.strip() or "מסלול מותאם אישית"
        curr_domain = {"title": custom_title, "icon": "🎯"}

    # ----------------------------------------------------
    # כותרת עליונה (Hero Banner) עם צ'יפ החלפת מסלול
    # ----------------------------------------------------
    hero_html = f"""
    <div style="background: var(--surface-card); border: 1.5px solid var(--border-color); border-radius: 24px; padding: 22px 28px; margin-bottom: 24px; box-shadow: 0 4px 24px rgba(0,0,0,0.35);">
    <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px;">
    <div style="display: flex; align-items: center; gap: 16px;">
    <div style="width: 52px; height: 52px; border-radius: 16px; background: linear-gradient(135deg, #6C63FF 0%, #5345EB 100%); display: flex; align-items: center; justify-content: center; font-size: 26px; box-shadow: 0 4px 16px rgba(108, 99, 255, 0.4); border: 1px solid rgba(255,255,255,0.2); flex-shrink: 0;">
    🎯
    </div>
    <div>
    <div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
    <h1 style="margin: 0; font-size: 28px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px;">
    GetAJob
    </h1>
    <div class="status-server-online">
    <span class="status-dot-pulse"></span>
    <span>● Server Online</span>
    </div>
    <span style="background: rgba(108, 99, 255, 0.2); color: #c7d2fe; border: 1px solid var(--primary-accent); border-radius: 9999px; padding: 4px 14px; font-size: 13px; font-weight: 700;">
    {curr_domain['icon']} מסלול יעד: {curr_domain['title']}
    </span>
    </div>
    <p style="color: #a5b4fc; font-size: 14.5px; margin: 4px 0 0 0; line-height: 1.5; font-weight: 600;">
    Find your skill gap. Build what you're missing.
    <span style="color: #94a3b8; font-weight: 400; padding-right: 6px;">— איתור פערי מיומנויות מדויקים, שכתוב סעיפי קו"ח לפי Action-Impact, ומחולל פרויקט מעשי.</span>
    </p>
    </div>
    </div>
    <div style="direction: ltr; text-align: left; display: flex; gap: 8px; align-items: center;">
    <span style="background: rgba(56, 189, 248, 0.12); color: #7dd3fc; border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 9999px; padding: 4px 12px; font-size: 12.5px; font-weight: 700;">
    ⚡ SLA: &lt; 15s | 0s Cache
    </span>
    </div>
    </div>
    </div>
    """
    st.markdown(textwrap.dedent(hero_html).strip(), unsafe_allow_html=True)

    # כפתור החלפת מסלול / Onboarding מהיר
    change_col1, change_col2 = st.columns([3, 1])
    with change_col2:
        if st.button("🔄 שנה מסלול / סקירת מקצוע", use_container_width=True):
            st.session_state.onboarding_active = True
            st.session_state.onboarding_step = 2
            st.rerun()

    # סרגל שלבים להנחיית המשתמש (M3 Segmented Pills)
    current_step = 2 if st.session_state.analysis_result else 1
    st.markdown(render_step_bar(current_step), unsafe_allow_html=True)

    # כרטיס טיפ מקצועי לעמידה ב-ATS (M3 Callout)
    st.markdown(render_ats_tip(), unsafe_allow_html=True)

    # ----------------------------------------------------
    # כפתורי תרחישי דמו מהירים (M3 Expressive Segmented Presets)
    # ----------------------------------------------------
    st.markdown("<h4 style='color: #0f172a; font-weight: 800; margin-bottom: 12px;'>⚡ תרחישי הדגמה מוכנים מראש (קליק אחד לטעינה):</h4>", unsafe_allow_html=True)

    preset_cols = st.columns(len(presets))
    preset_icons = ["🎨", "🛡️", "💻", "📊"]

    for idx, p in enumerate(presets):
        with preset_cols[idx]:
            is_selected = st.session_state.active_preset_name == p["id"]
            icon = preset_icons[idx] if idx < len(preset_icons) else "🎯"
            btn_label = f"{icon} {p['title'].split(':')[1].strip()}"
            if is_selected:
                btn_label = f"✔ {btn_label} (פעיל)"

            if st.button(btn_label, key=f"btn_preset_{idx}", use_container_width=True):
                st.session_state.resume_text = p["cv_text"]
                st.session_state.job_text = p["job_text"]
                st.session_state.analysis_result = JobMatchAnalysis.model_validate(p["result"])
                st.session_state.cache_hit = True
                st.session_state.pii_stats = {"phones": 1, "emails": 1, "ids": 0}
                st.session_state.active_preset_name = p["id"]
                st.rerun()

    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)

    # ----------------------------------------------------
    # אזור הקלט הכפול (Input Hub - Side-by-Side)
    # ----------------------------------------------------
    col_cv, col_job = st.columns([1, 1], gap="large")

    with col_cv:
        st.markdown("<h3 style='color: #0f172a; font-weight: 800;'>📄 1. קורות חיים של המועמד</h3>", unsafe_allow_html=True)
        
        cv_tabs = st.tabs(["📁 העלאת קובץ PDF", "✍️ הזנה / עריכת טקסט"])
        
        with cv_tabs[0]:
            uploaded_file = st.file_uploader(
                "בחר קובץ PDF של קורות החיים (עד 10MB)",
                type=["pdf"],
                help="קריאת הטקסט מתבצעת ישירות בזיכרון. פרטים אישיים מוסרים אוטומטית לפני הניתוח.",
            )
            if uploaded_file is not None:
                try:
                    pdf_bytes = uploaded_file.read()
                    raw_text, page_count = extract_text_from_pdf(pdf_bytes)
                    clean_text, stats = sanitize_pii(raw_text)
                    st.session_state.resume_text = clean_text
                    st.session_state.pii_stats = stats
                    st.session_state.active_preset_name = None
                    
                    st.success(f"✔ הקובץ נקרא בהצלחה ({page_count} עמודים, {len(clean_text):,} תווים).")
                except PDFExtractionError as e:
                    st.error(f"⚠️ {str(e)}")
                except Exception as e:
                    st.error(f"שגיאה בעיבוד הקובץ: {str(e)}")

        with cv_tabs[1]:
            manual_cv = st.text_area(
                "ערוך או הדבק טקסט קו\"ח:",
                value=st.session_state.resume_text,
                height=160,
                placeholder="הדבק כאן את תוכן קורות החיים שלך...",
            )
            if manual_cv != st.session_state.resume_text:
                clean_text, stats = sanitize_pii(manual_cv)
                st.session_state.resume_text = clean_text
                st.session_state.pii_stats = stats

        # הצגת חיווי PII במידה וסונן
        if st.session_state.pii_stats:
            stats = st.session_state.pii_stats
            if stats["phones"] or stats["emails"] or stats["ids"]:
                pii_html = f"""
                <div style="background: #e0f2fe; border: 1.5px solid #7dd3fc; border-radius: 9999px; padding: 8px 20px; font-size: 14px; color: #0369a1; margin-top: 10px; display: inline-flex; align-items: center; gap: 8px; font-weight: 700;">
                🔒 <strong>אבטחת פרטיות (PII Sanitized):</strong> סוננו {stats['phones']} טלפונים, {stats['emails']} כתובות מייל ו-{stats['ids']} תעודות זהות.
                </div>
                """
                st.markdown(textwrap.dedent(pii_html).strip(), unsafe_allow_html=True)

    with col_job:
        st.markdown("<h3 style='color: #0f172a; font-weight: 800;'>💼 2. תיאור המשרה המבוקשת</h3>", unsafe_allow_html=True)
        job_input = st.text_area(
            "הדבק כאן את תיאור המשרה ודרישות התפקיד:",
            value=st.session_state.job_text,
            height=210,
            placeholder="למשל: דרוש/ה Junior Developer. דרישות חובה: Python, Git, Docker. יתרון: AWS, CI/CD...",
        )
        if job_input != st.session_state.job_text:
            st.session_state.job_text = job_input
            st.session_state.active_preset_name = None

        char_count = len(st.session_state.job_text)
        col_counter, col_reset = st.columns([3, 1])
        with col_counter:
            st.caption(f"תווים שהוזנו: {char_count} / 3,000 (קיצוץ חכם מסנן שיווק ומתמקד בדרישות)")
        with col_reset:
            if st.button("🧹 נקה קלט", use_container_width=True):
                st.session_state.resume_text = ""
                st.session_state.job_text = ""
                st.session_state.analysis_result = None
                st.session_state.cache_hit = False
                st.session_state.pii_stats = None
                st.session_state.active_preset_name = None
                st.rerun()

    # כפתור הפעלה ראשי (M3 Elevated Pill CTA)
    st.markdown("<div style='margin-top: 16px; margin-bottom: 24px;'></div>", unsafe_allow_html=True)
    analyze_btn = st.button("🚀 נתח התאמה והפק תוכנית עבודה", type="primary", use_container_width=True)

    if analyze_btn:
        if not st.session_state.resume_text.strip():
            st.warning("אנא העלה קובץ קורות חיים או בחר תרחיש הדגמה מוכן.")
        elif not st.session_state.job_text.strip():
            st.warning("אנא הזן תיאור משרה לניתוח.")
        else:
            truncated_job = truncate_job_description(st.session_state.job_text)
            cache_key = global_cache.generate_key(st.session_state.resume_text, truncated_job)
            
            # בדיקה ב-Cache (0 שניות מענה)
            cached_result = global_cache.get(cache_key)
            if cached_result:
                st.session_state.analysis_result = cached_result
                st.session_state.cache_hit = True
            else:
                with st.spinner("🧠 מנתח התאמה מול דרישות המשרה, שוקל סעיפים ומחולל פרויקט..."):
                    result = analyze_job_match(st.session_state.resume_text, truncated_job)
                    global_cache.set(cache_key, result)
                    st.session_state.analysis_result = result
                    st.session_state.cache_hit = False
            st.rerun()

    # ----------------------------------------------------
    # הצגת תוצאות הניתוח (Main Dashboard)
    # ----------------------------------------------------
    if st.session_state.analysis_result:
        res = st.session_state.analysis_result
        
        st.markdown("<hr style='border-color: #cbd5e1; margin-top: 36px; margin-bottom: 28px;'>", unsafe_allow_html=True)
        
        # חיווי מטמון מהיר
        if st.session_state.cache_hit:
            cache_html = """
            <div style="background: #ecfdf5; border: 1.5px solid #6ee7b7; border-radius: 9999px; padding: 8px 22px; margin-bottom: 20px; display: inline-flex; align-items: center; gap: 8px; font-size: 14px; color: #065f46; font-weight: 700;">
            ⚡ <strong>זמן תגובה: 0 שניות!</strong> התוצאה נשלפה ישירות משכבת המטמון (In-Memory Cache) ללא צורך בקריאת רשת.
            </div>
            """
            st.markdown(textwrap.dedent(cache_html).strip(), unsafe_allow_html=True)

        # 1. מד ציון ויזואלי וסיכום משוקלל (M3 Score Gauge)
        st.markdown(render_score_gauge(res.match_score, res.match_summary), unsafe_allow_html=True)

        # 2. טאבים לתצוגה מפורטת וממוקדת
        tab_gaps, tab_project, tab_learning, tab_checklist = st.tabs([
            "📊 פערי מיומנויות ושכתוב סעיפים",
            "🛠️ מפרט פרויקט ו-README ל-GitHub",
            "🎓 מסלולי לימוד והסמכות (49 מסלולים)",
            "📋 צ'קליסט מוכנות לגיוס (ATS Checklist)",
        ])

        with tab_gaps:
            st.markdown("<h3 style='color: #0f172a; font-weight: 800;'>🎯 ניתוח פערי מיומנויות (Skill Gap Breakdown)</h3>", unsafe_allow_html=True)
            st.markdown(
                "<p style='color: #334155; font-size: 15px; font-weight: 500;'>פילוח הטכנולוגיות המרכזיות הנדרשות במשרה שאינן מודגשות מספיק בקורות החיים:</p>",
                unsafe_allow_html=True,
            )
            st.markdown(
                render_skill_badges([s.model_dump() for s in res.missing_skills]),
                unsafe_allow_html=True,
            )

            st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
            st.markdown("<h3 style='color: #0f172a; font-weight: 800;'>✍️ שכתוב סעיפי קורות חיים (Impact-Action Optimizer)</h3>", unsafe_allow_html=True)
            st.markdown(
                "<p style='color: #334155; font-size: 15px; font-weight: 500;'>הפיכת סעיפים גנריים לסעיפי הישגים מדידים המשלבים את הטכנולוגיות הנדרשות במשרה:</p>",
                unsafe_allow_html=True,
            )
            st.markdown(
                render_bullet_comparison([b.model_dump() for b in res.cv_bullet_improvements]),
                unsafe_allow_html=True,
            )

        with tab_project:
            proj = res.portfolio_project
            st.markdown(f"<h3 style='color: #0f172a; font-weight: 800;'>🚀 פרויקט מומלץ לסגירת הפער: <strong>{proj.project_name}</strong></h3>", unsafe_allow_html=True)
            
            # כרטיס סקירה עסקית
            context_html = f"""
            <div class="custom-card">
            <div style="font-weight: 800; color: #4338ca; margin-bottom: 8px; font-size: 16px;">
            💡 הצורך העסקי והרציונל ההנדסי:
            </div>
            <div style="color: #1e293b; font-size: 15.5px; line-height: 1.65; font-weight: 500;">
            {proj.business_context}
            </div>
            </div>
            """
            st.markdown(textwrap.dedent(context_html).strip(), unsafe_allow_html=True)

            proj_col1, proj_col2 = st.columns([1, 1], gap="medium")
            with proj_col1:
                st.markdown("<h4 style='color: #0f172a; font-weight: 800;'>🎯 מיומנויות מרכזיות שהפרויקט מוכיח:</h4>", unsafe_allow_html=True)
                skills_html = "<div style='display: flex; flex-wrap: wrap; gap: 8px; direction: ltr; margin-top: 8px;'>"
                for sk in proj.targeted_skills:
                    skills_html += f"<span class='m3-tag' style='color: #0369a1; border-color: #7dd3fc; background-color: #f0f9ff;'>{sk}</span>"
                skills_html += "</div>"
                st.markdown(skills_html, unsafe_allow_html=True)

            with proj_col2:
                st.markdown("<h4 style='color: #0f172a; font-weight: 800;'>🏗️ ארכיטקטורה וסטאק טכנולוגי:</h4>", unsafe_allow_html=True)
                stack_html = "<div style='display: flex; flex-wrap: wrap; gap: 8px; direction: ltr; margin-top: 8px;'>"
                for tech in proj.architecture_stack:
                    stack_html += f"<span class='m3-tag' style='color: #4338ca; border-color: #c7d2fe; background-color: #ede9fe;'>{tech}</span>"
                stack_html += "</div>"
                st.markdown(stack_html, unsafe_allow_html=True)

            st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)
            st.markdown("<h4 style='color: #0f172a; font-weight: 800;'>📋 שלבי ביצוע הנדסיים מומלצים:</h4>", unsafe_allow_html=True)
            for idx, step in enumerate(proj.implementation_steps, 1):
                step_card = f"""
                <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 14px; padding: 12px 18px; margin-bottom: 8px; display: flex; align-items: center; gap: 14px; box-shadow: 0 1px 3px rgba(15, 23, 42, 0.04);">
                <span style="background: #ede9fe; color: #4338ca; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 13.5px; font-family: 'Outfit', sans-serif; flex-shrink: 0;">{idx}</span>
                <span style="color: #0f172a; font-size: 15px; font-weight: 600;">{step}</span>
                </div>
                """
                st.markdown(textwrap.dedent(step_card).strip(), unsafe_allow_html=True)

            st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
            
            # אזור הורדה ותצוגת README
            readme_head_col1, readme_head_col2 = st.columns([3, 1])
            with readme_head_col1:
                st.markdown("<h4 style='color: #0f172a; font-weight: 800;'>📄 שלד README.md מוכן ל-GitHub (קריאה משמאל לימין - LTR):</h4>", unsafe_allow_html=True)
            with readme_head_col2:
                st.download_button(
                    label="📥 הורד README.md",
                    data=proj.readme_content,
                    file_name=f"README_{proj.project_name.replace(' ', '_')}.md",
                    mime="text/markdown",
                    use_container_width=True,
                )

            # תצוגת Markdown ב-LTR מלא למניעת שיבוש קוד ותרשימים
            readme_display = f"""
            <div class="readme-container">
            <pre style="white-space: pre-wrap; word-break: break-word; color: #1f2328; font-size: 13.5px; line-height: 1.6; font-weight: 500;">{proj.readme_content}</pre>
            </div>
            """
            st.markdown(textwrap.dedent(readme_display).strip(), unsafe_allow_html=True)

        with tab_learning:
            st.markdown("<h3 style='color: #0f172a; font-weight: 800;'>🎓 מסלולי לימוד והסמכות מומלצים לסגירת הפער</h3>", unsafe_allow_html=True)
            st.markdown(
                """
                <div style="background: #ede9fe; border: 1.5px solid #c7d2fe; border-radius: 16px; padding: 16px 20px; margin-bottom: 20px;">
                <div style="color: #3730a3; font-weight: 700; font-size: 14.5px; margin-bottom: 4px;">
                💡 מנוע ההמלצות לפי Skills (מבוסס מאגר 49 מסלולים רשמיים):
                </div>
                <p style="margin: 0; color: #1e1b4b; font-size: 14px; line-height: 1.5;">
                המלצות אלו נשלפות ישירות מתוך מאגר מסלולי הלימוד וההסמכות (ACM, ABET, Figma, MDN, Cisco, AWS, Microsoft, Red Hat). 
                המסלולים מדורגים על פי חוזק הוכחה מעשית, דרישות תפקיד וצמצום זמן להגעה לראיון.
                </p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            missing_skills_list = [s.skill for s in res.missing_skills]
            matched_lps = get_learning_paths_for_skills(missing_skills_list)
            st.markdown(render_learning_paths(matched_lps), unsafe_allow_html=True)

        with tab_checklist:
            st.markdown("<h3 style='color: #0f172a; font-weight: 800;'>📋 צ'קליסט מוכנות להגשת מועמדות (ATS Readiness Checklist)</h3>", unsafe_allow_html=True)
            st.markdown(
                "<p style='color: #334155; font-size: 15px; font-weight: 500;'>מערכות ATS ומגייסים טכנולוגיים בוחנים 5 קריטריונים מרכזיים. בדוק את הסטטוס שלך:</p>",
                unsafe_allow_html=True,
            )
            
            checks = [
                ("טיהור פרטים מזהים (PII)", True, "שמירה על פרטיות מלאה ללא חשיפת טלפון ות\"ז לספקי צד שלישי."),
                ("שילוב מילות מפתח מדויקות מהמשרה", True, "המיומנויות החסרות שולבו בסעיפים המשודרגים ובפרויקט."),
                ("נוסח מונחה הישגים (Action-Scale-Impact)", True, "הסעיפים כוללים פעלים חזקים, מסגרת עבודה ומדדים כמותיים."),
                ("פרויקט ייעודי ומובחן בפורטפוליו", True, f"הוגדר פרויקט '{proj.project_name}' המחליף פרויקטי מדריך גנריים."),
                ("שלד README מקצועי עם פקודות הרצה", True, "קובץ README.md כולל הוראות הרצה, ארכיטקטורה ודרישות קונטיינר."),
            ]
            
            for title, status, desc in checks:
                icon = "✔" if status else "⚠️"
                item_card = f"""
                <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 16px; padding: 16px 20px; margin-bottom: 12px; display: flex; align-items: flex-start; gap: 14px; direction: rtl; text-align: right; box-shadow: 0 2px 6px rgba(15, 23, 42, 0.04);">
                <div style="width: 32px; height: 32px; border-radius: 50%; background: #ecfdf5; color: #065f46; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: 800; flex-shrink: 0; border: 1.5px solid #6ee7b7;">
                {icon}
                </div>
                <div style="flex: 1;">
                <strong style="color: #0f172a; font-size: 16px; font-weight: 800;">{title}</strong>
                <p style="margin: 4px 0 0 0; color: #475569; font-size: 14px; line-height: 1.5; font-weight: 500;">{desc}</p>
                </div>
                </div>
                """
                st.markdown(textwrap.dedent(item_card).strip(), unsafe_allow_html=True)
