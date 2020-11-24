

import sqlite3

class DB():
    def __init__(self):
        self.conn = sqlite3.connect('my_notes.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS the_notes (id integer primary key, notes text, date text)''')
        self.conn.commit()

    # Вставка данных
    def insert_data(self, notes, date):
        self.cursor.execute('''SELECT date FROM the_notes''')
        self.all_dates = self.cursor.fetchone()

        if date in self.all_dates:
            print("I'm here")
            self.cursor.execute('''UPDATE the_notes SET notes = (?) WHERE date = (?)''', (notes, date))
            self.conn.commit()
        else:
            print("Something has gone wrong")
            self.cursor.execute('''INSERT INTO the_notes (notes, date) VALUES(?, ?)''', (notes, date))
            self.conn.commit()

    # Поиск данных и отображение
    def view_records(self, note_date):
        # Передаем кортеж, можно и список [note_date]
        self.cursor.execute('''SELECT notes FROM the_notes WHERE date = (?)''', (note_date,))
        # Возвращает список кортежей
        my_notes = self.cursor.fetchall()
        return my_notes


