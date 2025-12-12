from models.person import Person

class Teacher(Person):
    def __init__(self, id, name, age, subject_id):
        super().__init__(id, name, age)
        self._subject_id = subject_id

    def get_info(self):
        return f"Teacher {self._name}"

    def get_subject_id(self):
        return self._subject_id