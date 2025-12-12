from abc import ABC, abstractmethod
import os

# Файлға жазу үшін тұрақтыны анықтаймыз
LOG_FILE = "app_log.txt"


# 1. Жартылай Абстракциясы бар Logger абстрактілі класын құру
class Logger(ABC):
    """
    Тіркеу (логгер) операцияларына арналған абстрактілі негізгі класс.
    Ол нақты (іске асырылған) әдісті және абстрактілі әдісті қамтиды.
    """

    # Нақты әдіс (абстрактілі негізгі класта іске асырылған)
    def header(self):
        """Стандартталған лог бастау тақырыбын басып шығарады."""
        # Талап бойынша === LOG START === шығарады
        print("=== LOG START ===")

    # Абстрактілі әдіс (подкластар іске асыруы керек)
    @abstractmethod
    def log(self, message):
        """
        Хабарламаны нақты тіркеумен (логтаумен) айналысатын абстрактілі әдіс.
        Подкластар хабарламаның қалай өңделетінін анықтауы керек (файлға, консольға және т.б.).
        """
        pass


# 2. ConsoleLogger подкласын іске асыру
class ConsoleLogger(Logger):
    """
    Хабарламаларды тікелей консольға/экранға шығарады.
    Абстрактілі log(message) әдісін іске асырады.
    """

    # log() абстрактілі әдісін іске асыру
    def log(self, message):
        # Хабарламаны стандартты шығысқа шығару
        print(f"[CONSOLE LOG]: {message}")


# 3. FileLogger подкласын іске асыру
class FileLogger(Logger):
    """
    Хабарламаларды жергілікті мәтіндік файлға жазу арқылы тіркейді.
    Абстрактілі log(message) әдісін іске асырады.
    """

    # log() абстрактілі әдісін іске асыру
    def log(self, message):
        """Хабарламаны анықталған лог-файлға жазады."""
        try:
            # Қосу (append) режимін ('a') пайдаланамыз, бұл жазбаларды қайта жазбай, қосып отыруға мүмкіндік береді
            with open(LOG_FILE, 'a') as f:
                f.write(f"[FILE LOG] {message}\n")
            print(f"Successfully logged to file: '{LOG_FILE}'")
        except IOError as e:
            print(f"Error writing to file: {e}")


# --- Класстарды тексеру ---

# Алдыңғы іске қосулардан қалған лог-файлды тазалау (міндетті емес)
if os.path.exists(LOG_FILE):
    os.remove(LOG_FILE)
    print(f"Removed previous log file: {LOG_FILE}\n")

# 1. ConsoleLogger тексеру
print("--- Testing ConsoleLogger ---")
console_logger = ConsoleLogger()
# Абстрактілі кластағы НАҚТЫ әдісті пайдалану
console_logger.header()
# Подкласспен іске асырылған АБСТРАКТІЛІ әдісті пайдалану
console_logger.log("Application started successfully.")
console_logger.log("User 'admin' logged in.")
print("\n")

# 2. FileLogger тексеру
print("--- Testing FileLogger ---")
file_logger = FileLogger()
# Абстрактілі кластағы НАҚТЫ әдісті пайдалану
file_logger.header()
# Подкласспен іске асырылған АБСТРАКТІЛІ әдісті пайдалану
file_logger.log("Database connection established.")
file_logger.log("Processed 15 records.")
print("\n")

# Файл мазмұнын тексеру (міндетті емес)
if os.path.exists(LOG_FILE):
    print(f"--- Content of {LOG_FILE} ---")
    with open(LOG_FILE, 'r') as f:
        print(f.read().strip())
    print("----------------------------")