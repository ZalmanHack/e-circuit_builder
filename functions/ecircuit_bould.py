class ECircuit_Build():
    def __init__(self):
        self.items = []
        self.knot_quantity = 0
        self.element_with_knots = []
        self.matrix = []
        self.itemLen = 6
        self.branches = []  # массив веток (для вовда веток построчно в интерфесе)
        self.startIsValid = False # проверка на существование блока старт в таблице (items)

    # проверка на то, является ли элемент узлом ________________________________________________________________________
    def _is_knot(self, searchingElement: str):
        if searchingElement[0] == "(" or searchingElement[-1] == ")":
            return True
        return False

    # добавление найденой полноценной вктки в массив веток (нужно только для вывода в интерфейсе) ______________________
    def appendBranches(self, foundRows: list, searchingElement: str):
        result = []
        for row in foundRows:
            result.append(self.items[row][0])
        result.append(searchingElement)
        self.branches.append(result)

    # проход по таблице и создание узлов _______________________________________________________________________________
    def _add_knot(self, searchingElement):
        if searchingElement not in self.element_with_knots:
            self.element_with_knots.append(searchingElement)
            if searchingElement[0] != "(" or searchingElement[-1] != ")":
                self.knot_quantity += 1
                knot = "({0})".format(self.knot_quantity)
                self.items.append([knot, searchingElement, "0"])
                # перебираем все вторые и третьи колонки и меняем искомый элемент на наш узел
                for item in self.items[:-1]:
                    for i in [1, 2]:
                        if item[i] == searchingElement:
                            item[i] = knot

    # рекурсивный спуск по дерев для создания узлов ____________________________________________________________________
    def _create_knots(self, searchingElement, foundedItems):
        if searchingElement != 'END':             # Если элемент указывает на конец то пишем конец
            for index in range(len(self.items)):  # перебор введенных смежностей
                if searchingElement == self.items[index][0]:  # если нашли такой
                    if index in foundedItems:    # и если он уже вызывался в ветке
                        # создание узла (очень нужно для 2 проги)
                        self._add_knot(searchingElement)
                    else:  # иначе
                        foundedItems.append(index)        # помечаем как найденный
                        if self.items[index][-1] == '0':  # проверяем на тип "функциональный"
                            foundedItems = self._create_knots(self.items[index][1], foundedItems.copy())
                        else:  # иначе он является предикатным
                            foundedItems = self._create_knots(self.items[index][1], foundedItems.copy())
                            foundedItems = self._create_knots(self.items[index][2], foundedItems.copy())
                    break
        return foundedItems

    # проход по таблице и создание матрицы _____________________________________________________________________________
    def _elementSearch(self, searchingElement, foundedItems, mI, mJ): # рекурсивный спуск по дереву
        if searchingElement == 'END':  # Если элемент указывает на конец то пишем конец
            self.appendBranches(foundedItems, searchingElement)                  # добавляем новую ветку
            self.matrix[mI][mJ] = 'END'
        else:
            for index in range(len(self.items)):                # перебор введенных смежностей
                if searchingElement == self.items[index][0]:    # если нашли такой
                    if index in foundedItems:                   # и если он уже вызывался в ветке
                        self.appendBranches(foundedItems, searchingElement)      # добавляем новую ветку
                        if self._is_knot(searchingElement):     # если это узел то идем назад и пишем его на месте черты
                            mJ -= 1
                        self.matrix[mI][mJ] = searchingElement  # добавляем в матрицу
                    else:  # иначе
                        foundedItems.append(index)                  # помечаем как найденный
                        if self._is_knot(searchingElement):         # если это узел то пишем нго вместо прошлой -
                            mJ -= 1
                            self.matrix[mI][mJ] = searchingElement  # если да, то отображаем и идем по ветке далее
                            mI = self._elementSearch(self.items[index][1], foundedItems.copy(), mI, mJ + 1)
                        elif self.items[index][-1] == '0':            # проверяем на тип "функциональный"
                            self.matrix[mI][mJ] = searchingElement  # если да, то отображаем и идем по ветке далее
                            mJ += 1
                            self.matrix[mI][mJ] = "─"
                            mI = self._elementSearch(self.items[index][1], foundedItems.copy(), mI, mJ + 1)
                        else:  # иначе он является предикатным
                            self.matrix[mI][mJ] = searchingElement + "┤"  # отображаем в матрице
                            self._moveMatrix(mI)       # перемещаем текущую и нижние строки на 1 вниз
                            self.matrix[mI][mJ] = "┌"  # добавляем уголок и идем далее по правдивой ветке
                            self.matrix[mI][mJ+1] = "─"
                            mI = self._elementSearch(self.items[index][1], foundedItems.copy(), mI, mJ + 2)
                            mI += 1                        # становимся на центр предиката
                            self._moveMatrix(mI + 1)       # двигаем матрицу вниз без текущей строки
                            self.matrix[mI + 1][mJ] = "└"  # добавляем уголок и идем далее по ложной ветке
                            self.matrix[mI + 1][mJ + 1] = "─"
                            mI = self._elementSearch(self.items[index][2], foundedItems.copy(), mI + 1, mJ + 2)
                    break
        return mI

# ============================================ пост и пред обработка матрицы ===========================================

    # добавление связующих вертиакальных линий _________________________________________________________________________
    def _addingLines(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
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

    # оптимизация размеров матрицы _____________________________________________________________________________________
    def _resizeMatrix(self):
        for index in range(len(self.matrix)):
            while len(self.matrix[index]) != 0 and self.matrix[index][-1] == "":
                self.matrix[index].pop(-1)
        newMatrix = []
        for row in self.matrix:
            if row != []:
                newMatrix.append(row)
        self.matrix = newMatrix

    # двигаем матрицу вниз без текущей строки __________________________________________________________________________
    def _moveMatrix(self, startRow): # сдвиг части матрицы вниз
        for i in range(len(self.matrix[0]) - 2, startRow - 1, -1):
            for j in range(len(self.matrix)):
                self.matrix[i + 1][j] = self.matrix[i][j]
        for j in range(len(self.matrix)):
            self.matrix[startRow][j] = ""

# ----------------------------------------------------------------------------------------------------------------------

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

    def getItemLen(self):
        return self.itemLen

    def getMatrix(self):
        return self.matrix

    def get_branches(self):
        return self.branches

    def setTable(self, newItems): # задам таблицу смежности из готового списка
        self.items = []
        self.matrix = []
        self.itemLen = 6
        self.startIsValid = False  # проверка на существование блока старт в таблице (items)
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

    # построение Е-схемы _______________________________________________________________________________________________
    def build(self, add_knots: bool = True):
        self.matrix = [[""] * len(self.items) * 15 for i in range(len(self.items) * 15)]
        self.element_with_knots = []
        self.knot_quantity = 0
        self.branches = []
        if add_knots:
            self._create_knots("START", [])         # создание узлов
        self._elementSearch('START', [], 0, 0)  # поиск и отрисовка элементов
        self._addingLines()   # добавление вертикальных лний в матрицу
        self._resizeMatrix()  # оптимизация размеров матрицы
        print(self.matrix)
