# ==========================================
# 1. OBSERVER
# ==========================================
# The Observer defines what an observer must
# do when it receives an update.

class Observer:

    def update(self, price):
        pass


# ==========================================
# 2. CONCRETE OBSERVER
# ==========================================


class Investor(Observer):

    def __init__(self, name):
        self.name = name

    def update(self, price):
        print(self.name, "received new stock price:", price)


# ==========================================
# 3. SUBJECT
# ==========================================


class Subject:

    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, price):
        for observer in self.observers:
            observer.update(price)


# ==========================================
# 4. CONCRETE SUBJECT
# ==========================================


class Stock(Subject):

    def __init__(self):
        super().__init__()
        self.price = 0

    def change_price(self, price):
        self.price = price

        print("Stock price changed to:", price)

        self.notify(self.price)


# ==========================================
# 5. CREATE STOCK
# ==========================================

stock = Stock()


# ==========================================
# 6. CREATE INVESTORS
# ==========================================

investor1 = Investor("Palika")
investor2 = Investor("Krishshanth")
investor3 = Investor("John")


# ==========================================
# 7. SUBSCRIBE INVESTORS
# ==========================================

stock.attach(investor1)
stock.attach(investor2)
stock.attach(investor3)


# ==========================================
# 8. CHANGE STOCK PRICE
# ==========================================

stock.change_price(105)