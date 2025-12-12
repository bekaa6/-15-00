from models.subject import Subject

class SchoolJournal:
    __instance = None

    @staticmethod
    def get_instance():
        if SchoolJournal.__instance is None:
            SchoolJournal()
        return SchoolJournal.__instance

    def __init__(self):
        if SchoolJournal.__instance is not None:
            raise Exception("Singleton already exists!")
        SchoolJournal.__instance = self

        self.students = {}
        self.subjects = {
            1: Subject(1, "Math"),
            2: Subject(2, "Physics"),
            3: Subject(3, "English")
        }
        self.grades = []

    def add_student(self, student):
        self.students[student.get_id()] = student

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_grades_for_student(self, sid):
        return [g for g in self.grades if g.get_student_id() == sid]