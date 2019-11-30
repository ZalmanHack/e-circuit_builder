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

    def _is_knot(self, searchingElement: str):
        if searchingElement[0] == "(" or searchingElement[-1] == ")":
            return True
        return False

    def _knot_in(self, searchingElement: str, foundItems: list):  # проверка на существование узлов внутри найденых эл-ов (исключая первые и последние)
        for item in foundItems[2:-1]:
            if self._is_knot(item):  # элемент является узлом?
                return True
        return False

    def _update_element(self, items_is_template: bool,  index, column, foundRows: list, foundItems, iteration: int = 1, searchingElement: str = ""):
        if items_is_template and len(foundRows) > 1:
            new_item = "{0}.{1}/{2}".format(iteration, self.elemen_minimize, len(foundRows))
            self.elemen_minimize += 1
            # self.items[index][column] = new_item
            print(foundItems)
            is_knot = self._is_knot(self.items[foundRows[0]][0])
            if is_knot:

                self.items[foundRows[0]][1] = new_item
                self.items.append([new_item, foundItems[-1], "0"])
            else:
                self.items[index][column] = new_item
                self.items[foundRows[0]] = [new_item, foundItems[-1], "0"]
            foundRows.pop(0)
            temp = 0
            foundRows.sort()
            for i in foundRows:
                self.items.pop(i + temp)
                temp -= 1
            if is_knot:
                return self.items[foundRows[0]][0]
            else:
                return new_item
        return self.items[index][column]

    def _elementSearch(self, searchingElement, foundItems, iteration):  # рекурсивный спуск по дереву
        changed = False
        # elemen_minimize какой по счету элемент будет свернут в данной итерации (чисто для названия)
        if searchingElement != 'END':  # Если элемент указывает на конец то пишем конец
            for index in range(len(self.items)):  # перебор введенных смежностей
                if searchingElement == self.items[index][0]:  # если нашли такой
                    if index not in foundItems:  # и если он уже вызывался в ветке
                        foundItems.append(index)  # помечаем как найденный
                        if self.items[index][-1] == '0':  # проверяем на тип "функциональный"
                            foundRows, foundedElements, items_is_template = self._template_Search(self.items[index][1], [], [], self.template.copy())
                            searchingElement = self._update_element(items_is_template, index, 1, foundRows,  foundedElements, iteration, searchingElement)
                            self._elementSearch(searchingElement, foundItems.copy(), iteration)
                        else:  # иначе он является предикатным
                            foundRows, foundedElements, items_is_template = self._template_Search(self.items[index][1], [], [], self.template.copy())
                            searchingElement = self._update_element(items_is_template, index, 1, foundRows,  foundedElements, iteration, searchingElement)
                            self._elementSearch(searchingElement, foundItems.copy(), iteration)

                            foundRows, foundedElements, items_is_template = self._template_Search(self.items[index][2], [],[],self.template.copy())
                            searchingElement = self._update_element(items_is_template, index, 2, foundRows,foundedElements, iteration, searchingElement)
                            self._elementSearch(searchingElement, foundItems.copy(), iteration)
                    break

    def _template_Search(self, searchingElement: str, foundItems: list, foundRows: list, templates):
        items_is_template = False  # найден шаблон
        item_is_bigger = False  # искомая строка больше шаблонных
        reserve_foundRows = []
        reserve_foundItems = []
        correct_templates = []  # Массив подходящих шаблонов
        if len(foundItems) == 0:
            foundItems = ["0"]
        for index in range(len(self.items)):  # перебор введенных смежностей
            if searchingElement == self.items[index][0]:  # если нашли такой
                old_size_found_items = len(foundItems)
                foundItems = self.union(foundItems, self.items[index])
                for max_quantity, template in templates:  # перебор шаблонов
                    for template_row in template:
                        temp_row = self._convert_row_indexes(template_row, foundItems)
                        if len(temp_row) > 0 and self.items[index][0] == temp_row[0]:  # если первые стобцы строк соовпали
                            if self.items[index] == temp_row:  # если строка шаблона совпала с искомой
                                temp = template.copy()
                                temp.remove(template_row)
                                correct_templates.append([max_quantity, temp])
                                if index not in foundRows:
                                    foundRows.append(index)
                                if len(template) == 1:  # если последняя строка в шаблоне
                                    reserve_foundItems = foundItems.copy()
                                    reserve_foundRows = foundRows.copy()
                                break
                        else:
                            item_is_bigger = True
                if len(correct_templates) == 0:
                    if old_size_found_items != len(foundItems):
                        foundRows.clear()
                        foundItems.clear()
                else:
                    if self._knot_in(searchingElement,foundItems):
                        foundRows.clear()
                        foundItems.clear()
                    else:
                        # Продолжаем проход по ветке
                        if self.items[index][-1] == '0':  # проверяем на тип "функциональный"
                            foundRows, foundItems, items_is_template = self._template_Search(self.items[index][1], foundItems, foundRows.copy(), correct_templates.copy())
                        else:  # иначе он является предикатным
                            foundRows, foundItems, items_is_template = self._template_Search(self.items[index][1], foundItems, foundRows.copy(),correct_templates.copy())
                            if len(foundRows) > 0:
                                if not items_is_template:
                                    foundRows, foundItems, items_is_template = self._template_Search(self.items[index][2], foundItems, foundRows.copy(),correct_templates.copy())
                        if not items_is_template: # Если шаблон так и небыл найден
                            if len(reserve_foundRows) > 0:  # если есть резерв (более простые шаблоны)
                                items_is_template = True
                                return [reserve_foundRows, reserve_foundItems, items_is_template]
                            else:
                                items_is_template = False
                                foundRows.clear()
                                foundItems.clear()
                    return [foundRows, foundItems, items_is_template]
        return [foundRows, foundItems, items_is_template]

    def deleting_unnecessary_nodes(self, searchingElement, foundedItems):
        if searchingElement == 'END':  # Если элемент указывает на конец то пишем конец
            pass
        else:
            for index in range(len(self.items)):  # перебор введенных смежностей
                if searchingElement == self.items[index][0]:  # если нашли такой
                    if index in foundedItems:  # и если он уже вызывался в ветке
                        pass
                    else:  # иначе
                        foundedItems.append(index)  # помечаем как найденный
                        if self.items[index][-1] == '0':  # проверяем на тип "функциональный"
                            elements = self.deleting_unnecessary_nodes(self.items[index][1], foundedItems.copy())
                        else:  # иначе он является предикатным
                            self.deleting_unnecessary_nodes(self.items[index][1], foundedItems.copy())
                            self.deleting_unnecessary_nodes(self.items[index][2], foundedItems.copy())
                    break

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
        iterations = 1
        for _ in range(10):
            table_size = len(self.items)
            self._elementSearch("START", [], iterations)
            if table_size == len(self.items):
                return
            self.elemen_minimize = 1
            iterations +=1

    def getTable(self):
        return self.items

