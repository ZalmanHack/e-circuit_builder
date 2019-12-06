import sys
from client import *


if __name__ == "__main__":
    while True:
        os.system('cls')
        print("1 | Графический                   |")
        print("2 | Консольный                    |")
        print("3 | Выйти из программы            |")
        cin = input("Выберите режим работы >> ")
        if cin == "1":
            Client(Mode.graphic)
            sys.exit(0)
        if cin == "2":
            Client(Mode.console)
            sys.exit(0)
        if cin == "3":
            sys.exit(0)

    """
    if len(sys.argv) == 1:
        print("---------- Консольный режим ----------")
        Client(Mode.console)
        input("Для продолжения, нажмите любую клавишу...")
    elif len(sys.argv) == 2:
        if sys.argv[1] == "-G":
            print("---------- Консольный режим + графический вывод ----------")
            Client(Mode.graphic)
            input("Для продолжения, нажмите любую клавишу...")
    else:
        print("Ошибка. Слишком много параметров.")
        time.sleep(5)
        sys.exit(1)
    """