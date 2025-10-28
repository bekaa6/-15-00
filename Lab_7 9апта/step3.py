class Employee:
    def __init__(self, name, salary, bonus_percent):
        self.name = name
        self.__salary = salary
        self.__bonus = bonus_percent

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary >= 100000:
            self.__salary = new_salary
            print(f"Жаңа жалақы орнатылды: {new_salary} теңге")
        else:
            print("Қате: жалақы кемінде 100 000 теңге болуы керек!")

    def calculate_total(self):
        bonus = self.__salary * (self.__bonus / 100)
        return self.__salary + bonus

dev = Employee("Алихан", 1200000, 15)

dev.set_salary(1500000)

print(f"Жалпы табыс: {dev.calculate_total()} теңге")