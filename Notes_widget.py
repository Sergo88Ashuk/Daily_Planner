

import tkinter as tk
from Choose_a_date import get_choose_date

class NotesWidget(tk.Toplevel):
    def __init__(self, *args):
        tk.Toplevel.__init__(self)
        self.width, self.height, self.x, self.y = args
        self.init_child()

    def init_child(self):
        self.title("Введите заметку")

        self.text = tk.Text(self, height = 26, width = 35, bg="darkgreen", fg='white',
                            wrap='word', font=('Verdana', 10, 'bold'))
        self.text.pack()
        self.text.grid_propagate(True)
        self.btn = tk.Button(self, text='Choose the date', command = lambda : get_choose_date(self.get_tex()))
        self.btn.pack(ipady=10)


        self.geometry(f'300x465+{int(self.x) + int(self.width) + 12}+{int(self.y)}')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

    def get_tex(self):
        return self.text.get("0.0", "end-1c")


def show_notes_widget(coordinates):
    width, height, x, y = coordinates
    notes_widget=NotesWidget(width, height, x, y)
    notes_widget.mainloop()
