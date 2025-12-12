from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate(self, student, grades, subjects):
        pass