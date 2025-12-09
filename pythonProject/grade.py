# grade.py
class Grade:
    """Represents a score obtained in a specific subject."""
    def __init__(self, subject_code: str, score: float, weight: float = 1.0):
        # Encapsulation and validation
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100.")
        self._subject_code = subject_code
        self._score = score
        self._weight = weight

    def get_score(self) -> float:
        return self._score

    def get_weight(self) -> float:
        return self._weight

    def get_subject_code(self) -> str:
        return self._subject_code