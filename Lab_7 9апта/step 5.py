class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self._speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("Жылдамдық теріс болмауы керек!")
        if value > 300:
            raise ValueError("Жылдамдық 300 км/сағаттан аспауы керек!")
        self._speed = value

    def info(self):
        return f"{self.brand} — жылдамдығы: {self._speed} км/сағ"


class ElectricCar(Vehicle):
    def __init__(self, brand, speed, battery_level):
        super().__init__(brand, speed)
        self._battery = battery_level

    @property
    def battery(self):
        return self._battery

    def charge(self, percent):
        if percent < 0 or percent > 100:
            print("Қате: заряд 0-100% аралығында болуы керек!")
            return
        added = percent - self._battery
        self._battery = percent
        print(f"Заряд +{added}% қосылды. Қазір: {self._battery}%")

    def info(self):
        return f"{super().info()} | Батарея: {self._battery}%"


tesla = ElectricCar("Tesla Model S", 250, 65)
print(tesla.info())
tesla.speed = 280
print(tesla.info())
tesla.charge(90)
print(tesla.info())
tesla.speed = 350
tesla.charge(150)