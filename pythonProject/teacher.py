# teacher.py
# Person-нан мұра алу үшін импорттаңыз
from person import Person
from student import Student
from grade import Grade  # Grade нысанын жасау үшін


# Inheritance: Teacher inherits from Person
class Teacher(Person):
    """Represents a teacher who can enter grades."""

    def __init__(self, teacher_id: int, name: str):
        super().__init__(teacher_id, name)
        self._subjects_taught = []

    def get_details(self):
        return f"Teacher ID: {self._id}, Name: {self._name}, Subjects: {', '.join(self._subjects_taught)}"

    # Controlled system action
    def enter_grade(self, student: Student, subject_code: str, score: float):
        try:
            # Grade нысанын жасайды, бұл кезде валидация жүреді
            new_grade = Grade(subject_code, score)
            student.add_grade(new_grade)
            print(f"Grade {score} entered by {self._name} for {student.get_name()} in {subject_code}.")
        except ValueError as e:
            print(f"Failed to enter grade: {e}")