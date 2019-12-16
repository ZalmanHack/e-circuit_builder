import os

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal

from functions.ecircuit_bould import *
from functions.ecircuit_draw import *
from functions.ecircuit_minimize import *
from functions.ecircuit_structuring import *


class ECircuit(QObject):
    built = pyqtSignal(list, list, list, int, int)
    error = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.builder = ECircuit_Build()
        self.minimizer = ECircuit_Minimize()
        self.structurer = ECircuit_Structuring()

        self.items = []
        self.matrix = []
        self.itemLen = 6
        self.quantityKnots = 0
        self.branches = 0
        self.startIsValid = False  # проверка на существование блока старт в таблице (items)
        self.menu_items = [
            ["| Ввод таблицы смежности        |", [self.enterTable]],
            ["| Генерировать Е-Схему          |", [self.build, self.show]],
            ["| Минимизировать Е-Схему        |", [self.build, self.minimize, self.build, self.show]],
            ["| Отобразить таблицу смежности  |", [self.show_items]]
        ]

    def show(self):  # отображение Е-схемы на экране
        self._console_show()

    def show_items(self):
        for item in self.items:
            print(",".join(item))

    def _console_show(self):
        matrix = self.builder.getMatrix()
        for i in range(len(self.builder.getMatrix())):
            str = ""
            for j in range(len(matrix[i])):
                if matrix[i][j] in ["│", ""]:
                    space = " " * (self.builder.itemLen - len(matrix[i][j]))
                    str += space + matrix[i][j]
                elif matrix[i][j] in ["└", "┌"]:
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

    def _build(self, add_knots: bool = True):
        self.builder.setTable(self.items)
        self.builder.build(add_knots)
        self.items = self.builder.getTable()
        self.matrix = self.builder.getMatrix()
        self.itemLen = self.builder.getItemLen()
        self.branches = self.builder.get_branches()
        self.quantityKnots = self.builder.knot_quantity
        self.show()

    @pyqtSlot()
    def build(self):
        self._build()
        self.built.emit(self.branches, self.matrix, [], self.itemLen, self.quantityKnots)

    @pyqtSlot()
    def minimize(self):
        if self.items:
            self._build()
            if self.minimizer.setTable(self.items):
                self.minimizer.build()
                self.items = self.minimizer.getTable()
                self._build()
                self.built.emit(self.branches, self.matrix, self.items, self.itemLen, self.quantityKnots)
            else:
                self.error.emit("Минимизация с Case элементами не возможна.\n")

    @pyqtSlot()
    def structuring(self):
        if self.items:
            if self.structurer.setTable(self.items):
                self.structurer.build()
                self.items = self.structurer.getTable()
                self._build(add_knots=False)
                self.built.emit(self.branches, self.matrix, self.items, self.itemLen, self.quantityKnots)
            else:
                self.error.emit("Структурирование не возможно.\n"
                                "Таблица смежности уже имеет Case элементы")

    def option_check(self, items: list):
        option = [
            [
                ['START', 'A', '0'], ['A', 'X', '0'], ['X', 'C', 'B'], ['C', 'Y', '0'], ['Y', 'D', 'Z'],
                ['D', 'Y', '0'],
                ['B', 'Z', '0'], ['Z', 'G', 'U'], ['U', 'V', 'T'], ['G', 'M', '0'], ['M', 'W', '0'], ['W', 'M', 'END'],
                ['V', 'K', 'H'], ['H', 'END', '0'], ['K', 'P', '0'], ['P', 'L', 'END'], ['L', 'K', '0'],
                ['T', 'F', '0'],
                ['F', 'N', '0'], ['N', 'R', '0'], ['R', 'N', 'Q'], ['Q', 'N', 'Z']
            ],
            [
                ['START', '4.1/10', '0'], ['4.1/10', '(5)', '0'], ['Z', '2.2/5', 'U'], ['U', '2.3/7', '2.4/10'],
                ['2.2/5', 'END', '0'], ['2.3/7', 'END', '0'], ['2.4/10', '(5)', '0'], ['(5)', 'Z', '0']
            ],
            [
                ['(1)', 'I==0', '0'], ['I==0', 'END', 'I==1'], ['I==1', '4.1/10', 'I==4'], ['I==4', 'U', 'I==6'],
                ['I==6', '2.4/10', '(1)'], ['START', 'I=1', '0'], ['4.1/10', 'Z', '0'], ['Z', '2.2/5', 'I=4'],
                ['U', '2.3/7', 'I=6'], ['2.2/5', 'I=0', '0'], ['2.3/7', 'I=0', '0'], ['2.4/10', 'Z', '0'],
                ['I=0', '(1)', '0'], ['I=1', '(1)', '0'], ['I=4', '(1)', '0'], ['I=6', '(1)', '0']
            ]
        ]
        for opt in option:
            check = True
            for index in range(0, len(items)):
                if ' '.join(items[index]).upper() != ' '.join(opt[index]).upper():
                    check = False
                    break
            if check:
                return True
        return False

    @pyqtSlot(list)
    def setTable(self, newItems):  # задам таблицу смежности из готового списка
        if not self.option_check(newItems):
            self.error.emit("Введенная таблица смежности не соответствует вашему варианту.")
            return
        self.items = []
        self.matrix = []
        self.itemLen = 6
        self.quantityKnots = 0
        self.branches = 0
        self.startIsValid = False  # проверка на существование блока старт в таблице (items)
        for item in newItems:
            if self.itemIsValid(item):
                self.items.append(item)

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

    def enterTable(self):  # ввод таблиц смежности с клавиатуры
        self.items = []
        self.itemLen = 6
        self.quantityKnots = 0
        self.branches = 0
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


if __name__ == "__main__":
    test = ECircuit()
    test.start()
