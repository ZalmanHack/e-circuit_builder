import json
import sys
import time

class ECircuit_Structuring():
    def __init__(self):
        self.items = []  # таблица смежности

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
                            self.items.append(["I={0}".format(len(foundElements)-1),
                                               "(1)", "0"])
                            foundElements = self._adding_I_elements(self.items[index][index_element], foundElements)
                        temp_index = foundElements.index(self.items[index][index_element])
                        self.items[index][index_element] = "I={0}".format(temp_index)
                break
        return foundElements

    def _is_knot(self, searchingElement: str):
        if searchingElement[0] == "(" or searchingElement[-1] == ")":
            return True
        return False

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


    # задам таблицу смежности из готового списка _______________________________________________________________________
    def setTable(self, newItems):
        self.items = []
        for item in newItems:
            if len(item) == 3:
                self.items.append(item)

    def getTable(self):
        return self.items

    def build(self):
        self._delete_nods()
        foundElements = self._adding_I_elements('START', [])
        for item in self.items:
            print(item)
        self._adding_I_cases(foundElements)
        print("------------------------")
        for item in self.items:
            print(item)

if __name__ == "__main__":
    items = [
        ['START','A','0'],
        ['A','C','0'],
        ['C','D','A'],
        ['D','A', 'END']
    ]
    test = ECircuit_Structuring()
    test.items = items
    test.build()