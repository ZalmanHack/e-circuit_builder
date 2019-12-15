import json
import sys
import time

class ECircuit_Minimize():
    def __init__(self):
        self.items = []  # таблица смежности
        self.template = {}  # шаблоны (из файла data.json)
        self._load_templates()  # загрузка шаблонов
        self.elemen_minimize = 1 # кол-во элементов минимизации (для замены)

    # загрузка шаблонов ________________________________________________________________________________________________
    def _load_templates(self):
        try:
            with open("data.json", 'r', encoding="utf-8") as file:
                self.template = json.load(file)
                res = []
                for name, item in self.template.items():
                    for i in item:
                        res.append(i)
                self.template = res
        except:
            print("Произошла ошибка при работе с файлом шаблонов :: data.json")
            time.sleep(3)
            sys.exit(-1)

    # замена инд-ов шаблонной строки на найденые элементы ______________________________________________________________
    def _convert_row_indexes(self, row: list, foundItems: list):
        try:
            return [foundItems[row[0]],
                    foundItems[row[1]],
                    foundItems[row[2]]]
        except Exception as E:
            return []

    # объединение двух массивов ________________________________________________________________________________________
    def union(self, A: list, B: list):
        C = A
        for i in B:
            if i not in A:
                C.append(i)
        return C

    # проверка на то, является ли элемент узлом ________________________________________________________________________
    def _is_knot(self, searchingElement: str):
        if searchingElement[0] == "(" or searchingElement[-1] == ")":
            return True
        return False

    # проверка на существование узлов внутри найденых эл-ов (исключая первые и последние) ______________________________
    def _knot_in(self, searchingElement: str, foundItems: list):
        for item in foundItems[2:-1]:
            if self._is_knot(item):  # элемент является узлом?
                return True
        return False

    # обновление элементов таблицы смежности (применение шаблона) ______________________________________________________
    def _update_element(self, items_is_template: bool, index, column, foundRows: list, foundItems, iteration: int = 1,
                        searchingElement: str = ""):
        if items_is_template and len(foundRows) > 1:
            # считаем кол-во свернутых элементов
            quantity_elemets = len(foundRows)
            for element in foundItems[1:-1]:
                try:
                    if len(element.split('/')) == 2:
                        quantity_elemets += int(element.split('/')[1])
                except Exception as e:
                    pass
            new_item = "{0}.{1}/{2}".format(iteration, self.elemen_minimize, quantity_elemets)
            self.elemen_minimize += 1
            is_knot = self._is_knot(self.items[foundRows[0]][0])
            if is_knot:
                if len(foundRows) > 2:
                    if self._is_knot(self.items[foundRows[0]][1]):
                        old_item = str(self.items[foundRows[0]][1]).split("/")[1]
                        new_item = "{0}.{1}/{2}".format(iteration, self.elemen_minimize, quantity_elemets + int(old_item))
                    self.items[foundRows[0]][1] = new_item
                    self.items.append([new_item, foundItems[-1], "0"])
                else:
                    return self.items[index][column]
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

    # поиск элемента в таблице смежности _______________________________________________________________________________
    def _elementSearch(self, searchingElement, foundItems, iteration):  # рекурсивный спуск по дереву
        # elemen_minimize какой по счету элемент будет свернут в данной итерации (чисто для названия)
        if searchingElement != 'END':  # Если элемент указывает на конец то пишем конец
            for index in range(len(self.items)):  # перебор введенных смежностей
                if searchingElement == self.items[index][0]:  # если нашли такой
                    if index not in foundItems:  # и если он уже вызывался в ветке
                        foundItems.append(index)  # помечаем как найденный
                        if self.items[index][-1] == '0':  # проверяем на тип "функциональный"
                            correct_templates, foundRows, foundedElements, items_is_template = self._template_Search(
                                self.items[index][1], [], [], self.template.copy())
                            searchingElement = self._update_element(items_is_template, index, 1, foundRows,
                                                                    foundedElements, iteration, searchingElement)
                            self._elementSearch(searchingElement, foundItems.copy(), iteration)
                        else:  # иначе он является предикатным
                            correct_templates, foundRows, foundedElements, items_is_template = self._template_Search(
                                self.items[index][1], [], [], self.template.copy())
                            searchingElement = self._update_element(items_is_template, index, 1, foundRows,
                                                                    foundedElements, iteration, searchingElement)
                            self._elementSearch(searchingElement, foundItems.copy(), iteration)

                            correct_templates, foundRows, foundedElements, items_is_template = self._template_Search(
                                self.items[index][2], [], [], self.template.copy())
                            searchingElement = self._update_element(items_is_template, index, 2, foundRows,
                                                                    foundedElements, iteration, searchingElement)
                            self._elementSearch(searchingElement, foundItems.copy(), iteration)
                    break

    # поиск шаблона ____________________________________________________________________________________________________
    def _template_Search(self, searchingElement: str, foundItems: list, foundRows: list, templates):
        items_is_template = False  # найден шаблон
        item_is_bigger = False  # искомая строка больше шаблонных
        reserve_foundRows = []
        reserve_foundItems = []
        correct_templates = []  # Массив подходящих шаблонов
        if searchingElement == 'END':
            return [templates, foundRows, foundItems, items_is_template]
        if len(foundItems) == 0:
            foundItems = ["0"]
        for index in range(len(self.items)):  # перебор введенных смежностей
            if searchingElement == self.items[index][0]:  # если нашли такой
                reserve_2_foundItems = foundItems.copy()  # для возврата исходных данных если не найдем ничего
                reserve_2_foundRows = foundRows.copy()    # для возврата исходных данных если не найдем ничего
                foundItems = self.union(foundItems, self.items[index])
                for template in templates:  # перебор шаблонов
                    for template_row in template:         # перебор строк шаблона
                        temp_row = self._convert_row_indexes(template_row, foundItems)
                        if len(temp_row) > 0 and self.items[index][0] == temp_row[0]:  # если 1е столбцы строк соовпали
                            if self.items[index] == temp_row:  # если строка шаблона совпала с искомой
                                if index not in foundRows:     # если эту строку еще не находили то запоминаем ее
                                    foundRows.append(index)
                                if len(template) == 1:         # если последняя строка в шаблоне
                                    reserve_foundItems = foundItems.copy()
                                    reserve_foundRows = foundRows.copy()
                                # Добавляемподходящий шаблон с удалением из него найденой строки
                                temp = template.copy()
                                temp.remove(template_row)
                                correct_templates.append(temp)
                                break
                        else:
                            item_is_bigger = True  # 1 эл-ент строки больше чем у шаблонной
                if len(correct_templates) == 0:    # если массив шаблонов пуст
                    if not item_is_bigger:   # если 1 эл-ент найденной строки не совпал ни с одним шаблоном очищаем все
                        foundRows.clear()
                        foundItems.clear()
                    else:  # иначе возвращаем резерв
                        return [templates, reserve_2_foundRows, reserve_2_foundItems, items_is_template]
                else:
                    if self._knot_in(searchingElement, foundItems):  # если в найденном шаблоне есть узлы то очищаем все
                        foundRows.clear()
                        foundItems.clear()
                    else:
                        # Продолжаем проход по ветке -------------------------------------------------------------------
                        if self.items[index][-1] == '0':  # проверяем на тип "функциональный"
                            correct_templates, foundRows, foundItems, items_is_template = self._template_Search(
                                self.items[index][1], foundItems, foundRows.copy(), correct_templates)
                        else:  # иначе он является предикатным
                            # по ветке истины --------------------------------------------------------------------------
                            correct_templates, foundRows, foundItems, items_is_template = self._template_Search(
                                self.items[index][1], foundItems, foundRows.copy(), correct_templates)
                            if len(foundRows) > 0: # если ест найденные строки
                                if not items_is_template:  # если шаблон все еще не найцден продолжаем искать по false
                                    # по ветке истины ------------------------------------------------------------------
                                    correct_templates, foundRows, foundItems, items_is_template = self._template_Search(
                                        self.items[index][2], foundItems, foundRows.copy(), correct_templates)
                        if not items_is_template:  # Если шаблон так и небыл найден
                            if len(reserve_foundRows) > 0:  # если есть резерв (более простые шаблоны)
                                items_is_template = True
                                return [correct_templates, reserve_foundRows, reserve_foundItems, items_is_template]
                    return [correct_templates, foundRows, foundItems, items_is_template]
        return [correct_templates, foundRows, foundItems, items_is_template]

    # удаление ненужный узлов __________________________________________________________________________________________
    def deleting_unnecessary_nodes(self, searchingElement, foundItems):
        nodes = []
        to_delete = []
        if searchingElement != 'END':
            for index in range(len(self.items)):  # перебор введенных смежностей
                if searchingElement == self.items[index][0]:  # если нашли такой
                    if index in foundItems:  # и если он уже вызывался в ветке
                        if self._is_knot(searchingElement):
                            nodes.append(searchingElement)
                    else:  # иначе
                        foundItems.append(index)  # помечаем как найденный
                        if self.items[index][-1] == '0':  # проверяем на тип "функциональный"
                            temp_nodes, temp_to_delete = self.deleting_unnecessary_nodes(self.items[index][1], foundItems.copy())
                            nodes = self.union(nodes, temp_nodes)
                            to_delete = self.union(to_delete, temp_to_delete)
                        else:  # иначе он является предикатным
                            # по ветке истины --------------------------------------------------------------------------
                            temp_nodes, temp_to_delete = self.deleting_unnecessary_nodes(self.items[index][1], foundItems.copy())
                            nodes = self.union(nodes, temp_nodes)
                            to_delete = self.union(to_delete, temp_to_delete)
                            # по ветке лжи -----------------------------------------------------------------------------
                            temp_nodes, temp_to_delete = self.deleting_unnecessary_nodes(self.items[index][2], foundItems.copy())
                            nodes = self.union(nodes, temp_nodes)
                            to_delete = self.union(to_delete, temp_to_delete)
                        if len(foundItems) > 1 and self._is_knot(searchingElement) and searchingElement not in nodes:
                            # проверка на наличие узла в других ветках -------------------------------------------------
                            quantity = 0
                            for item in self.items:
                                for i in [1, 2]:
                                    if item[i] == searchingElement:
                                        quantity += 1
                                    if quantity >= 2:
                                        return nodes, to_delete
                            # замена элемента --------------------------------------------------------------------------
                            for i in [1, 2]:
                                if self.items[foundItems[-2]][i] == searchingElement:
                                    self.items[foundItems[-2]][i] = self.items[foundItems[-1]][1]
                                    to_delete.append(index)
                                    break
        return nodes, to_delete

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

    # главнй метод построения __________________________________________________________________________________________
    def build(self):
        self.elemen_minimize = 1
        iterations = 1
        for _ in range(10):
            table_size = len(self.items)
            self._elementSearch("START", [], iterations)
            nodes, items_to_delete = self.deleting_unnecessary_nodes("START", [])
            items_to_delete.sort(reverse=True)
            for item in items_to_delete:
                self.items.pop(item)
            self.elemen_minimize = 1
            iterations += 1

    def getTable(self):
        return self.items

    # ввод таблиц смежности с клавиатуры _______________________________________________________________________________
    def enterTable(self):
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