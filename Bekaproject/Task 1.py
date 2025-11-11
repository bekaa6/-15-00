# Базовый класс
class Animal:
    def __init__(self, species, sound="Some sound"):
        self.species = species
        self.sound = sound

    def make_sound(self):
        """Выводит общий звук животного."""
        print(f"The {self.species} goes: {self.sound}")


# Производный класс
class Dog(Animal):
    def __init__(self, name, sound="Woof"):
        # Вызываем конструктор базового класса (Animal)
        # Устанавливаем species как "Dog"
        super().__init__(species="Dog", sound=sound)
        self.name = name

    # Переопределение метода make_sound
    def make_sound(self):
        """Выводит звук, используя имя собаки."""
        print(f"{self.name} the {self.species} says: {self.sound}!")


# Создание экземпляров и вызов метода
general_animal = Animal("Cat", "Meow")
dog_instance = Dog("Buddy")

print("--- Animal Instance ---")
general_animal.make_sound()

print("\n--- Dog Instance ---")
dog_instance.make_sound()