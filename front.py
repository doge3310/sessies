from tkinter import Tk, ttk
import tkinter as tk
from math import cos, sin
from db_init import VendMachine


class Main(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.pack()

        self.up_frame = tk.Frame(master)
        self.main_frame = tk.Frame(master)
        self.left_bar_frame = tk.Frame(master, background="grey")
        self.current_page = tk.Frame(master, background="grey")

        self.logo_canv = tk.Canvas(self.up_frame)
        self.logo_canv.create_text(50, 50, text="LOGO", font=("Arial", 15))

        self.person_canv = tk.Canvas(self.up_frame)
        self.person_canv.create_text(70, 40, text="Пенисенко ВВВ", font=("Arial", 13))
        self.person_canv.create_text(70, 70, text="Администратор", font=("Arial", 13))
        self.person_settings = ttk.Combobox(self.up_frame, values=["Мои сессии", "Мой профиль", "Выход"])

        self.main_button = tk.Button(self.left_bar_frame, text="Главная", command=self.main_window)
        self.ta_monitor_but = tk.Button(self.left_bar_frame, text="Монитор ТА")
        self.report_list = ttk.Combobox(self.left_bar_frame, values=["Детальные отчёты"])
        self.record_tmc = ttk.Combobox(self.left_bar_frame, values=["Учёт ТМЦ"])
        self.administr_list = ttk.Combobox(self.left_bar_frame, values=["Дополнительное",
                                                                        "Торговые автоматы",
                                                                        "Пользователи",
                                                                        "Компании",
                                                                        "Модемы"])

        self.page_name = tk.Label(self.current_page, text="ООО Торговые Автоматы", font=("Arial", 15))
        self.current_dir = tk.Label(self.current_page, text="Главная", font=("Arial", 15))

        self.up_frame.place(x=0, y=0, width=1500, height=100)
        self.main_frame.place(x=300, y=150, width=1200, height=600)
        self.left_bar_frame.place(x=0, y=100, width=300, height=600)
        self.logo_canv.place(x=0, y=0, width=100, height=100)
        self.person_canv.place(x=1350, y=0, width=150, height=100)
        self.person_settings.place(x=1350, y=80)
        self.main_button.place(x=10, y=0)
        self.ta_monitor_but.place(x=10, y=50)
        self.report_list.place(x=10, y=100)
        self.record_tmc.place(x=10, y=150)
        self.administr_list.place(x=10, y=200)
        self.current_page.place(x=300, y=100, width=1200, height=50)
        self.page_name.place(x=0, y=10)
        self.current_dir.place(x=1000, y=10)

        self.main_window()
        self.administr_list.bind("<<ComboboxSelected>>", self.choice)

    def clear_main(self):
        for item in self.main_frame.winfo_children():
            item.destroy()

    def choice(self, event=None):
        match self.administr_list.get():
            case "Торговые автоматы":
                self.vend_machine()

    def main_window(self):
        self.clear_main()

        net_efficient = 30
        net_status = 300
        brief_data = [1000, 122, 124, 3563, 374563, 8756, "2/8"]
        sell_data = [100, 200, 50, 100, 20, 170, 200]
        news = ["kdslfb", "slkdnjghlnjkd", "skdhjfgb", "dskjgf", "slgfdihuldsif", "dsjfghbdsjhbkfdsjb"]
        xStep = 30

        self.name = tk.Canvas(self.main_frame)
        self.name.create_text(150, 20, text="Личный кабинет. Главная", font=("Arial", 15))

        self.net_efficient = tk.Canvas(self.main_frame, background="white")
        self.net_efficient.create_text(70, 20, text="Эффективность сети", font=("Arial", 10))
        self.net_efficient.create_arc(50, 50, 250, 250, start=0, extent=180, fill="green")
        self.net_efficient.create_line(150, 150, 150 + 100 * cos(net_efficient), 150 + 100 * sin(net_efficient))

        self.net_status = tk.Canvas(self.main_frame, background="white")
        self.net_status.create_text(70, 20, text="Состояние сети", font=("Arial", 10))
        self.net_status.create_arc(70, 40, 220, 190, start=0, extent=net_status, fill="blue")
        self.net_status.create_oval(80, 50, 210, 180, fill="white", outline="")

        self.brief = tk.Canvas(self.main_frame, background="white")
        self.brief.create_text(70, 20, text="Сводка", font=("Arial", 10))
        self.ta_money = tk.Label(self.main_frame, text=f"Денег в ТА {brief_data[0]}")
        self.ta_return = tk.Label(self.main_frame, text=f"Сдача в ТА {brief_data[1]}")
        self.money_tod = tk.Label(self.main_frame, text=f"Выручка сегодня {brief_data[2]}")
        self.money_yes = tk.Label(self.main_frame, text=f"Выручка вчера {brief_data[3]}")
        self.incas_tod = tk.Label(self.main_frame, text=f"Инкассировано сегодня {brief_data[4]}")
        self.incas_yes = tk.Label(self.main_frame, text=f"Инкассированно вчера {brief_data[5]}")
        self.servesed = tk.Label(self.main_frame, text=f"Обслужено сег.\вчера {brief_data[6]}")

        self.sell_dinamic = tk.Canvas(self.main_frame, background="white")
        self.sell_dinamic.create_text(130, 20, text="Динамика продаж за последние 10 дней", font=("Arial", 10))
        for index, item in enumerate(sell_data):
            self.sell_dinamic.create_rectangle((index + 1) * xStep, item, ((index + 1) * xStep) + 20, 200)

        self.news = tk.Canvas(self.main_frame, background="white")
        self.news.create_text(130, 20, text="Новости", font=("Arial", 10))
        for index, item in enumerate(news):
            self.lab = tk.Label(self.main_frame, text=item)
            self.lab.place(x=720, y=270 + ((index + 1) * xStep))

        self.name.place(x=0, y=0)
        self.net_efficient.place(x=50, y=50, width=300, height=200)
        self.net_status.place(x=400, y=50, width=300, height=200)
        self.brief.place(x=750, y=50, width=300, height=200)
        self.ta_money.place(x=770, y=80)
        self.ta_return.place(x=770, y=100)
        self.money_tod.place(x=770, y=120)
        self.money_yes.place(x=770, y=140)
        self.incas_tod.place(x=770, y=160)
        self.incas_yes.place(x=770, y=180)
        self.servesed.place(x=770, y=200)
        self.sell_dinamic.place(x=50, y=250, width=600, height=250)
        self.news.place(x=700, y=250, width=300, height=250)

    def vend_machine(self):
        self.clear_main()

        columns = ["ID", "Название автомата", "Модель", "Компания", "Модем", "Адрес\место", "В работе с", "Действия"]

        self.table = ttk.Treeview(self.main_frame, columns=columns, show="headings")
        self.table.heading("ID", text="ID")
        self.table.column("ID", width=50)
        self.table.heading("Название автомата", text="Название автомата")
        self.table.heading("Модель", text="Модель")
        self.table.column("Модель", width=100)
        self.table.heading("Компания", text="Компания")
        self.table.column("Компания", width=100)
        self.table.heading("Модем", text="Модем")
        self.table.column("Модем", width=100)
        self.table.heading(r"Адрес\место", text=r"Адрес\место")
        self.table.heading("В работе с", text="В работе с")
        self.table.column("В работе с", width=100)
        self.table.heading("Действия", text="Действия")
        self.table.column("Действия", width=100)

        self.add_button = tk.Button(self.main_frame, text="Добавить", command=self.create_machine)
        self.export_button = tk.Button(self.main_frame, text="Экспорт")
        self.sort_line = tk.Entry(self.main_frame)
        self.title = tk.Label(self.main_frame, text="Торговый автомат", font=("Arial", 15))

        self.table.place(x=50, y=100, width=1100, height=600)
        self.add_button.place(x=900, y=25)
        self.export_button.place(x=1000, y=25)
        self.sort_line.place(x=550, y=25, width=200, height=25)
        self.title.place(x=50, y=25)

        self.add_vend_machine()

    def add_vend_machine(self):
        lst = VendMachine.select()
        for i in lst:
            self.table.insert("", tk.END, values=[i.id, i.name, i.model, i.firm, i.modem, i.adress, i.date_expluatation])

    def create_machine(self):
        self.clear_main()

        lst = [
            tk.Label(self.main_frame, text="Название ТА"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Производитель ТА"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Модель ТА"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Режим работы"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Производитель ТА (Slave)"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Модель ТА (Slave)"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Адрес"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Место"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Координаты"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Номер автомата"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Время работы"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Часовой пояс"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Товарная матрица"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Шаблон крит. значений"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Шаблон уведомлений"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Клиент"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Менеджер"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Инженер"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Техник-оператор"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Платёжные системы"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="RFID карты обслужывания"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="RFID карты инкасации"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="RFID карты загрузки"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="id кассы Kit Online"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Приоритет обслуживания"),
            tk.Entry(self.main_frame),
            tk.Label(self.main_frame, text="Модем"),
            tk.Entry(self.main_frame),
        ]

        for index, item in enumerate(lst):
            x_step = (index // 2) % 3
            y_step = (index // 2) // 3
            offset_x = (index % 2) * 160
            item.place(x=x_step * (120 + 160) + offset_x, y=70 * y_step)

        self.create_button = tk.Button(self.main_frame, text="Создать")
        self.dell = tk.Button(self.main_frame, text="Отменить")

        self.create_button.place(x=900, y=500, width=80, height=20)
        self.dell.place(x=1000, y=500, width=80, height=20)


if __name__ == "__main__":
    master = Tk()
    main_window = Main(master)
    master.geometry("1500x700")
    master.mainloop()
