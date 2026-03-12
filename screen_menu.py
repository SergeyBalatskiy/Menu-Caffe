# Импорт библиотеки Tkinter
import tkinter as tk

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
            width=70,
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

        price_widget.place(x=self.posX + 675, y=self.posY)


# Инициализирую род. класс
obj_main = Main()

# Аргументы: Текст, цвет фона у текста, расположение
obj = Menu("Первое блюдо", "blue", "w", "w", 4, 30, 50, "Arial", 19)

# Аргументы для меню 1
obj_dishes = Dishes(
    'Суп "Харчо" с курицей',
    5,
    68,
    "Arial",
    12,
    220,
    250,
)


# Родительский класс запускает постоянное окно
obj_main.run()
