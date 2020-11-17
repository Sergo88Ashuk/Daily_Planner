

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
                self.but = tk.Button(self, text='0', width=4, height=2, activebackground='#555555',
                                 font=('Verdana', 16, 'bold'), command=lambda : show_my_notes(self.get_btn_txt(self.but)))
                self.but.grid(row=row, column=col, sticky='nsew')
                self.days.append(self.but)

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

    def prev_month(self):
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1
        self.fill()

    def next_month(self):
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        self.fill()

    def get_root_position(self):
        self.update_idletasks()
        self.width, self.height, self.x, self.y = re.split(r'[x+]', self.geometry())
        return self.width, self.height, self.x, self.y

    def get_btn_txt(self, but):
        button_text = but['text']
        print(button_text)
        return button_text


def show_calendar(coordinates):
    width, height, x, y = coordinates
    calendar=TheCalendar(width, height, x, y)
    calendar.mainloop()


















# def show_calendar():
#
#     root = Tk()
#     root.title('Calendar')
#
#     days = []
#     now = datetime.datetime.now()
#     year = now.year
#     month = now.month
#
# # Скидываем месяц и год до нужных значений
#     def prev_month():
#         nonlocal month, year
#         month -= 1
#         if month == 0:
#             month = 12
#             year -= 1
#         fill()
#
#     def next_month():
#         nonlocal month, year
#         month += 1
#         if month == 13:
#             month = 1
#             year += 1
#         fill()
#
# # Создаем кнопки пролистывания вперед и назад, а также надпись с месяцем и годом
#     prev_button = Button(root, text='<', command=prev_month)
#     prev_button.grid(row=0, column=0, sticky='nsew')
#     next_button = Button(root, text='>', command=next_month)
#     next_button.grid(row=0, column=6, sticky='nsew')
#     info_label = Label(root, text='0', width=1, height=1,
#                        font=('Verdana', 16, 'bold'), fg='blue')
#     info_label.grid(row=0, column=1, columnspan=5, sticky='nsew')
#
# # Создаем метки с аббревиатурами дней недель
#     for n in range(7):
#         lbl = Label(root, text=calendar.day_abbr[n], width=1, height=1,
#                     font=('Verdana', 10, 'normal'), fg='darkblue')
#         lbl.grid(row=1, column=n, sticky='nsew')
# # Создаем пустые кнопки под дни месяца и записываем в список days
#     for row in range(2, 8):
#         for col in range(7):
#             but = Button(root, text='0', width=4, height=2, activebackground='#555555',
#                          font=('Verdana', 16, 'bold'), command=lambda : show_notes_widget(get_root_position()))
#             but.grid(row=row, column=col, sticky='nsew')
#             days.append(but)
#
#     def get_root_position():
#         root.update_idletasks()
#         width, height, x, y = re.split(r'[x+]', root.geometry())
#         print(width, height, x, y)
#         return width, height, x, y
#
# # Создаем календарь
#     def fill():
# # Заполняем метку названием нужного месяца и года
#         info_label['text'] = calendar.month_name[month] + ', ' + str(year)
# # Узнаем количество дней в месяце по необходимости сдвигаем год или месяц
#         month_days = calendar.monthrange(year, month)[1]
#         if month == 1:
#             prev_month_days = calendar.monthrange(year-1, 12)[1]
#         else:
#             prev_month_days = calendar.monthrange(year, month - 1)[1]
# # Узнаем день недели сегодняшнего дня (от 0 до 6)
#         week_day = calendar.monthrange(year, month)[0]
# # Устанавливаем дату и цвет на кнопках текущего месяца
#         for n in range(month_days):
#             days[n + week_day]['text'] = n+1
#             days[n + week_day]['fg'] = 'black'
#             days[n + week_day]['background'] = 'lightgray'
#             if year == now.year and month == now.month and n == now.day:
#                 days[n + week_day-1]['background'] = 'green'
# # Устанавливаем дату и цвет предыдущего и следующего месяца
#         for n in range(week_day):
#             days[week_day - n - 1]['text'] = prev_month_days - n
#             days[week_day - n - 1]['fg'] = 'gray'
#             days[week_day - n - 1]['background'] = '#f3f3f3'
#         for n in range(6*7 - month_days - week_day):
#             days[week_day + month_days + n]['text'] = n+1
#             days[week_day + month_days + n]['fg'] = 'gray'
#             days[week_day + month_days + n]['background'] = '#f3f3f3'
#
#     fill()
#     root.mainloop()
