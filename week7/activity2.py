class Bank:
    def __init__(self, name, customer_name, account_number, initial_balance=5000):
        self.name = name
        self.customer_name = customer_name
        self.account_number = account_number
        self.balance = initial_balance
        self.accounts = {}

    def create_account(self, account_number, initial_balance=5000):
        print(f"Creating account {account_number} with initial balance ${initial_balance}.")
        if account_number in self.accounts:
            print(f"Account {account_number} already exists.")
        else:
            self.accounts[account_number] = initial_balance
            print(f"Account {account_number} created with balance ${initial_balance}.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"Deposited ${amount} to account {account_number}. New balance: ${self.accounts[account_number]}.")
        else:
            print(f"Account {account_number} does not exist.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print(f"Withdrew ${amount} from account {account_number}. New balance: ${self.accounts[account_number]}.")
            else:
                print(f"Insufficient funds in account {account_number}. Current balance: ${self.accounts[account_number]}.")
        else:
            print(f"Account {account_number} does not exist.")  

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Account {account_number} balance: ${self.accounts[account_number]}.")
        else:
            print(f"Account {account_number} does not exist.")

    def calculate_interest(self, account_number, interest_rate):
        if account_number in self.accounts:
            interest = self.accounts[account_number] * (interest_rate / 100)
            print(f"Interest for account {account_number} at rate {interest_rate}% is ${interest}.")
        else:
            print(f"Account {account_number} does not exist.")       

                       
    def customer_details(self, account_number):
        if account_number in self.accounts:
            print(f"Account {account_number} details: Balance ${self.accounts[account_number]}.")
        else:
            print(f"Account {account_number} does not exist.")

            #get customer balance
    def get_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print(f"Account {account_number} does not exist.")
            return None
# create bank instance and create an account
customer = Bank("Kiwi Bank", "John Doe", "SA1001", 5000)
# create an account with account number "SA1001" and initial balance of 1000
customer.create_account("SA1001", 1000)
print(customer.get_balance("SA1001"))  
#customer deposit 500 and withdraw 200 from the account
#customer.deposit("SA1001", 500)
#customer withdraw 200 from the account
#customer.withdraw("SA1001", 1500)
#customer check balance of the account
#customer.check_balance("SA1001")

#print(customer.withdraw("SA1001", 1500))  
print(customer.calculate_interest("SA1001", 5))  