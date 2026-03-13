# Импорт библиотеки Tkinter
import tkinter as tk

from PIL import Image, ImageTk

img = Image.open("fruits.png")


# Загружает все методы из данной библиотеки
from tkinter import *


class Main:

    # Создаю основное окно приложения
    window = Tk()

    # Называю главное окно
    window.title("Меню ресторана 'Клод-Моне':")

    # Указываю явный размер окна, где будет меню:
    window.geometry("1000x700")

    # Указываем, какой фон у нас будет по дефолту
    window.config(bg="black")

    # Функция, которая заставляет работать наше окно постоянно
    def run(self):
        self.window.mainloop()


class Menu(Main):

    def __init__(
        self,
        text,
        color,
        position,
        position_text,
        posX,
        posY,
        width,
        font_name,
        font_size,
        right_pos,
    ):

        # Запоминаем полученный текст
        self.text = text

        # Запоминаем полученный цвет
        self.color = color

        # Запоминаем полученную позицию ОБЛАСТИ ТЕКСТА!
        self.position = position

        # Запоминаем положение нашего текста ВНУТРИ области
        self.position_text = position_text

        # Запоминаем полученные координаты X
        self.posX = posX

        # Запоминаем полученные координаты Y
        self.posY = posY

        # Запоминаем ширину ОБЛАСТИ нашего текста!
        self.width = width

        # Задаем тип шрифта
        self.font_name = font_name

        # Задаем размер шрифта
        self.font_size = font_size

        # Если меню справа
        self.right_pos = right_pos

        # Label используется для "Поверхностного представления" нашего текста
        lbl = Label(
            self.window,
            text=self.text,
            bg=self.color,
            width=self.width,
            anchor=self.position_text,
            font=(self.font_name, self.font_size),
        )

        # .pack() Используется для воплощения нашего "представления" на экране
        lbl.pack(anchor=self.position, padx=self.posX, pady=self.posY)

        if self.right_pos[0] == "+":

            x_pos, y_pos = self.right_pos.split()[1], self.right_pos.split()[2]
            lbl.place(x=x_pos, y=y_pos)


class Dishes(Main):

    def __init__(
        self,
        text,
        posX,
        posY,
        font_name,
        font_size,
        grams,
        price,
    ):
        # Текст
        self.text_1 = text

        # положение X
        self.posX = posX

        # положение Y
        self.posY = posY

        # название шрифта
        self.font_name = font_name

        # размер
        self.font_size = font_size

        # граммы
        self.grams = grams

        # цена
        self.price = price

        # Печатается само блюдо
        text_widget = Text(
            self.window,
            width=55,
            height=20,
            wrap="word",
            fg="white",
            bg="black",
            borderwidth=0,
            padx=0,
            pady=0,
            font=(self.font_name, self.font_size),
        )

        # Место, куда вставляется текст
        text_widget.insert("1.0", chars=self.text_1)

        # Отрисовка
        text_widget.pack()

        # Расположение
        text_widget.place(x=self.posX, y=self.posY)

        # Отрисовывает граммовку и цену
        price_widget = Label(
            self.window,
            text=f"{self.grams}     {self.price}",
            bg="black",
            fg="white",
            font=(self.font_name, self.font_size),
        )

        price_widget.pack()

        price_widget.place(x=self.posX + 590, y=self.posY)


# Инициализирую род. класс
obj_main = Main()

# Аргументы: Текст, цвет фона у текста, расположение
obj = Menu("ПЕРВОЕ БЛЮДО", "blue", "w", "w", 4, 30, 45, "Arial", 19, "-")

# Аргументы для меню 1
obj_dishes1 = Dishes(
    'Суп "Харчо" с курицей',
    5,
    68,
    "Arial",
    12,
    250,
    90.00,
)

obj_dishes2 = Dishes("Суп-крем из шпината и картофеля", 5, 90, "Arial", 12, 250, 135.00)

obj_menu2 = Menu("ВТОРЫЕ БЛЮДА", "blue", "w", "w", 4, 36, 45, "Arial", 19, "-")

obj_dishes3 = Dishes(
    "Котлета 'По-Кишиневски' с макаронами", 4, 169, "Arial", 12, 220, 205.00
)

obj_dishes4 = Dishes(
    "Спагетти с ветчиной, сыром в сливочном соусе", 4, 194, "Arial", 12, 220, 205.00
)

obj_dishes5 = Dishes("Котлета по-кишиневски с гречей", 4, 218, "Arial", 12, 220, 205.00)

obj_dishes6 = Dishes("Свинина в яйце с рисом", 4, 240, "Arial", 12, 250, 257.00)

obj_dishes7 = Dishes("Грудка куриная с паприкой", 4, 263, "Arial", 12, 250, 285.00)

obj_dishes8 = Dishes("Тефтели куриные с макаронами", 4, 285, "Arial", 12, 220, 165.00)

obj_dishes9 = Dishes("Тефтели куриные с гречей", 4, 305, "Arial", 12, 220, 165.00)

obj_dishes10 = Dishes(
    "Стофато из филе цыпленка с макаронами", 4, 325, "Arial", 12, 220, 225.00
)

obj_dishes11 = Dishes(
    "Стофато из филе цыпленка с рисом", 4, 345, "Arial", 12, 220, 235.00
)

obj_dishes12 = Dishes("Котлета по кишиневски с рисом", 4, 365, "Arial", 12, 220, 215.00)

obj_menu3 = Menu("САЛАТЫ", "blue", "e", "w", 5, 10, 60, "Arial", 19, "+ 853 30")

obj_dishes13 = Dishes("Салат 'Цезарь' с курицей", 854, 66, "Arial", 12, 120, 140.00)

obj_dishes14 = Dishes("Крабовый", 854, 86, "Arial", 12, 100, 85.00)

obj_dishes15 = Dishes("Салат 'Крымский'", 854, 106, "Arial", 12, 120, 95.00)

img_fruits = ImageTk.PhotoImage(img)

c = Canvas()

c.create_image(1, 1, anchor="w", image=img_fruits)

c.pack()

c.place(x=1150, y=630)


# Родительский класс запускает постоянное окно
obj_main.run()
