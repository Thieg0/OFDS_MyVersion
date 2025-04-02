from abc import ABC, abstractmethod
from datetime import datetime


class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def process_payment(self):
        pass


class CreditCard(Payment):
    def __init__(self, amount, card_number, expiration_date, cvv):
        super().__init__(amount)
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv

    def validate_card(self):
        if len(self.card_number) != 16 or not self.card_number.isdigit():
            return False

        # Verifica se a data de vencimento é válida e está no futuro
        try:
            exp_date = datetime.strptime(self.expiration_date, "%m/%y")
            if exp_date < datetime.now():
                return False
        except ValueError:
            return False

        if len(self.cvv) != 3 or not self.cvv.isdigit():
            return False

        return True

    def process_payment(self):
        if not self.validate_card():
            return "Pagamento falhou: Dados do cartão inválidos."
        return f"Pagamento de R${self.amount:.2f} realizado com Cartão de Crédito."


class DebitCard(Payment):
    def __init__(self, amount, card_number, expiration_date, cvv):
        super().__init__(amount)
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv

    def validate_card(self):
        if len(self.card_number) != 16 or not self.card_number.isdigit():
            return False

        try:
            exp_date = datetime.strptime(self.expiration_date, "%m/%y")
            if exp_date < datetime.now():
                return False
        except ValueError:
            return False

        if len(self.cvv) != 3 or not self.cvv.isdigit():
            return False

        return True

    def process_payment(self):
        if not self.validate_card():
            return "Pagamento falhou: Dados do cartão inválidos."
        return f"Pagamento de R${self.amount:.2f} realizado com Cartão de Débito."


class Pix(Payment):
    def process_payment(self):
        return f"Pagamento de R${self.amount:.2f} realizado com Pix."


class Cash(Payment):
    def process_payment(self):
        return f"Pagamento de R${self.amount:.2f} realizado em Dinheiro."
