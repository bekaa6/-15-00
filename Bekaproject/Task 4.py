class BaseService:
    def __init__(self):
        print("Initializing BaseService.")


class Logging(BaseService):
    def __init__(self):
        super().__init__()
        print("Adding Logging functionality.")


class Caching(BaseService):
    def __init__(self):
        super().__init__()
        print("Adding Caching functionality.")


class DataProcessor(Logging, Caching):
    def __init__(self):
        # super() вызывает следующий класс в MRO,
        # который будет Caching, а Caching вызовет BaseService.
        super().__init__()
        print("Initializing DataProcessor.")


# Вызов
processor = DataProcessor()

# Вывод MRO (для демонстрации порядка):
print("\nMethod Resolution Order (MRO):")
print(DataProcessor.__mro__)