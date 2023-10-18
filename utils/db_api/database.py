import sqlite3


class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL,
        photo TEXT,
        about TEXT,
        category INTEGER,
        status INTEGER,
        created_at TEXT
        )""")
        self.conn.commit()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
        )""")
        self.conn.commit()

    def add_category(self, name):
        try:
            self.cursor.execute(f"INSERT INTO categories (name) VALUES ('{name}')")
            self.conn.commit()
            return True
        except Exception as exc:
            print(exc)
            return False

    def get_all_categories(self):
        try:
            return self.cursor.execute("SELECT * FROM categories;").fetchall()
        except Exception as exc:
            print(exc)
            return False

    def get_category_by_name(self, name):
        try:
            return self.cursor.execute(f"SELECT * FROM categories WHERE name='{name}'").fetchone()
        except Exception as exc:
            print(exc)
            return False

    def get_products_by_cat_id(self, cat_id):
        try:
            return self.cursor.execute(f"SELECT * FROM products WHERE category={cat_id}").fetchall()
        except Exception as exc:
            print(exc)
            return False