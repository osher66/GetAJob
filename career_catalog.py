"""
career_catalog.py - מנוע מאגר תפקידים, Skills ומסלולי לימוד
מבוסס על 'מאגר_מסלולי_לימוד_לפי_Skills.xlsx' ו-'מאגר דרישות וכישורים למשרות UX UI.docx'.
"""

import os
import json
from typing import List, Dict, Any, Optional

CATALOG_PATH = os.path.join(os.path.dirname(__file__), "data", "career_catalog.json")

def _load_catalog() -> Dict[str, Any]:
    try:
        with open(CATALOG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"learning_paths": [], "skills": {}, "roles": {}}

_CATALOG = _load_catalog()

# מפרט עומק מלא למשרות UX/UI מתוך הקובץ הרשמי
UX_UI_OFFICIAL_SPEC = {
    "role_name": "UX/UI Designer",
    "title_he": "מעצב/ת חוויית וממשק משתמש (UX/UI Designer)",
    "is_flagship": False,
    "tools": {
        "must_have": [
            {"name": "Figma", "note": "הכלי השולט כיום בשוק (חובה כמעט בכל משרה)"},
            {"name": "Sketch", "note": "נפוץ בצוותים וארגונים ותיקים"}
        ],
        "nice_to_have": [
            {"name": "Adobe XD", "note": "נפוץ בסביבות Adobe"},
            {"name": "Axure", "note": "אפיון מורכב ומערכות Enterprise"},
            {"name": "InVision", "note": "שיתוף והצגת אב-טיפוס"},
            {"name": "Balsamiq", "note": "אפיון Low-Fidelity ו-Wireframes ראשוניים"}
        ],
        "scan_keywords": ["UI Design", "Prototyping", "Mockups", "Wireframing"]
    },
    "research_and_analytics": {
        "must_have": [
            {"name": "User Research", "name_he": "מחקר משתמשים", "note": "ראיונות, סקרים והבנת צרכים"},
            {"name": "Usability Testing", "name_he": "בדיקות שמישות", "note": "העברת משתמשים במשימות ואיתור נקודות חסימה"}
        ],
        "nice_to_have": [
            {"name": "A/B Testing", "note": "ולידציה כמותית של עיצובים שונים"},
            {"name": "Hotjar / CrazyEgg", "note": "כלי מפות חום והקלטות משתמשים"},
            {"name": "Google Analytics", "note": "ניתוח נתוני תנועה, יחסי המרה ונטישה"}
        ],
        "scan_keywords": ["UX Strategy", "User Flows", "Personas", "Customer Journey", "Information Architecture (IA)"]
    },
    "visual_and_ui": {
        "must_have": [
            {"name": "Typography", "name_he": "טיפוגרפיה", "note": "היררכיה, קריאות, משקלים ומרווחי שורות"},
            {"name": "Color Theory", "name_he": "תורת הצבעים", "note": "ניגודיות נגישה (WCAG), פלטות הרמוניות והקשר רגשי"},
            {"name": "Layouts & Grids", "name_he": "גריד ופריסות", "note": "מערכות 8pt grid, יישור וריווח עקבי"}
        ],
        "nice_to_have": [
            {"name": "Motion Design", "name_he": "עיצוב בתנועה", "note": "מיקרו-אינטראקציות ומעברים"},
            {"name": "After Effects", "note": "אנימציות מתקדמות"},
            {"name": "Lottie", "note": "ייצוא אנימציות קלות משקל לממשקים"},
            {"name": "Illustration", "name_he": "איור דיגיטלי", "note": "יצירת שפה גרפית מותאמת אישית"}
        ],
        "scan_keywords": ["Visual Design", "Pixel Perfect", "Micro-interactions"]
    },
    "methodologies_and_tech": {
        "must_have": [
            {"name": "Design Systems", "name_he": "מערכות עיצוב", "note": "בנייה, שימוש ותחזוקת קומפוננטות, Variants ו-Tokens ב-Figma"},
            {"name": "Responsive Design", "name_he": "עיצוב רספונסיבי", "note": "התאמה מלאה ל-Desktop, Tablet ומובייל"},
            {"name": "Mobile / Web App Design", "name_he": "עיצוב מערכות ווב ואפליקציות", "note": "חוקי UX ייעודיים ל-iOS, Android ו-SaaS"}
        ],
        "nice_to_have": [
            {"name": "HTML & CSS", "note": "הבנת עקרונות הפיתוח, Flexbox ו-Box Model להעברה חלקה למפתחים"},
            {"name": "Webflow / Framer", "note": "בניית אתרים אינטראקטיביים ללא קוד (Low-code / No-code)"}
        ],
        "scan_keywords": ["Agile", "Scrum", "Dev Hand-off", "Cross-functional teams"]
    },
    "portfolio_prerequisites": {
        "requirement": "תיק עבודות (Portfolio) הוא דרישת סף קריטית ומחייבת כמעט בכל משרה.",
        "platforms": ["Behance", "Dribbble", "אתר אישי (Webflow/Framer)", "PDF מקצועי"],
        "critical_elements": [
            "לפחות 2-3 מקרי בוחן מעמיקים (Case Studies) המציגים תהליך עבודה מלא ולא רק מסכים יפים.",
            "הצגת שלבי מחקר, הבנת בעיה עסקית, User Persona, User Flow, בדיקות שמישות ואיטרציות עיצוביות.",
            "הדגשת נישה רלוונטית: מוצרי B2B, מערכות SaaS מורכבות או אפליקציות B2C מובייל."
        ]
    },
    "ats_winning_formula": "Spearheaded end-to-end UX/UI redesign of SaaS workflow in Figma, reducing user drop-off by 34% as measured by usability testing across 20 participants.",
    "recommended_project": "קייס סטאדי מקצה לקצה למערכת SaaS B2B הכולל: מחקר משתמשים, Design System מלא ב-Figma (עם Auto-layout ו-Tokens), אב-טיפוס אינטראקטיבי, ותיעוד Dev Hand-off מסודר למפתחים."
}


def get_all_roles() -> List[str]:
    """מחזיר את רשימת כל 21 תפקידי היעד מתוך המאגר"""
    return list(_CATALOG.get("roles", {}).keys())


def get_role_data(role_name: str) -> Optional[Dict[str, Any]]:
    """שולף את המידע המלא על תפקיד מתוך המאגר"""
    roles = _CATALOG.get("roles", {})
    if role_name in roles:
        return roles[role_name]
    # חיפוש גמיש
    for name, data in roles.items():
        if role_name.lower() in name.lower() or name.lower() in role_name.lower():
            return data
    return None


def search_roles(query: str) -> List[Dict[str, Any]]:
    """חיפוש תפקידים לפי מחרוזת חופשית (אנגלית או עברית)"""
    q = query.strip().lower()
    if not q:
        return [data for data in _CATALOG.get("roles", {}).values()]
    
    matches = []
    for name, data in _CATALOG.get("roles", {}).items():
        if q in name.lower():
            matches.append(data)
            continue
        # בדיקה בכישורים
        skills_str = " ".join(data.get("main_skills", [])).lower()
        tools_str = " ".join(data.get("common_tools", [])).lower()
        if q in skills_str or q in tools_str:
            matches.append(data)
    return matches


def get_learning_paths_for_skills(missing_skills: List[str]) -> List[Dict[str, Any]]:
    """
    מאתר מסלולי לימוד והסמכות (LP-xxx) המתאימים לסגירת פערי המיומנויות.
    מחזיר מסלולים רשמיים עם קישורים, משך ודרישות הוכחה מעשית.
    """
    matched_paths = []
    seen_ids = set()
    all_paths = _CATALOG.get("learning_paths", [])

    for skill in missing_skills:
        skill_lower = skill.strip().lower()
        for lp in all_paths:
            if lp["id"] in seen_ids:
                continue
            
            # בדיקת התאמה בשם, בכלים או בכישורים הקנוניים
            text_corpus = (
                lp["name"].lower() + " " +
                " ".join(lp.get("canonical_skills", [])).lower() + " " +
                " ".join(lp.get("tools", [])).lower()
            )
            
            if skill_lower in text_corpus:
                matched_paths.append(lp)
                seen_ids.add(lp["id"])
                if len(matched_paths) >= 4:
                    break

    # אם לא נמצאו מסלולים ישירים, נחזיר מסלולים מובילים רלוונטיים
    if not matched_paths and all_paths:
        matched_paths = all_paths[:3]

    return matched_paths
