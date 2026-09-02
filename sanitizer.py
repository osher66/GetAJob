import re
from typing import Tuple


def sanitize_pii(text: str) -> Tuple[str, dict]:
    """
    מנקה פרטים מזהים (PII) מטקסט קורות החיים באמצעות Regex מקומי:
    - מספרי טלפון ישראליים ובינלאומיים
    - כתובות דוא"ל
    - מספרי תעודת זהות (9 ספרות)
    """
    stats = {"emails": 0, "phones": 0, "ids": 0}

    # טלפונים: 05X-XXXXXXX, 05XXXXXXXX, +972..., וכדומה
    phone_pattern = r"(?:\+972[- ]?|0)(?:[23489]|5[0-9]|7[2-9])[- ]?\d{3}[- ]?\d{4}\b"
    phones_found = len(re.findall(phone_pattern, text))
    text = re.sub(phone_pattern, "[CANDIDATE_PHONE]", text)
    stats["phones"] = phones_found

    # כתובות דוא"ל
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    emails_found = len(re.findall(email_pattern, text))
    text = re.sub(email_pattern, "[CANDIDATE_EMAIL]", text)
    stats["emails"] = emails_found

    # תעודות זהות ישראליות (מספרי 9 ספרות עצמאיים)
    id_pattern = r"\b\d{9}\b"
    ids_found = len(re.findall(id_pattern, text))
    text = re.sub(id_pattern, "[CANDIDATE_ID]", text)
    stats["ids"] = ids_found

    return text, stats


def truncate_job_description(job_text: str, max_chars: int = 3000) -> str:
    """
    קיצוץ תיאור משרה ל-3000 תווים מרכזיים תוך שמירה על דרישות התפקיד.
    """
    clean_text = job_text.strip()
    if len(clean_text) <= max_chars:
        return clean_text
    return clean_text[:max_chars] + "... [TRUNCATED]"
