from typing import List, Literal
from pydantic import BaseModel, Field


class MissingSkill(BaseModel):
    skill: str = Field(description="שם המיומנות או הטכנולוגיה החסרה")
    importance: Literal["High", "Medium", "Low"] = Field(
        description="רמת החומרה של הפער: High (חובה קריטית), Medium (דרישה חשובה), Low (יתרון)"
    )


class CVBulletImprovement(BaseModel):
    original: str = Field(description="הנוסח המקורי מקורות החיים")
    improved: str = Field(description="הנוסח המשודרג מונחה Action-Impact עם מספרים וטכנולוגיות")
    reason: str = Field(description="הסבר קצר על היתרון והערך ההנדסי של השכתוב")


class PortfolioProject(BaseModel):
    project_name: str = Field(description="שם הפרויקט המוצע")
    targeted_skills: List[str] = Field(description="רשימת המיומנויות המרכזיות שהפרויקט מכסה")
    business_context: str = Field(description="הבעיה העסקית והצורך המעשי שהפרויקט פותר")
    architecture_stack: List[str] = Field(description="סטאק טכנולוגי מומלץ (שפות, ספריות, תשתית)")
    implementation_steps: List[str] = Field(description="שלבי ביצוע הנדסיים מפורטים")
    readme_content: str = Field(description="טקסט מלא של קובץ README.md מוכן ל-GitHub")


class JobMatchAnalysis(BaseModel):
    match_score: int = Field(
        ge=0, le=100, description="ציון התאמה משוקלל בין 0 ל-100"
    )
    match_summary: str = Field(description="סיכום תמציתי ומקצועי של ההתאמה והפערים")
    missing_skills: List[MissingSkill] = Field(description="פילוח מיומנויות חסרות לפי רמות חומרה")
    cv_bullet_improvements: List[CVBulletImprovement] = Field(
        description="שכתוב של עד 3 סעיפי הישגים מתוך קורות החיים"
    )
    portfolio_project: PortfolioProject = Field(description="מפרט פרויקט מעשי לסגירת הפער")
