# student.py
# Person-нан мұра алу үшін импорттаңыз
from person import Person
from grade import Grade


# Inheritance: Student inherits from Person
class Student(Person):
    """Represents a student enrolled in the school."""

    def __init__(self, student_id: int, name: str):
        super().__init__(student_id, name)
        # Composition: Student "has-a" list of Grades
        self._grades = []
        self._enrolled_subjects = set()

    def get_details(self):
        return f"Student ID: {self._id}, Name: {self._name}, Enrolled Subjects: {len(self._enrolled_subjects)}"

    def enroll_subject(self, subject_code: str):
        self._enrolled_subjects.add(subject_code)

    def add_grade(self, grade: Grade):
        if grade.get_subject_code() in self._enrolled_subjects:
            self._grades.append(grade)
        else:
            print(f"Error: Student not enrolled in {grade.get_subject_code()}.")

    def calculate_gpa(self) -> float:
        if not self._grades:
            return 0.0

        total_weighted_score = 0
        total_weight = 0

        for grade in self._grades:
            total_weighted_score += grade.get_score() * grade.get_weight()
            total_weight += grade.get_weight()

        return total_weighted_score / total_weight if total_weight > 0 else 0.0

    # Polymorphism: A basic report method
    def generate_report(self):
        # ... (implementation details are included in the demo output)
        return self._grades