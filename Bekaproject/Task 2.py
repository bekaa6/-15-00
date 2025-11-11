class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class Manager(Employee):
    def __init__(self, name, base_salary, bonus_rate):
        super().__init__(name, base_salary)
        self.bonus_rate = bonus_rate

    def calculate_salary(self):
        base = super().calculate_salary()
        bonus = base * self.bonus_rate
        return base + bonus


emp = Employee("Alex", 50000)
mgr = Manager("Sarah", 70000, 0.15)

print(f"Employee {emp.name} salary: ${emp.calculate_salary():,.2f}")
print(f"Manager {mgr.name} salary: ${mgr.calculate_salary():,.2f}")