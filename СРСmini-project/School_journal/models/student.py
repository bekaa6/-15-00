from models.person import Person

class Student(Person):
    def __init__(self, id, name, age, class_num):
        super().__init__(id, name, age)
        self._class_num = class_num

    def get_info(self):
        return f"{self._name} (Class {self._class_num})"

    def get_class(self):
        return self._class_num