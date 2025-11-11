# Базовый класс
class Vehicle:
    def drive(self):
        print("Vehicle is moving.")


# Производный класс 1
class Car(Vehicle):
    def __init__(self, model):
        self.model = model

    def drive(self):
        # Переопределение
        print(f"The {self.model} is driving smoothly.")


# Производный класс 2
class Truck(Vehicle):
    def __init__(self, load_weight):
        self.load_weight = load_weight

    def drive(self):
        # Переопределение
        print(f"The Truck is driving, carrying {self.load_weight} tons.")


# Список объектов разных классов
vehicles = [
    Car("Sedan"),
    Truck(10),
    Car("SUV"),
    Truck(5)
]

print("--- Start Driving ---")
# Единый цикл для всех объектов
for v in vehicles:
    v.drive()