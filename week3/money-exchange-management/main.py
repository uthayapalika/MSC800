from db import add_customer
from db import add_currency
from db import add_exchange_rate
from db import add_transaction


class CurrencyManagement:

    def add_customer_details(self):

        # Get customer details
        c_name = input("Enter customer name: ")
        c_email = input("Enter customer email: ")

        add_customer(c_name, c_email)

        print("Customer added successfully!")


    def add_currency_details(self):

        currency_name = input("Enter currency name: ")
        short_name = input("Enter short name: ")
        status = input("Enter 1 for active, 0 for inactive: ")

        add_currency(
            currency_name,
            short_name,
            status
        )

        print("Currency added successfully!")


    def add_exchange_rate_details(self):

        currency_id = int(input("Enter currency ID: "))
        buying_rate = float(input("Enter buying rate: "))
        selling_rate = float(input("Enter selling rate: "))

        add_exchange_rate(
            currency_id,
            buying_rate,
            selling_rate
        )

        print("Exchange rate added successfully!")


    def exchange_transaction(self):

        customer_id = int(input("Enter customer ID: "))
        currency_id = int(input("Enter currency ID: "))
        transaction_type = input("Enter transaction type: ")
        amount = float(input("Enter amount: "))

        add_transaction(
            customer_id,
            currency_id,
            transaction_type,
            amount
        )

        print("Transaction added successfully!")


# Create object
userdata = CurrencyManagement()
#get user inputs
userdata.exchange_transaction()