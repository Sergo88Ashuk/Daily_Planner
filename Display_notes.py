

import tkinter as tk

class DisplayNotes(tk.Toplevel):
    def __init__(self, text):
        tk.Toplevel.__init__(self)
        self.content = text
        self.init_child()

    def init_child(self):
        self.title('Your current notes')

        self.text = tk.Text(self, height=26, width=35, bg="darkgreen", fg='white',
                            wrap='word', font=('Verdana', 10, 'bold'))
        self.text.insert('0.0', self.content)
        self.text.pack()
        self.text.grid_propagate(True)

def show_my_notes(text):
    my_notes = DisplayNotes(text)
    my_notes.mainloop()
