import json


class ECircuit_Minimize():
    def __init__(self):
        self.items = []
        self.template = {}
        self._load_templates()

        self.elemen_minimize = 1

    def _load_templates(self):
        with open("data.json", 'r', encoding="utf-8") as file:
            self.template = json.load(file)
            res = []
            for name, item in self.template.items():
                for i in item:
                    res.append([self._max_in_matrix(i), i])
            self.template = res
            print("_load_templates:: good")

    def _update_element(self, items_is_template: bool,  index, column, foundRows: list, foundItems, iteration: int = 1):
        if items_is_template:
            new_item = "{0}.{1}/{2}".format(iteration, self.elemen_minimize, len(foundRows))
            self.elemen_minimize += 1
            self.items[index][column] = new_item
            print(foundItems)
            self.items[foundRows[0]] = [new_item, foundItems[-1], "0"]
            foundRows.pop(0)
            temp = 0
            foundRows.sort()
            for i in foundRows:
                self.items.pop(i + temp)
                temp -= 1
            return new_item
        return self.items[index][column]

    def _elementSearch(self, searchingElement, foundItems, iteration):  # рекурсивный спуск по дереву
        # elemen_minimize какой по счету элемент будет свернут в данной итерации (чисто для названия)
        if searchingElement != 'END':  # Если элемент указывает на конец то пишем конец
            for index in range(len(self.items)):  # перебор введенных смежностей
                if searchingElement == self.items[index][0]:  # если нашли такой
                    if index not in foundItems:  # и если он уже вызывался в ветке
                        foundItems.append(index)  # помечаем как найденный
                        if self.items[index][-1] == '0':  # проверяем на тип "функциональный"
                            foundRows, foundedElements, items_is_template = self._template_Search(self.items[index][1], [], [], self.template.copy())
                            searchingElement = self._update_element(items_is_template, index, 1, foundRows,  foundedElements, iteration)
                            self._elementSearch(searchingElement, foundItems.copy(), iteration)
                        else:  # иначе он является предикатным
                            foundRows, foundedElements, items_is_template = self._template_Search(self.items[index][1], [], [], self.template.copy())
                            searchingElement = self._update_element(items_is_template, index, 1, foundRows,  foundedElements, iteration)
                            self._elementSearch(searchingElement, foundItems.copy(), iteration)

                            foundRows, foundedElements, items_is_template = self._template_Search(self.items[index][2], [],[],self.template.copy())
                            searchingElement = self._update_element(items_is_template, index, 2, foundRows,foundedElements, iteration)
                            self._elementSearch(searchingElement, foundItems.copy(), iteration)
                    break

    def _convert_row_indexes(self, row: list, foundItems: list):
        try:
            return [foundItems[row[0]],
                    foundItems[row[1]],
                    foundItems[row[2]]]
        except Exception as E:
            return []

    def union(self, A: list, B: list):
        C = A
        for i in B:
            if i not in A:
                C.append(i)
        return C

    def _max_in_matrix(self, items: list):
        res = max([max(a) for a in items])
        return res

    def _template_Search(self, searchingElement: str, foundItems: list, foundRows: list, templates):
        items_is_template = False  # найден шаблон
        item_is_bigger = False  # искомая строка больше шаблонных
        correct_templates = []  # Массив подходящих шаблонов
        if len(foundItems) == 0:
            foundItems = ["0"]
        for index in range(len(self.items)):  # перебор введенных смежностей
            if searchingElement == self.items[index][0]:  # если нашли такой
                foundItems = self.union(foundItems, self.items[index])

                for max_quantity, template in templates:  # перебор шаблонов
                    for template_row in template:
                        temp_row = self._convert_row_indexes(template_row, foundItems)
                        if len(temp_row) > 0 and self.items[index][0] == temp_row[0]:  # если первые стобцы сток соовпали
                            if self.items[index] == temp_row:  # если строка шаблона совпала с искомой
                                if len(template) == 1:  # если это единственная строка в шаблоне
                                    items_is_template = True
                                    return [foundRows, foundItems, items_is_template]
                                else:
                                    if index not in foundRows:
                                        foundRows.append(index)
                                    temp = template.copy()
                                    temp.remove(template_row)
                                    correct_templates.append([max_quantity, temp])
                                    break
                        else:
                            item_is_bigger = True
                if len(correct_templates) == 0:
                    if not item_is_bigger:
                        foundRows.clear()
                else:
                    if searchingElement[0] == "(" or searchingElement[-1] == ")":  # элемент является узлом?
                        foundRows.clear()
                    else:
                        # Продолжаем проход по ветке
                        if self.items[index][-1] == '0':  # проверяем на тип "функциональный"
                            foundRows, foundItems, items_is_template = self._template_Search(self.items[index][1],
                                                                                             foundItems, foundRows,
                                                                                             correct_templates.copy())
                        else:  # иначе он является предикатным
                            foundRows, foundItems, items_is_template = self._template_Search(self.items[index][1],
                                                                                             foundItems, foundRows,
                                                                                             correct_templates.copy())
                            if len(foundRows) > 0:
                                if not items_is_template:
                                    foundRows, foundItems, items_is_template = self._template_Search(self.items[index][2],
                                                                                                     foundItems, foundRows,
                                                                                                     correct_templates.copy())
                    return [foundRows, foundItems, items_is_template]
        return [foundRows, foundItems, items_is_template]

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

    def setTable(self, newItems):  # задам таблицу смежности из готового списка
        self.items = []
        self.matrix = []
        self.itemLen = 6
        self.startIsValid = False  # проверка на существование блока старт в таблице (items)
        for item in newItems:
            if self.itemIsValid(item):
                self.items.append(item)

    def build(self):
        self.elemen_minimize = 1
        self._elementSearch("START", [], 1)

    def getTable(self):
        return self.items


if __name__ == "__main__":

    data = items[0]

    for i in data:
        print(i)

    test = ECircuit_Minimize()
    test.setTable(data)
    result = test.build()

    print("-------------------------")
    for i in result:
        print(i)
