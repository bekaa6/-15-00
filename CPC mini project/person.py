# person.py
from abc import ABC, abstractmethod

# Abstraction & Inheritance: Abstract Base Class
class Person(ABC):
    """Abstract base class for all people in the system."""
    def __init__(self, person_id: int, name: str):
        # Encapsulation: Private/Protected Fields
        self._id = person_id
        self._name = name

    # Encapsulation: Getter
    def get_name(self) -> str:
        return self._name

    @abstractmethod
    def get_details(self):
        """Must be implemented by concrete classes."""
        pass


