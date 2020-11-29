

import tkinter as tk
from tkinter import ttk
import datetime
import Database as db


class NotesWidget(tk.Toplevel):
    def __init__(self, my_db, *args):
        tk.Toplevel.__init__(self)
        self.width, self.height, self.x, self.y = args
        self.db = my_db
        self.init_child()

    def init_child(self):
        self.title("Введите заметку")

        self.text = tk.Text(self, height=26, width=35, bg="darkgreen", fg='white',
                            wrap='word', font=('Verdana', 10, 'bold'))
        self.text.grid(row=0, columnspan=3)
        self.text.grid_propagate(True)
        self.btn = tk.Button(self, text='Submit', command=lambda: self.record_the_note(self.get_tex()))
        self.btn.grid(row=2, column=1, ipady=10)

        #Creating and filling in combobox
        self.year_combobox = tk.StringVar()
        self.yearchoosen = ttk.Combobox(self, width=11, justify=tk.CENTER, textvariable=self.year_combobox)
        self.month_combobox = tk.StringVar()
        self.monthchoosen = ttk.Combobox(self, width=11, justify=tk.CENTER, textvariable=self.month_combobox)
        self.day_combobox = tk.StringVar()
        self.daychoosen = ttk.Combobox(self, width=11, justify=tk.CENTER, textvariable=self.day_combobox)

        self.now = datetime.datetime.now()
        self.day = self.now.day
        self.month = self.now.month
        self.year = self.now.year

        self.year_list = []
        for i in range(2020, 2050):
            self.year_list.append(i)
        self.month_list = ['January', 'February', 'March', 'April', 'May', 'June',
                            'July', 'August', 'September', 'October', 'November', 'December']
        self.day_list = []
        for i in range(1, 32):
            self.day_list.append(i)

        self.daychoosen['values'] = self.day_list
        self.daychoosen.grid(row=1, column=1)
        self.daychoosen.current(self.day - 1)

        self.monthchoosen.bind("<<ComboboxSelected>>", self.on_month)
        self.monthchoosen.grid(row=1, column=0)
        # self.monthchoosen.current(self.month - 1)

        self.monthchoosen['values'] = self.month_list
        self.monthchoosen.grid(row=1, column=0)
        # self.monthchoosen.current(self.month - 1)

        self.yearchoosen['values'] = self.year_list
        self.yearchoosen.grid(row=1, column=2)
        self.yearchoosen.current(0)

        self.geometry(f'318x487+{int(self.x) + int(self.width) + 12}+{int(self.y)}')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

    def on_month(self, event):
        if self.month_combobox.get() in ('January', 'March', 'May', 'July', 'August', 'October', 'December'):
            self.day_list = list(range(1, 32))
        else:
            self.day_list = list(range(1, 31))
        # todo: handle 28/29 days for Feb depending on year
        self.daychoosen.config(values= self.day_list)
    #
    # year = tk.IntVar()
    # month = tk.StringVar()
    # day = tk.IntVar()
    #
    # m = ttk.Combobox(root, values=months, state="readonly")
    # self.monthchoosen.bind("<<ComboboxSelected>>", self.on_month)
    # m.pack()

    def get_tex(self):
        return self.text.get("0.0", "end-1c")

    def record_the_note(self, text):
        d1 = self.daychoosen.get()
        d2 = self.monthchoosen.get()
        d3 = self.yearchoosen.get()
        d2_index = self.month_list.index(d2)
        d2_index += 1
        date = d1 + '.' + str(d2_index) + '.' + d3
        print(text, date)
        self.db.insert_data_from_notes_widget(text, date)
        self.destroy()


def show_notes_widget(coordinates):
    my_db = db.DB()
    width, height, x, y = coordinates
    notes_widget=NotesWidget(my_db, width, height, x, y)
    notes_widget.mainloop()

