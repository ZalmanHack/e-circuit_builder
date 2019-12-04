from client import *


if __name__ == "__main__":
    Client(Mode.console)
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