import io
from typing import Tuple
from pypdf import PdfReader


class PDFExtractionError(Exception):
    """שגיאה מותאמת עבור בעיות בחילוץ קובץ PDF"""
    pass


def extract_text_from_pdf(file_bytes: bytes) -> Tuple[str, int]:
    """
    מחלץ טקסט מקובץ PDF ישירות מזרם בייטים בזיכרון (In-Memory BytesIO)
    ללא שמירה בדיסק.
    
    מחזיר:
        (טקסט מחולץ, מספר עמודים)
        
    מעלה:
        PDFExtractionError במקרה של קובץ סרוק (<50 תווים) או פגום
    """
    if not file_bytes:
        raise PDFExtractionError("הקובץ שהועלה ריק.")

    try:
        pdf_stream = io.BytesIO(file_bytes)
        reader = PdfReader(pdf_stream)
        num_pages = len(reader.pages)
        
        extracted_pages = []
        for i, page in enumerate(reader.pages):
            page_text = page.extract_text() or ""
            extracted_pages.append(page_text)
            
        full_text = "\n".join(extracted_pages).strip()
        
        # אימות חומרה: זיהוי קובץ סרוק או תמונה ללא שכבת טקסט (פחות מ-50 תווים)
        if len(full_text) < 50:
            raise PDFExtractionError(
                "הקובץ שהועלה אינו מכיל שכבת טקסט קריאה (ייתכן שמדובר בקובץ סרוק או תמונה). "
                "אנא העלה קובץ PDF דיגיטלי מקורי."
            )
            
        return full_text, num_pages

    except PDFExtractionError:
        raise
    except Exception as e:
        raise PDFExtractionError(f"שגיאה בעיבוד קובץ ה-PDF: {str(e)}")
