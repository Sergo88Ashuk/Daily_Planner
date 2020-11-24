

import tkinter as tk
from Notes_widget import show_notes_widget
from Display_notes import show_my_notes
import re
import calendar
import datetime


class TheCalendar(tk.Toplevel):
    def __init__(self, *args):
        tk.Toplevel.__init__(self)
        self.width, self.height, self.x, self.y = args
        self.init_child()

    def init_child(self):
        self.title('Calendar')
        self.days = []
        self.now = datetime.datetime.now()
        self.year = self.now.year
        self.month = self.now.month

        # Создаем кнопки пролистывания вперед и назад, а также надпись с месяцем и годом
        self.prev_button = tk.Button(self, text='<', command=self.prev_month)
        self.prev_button.grid(row=0, column=0, sticky='nsew')

        self.next_button = tk.Button(self, text='>', command=self.next_month)
        self.next_button.grid(row=0, column=6, sticky='nsew')

        self.info_label = tk.Label(self, text='0', width=1, height=1,
                           font=('Verdana', 16, 'bold'), fg='blue')
        self.info_label.grid(row=0, column=1, columnspan=5, sticky='nsew')

        self.geometry(f'+{int(self.x) + int(self.width) + 12}+{int(self.y)}')
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

        # Создаем метки с аббревиатурами дней недель
        for n in range(7):
            self.lbl = tk.Label(self, text=calendar.day_abbr[n], width=1, height=1,
                            font=('Verdana', 10, 'normal'), fg='darkblue')
            self.lbl.grid(row=1, column=n, sticky='nsew')
        # Создаем пустые кнопки под дни месяца и записываем в список days
        for row in range(2, 8):
            for col in range(7):
                but = tk.Button(self, text=col, width=4, height=2, activebackground='#555555',
                                 font=('Verdana', 16, 'bold'))
                but.config(command = lambda but=but, row=row, col=col : show_my_notes(self.get_btn_txt(but, row, col)))
                but.grid(row=row, column=col, sticky='nsew')
                self.days.append(but)
        self.fill()

    # Создаем календарь
    def fill(self):
    # Заполняем метку названием нужного месяца и года
        self.info_label['text'] = calendar.month_name[self.month] + ', ' + str(self.year)
    # Узнаем количество дней в месяце по необходимости сдвигаем год или месяц
        self.month_days = calendar.monthrange(self.year, self.month)[1]
        if self.month == 1:
            self.prev_month_days = calendar.monthrange(self.year-1, 12)[1]
        else:
            self.prev_month_days = calendar.monthrange(self.year, self.month - 1)[1]
    # Узнаем день недели сегодняшнего дня (от 0 до 6)
        self.week_day = calendar.monthrange(self.year, self.month)[0]
    # Устанавливаем дату и цвет на кнопках текущего месяца
        for n in range(self.month_days):
            self.days[n + self.week_day]['text'] = n+1
            self.days[n + self.week_day]['fg'] = 'black'
            self.days[n + self.week_day]['background'] = 'lightgray'
            if self.year == self.now.year and self.month == self.now.month and n == self.now.day:
                self.days[n + self.week_day-1]['background'] = 'green'
    # Устанавливаем дату и цвет предыдущего и следующего месяца
        for n in range(self.week_day):
            self.days[self.week_day - n - 1]['text'] = self.prev_month_days - n
            self.days[self.week_day - n - 1]['fg'] = 'gray'
            self.days[self.week_day - n - 1]['background'] = '#f3f3f3'
        for n in range(6*7 - self.month_days - self.week_day):
            self.days[self.week_day + self.month_days + n]['text'] = n+1
            self.days[self.week_day + self.month_days + n]['fg'] = 'gray'
            self.days[self.week_day + self.month_days + n]['background'] = '#f3f3f3'

    # Устанавливаем новые значения месяца
    def prev_month(self):
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1
        self.fill()

    # Устанавливаем новые значения месяца
    def next_month(self):
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        self.fill()

    # Понадобится для передачи своей геометрии
    # def get_root_position(self):
    #     self.update_idletasks()
    #     self.width, self.height, self.x, self.y = re.split(r'[x+]', self.geometry())
    #     return self.width, self.height, self.x, self.y

    # Извлекаем текст с числом месяца из кнопки
    def get_btn_txt(self, but, row, col):
        button_text = but['text']

        if but['text'] > 21 and row <= 3 and self.info_label['text'].split(',')[0] == 'January':
                return button_text, 12, int(self.info_label['text'].split(',')[1]) - 1
        elif but['text'] < 15 and row >= 6 and self.info_label['text'].split(',')[0] == 'December':
            return button_text, 1, int(self.info_label['text'].split(',')[1]) + 1
        elif but['text'] > 21 and row <= 3:
            return button_text, self.month - 1, self.year
        elif but['text'] < 15 and row >= 6:
            return button_text, self.month + 1, self.year
        else:
            return button_text, self.month, self.year




def show_calendar(coordinates):
    width, height, x, y = coordinates
    calendar=TheCalendar(width, height, x, y)
    calendar.mainloop()

# def get_root_position():
#     self.update_idletasks()
#     self.width, self.height, self.x, self.y = re.split(r'[x+]', self.geometry())
#     return self.width, self.height, self.x, self.y

