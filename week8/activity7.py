
class Target:
    def pay(self, amount):
        pass


class OldPaymentSystem:
    def make_payment(self, amount):
        print(f"Payment of ${amount} made using Old Payment System.")



class PaymentAdapter(Target):

    def __init__(self, old_payment_system):
        self.old_payment_system = old_payment_system

    def pay(self, amount):
        self.old_payment_system.make_payment(amount)



old_payment = OldPaymentSystem()

adapter = PaymentAdapter(old_payment)

adapter.pay(500)