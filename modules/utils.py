# modules/utils.py
import re

def extract_after_keyword(text, keyword):
    """
    Basic helper: splits on keyword and returns trailing part.
    """
    if keyword in text:
        return text.split(keyword, 1)[1].strip()
    return ""
