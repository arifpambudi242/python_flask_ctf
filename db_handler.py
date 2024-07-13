# make db handler for the users using sqlite3 migrate and action crud

import sqlite3
from sqlite3 import Error

class DBHandler:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connect()
        self.create_table()
    
    def connect(self):
        try:
            self.conn = sqlite3.connect("users.db")
            self.cursor = self.conn.cursor()
        except Error as e:
            print(e)
    
    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
        self.conn.commit()
    
    def insert_user(self, username, password):
        self.connect()
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        self.conn.commit()
        # close the connection
        self.close()
    
    def get_user(self, username):
        self.connect()
        sql_text = f"SELECT * FROM users WHERE username = '{username}'"
        print(sql_text)
        self.cursor.execute(sql_text)
        datas = self.cursor.fetchall()
        # close the cursor
        self.close()
        return datas if datas else None
    
    def close(self):
        self.conn.close()
    
    def __del__(self):
        self.close()

# Usage
# from db_handler import DBHandler
# 

if __name__ == "__main__":
    db = DBHandler()
    db.insert_user("admin", "password123")
    print(db.get_user("admin"))

    db.close()