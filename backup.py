def entaerTable():
    items = []
    print("Введите матрицу смежности\nДля завершения ввода нажмите 'exit'")
    while True:
        text = input()
        if len(text) == 3:
            items.append(text.upper())
        elif text == 'exit':
            if len(items) == 0:
                print("Таблица пустая!")
            else: break
        else: print("Для завершения ввода нажмите 'exit'")
    return items

def moveMatrix(startRow, matrix):
    for i in range(len(matrix[0]) - 2, startRow - 1, -1):
        for j in range(len(matrix)):
            matrix[i + 1][j] = matrix[i][j]
    for j in range(len(matrix)):
        matrix[startRow][j] = "  "
    return matrix

def printM(matrix):
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[i][j])
        while  len(row) != 0 and row[-1] == "  ":
            row.pop(-1)
        print(str(row))

def addingLines(matrix):
    for i in range(len(matrix)):    # добавляем горизонтальные линии
        for j in range(len(matrix)):
            if matrix[i][j] == "└─":
                for k in range(i-1, 0-1, -1):
                    if matrix[k][j] == "│ " or matrix[k][j] == "  ":
                        matrix[k][j] = "│ "
                    else: break
            elif matrix[i][j] == "┌─":
                for k in range(i + 1, len(matrix), 1):
                    if matrix[k][j] == "│ " or matrix[k][j] == "  ":
                        matrix[k][j] = "│ "
                    else: break
    return matrix

def resizeMatrix(matrix):
    for row in matrix:
        while len(row) != 0 and row[-1] == "  ":
            row.pop(-1)

def elementSearch(searchingElement, items, foundedItems, matrix, mI, mJ):
    if searchingElement == 'E':                                 # Если элемент указывает на конец то пишем конец
        matrix[mI][mJ] = 'End'
    else:
        for index in range(len(items)):                         # перебор введенных смежностей
            if searchingElement == items[index][0]:             # если нашли такой
                if index in foundedItems:                       # и если он уже вызывался в ветке
                    matrix[mI][mJ] = searchingElement           # добавляем в матрицу
                else:                                           # иначе
                    foundedItems.append(index)                  # помечаем как найденный
                    if items[index][-1] == '0':                 # проверяем на тип "функциональный"
                        matrix[mI][mJ] = searchingElement + "─" # если да, то отображаем и идем по ветке далее
                        mI, matrix = elementSearch(items[index][1], items, foundedItems.copy(), matrix, mI, mJ + 1)
                    else:                                       # иначе он является предикатным
                        matrix[mI][mJ] = searchingElement       # отображаем в матрице
                        matrix = moveMatrix(mI, matrix)         # перемещаем текущую и нижние строки на 1 вниз
                        matrix[mI][mJ] = "┌─"                   # добавляем уголок и идем далее по правдивой ветке
                        mI, matrix = elementSearch(items[index][1], items, foundedItems.copy(), matrix, mI, mJ + 1)
                        mI += 1                                 # становимся на центр предиката
                        matrix = moveMatrix(mI + 1, matrix)     # двигаем матрицу вниз без текущей строки
                        matrix[mI + 1][mJ] = "└─"               # добавляем уголок и идем далее по ложной ветке
                        mI, matrix = elementSearch(items[index][2], items, foundedItems.copy(), matrix, mI + 1, mJ + 1)
    return mI, matrix

if __name__ == "__main__":
    inputItems = entaerTable()
    foundedItems = []
    matrix = [["  "] * len(inputItems)*16 for i in range(len(inputItems)*16)]
    mI, matrix = elementSearch('S', inputItems, foundedItems, matrix, 0, 0)
    matrix = addingLines(matrix)
    resizeMatrix(matrix)
    printM(matrix)
    key = input()