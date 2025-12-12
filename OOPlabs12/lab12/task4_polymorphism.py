from abc import ABC, abstractmethod


# --- 1. Vehicle Абстрактілі Класын Қайта Пайдалану ---

class Vehicle(ABC):
    """Абстрактілі негізгі класс 'move' келісімшартын анықтайды."""

    @abstractmethod
    def move(self):
        pass


# --- 2. 1-ші Тапсырмадағы Подкластарды Қайта Пайдалану ---

class Car(Vehicle):
    def move(self):
        print("Car: Жолда жүруде.")


class Bicycle(Vehicle):
    def move(self):
        print("Bicycle: Адам күшімен педаль арқылы қозғалуда.")


# --- 3. Жаңа Минималды Подкластарды Құру (Airplane, Train) ---

class Airplane(Vehicle):
    """Vehicle келісімшартын орындайтын минималды подкласс."""

    def move(self):
        print("Airplane: Аспанда ұшуда.")


class Train(Vehicle):
    """Vehicle келісімшартын орындайтын минималды подкласс."""

    def move(self):
        print("Train: Рельстерде жүруде.")


# --- 4. Тапсырманы Орындау: Полиморфизмді Көрсету ---

# Түрлі объектілер тізімін құру
# Бұл тізімдегі барлық объектілер Vehicle абстрактілі типін бөліседі.
fleet = [
    Car(),
    Bicycle(),
    Airplane(),
    Train()
]

print("--- Полиморфтық Мінез-құлықты Көрсету ---")
print("Көліктер тізімін аралап, әр объектіде 'move()' әдісін шақыруда.")

# Тізімді айналып өтіп, барлық объектілер үшін бірдей әдісті (move()) шақыру
for transport in fleet:
    # transport.move() әдісін шақыру объектінің нақты типіне байланысты әртүрлі кодты орындайды (Полиморфизм)
    transport.move()

print("------------------------------------------")
#