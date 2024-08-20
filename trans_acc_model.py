# Создаем БД SQLite в каталоге нахождения данного файла
import sqlite3


connnection = sqlite3.connect("bank.bd")
cursor = connnection.cursor()

# Tаблица клиентов Банка:
cursor.execute("""
CREATE TABLE IF NOT EXISTS tbl_clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    place_of_birth TEXT NOT NULL,
    date_of_birth DATE NOT NULL,
    address TEXT NOT NULL,
    passport TEXT UNIQUE NOT NULL
    )
""")

# Таблица продуктов Банка:
cursor.execute("""
CREATE TABLE IF NOT EXISTS tbl_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    open_date DATE NOT NULL,
    close_date DATE NOT NULL,
    client_ref INTEGER NOT NULL,
    products_type_id INTEGER UNIQUE NOT NULL,
    FOREIGN KEY (client_ref) REFERENCES tbl_clients(id),
    FOREIGN KEY (products_type_id) REFERENCES tbl_products_type(id)
    )
""")

# Таблица типов продуктов:
cursor.execute("""
CREATE TABLE IF NOT EXISTS tbl_products_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    begin_date DATE NOT NULL,
    end_date DATE NOT NULL,
    tariff_ref INTEGER NOT NULL,
    FOREIGN KEY (tariff_ref) REFERENCES tbl_tariffs(id)
    )
""")

# Таблица счетов клиентов:
cursor.execute("""
CREATE TABLE IF NOT EXISTS tbl_accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    saldo NUMERIC(10, 2),
    open_date DATE NOT NULL,
    close_date DATE NOT NULL,
    acc_num INTEGER NOT NULL,
    client_ref INTEGER NOT NULL,
    product_ref INTEGER NOT NULL,
    FOREIGN KEY (product_ref) REFERENCES tbl_products(id),
    FOREIGN KEY (client_ref) REFERENCES tbl_clients(id)
    )
""")

# Таблица содержит информацию об операциях по счетам:
cursor.execute("""
CREATE TABLE IF NOT EXISTS tbl_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dt BOOLEAN DEFAULT 1,
    open_date DATE NOT NULL,
    sum INTEGER,
    acc_ref INTEGER NOT NULL,
    FOREIGN KEY (acc_ref) REFERENCES tbl_accounts(id)
    )
""")

# Таблица содержит информацию о тарифах:
cursor.execute("""
CREATE TABLE IF NOT EXISTS tbl_tariffs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    cost INTEGER NOT NULL
    )
""")

connnection.commit()
connnection.close()