class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary <= 0:
            raise ValueError("Қате: жалақы оң сан болуы керек!")
        if new_salary < 300000:
            print("Ескерту: жалақы 300 000 теңгеден кем болмауы ұсынылады.")
        self._salary = new_salary


emp = Employee("Айжан", 750000)
print(f"Ағымдағы жалақы: {emp.salary} теңге")

emp.salary = 950000
print(f"Жаңа жалақы: {emp.salary} теңге")

emp.salary = 250000
print(f"Соңғы жалақы: {emp.salary} теңге")

