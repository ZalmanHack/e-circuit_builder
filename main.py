from client import *

if __name__ == "__main__":


    p = [1,2,3]
    b = [4,5,6]
    c = []
    [c.append(a) for a in b]
    [c.append(a) for a in p]
    print(c)
"""
    j = [0,1,2,3]
    print(j[2:-1])
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