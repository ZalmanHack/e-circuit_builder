class ECircuit_Structuring():
    def __init__(self):
        self.items = []  # таблица смежности

    # добавление обявления I==X_________________________________________________________________________________________
    def _adding_I_cases(self, foundElements: list):
        cases = []
        # Добавляем узел на возврат
        cases.append(["(1)", "I==0", "0"])
        for index in range(0, len(foundElements)):
            end_element = "(1)"
            if index + 1 < len(foundElements):
                end_element = "I=={0}".format(index + 1)
            cases.append(["I=={0}".format(index), foundElements[index], end_element])
        self.items = cases + self.items

    # добавление обявления I=X _________________________________________________________________________________________
    def _adding_I_elements(self, searchingElement: str, foundElements: list):
        if "END" not in foundElements:
            foundElements.append("END")
            self.items.append(["I=0", "(1)", "0"])
        for index in range(len(self.items)):  # перебор введенных смежностей
            if searchingElement == self.items[index][0]:  # если нашли такой
                for index_element in range(1, len(self.items[index])):
                    if self.items[index][index_element] != "0":
                        if self.items[index][index_element] not in foundElements:
                            foundElements.append(self.items[index][index_element])
                            self.items.append(["I={0}".format(len(foundElements) - 1), "(1)", "0"])
                            foundElements = self._adding_I_elements(self.items[index][index_element], foundElements)
                        temp_index = foundElements.index(self.items[index][index_element])
                        self.items[index][index_element] = "I={0}".format(temp_index)
                break
        return foundElements

    # проверка элемента на то, является ли он уззлом ___________________________________________________________________
    def _is_knot(self, searchingElement: str):
        if searchingElement[0] == "(" or searchingElement[-1] == ")":
            return True
        return False

    # удаление узлов ___________________________________________________________________________________________________
    def _delete_nods(self):
        index = 0
        while index < len(self.items):
            if self._is_knot(self.items[index][0]):
                temp_name = self.items[index][1]
                for _index in range(0, len(self.items)):
                    for i in [1, 2]:
                        if self.items[_index][i] == self.items[index][0]:
                            self.items[_index][i] = temp_name
                self.items.pop(index)
                index -= 1
            index += 1

    # полчение данных о входах и выходах каждого кейса _________________________________________________________________
    def _get_in_out_of_cases(self):
        result = []
        for row in self.items[1:]:
            if "I==" not in row[0]:
                break
            outputs = self._get_case_outputs(row[1], [], [])
            result.append([row[0][3:], row[1], outputs])
        return result

    # полчение данных о выходах кейса (для _get_in_out_of_cases()) _____________________________________________________
    def _get_case_outputs(self, searchingElement: str, foundItems: list, foundIElements: list):
        for index in range(len(self.items)):  # перебор введенных смежностей
            if searchingElement == self.items[index][0]:  # если нашли такой
                if "I=" in searchingElement:
                    if searchingElement[2:] not in foundIElements:
                        foundIElements.append(searchingElement[2:])
                elif index not in foundItems:  # и если он уже вызывался в ветке
                    foundItems.append(index)  # помечаем как найденный
                    if self.items[index][-1] == '0':  # проверяем на тип "функциональный"
                        foundIElements = self._get_case_outputs(self.items[index][1],
                                                                foundItems.copy(),
                                                                foundIElements.copy())
                    else:  # иначе он является предикатным
                        foundIElements = self._get_case_outputs(self.items[index][1],
                                                                foundItems.copy(),
                                                                foundIElements.copy())
                        foundIElements = self._get_case_outputs(self.items[index][2],
                                                                foundItems.copy(),
                                                                foundIElements.copy())
                break
        return foundIElements

    # проверка на то, можно ли подставить кейс или нет _________________________________________________________________
    def _isReplaceable(self, in_out_cases: list, replaceable: list):
        is_such = False
        for item in in_out_cases:
            if replaceable[0] in item[2]:  # если заменяемый элемент хоть раз вызвается в этом кейсе
                is_such = True
                if item[0] in replaceable[2]:  # если этот элемент рекурсивный то ничего не заменяем и выходим
                    return False
        return is_such

    # удаление кейса и подставление его в нужные места других кейсов ___________________________________________________
    def _updateReplaceable(self, searchingElemnet):
        temp: str = ""
        # поиск строки
        for index in range(0, len(self.items)):
            # удаляем I==X строку
            if self.items[index][0] == "I=={0}".format(searchingElemnet[0]):
                temp = self.items[index][2]
                self.items.pop(index)
                # заменяем ссылку на нее
                for _index in range(0, len(self.items)):
                    for i in [1, 2]:
                        if self.items[_index][i] == "I=={0}".format(searchingElemnet[0]):
                            self.items[_index][i] = temp
                            check = True
                            break
                break
        # заменяем ссылки I=X
        isStart = False  # для того чтобы I=X что идет после старта не удалялась
        for index in range(0, len(self.items)):
            for i in [1, 2]:
                if self.items[index][i] == "I={0}".format(searchingElemnet[0]):
                    if self.items[index][0] != "START":
                        self.items[index][i] = searchingElemnet[1]
                    else:
                        self.items[index][1] = "I={0}".format(temp[3:])
        for index in range(0, len(self.items)):
            # удаляем I=X строку
            if self.items[index][0] == "I={0}".format(searchingElemnet[0]):
                self.items.pop(index)
                break

    # задам таблицу смежности из готового списка _______________________________________________________________________
    def setTable(self, newItems):
        self.items = []
        for row in newItems:
            for element in row:
                if "I=" in element:
                    return False
        for row in newItems:
            if len(row) == 3:
                self.items.append(row)
        return True

    # структурирование _________________________________________________________________________________________________
    def build(self):
        # удаление всех узлов
        self._delete_nods()
        # создаем I=X элементы
        foundElements = self._adding_I_elements('START', [])
        # создаем кейсы
        self._adding_I_cases(foundElements)
        # Анализ кейсов (получение их входов и выходов)
        isAnalis = True
        while isAnalis:
            in_out_cases = self._get_in_out_of_cases()
            # перебераем строки и пытаемся их заменить
            isAnalis = False
            for item in in_out_cases:
                if self._isReplaceable(in_out_cases, item) and item[0] != '0':
                    self._updateReplaceable(item)
                    isAnalis = True
                    break

    def getTable(self):
        return self.items