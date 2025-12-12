from abc import ABC, abstractmethod


# 1. Абстрактілі PaymentSystem интерфейсін жобалау
class PaymentSystem(ABC):
    """
    Барлық төлем жүйелеріне арналған абстрактілі интерфейс.
    Ол барлық подкластар орындауға міндетті келісімшартты анықтайды.
    """

    @abstractmethod
    def authorize(self, amount: float) -> bool:
        """Метод алдын ала авторизациялау (қаржыны тексеру) үшін."""
        pass

    @abstractmethod
    def process(self, payment_details: dict) -> str:
        """Нақты төлемді өңдеу және аяқтауға арналған метод."""
        pass

    @abstractmethod
    def refund(self, transaction_id: str) -> str:
        """Транзакция бойынша ақшаны қайтаруды бастауға арналған метод."""
        pass


# 2. PayPal подкласын құру
class PayPal(PaymentSystem):
    """
    PayPal жүйесін іске асыру.
    """

    def authorize(self, amount: float) -> bool:
        print(f"PayPal: Авторизация сұрауы ${amount:.2f} сомасына жіберілді.")
        # PayPal API-мен байланыс логикасы
        return True

    def process(self, payment_details: dict) -> str:
        tx_id = payment_details.get('id', 'N/A')
        print(f"PayPal: Транзакция ID {tx_id} өңделуде...")
        return "Транзакция PayPal арқылы сәтті аяқталды."

    def refund(self, transaction_id: str) -> str:
        print(f"PayPal: {transaction_id} транзакциясы үшін ақшаны қайтару басталды.")
        return "PayPal жүйесінде ақшаны қайтару бастамасы қабылданды."


# 3. KaspiPay подкласын құру
class KaspiPay(PaymentSystem):
    """
    KaspiPay жүйесін іске асыру.
    """

    def authorize(self, amount: float) -> bool:
        # KaspiPay көбінесе KZT-мен жұмыс істейді
        print(f"KaspiPay: {amount} KZT үшін баланс пен рұқсаттарды тексеру.")
        # Kaspi API-мен байланыс логикасы
        return True

    def process(self, payment_details: dict) -> str:
        merchant_id = payment_details.get('merchant_id', 'N/A')
        print(f"KaspiPay: Қаражатты сатушы ID {merchant_id} шотына аудару...")
        return "Транзакция KaspiPay арқылы сәтті өңделді."

    def refund(self, transaction_id: str) -> str:
        print(f"KaspiPay: Ішкі ID {transaction_id} бойынша төлемді кері қайтару (отмена) жасалуда.")
        return "KaspiPay жүйесі ақшаны қайтаруды растады."


# 4. VisaPayment подкласын құру
class VisaPayment(PaymentSystem):
    """
    Visa картасы арқылы төлемді іске асыру.
    """

    def authorize(self, amount: float) -> bool:
        print(f"Visa: Эмитент банкке ${amount:.2f} сомасына алдын ала авторизация сұрауын жіберу.")
        # Visa желісімен өзара әрекеттесу логикасы
        return True

    def process(self, payment_details: dict) -> str:
        card_digits = payment_details.get('card', '****')[-4:]
        print(f"Visa: Соңғы {card_digits} цифрлы карта үшін төлемді аяқтау.")
        return "Төлем Visa желісі арқылы сәтті алынды."

    def refund(self, transaction_id: str) -> str:
        print(f"Visa: {transaction_id} ID бойынша сторнирлеу (reversal) сұрауын жіберу.")
        return "Visa-ға ақшаны қайтару сұрауы жіберілді."


# --- Төлем Ағынын Тексеру ---

def run_payment_flow(system: PaymentSystem, amount: float, tx_id: str):
    """
    Кез келген PaymentSystem интерфейсін орындайтын жүйемен жұмыс істейтін функция.
    Полиморфизмді көрсетеді.
    """
    details = {'id': tx_id, 'amount': amount, 'card': '4000123456789012', 'merchant_id': 'MERCH123'}

    print(f"\n--- Тестілеу: {type(system).__name__} ---")

    if system.authorize(amount):
        result = system.process(details)
        print(f" -> Өңдеу нәтижесі: {result}")
        refund_result = system.refund(tx_id)
        print(f" -> Қайтару нәтижесі: {refund_result}")
    else:
        print("Авторизация сәтсіз аяқталды.")


# Объектілерді құру және тестілеу
run_payment_flow(PayPal(), 55.99, "PP-2023001")
run_payment_flow(KaspiPay(), 12500.00, "KP-T88231")
run_payment_flow(VisaPayment(), 249.50, "VS-X99477")