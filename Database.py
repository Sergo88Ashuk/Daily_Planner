

import sqlite3

class DB():
    def __init__(self):
        self.conn = sqlite3.connect('my_notes.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS notes (id integer primary key, notes text, date text)''')
        self.conn.commit()

    def insert_data(self, notes, date):
        self.cursor.execute('''INSERT INTO notes (notes, date) VALUES(?, ?)''', (notes, date))
        self.conn.commit()
