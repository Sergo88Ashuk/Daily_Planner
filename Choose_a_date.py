

import tkinter as tk
import Database as db

class DateChoice(tk.Toplevel):
    def __init__(self, db, note_text):
        tk.Toplevel.__init__(self)
        self.note_text = note_text
        self.db = db
        self.init_yourself()


    def init_yourself(self):
        self.title("Date choice")
        self.day_entry1 = tk.Entry(self, text='day')
        self.day_entry2 = tk.Entry(self, text='month')
        self.day_entry3 = tk.Entry(self, text='year')

        self.add_btn = tk.Button(self, text='Add the note', width=20, height=3, command=self.record_the_note)

        self.day_entry1.grid(row=1, column=1)
        self.day_entry2.grid(row=1, column=2)
        self.day_entry3.grid(row=1, column=3)
        self.add_btn.grid(row=2, column=2)

        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

    def record_the_note(self):
        d1 = self.day_entry1.get()
        d2 = self.day_entry2.get()
        d3 = self.day_entry3.get()
        date = d1 + '.' + d2 + '.' + d3
        self.db.insert_data(self.note_text, date)



def get_choose_date(note_text):
    my_db = db.DB()
    dat = DateChoice(my_db, note_text)
    dat.mainloop()
