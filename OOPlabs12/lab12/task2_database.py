from abc import ABC, abstractmethod


# 1. Интерфейс тәрізді DatabaseInterface абстрактілі класын құру
class DatabaseInterface(ABC):
    """
    Дерекқор қосылымына арналған интерфейс тәрізді Абстрактілі Негізгі Класс (АНК).
    Ол барлық дерекқор іске асырулары сақтауы керек келісімшартты анықтайды.
    """

    # Абстрактілі әдіс: қосылу
    @abstractmethod
    def connect(self):
        """Дерекқор қосылымын орнатуға арналған абстрактілі әдіс."""
        pass

    # Абстрактілі әдіс: сұрауды орындау
    @abstractmethod
    def execute_query(self, query):
        """SQL сұрауын орындауға арналған абстрактілі әдіс."""
        pass

    # Абстрактілі әдіс: жабу
    @abstractmethod
    def close(self):
        """Дерекқор қосылымын жабуға арналған абстрактілі әдіс."""
        pass


# 2. SQLiteDatabase подкласын іске асыру
class SQLiteDatabase(DatabaseInterface):
    """
    SQLite дерекқорына қосылуға арналған нақты іске асыру.
    """

    def connect(self):
        # SQLite-ға қосылуды модельдеу
        print("Connecting to SQLite...")

    def execute_query(self, query):
        # SQLite-да сұрауды орындауды модельдеу
        print(f"Executing SQLite query: {query}")
        # Жалған деректерді қайтару
        return [("SQLite Result 1",), ("SQLite Result 2",)]

    def close(self):
        # SQLite қосылымын жабуды модельдеу
        print("Closing SQLite connection...")


# 3. PostgreSQLDatabase подкласын іске асыру
class PostgreSQLDatabase(DatabaseInterface):
    """
    PostgreSQL дерекқорына қосылуға арналған нақты іске асыру.
    """

    def connect(self):
        # PostgreSQL-ға қосылуды модельдеу
        print("Connecting to PostgreSQL...")

    def execute_query(self, query):
        # PostgreSQL-да сұрауды орындауды модельдеу
        print(f"Executing PostgreSQL query: {query}")
        # Жалған деректерді қайтару
        return [("PostgreSQL Result A",), ("PostgreSQL Result B",)]

    def close(self):
        # PostgreSQL қосылымын жабуды модельдеу
        print("Closing PostgreSQL connection...")


# --- Іске асыруларды тексеру функциясы ---

def run_db_operations(db: DatabaseInterface, db_name: str):
    """
    DatabaseInterface келісімшартын орындайтын кез келген объектімен жұмыс істейді.
    """
    print(f"\n--- Testing {db_name} ---")

    # Қосылу
    db.connect()

    # Сұрауды орындау
    query_string = "SELECT * FROM users;"
    results = db.execute_query(query_string)

    # Нәтижелерді көрсету
    print(f"Query Results (Mock): {results}")

    # Жабу
    db.close()


# SQLite-мен тексеру
sqlite_db = SQLiteDatabase()
run_db_operations(sqlite_db, "SQLiteDatabase")

# PostgreSQL-мен тексеру
postgres_db = PostgreSQLDatabase()
run_db_operations(postgres_db, "PostgreSQLDatabase")