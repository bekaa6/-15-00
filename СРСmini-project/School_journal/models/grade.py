class Grade:
    def __init__(self, id, student_id, subject_id, value):
        self._id = id
        self._student_id = student_id
        self._subject_id = subject_id
        self._value = value

    def get_value(self):
        return self._value

    def get_student_id(self):
        return self._student_id

    def get_subject_id(self):
        return self._subject_id

    def get_id(self):
        return self._id