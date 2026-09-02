"""
מאגר ידע מובנה ומקצועי אודות מסלולי קריירה בהייטק לג'וניורים.
משמש את תהליך ה-Onboarding לבחירת תחום, סקירת השוק, וחיבור למנוע הניתוח.
כולל דגש מיוחד על תחום ה-UX/UI כמקצוע הדגל הראשי לפי מסמך האפיון הרשמי.
"""

CAREER_DOMAINS = {
    "ux_ui": {
        "id": "ux_ui",
        "title": "עיצוב חוויית וממשק משתמש – UX/UI Designer",
        "icon": "🎨",
        "is_flagship": True,
        "badge_text": "⭐ מסלול הדגל הראשי",
        "short_desc": "אפיון ועיצוב מוצרים דיגיטליים: מחקר משתמשים, בדיקות שמישות, Design Systems ב-Figma ובניית תיק עבודות.",
        "demand_level": "ביקוש גבוה ודגש על תיק עבודות ⭐ מסלול הדגל",
        "salary_range": "14,000 עד 19,000 ₪ (ג'וניור) | 20,000 עד 27,000 ₪ (Mid)",
        "must_have_skills": [
            "Figma (Auto-layout, Components, Tokens)",
            "User Research & Usability Testing",
            "Design Systems & Component Libraries",
            "Wireframing & Interactive Prototyping",
            "Typography & 8pt Grid Systems",
            "Mobile & Responsive Web Design"
        ],
        "good_to_have_skills": [
            "Micro-interactions & Lottie / After Effects",
            "A/B Testing & Hotjar / Analytics",
            "HTML/CSS Basics for Dev Hand-off",
            "Webflow / Framer (No-Code Interactive)",
            "B2B SaaS / Complex Web Apps Experience"
        ],
        "market_reality": "במשרות UX/UI, תיק עבודות (Portfolio) הוא תנאי הסף המחייב ביותר: מעסיקים מסננים מועמדים שרק מציגים 'מסכים יפים' מ-Dribbble. כדי להתקבל, חובה להציג 2-3 מקרי בוחן (Case Studies) מלאים המראים את תהליך החשיבה: הגדרת הבעיה, מחקר משתמשים, ארכיטקטורת מידע (IA), בדיקות שמישות וההחלטות העיצוביות.",
        "ats_winning_formula": "Spearheaded end-to-end UX/UI redesign of SaaS workflow in Figma, reducing user drop-off by 34% as validated through iterative usability testing across 20 participants.",
        "recommended_project_type": "Case Study מעמיק למערכת SaaS B2B או אפליקציית מובייל מורכבת: מחקר משתמשים, Design System מלא ב-Figma (Variants & Variables), אב-טיפוס אינטראקטיבי ותיעוד Dev Hand-off מפורט למפתחים.",
        "matching_preset_id": "ux_ui_preset"
    },
    "fullstack": {
        "id": "fullstack",
        "title": "פיתוח תוכנה ו-Fullstack",
        "icon": "💻",
        "is_flagship": False,
        "badge_text": "🔥 High Demand",
        "short_desc": "פיתוח מערכות Web מקצה לקצה – צד לקוח מודרני, שרתי API ובסיסי נתונים חיים.",
        "demand_level": "ביקוש גבוה מאוד (🔥 High Demand)",
        "salary_range": "16,000 - 22,000 ₪",
        "must_have_skills": ["React / TypeScript", "Node.js / Python", "REST APIs & WebSockets", "PostgreSQL / MongoDB", "Docker", "Git"],
        "good_to_have_skills": ["Next.js", "Redis Caching", "CI/CD Actions", "Microservices", "Unit & E2E Testing"],
        "market_reality": "המגייסים כבר לא מתרשמים מאתרי To-Do או חנויות גנריות ממדריכי יוטיוב. מה שמבטיח ראיון הוא פרויקט עם ארכיטקטורת נתונים אמיתית, טיפול בשגיאות, ניהול הרשאות (Auth) ופריסה מלאה בענן.",
        "ats_winning_formula": "Architected resilient Fullstack application utilizing TypeScript & React, integrating secure REST APIs and PostgreSQL with 99.8% test coverage.",
        "recommended_project_type": "פלטפורמת SaaS מקצה לקצה עם ניהול משתמשים, מסד נתונים רלציוני, שכבת Cache מהירה ו-Docker Compose להרצה בפקודה אחת.",
        "matching_preset_id": "fullstack_preset"
    },
    "cyber": {
        "id": "cyber",
        "title": "סייבר ואבטחת מידע (SOC & SecOps)",
        "icon": "🛡️",
        "is_flagship": False,
        "badge_text": "⚡ Critical Need",
        "short_desc": "הגנת רשתות, ניטור אירועי אבטחה, תחקור תקיפות בזמן אמת ופורנזיקה.",
        "demand_level": "מחסור כרוני בכישרונות (⚡ Critical Need)",
        "salary_range": "14,000 - 19,000 ₪",
        "must_have_skills": ["Network Protocols (TCP/IP, DNS)", "Linux CLI & Administration", "Wireshark & Packet Analysis", "SIEM (Splunk / Elastic)", "Python Scripting", "Firewall & IDS/IPS"],
        "good_to_have_skills": ["Snort / Suricata", "MITRE ATT&CK Framework", "Bash Scripting", "Cloud Security (AWS/Azure)"],
        "market_reality": "למועמדי SOC חסר לעיתים קרובות ניסיון פרקטי. מגייסים בוחנים מיידית האם הקמת מעבדת Home Lab ביתית, האם ניתחת קובץ PCAP של תקיפה אמיתית והאם אתה מסוגל לכתוב סקריפט אוטומציה ב-Python לפענוח לוגים.",
        "ats_winning_formula": "Analyzed PCAP network captures via Wireshark, authored automated SIEM correlation rules and mitigated simulated brute-force intrusions.",
        "recommended_project_type": "מערכת SIEM ביתית מבוססת Elastic/Splunk המנתחת תעבורת רשת חיה, מזהה סריקות פורטים ופולטת התראות אוטומטיות ב-Telegram/Slack.",
        "matching_preset_id": "cyber_preset"
    },
    "data": {
        "id": "data",
        "title": "דאטה, BI ו-Data Analytics",
        "icon": "📊",
        "is_flagship": False,
        "badge_text": "📈 Strong Growth",
        "short_desc": "תרגום נתונים מורכבים לתובנות עסקיות, בניית תהליכי ETL ודשבורדים אסטרטגיים.",
        "demand_level": "צמיחה מתמדת (📈 Strong Growth)",
        "salary_range": "15,000 - 20,000 ₪",
        "must_have_skills": ["Advanced SQL (Window, CTE)", "Python (Pandas, NumPy)", "Power BI / Tableau", "Data Modeling & Normalization", "ETL Pipelines", "Business KPIs"],
        "good_to_have_skills": ["Airflow", "Snowflake / BigQuery", "dbt", "Statistical Modeling", "Git"],
        "market_reality": "חברות מחפשות אנליסטים שמבינים את העסק ולא רק מריצים קוד. פרויקט מנצח מציג פתרון בעיה עסקית מוחשית: ניבוי נטישת לקוחות, אופטימיזציית רווחיות או ניתוח משפך מכירות עם דשבורד אינטראקטיבי.",
        "ats_winning_formula": "Engineered robust SQL queries and automated ETL data ingestion pipelines, visualizing revenue retention KPIs in Power BI for executive stakeholders.",
        "recommended_project_type": "צינור ETL אוטומטי ב-Python ששואב נתונים חיים מ-API, מנרמל אותם ב-PostgreSQL/DuckDB ומציג דשבורד מנהלים ב-Streamlit או Power BI.",
        "matching_preset_id": "data_preset"
    },
    "devops": {
        "id": "devops",
        "title": "DevOps, Cloud ו-Infrastructure",
        "icon": "☁️",
        "is_flagship": False,
        "badge_text": "🚀 High Value",
        "short_desc": "אוטומציית פריסות קוד, ניהול תשתיות ענן, קונטיינרים וצינורות CI/CD.",
        "demand_level": "ביקוש עולמי יציב ומבוקש (🚀 High Value)",
        "salary_range": "17,000 - 24,000 ₪",
        "must_have_skills": ["Linux Deep Dive", "Docker & Containers", "CI/CD (GitHub Actions / GitLab)", "AWS or GCP Basics", "Bash & Python Automation", "Git Workflows"],
        "good_to_have_skills": ["Kubernetes", "Terraform (IaC)", "Prometheus & Grafana", "Nginx / Reverse Proxies", "Ansible"],
        "market_reality": "בתחום ה-DevOps, הוכחת יכולת עצמאית היא קריטית: מגייס רוצה לראות מאגר GitHub עם קובץ Workflow של Actions, Dockerfile בעל שכבות אופטימליות, ותשתית ענן מוגדרת כקוד (IaC).",
        "ats_winning_formula": "Constructed automated multi-stage CI/CD deployment pipelines on AWS using Docker containers and GitHub Actions with zero downtime.",
        "recommended_project_type": "פרויקט CI/CD שלם המרים שירות Microservice מבוסס Docker, מבצע בדיקות אוטומטיות, דוחף ל-Docker Hub ופורס בענן עם מוניטורינג של Prometheus.",
        "matching_preset_id": "fullstack_preset"
    },
    "ai_llm": {
        "id": "ai_llm",
        "title": "הנדסת AI ויישומי LLM",
        "icon": "🤖",
        "is_flagship": False,
        "badge_text": "🔮 Emerging Future",
        "short_desc": "פיתוח סוכנים אוטונומיים, ארכיטקטורות RAG, אינטגרציית מודלים וחיפוש וקטורי.",
        "demand_level": "תחום בצמיחה מואצת (🔮 Emerging Future)",
        "salary_range": "18,000 - 26,000 ₪",
        "must_have_skills": ["Python & Async", "Vector DBs (Pinecone, Chroma)", "RAG Architectures", "LLM APIs (OpenAI, Gemini, Claude)", "Function Calling & Tools", "LangChain / LlamaIndex"],
        "good_to_have_skills": ["Model Fine-Tuning", "vLLM & Ollama", "Evaluation Frameworks (Ragas)", "FastAPI", "Docker"],
        "market_reality": "השוק מוצף במפתחים שיודעים רק לקרוא ל-API פשוט של OpenAI. מעסיקים מחפשים מהנדסים שמבינים RAG מתקדם: Chunking אופטימלי, מניעת הלוצינציות, הערכת דיוק (Evaluation), ומדידת ביצועים ועלויות טוקנים.",
        "ats_winning_formula": "Implemented production-grade RAG pipeline using Vector Embeddings & Gemini API, cutting token costs by 42% while preserving 94% retrieval accuracy.",
        "recommended_project_type": "סוכן בינה מלאכותית ארגוני המבצע Semantic Search מעל מאגר מסמכים מקומי, מצטט מקורות במדויק ומספק ממשק צ'אט מהיר עם Streaming.",
        "matching_preset_id": "fullstack_preset"
    }
}
