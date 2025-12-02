# student_utils/string_tools.py

def to_upper(text):
    """Return the text converted to uppercase."""
    return text.upper()

def count_words(text):
    """Return the number of words in text (split on whitespace)."""
    return len(text.split())

def reverse_text(text):
    """Return the text reversed (useful for simple transformations).

    Example:
      reverse_text("abc") -> "cba"
    """
    return text[::-1]