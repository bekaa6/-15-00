class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.__salary = salary
        self.position = position

    def get_salary(self):
        return self.__salary

worker = Employee("Арман", 850000, "Аналитик")
print(worker.get_salary())