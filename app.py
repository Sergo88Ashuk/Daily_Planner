

import tkinter as tk
import re
# from Calendar import show_calendar
import Calendar
from Notes_widget import show_notes_widget


class MainMenu(tk.Frame):
    def __init__(self, parent,):
        super().__init__(parent)
        self.init_main()

        # Configuring Frame object on the Main window
    def init_main(self):
        self.btn1 = tk.Button(text='Show my notes', width=20, height=3,
                              command=lambda : Calendar.show_calendar(self.get_root_position()))
        self.btn2 = tk.Button(text='Enter your notes', width=20, height=3,
                              command=lambda : show_notes_widget(self.get_root_position()))

        self.btn1.pack()
        self.btn2.pack()

    def get_root_position(self):
        self.update_idletasks()
        self.width, self.height, self.x, self.y = re.split(r'[x+]', root.geometry())
        return self.width, self.height, self.x, self.y


def dock(master):
    width, height, x, y = re.split(r'[x+]', Calendar.get_root_position())
    # x = int(x) + master.winfo_width()
    master.geometry(f"+{x}+{y}")


if __name__ == '__main__':
    # Creating Main window
    root = tk.Tk()
    root.title('ИВРО')
    root.update_idletasks()
    root.width = 180
    root.height = 110
    root.x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    root.y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry(f'{root.width}x{root.height}+{int(root.x - root.width / 2)}+{int(root.y - root.height / 2)}')
    root.resizable(False, False)

    # Creating Frame object
    app = MainMenu(root)
    app.pack()
    # root.bind("<Configure>", lambda event: dock(root))

    root.mainloop()
