import sqlite3


class SQL:
    def __init__(self):
        self.connect = sqlite3.connect("users.db")
        self.cursor = self.connect.cursor()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    		id Integer PRIMARY KEY AUTOINCREMENT,
    		name varchar(20), 
    		telegram_id varchar(20)
    		 )""")

    def add_users_to_db(self, name, telegram_id):
        'Добавить юзеров'
        self.cursor.execute(f"INSERT INTO users (name,telegram_id) VALUES ('{name}','{telegram_id}')")
        return self.connect.commit()

    #
    def select_id(self, telegram_id):
        "Id bo'yicha olib beradi"
        self.cursor.execute(f"SELECT * FROM users where telegram_id = {telegram_id}")
        info = self.cursor.fetchall()
        return info

    def select_all_users(self):
        "Id bo'yicha olib beradi"
        self.cursor.execute(f"SELECT * FROM users")
        info = self.cursor.fetchall()
        return info

    def save(self):
        self.connect.commit()
        # self.connect.close()
