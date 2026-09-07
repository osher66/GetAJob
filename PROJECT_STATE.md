# 🚀 GetAJob - תמונת מצב והנחיות להמשך עבודה (Project State & Continuity)

מסמך זה מרכז את כל המידע הנדרש להמשך עבודה רציף ומדויק על הפרויקט מכל מחשב (לרבות מחשב העבודה).

---

## 📌 1. סקירת הפרויקט ומטרתו
**GetAJob** היא פלטפורמת AI ישראלית לקריירה והכנה לעבודה בהייטק, המיועדת לפרויקט גמר לימודים.  
המערכת מנתחת קורות חיים של מועמדים מול דרישות השוק במגוון מקצועות (עיצוב UX/UI, ניתוח נתונים, פיתוח תוכנה, DevOps, QA, סייבר ועוד).

---

## 🎨 2. עיצוב ושפה גרפית (Material Design 3)
הממשק הוסב במלואו ל-**Google Material Design 3 (M3)** ותומך RTL מלא:
1. **צבעים וטוקנים:** מוגדרים ב-[ui_styles.py](file:///c:/Users/Osher/Desktop/GetAJob/ui_styles.py) לפי סטנדרט M3 (Tonal Elevations, Secondary Containers, On-Surface).
2. **כפתורים:** סגנון Pill מעוגל (`border-radius: 9999px`) עם אפקטי ריחוף (Hover Elevation).
3. **דף הבית (Hero Section):**
   - כותרת וסלוגן בעברית ללא שבירת שורות מיותרת (`white-space: nowrap`).
   - כפתור הנעה לפעולה (CTA) מיושר לימין הטקסט.
   - לוגו באנגלית ממוקם כעוגן מותג אלגנטי (Brand Anchor Pill).
   - תמונת ה-Hero ממוקמת ב-[assets/hero_illustration.jpg](file:///c:/Users/Osher/Desktop/GetAJob/assets/hero_illustration.jpg) ומיושרת לגובה הטקסט.

---

## 🛠️ 3. פיצ'רים מרכזיים שהוטמעו
1. **צ'קליסט אבני דרך אינטראקטיבי (Career Progress Tracker):**
   - פותח במיוחד עבור פרויקט הגמר בהתאמה לכל תפקיד (UX/UI, Data, Dev וכו').
   - מזהה את החוסרים הספציפיים של המועמד ומציג משימות ממוקדות לסגירת הפער.
   - כולל מעקב התקדמות עם מד התקדמות ליניארי של Material Design 3.
   - מנגנון נגישות מלא (`label_visibility="collapsed"`).
2. **דף בחירת תפקיד והעלאת קו"ח:**
   - רכיבי M3 Filter Chips (`st.pills`) לבחירה מהירה בין תפקידים מובילים (UX/UI, Frontend, Data).
   - תרחישי דמו מהירים וטעינת קבצי PDF.
3. **דף תוצאות ואבחון:**
   - ציון התאמה דינמי, ניתוח פערי מיומנויות (High / Medium / Low).
   - שדרוג קו"ח לפורמט ATS (לפני / אחרי).
   - סילבוס למידה מותאם אישית.

---

## ⚙️ 4. קונפיגורציה וטעינה חמה (Hot Reload)
- הקובץ [.streamlit/config.toml](file:///c:/Users/Osher/Desktop/GetAJob/.streamlit/config.toml) הוגדר עם:
  ```toml
  [server]
  headless = true
  runOnSave = true
  ```
  הגדרה זו מבטיחה שכל שמירת קובץ תתרענן מיידית בשרת ללא צורך בהפעלה מחדש.

---

## 💻 5. צעדים להמשך עבודה ממחשב העבודה
1. **משיכת הקוד העדכני:**
   ```bash
   git pull origin main
   ```
   *(אם הפרויקט טרם שובט: `git clone https://github.com/osher66/GetAJob.git`)*
2. **התקנת תלויות (במידת הצורך):**
   ```bash
   pip install -r requirements.txt
   ```
3. **מפתח API של Gemini:**
   לוודא שבתיקיית `.streamlit/` קיים קובץ `secrets.toml` עם:
   ```toml
   GEMINI_API_KEY = "המפתח_שלך"
   ```
4. **הרצת השרת המקומי:**
   ```bash
   streamlit run app.py
   ```
   הממשק ייפתח בכתובת: `http://localhost:8501`.
5. **המשך שיחה עם סוכן ה-AI (Antigravity):**
   בפתיחת השיחה במחשב העבודה, כל מה שצריך לכתוב לסוכן הוא:
   > "אני ממשיך את העבודה על GetAJob. קרא את PROJECT_STATE.md ואת .agents/rules/workflow.md כדי להכיר את המצב הקיים, ובוא נמשיך מאיפה שעצרנו."
