import sys
import os

from PyQt5.QtCore import QObject

from functions.ecircuit_bould import *
from functions.ecircuit_draw import *
from functions.ecircuit_minimize import *


class Mode:
    graphic = 1
    console = 2

class ECircuit:
    def __init__(self, mode: Mode = Mode.console):
        self.mode = mode
        self.builder = ECircuit_Build()
        self.minimizer = ECircuit_Minimize()

        self.items = []
        self.matrix = []
        self.itemLen = 6
        self.startIsValid = False  # проверка на существование блока старт в таблице (items)

        self.menu_items = [
            ["| Ввод таблицы смежности        |", [self.enterTable]],
            ["| Генерировать Е-Схему          |", [self.build, self.show]],
            ["| Минимизировать Е-Схему        |", [self.build, self.minimize, self.build, self.show]],
            ["| Отобразить таблицу смежности  |", [self.show_items]],
            ["| Выйти из программы            |", [self.get_quit]]
        ]

    def get_quit(self):
        sys.exit(0)

    def show(self): # отображение Е-схемы на экране
        if self.mode == Mode.graphic:
            print("Отрисовка схемы в отдельном окне...")
            self._graphic_show()
            os.system('cls')
        if self.mode == Mode.console:
            self._console_show()

    def show_items(self):
        for item in self.items:
            print(",".join(item))


    def _console_show(self):
        matrix = self.builder.getMatrix()
        for i in range(len(self.builder.getMatrix())):
            str = ""
            for j in range(len(matrix[i])):
                if matrix[i][j] in ["│",""]:
                    space = " " * (self.builder.itemLen - len(matrix[i][j]))
                    str += space + matrix[i][j]
                elif matrix[i][j] in ["└","┌"]:
                    space = " " * (self.builder.itemLen - len(matrix[i][j]))
                    str += space + matrix[i][j]
                else:
                    space = "─" * (self.builder.itemLen - len(matrix[i][j]))
                    str += space + matrix[i][j]
            print(str)

    def _graphic_show(self):
        painter = ECircuit_Draw()
        painter.setMatrix(self.builder.getMatrix())
        painter.setTextSetting(self.builder.getItemLen(), 8)
        painter.draw()
        del painter

    def build(self):
        self.builder.setTable(self.items)
        self.builder.build()
        self.items = self.builder.getTable()
        self.matrix = self.builder.getMatrix()
        self.itemLen = self.builder.getItemLen()

    def minimize(self):
        self.minimizer.setTable(self.items)
        self.minimizer.build()
        self.items = self.minimizer.getTable()

    def getTable(self):
        return self.items

    def itemIsValid(self, item):  # проверка корректности строки из таблицы смежности
        if len(item) == 3:
            if item[0] == "START":
                if not self.startIsValid:
                    self.startIsValid = True
                    return True
                else:
                    self.startIsValid = False
                    return False
            elif item[0] == "END":
                return False
            else:
                if self.itemLen < len(max(item, key=len)):
                    self.itemLen = len(max(item, key=len))
                    if self.itemLen % 2 != 0:
                        self.itemLen += 1
                return True
        else:
            return False

    def enterTable(self):   # ввод таблиц смежности с клавиатуры
        self.items = []
        self.itemLen = 6
        self.startIsValid = False  # проверка на существование блока старт в таблице (items)
        print("Введите матрицу смежности\nДля завершения ввода нажмите 'exit'")
        while True:
            item = input().upper().split(',')
            if self.itemIsValid(item):
                self.items.append(item)
            elif item == ['EXIT']:
                if len(self.items) == 0:
                    print("Таблица пустая!")
                elif not self.startIsValid:
                    print("Не найден блок START!")
                else:
                    break
            else:
                print("Для завершения ввода нажмите 'exit'")
        os.system('cls')

    def setTable(self, newItems): # задам таблицу смежности из готового списка
        self.items = []
        self.matrix = []
        self.itemLen = 6
        self.startIsValid = False  # проверка на существование блока старт в таблице (items)
        for item in newItems:
            if self.itemIsValid(item):
                self.items.append(item)

    def start(self):
        os.system('cls')
        while True:
            try:
                size = 0
                for item in self.menu_items:
                    size += 1
                    print("{0} {1}".format(size, item[0]))
                cin = input("Выберите пункт меню >> ")
                os.system('cls')
                if int(cin) in range(0, size + 1):
                    for foo in self.menu_items[int(cin) - 1][1]:
                        foo()
            except Exception as e:
                continue