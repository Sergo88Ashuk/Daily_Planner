

import tkinter as tk
import Database as db

class DisplayNotes(tk.Toplevel):
    def __init__(self, day, month, year, my_db):
        tk.Toplevel.__init__(self)
        self.day = day
        self.month = month
        self.year = year
        self.date = str(self.day) + '.' + str(self.month) + '.' + str(self.year)
        self.db = my_db
        self.init_child()

    def init_child(self):
        self.title('Your current notes')

        self.notes = self.db.view_records(self.date)

        self.text = tk.Text(self, height=26, width=35, bg="darkgreen", fg='white',
                            wrap='word', font=('Verdana', 10, 'bold'))
        for note in self.notes:
            self.text.insert('0.0', note[0] + '\n')
        self.text.pack()
        self.btn = tk.Button(self, text='Submit and close', command=lambda: self.record_the_note())
        self.btn.pack(ipady=10)
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()
        self.text.grid_propagate(True)

    # Recording the data
    def record_the_note(self):
        date = str(self.day) + '.' + str(self.month) + '.' + str(self.year)
        self.db.insert_data(self.text.get("0.0", "end-1c"), date)
        self.destroy()

def show_my_notes(date_tuple):
    my_db = db.DB()
    day, month, year = date_tuple
    my_notes = DisplayNotes(day, month, year, my_db)
    my_notes.mainloop()
