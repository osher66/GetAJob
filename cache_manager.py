import hashlib
import json
from typing import Optional
from cachetools import LRUCache
from schemas import JobMatchAnalysis


class AnalysisCache:
    """
    מנגנון מטמון בזיכרון (In-Memory LRU Cache) למהירות תגובה של 0 שניות בהדגמות חוזרות.
    מפתח המטמון מחושב מ-SHA256 של הטקסט המטוהר של קו"ח + תיאור המשרה.
    """
    def __init__(self, maxsize: int = 100):
        self._cache = LRUCache(maxsize=maxsize)

    @staticmethod
    def generate_key(sanitized_resume_text: str, normalized_job_desc: str) -> str:
        combined = f"{sanitized_resume_text.strip()}###{normalized_job_desc.strip()}".encode("utf-8")
        return hashlib.sha256(combined).hexdigest()

    def get(self, key: str) -> Optional[JobMatchAnalysis]:
        return self._cache.get(key)

    def set(self, key: str, analysis: JobMatchAnalysis) -> None:
        self._cache[key] = analysis

    def clear(self) -> None:
        self._cache.clear()

    def size(self) -> int:
        return len(self._cache)


# מופע גלובלי יחיד עבור השרת / הממשק
global_cache = AnalysisCache()
