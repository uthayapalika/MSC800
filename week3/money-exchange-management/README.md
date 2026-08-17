# Money Exchange System

A Python and SQLite-based money exchange management system.

## Technologies

- Python
- SQLite3

## Features

- Customer management
- Currency management
- Exchange rate management
- Currency transaction management
- SQLite database


## Project Structuer

money_exchange/
│
├── main.py
├── db.py
└── README.md


## Database Design

The Money Exchange System has four main tables:

### 1. Customer

Stores customer details such as name, email, and created date.

### 2. Currency

Stores available currencies, including:

- Currency name
- Short name
- Status
- Created date

### 3. Exchange Rate

Stores the buying and selling rates for each currency.

The `currency_id` is a foreign key that connects to the `currency` table.

The `created_at` field is useful for keeping track of exchange-rate history and future reports.

### 4. Currency Transaction

Stores customer currency transactions.

It includes:

- Customer ID
- Currency ID
- Transaction type - It can be anything(cash, bank transfer, cheque and anyother method)
- Amount
- Created date

The `customer_id` connects to the `customer` table, and `currency_id` connects to the `currency` table.

These transaction records can be used by the organization to generate reports in the future.

## Future Enhancement

In the future, exchange rates could be retrieved from an external API and updated daily.
then we can remove the currency table.