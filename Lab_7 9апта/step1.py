class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

worker = Employee("Бекзат", 920000, "Менеджер")

print(f"Аты: {worker.name}")
print(f"Лауазымы: {worker.position}")
print(f"Жалақысы: {worker.salary} теңге")