import sqlite3
import os

# Connect DB
db_path = os.path.join(
    os.path.dirname(__file__),
    "money_exchange.db"
)

connection = sqlite3.connect(db_path)

print("Connection to database successful")

cursor = connection.cursor()


# Create customer table
command1 = '''CREATE TABLE IF NOT EXISTS customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    c_name TEXT NOT NULL,
    c_email TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)'''

cursor.execute(command1)


# Create currency table
command2 = '''CREATE TABLE IF NOT EXISTS currency (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    c_name TEXT NOT NULL,
    c_short_name TEXT NOT NULL UNIQUE,
    c_status BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)'''

cursor.execute(command2)


# Create exchange_rate table
command3 = '''CREATE TABLE IF NOT EXISTS exchange_rate (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    currency_id INTEGER NOT NULL,
    buying_rate REAL NOT NULL,
    selling_rate REAL NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (currency_id) REFERENCES currency (id)
)'''

cursor.execute(command3)


# Create currency_transaction table
command4 = '''CREATE TABLE IF NOT EXISTS currency_transaction (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    currency_id INTEGER NOT NULL,
    transaction_type TEXT NOT NULL,
    amount REAL NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customer (id),
    FOREIGN KEY (currency_id) REFERENCES currency (id)
)'''

cursor.execute(command4)

connection.commit()


# Add customer
def add_customer(c_name, c_email):

    customer = connection.cursor()

    customer.execute("""
        INSERT INTO customer (c_name, c_email)
        VALUES (?, ?)
    """, (c_name, c_email))

    connection.commit()

# add currencies
def add_currency(c_name,c_short_name,c_status):
    currency=connection.cursor()

    currency.execute("""
           INSERT INTO currency (c_name, c_short_name,c_status)
           VALUES (?, ?, ?)
       """, (c_name, c_short_name,c_status))
    connection.commit()


def add_exchange_rate(currency_id,buying_rate,selling_rate):
      exchangerate = connection.cursor()
      exchangerate.execute("""
           INSERT INTO exchange_rate (currency_id,buying_rate,selling_rate)
           VALUES (?, ?, ?)
       """, (currency_id,buying_rate,selling_rate)) 
      connection.commit()  

def add_transaction(customer_id, currency_id, transaction_type, amount):

    transaction = connection.cursor()

    transaction.execute("""
        INSERT INTO currency_transaction
        (customer_id, currency_id, transaction_type, amount)
        VALUES (?, ?, ?, ?)
    """, (customer_id, currency_id, transaction_type, amount))

    connection.commit()



# insert currencies
def insert_default_currencies():

    currency = connection.cursor()

    currencies = [
        ("New Zealand Dollar", "NZD", 1),
        ("Australian Dollar", "AUD", 1),
        ("US Dollar", "USD", 1),
        ("Euro", "EUR", 1),
        ("British Pound Sterling", "GBP", 1),
        ("Japanese Yen", "JPY", 1),
        ("Canadian Dollar", "CAD", 1),
        ("Swiss Franc", "CHF", 1),
        ("Singapore Dollar", "SGD", 1),
        ("Sri Lankan Rupee", "LKR", 1)
    ]

    currency.executemany("""
        INSERT OR IGNORE INTO currency
        (c_name, c_short_name, c_status)
        VALUES (?, ?, ?)
    """, currencies)

    connection.commit()

    
def insert_default_exchangerate():

    exchange = connection.cursor()

    exchange_rates = [
        (1, 1.00, 1.00),      
        (2, 1.10, 1.15),      
        (3, 0.58, 0.62),      
        (4, 0.50, 0.54),      
        (5, 0.43, 0.47),      
        (6, 85.00, 90.00),    
        (7, 0.78, 0.82),      
        (8, 0.46, 0.50),      
        (9, 0.75, 0.80),      
        (10, 185.00, 195.00)  
    ]

    exchange.executemany("""
        INSERT INTO exchange_rate
        (currency_id, buying_rate, selling_rate)
        VALUES (?, ?, ?)
    """, exchange_rates)

    connection.commit()
# Insert default currencies
insert_default_currencies()
insert_default_exchangerate()