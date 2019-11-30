from ecircuit_bould import *
from ecircuit_draw import *
from ecircuit_minimize import *

class Mode:
    graphic = 1
    console = 2


class ECircuit():
    def __init__(self, mode: Mode = Mode.console):
        self.mode = mode
        self.builder = ECircuit_Build()
        self.minimizer = ECircuit_Minimize()

        self.items = []
        self.matrix = []
        self.itemLen = 6
        self.startIsValid = False  # проверка на существование блока старт в таблице (items)

    def show(self): # отображение Е-схемы на экране
        if self.mode == Mode.graphic:
            self._graphic_show()
        if self.mode == Mode.console:
            self._console_show()

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
        painter.setTextSetting(self.builder.getItemLen(), 10)
        painter.draw()

    def build(self, add_knots: bool = True):
        self.builder.setTable(self.items)
        self.builder.build(add_knots)
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

    def setTable(self, newItems): # задам таблицу смежности из готового списка
        self.items = []
        self.matrix = []
        self.itemLen = 6
        self.startIsValid = False  # проверка на существование блока старт в таблице (items)
        for item in newItems:
            if self.itemIsValid(item):
                self.items.append(item)