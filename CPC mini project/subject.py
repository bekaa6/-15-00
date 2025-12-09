# subject.py
class Subject:
    """Represents a course subject."""
    def __init__(self, code: str, name: str):
        # Encapsulation
        self._code = code
        self._name = name

    def get_code(self) -> str:
        return self._code

    def get_name(self) -> str:
        return self._name