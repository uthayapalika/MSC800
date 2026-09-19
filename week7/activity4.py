class Payment:
   
    
    def make_payment(self, amount):
        raise NotImplementedError("Subclass must implement make_payment()")


class CreditCard(Payment):
    def __init__(self, card_number):
        self.card_number = card_number
    
    def make_payment(self, amount):
        print(f"Paid ${amount} using Credit Card ending in {self.card_number[-4:]}")


class PayPal(Payment):
    def __init__(self, email):
        self.email = email
    
    def make_payment(self, amount):
        print(f"Paid ${amount} using PayPal account {self.email}")


class BankTransfer(Payment):
    def __init__(self, account_number):
        self.account_number = account_number
    
    def make_payment(self, amount):
        print(f"Paid ${amount} via Bank Transfer from account {self.account_number}")


# ---- Polymorphic behaviour ----
payments = [
    CreditCard("1234-5678-9012-3456"),
    PayPal("palika@gmail.com"),
    BankTransfer("ACC-987654")
]

for method in payments:
    method.make_payment(250)