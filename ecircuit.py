class ECircuit():
    def __init__(self):
        self.items = []
        self.matrix = []
        self.itemLen = 6
        self.startIsValid = False # проверка на существование блока старт в таблице (items)

    def getMatrix(self):
        return self.matrix

    def build(self): # построение Е-схемы
        self.matrix = [[""] * len(self.items) * 15 for i in range(len(self.items) * 15)]
        self.elementSearch('START', self.items, [], 0, 0)
        self.addingLines()

    def show(self): # отображение Е-схемы на экране
        for i in range(len(self.matrix)):
            str = ""
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] in ["│",""]:
                    space = " " * (self.itemLen - len(self.matrix[i][j]))
                    str += space + self.matrix[i][j]
                elif self.matrix[i][j] in ["└","┌"]:
                    space = " " * (self.itemLen - len(self.matrix[i][j]))
                    str += space + self.matrix[i][j]
                else:
                    space = "─" * (self.itemLen - len(self.matrix[i][j]))
                    str += space + self.matrix[i][j]
            print(str)

    def elementSearch(self, searchingElement, items, foundedItems, mI, mJ): # рекурсивный спуск по дереву
        if searchingElement == 'END':  # Если элемент указывает на конец то пишем конец
            self.matrix[mI][mJ] = 'END'
        else:
            for index in range(len(items)):  # перебор введенных смежностей
                if searchingElement == items[index][0]:  # если нашли такой
                    if index in foundedItems:  # и если он уже вызывался в ветке
                        self.matrix[mI][mJ] = searchingElement  # добавляем в матрицу
                    else:  # иначе
                        foundedItems.append(index)  # помечаем как найденный
                        if items[index][-1] == '0':  # проверяем на тип "функциональный"
                            self.matrix[mI][mJ] = searchingElement  # если да, то отображаем и идем по ветке далее
                            mI = self.elementSearch(items[index][1], items, foundedItems.copy(), mI, mJ + 1)
                        else:  # иначе он является предикатным
                            self.matrix[mI][mJ] = searchingElement  # отображаем в матрице
                            self.moveMatrix(mI)  # перемещаем текущую и нижние строки на 1 вниз
                            self.matrix[mI][mJ] = "┌"  # добавляем уголок и идем далее по правдивой ветке
                            mI = self.elementSearch(items[index][1], items, foundedItems.copy(), mI, mJ + 1)
                            mI += 1  # становимся на центр предиката
                            self.moveMatrix(mI + 1)  # двигаем матрицу вниз без текущей строки
                            self.matrix[mI + 1][mJ] = "└"  # добавляем уголок и идем далее по ложной ветке
                            mI = self.elementSearch(items[index][2], items, foundedItems.copy(), mI + 1, mJ + 1)
        return mI

    def addingLines(self):  # добавление связующих вертиакальных линий
        for i in range(len(self.matrix)):  # добавляем горизонтальные линии
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == "└":
                    for k in range(i - 1, 0 - 1, -1):
                        if self.matrix[k][j] == "│" or self.matrix[k][j] == "":
                            self.matrix[k][j] = "│"
                        else:
                            break
                elif self.matrix[i][j] == "┌":
                    for k in range(i + 1, len(self.matrix), 1):
                        if self.matrix[k][j] == "│" or self.matrix[k][j] == "":
                            self.matrix[k][j] = "│"
                        else:
                            break

    def itemIsValid(self, item):    # проверка корректности строки из таблицы смежности
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

    def setTable(self, newItems): # задам таблицу смежности из готового списка
        self.__init__()
        for item in newItems:
            if self.itemIsValid(item):
                self.items.append(item)

    def getTable(self):
        return self.items

    def enterTable(self):   # ввод таблиц смежности с клавиатуры
        self.__init__()
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

    def moveMatrix(self, startRow): # сдвиг части матрицы вниз
        for i in range(len(self.matrix[0]) - 2, startRow - 1, -1):
            for j in range(len(self.matrix)):
                self.matrix[i + 1][j] = self.matrix[i][j]
        for j in range(len(self.matrix)):
            self.matrix[startRow][j] = ""

    def resizeMatrix(self):
        for index in range(len(self.matrix)):
            while len(self.matrix[index]) != 0 and self.matrix[index][-1] == "":
                self.matrix[index].pop(-1)
        newMatrix = []
        for row in self.matrix:
            if row != []:
                newMatrix.append(row)
        self.matrix = newMatrix
