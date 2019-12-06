import json
import socket

import subprocess
from threading import Thread

import pickle       # для работы с бинарными файлами
import time
import sys
import os

from ecircuit import *

class Client():
    def __init__(self, mode: Mode.console):
        self.mode = mode
        self.key_len = 36
        self.time = 300
        self.key = None
        self.folder_path = os.path.expanduser('~') + "\\.E-Circuit builder"
        self.file_name = "authorization.bin"
        self.menu_items = {
            "set_key": ["Ввести ключ активации", self.set_key],
            "get_free": ["Начать пробный период", self.get_free],
            "get_quit": ["Выйти из программы", self.get_quit]
        }
        self.current_machine_id = self.get_current_machine_id()
        # если файла конфига нет
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
        # --------------------------------------------------------------------------------------------------------------
        self.HOST = str('109.254.54.221')  # '127.0.0.1'  # Standard loopback interface address (localhost)
        self.PORT = 8888  # 65432  # Port to listen on (non-privileged ports are > 1023)
        # --------------------------------------------------------------------------------------------------------------
        self.chek_authorization()

    def get_current_machine_id(self):
        return subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

    def get_file_data(self):
        if not os.path.isfile(self.folder_path + "\\" + self.file_name):
            if not os.path.exists(self.folder_path):
                os.makedirs(self.folder_path)
            with open("{0}\\{1}".format(self.folder_path, self.file_name), 'wb') as file:
                info = [None, self.current_machine_id, self.key, self.time]
                pickle.dump(info, file)
        else:
            with open("{0}\\{1}".format(self.folder_path, self.file_name), 'rb') as file:
                info = pickle.load(file)
        return info

    def set_file_data(self, password=None, key=None, time=None):
        info = self.get_file_data()
        if password is None:
            password = info[0]
        if key is None:
            key = info[2]
        if time is None:
            time = info[3]
        if not os.path.isfile(self.folder_path + "\\" + self.file_name):
            if not os.path.exists(self.folder_path):
                os.makedirs(self.folder_path)
        with open("{0}\\{1}".format(self.folder_path, self.file_name), 'wb') as file:
            info = [password, self.current_machine_id, key, time]
            pickle.dump(info, file)

    def get_xor(self, A=None, B=None):
        password: str = ""
        if type(A) == str and type(B) == str:
            if len(A) > 0 and len(B) > 1:
                index_b = -1
                for index_a in range(0, len(A)):
                    index_b += 1
                    if index_b == len(B):
                        index_b = 0
                    password += chr(ord(A[index_a]) ^ ord(B[index_b]))
            return password
        return "-1"

    def set_key(self):
        key: str = ""
        os.system('cls')
        while len(key) != self.key_len:
            key = input("Введите ключ активации: ")
            os.system('cls')
            if len(key) != self.key_len:
                print("Длина ключа должна быть равна {0}".format(self.key_len))
        status_activation = self.chek_key(key)
        if status_activation is True:
            print("Активация успешно пройдена!")
        elif status_activation is False:
            print("Ключ не верен или не действителен!")
        else:
            print("Соединение с сервером потеряно!")
        time.sleep(3)

    def program_process(self):
        ECircuit(mode=self.mode).start()

    def get_free(self):
        info = self.get_file_data()
        time_left = info[3]
        print("\n\nУ Вас осталось: {0:.1f} мин.\n".format(time_left/60.0))
        time.sleep(3)

        p1 = Thread(target=self.program_process, daemon=True)
        p1.start()

        while time_left > 0 and p1.is_alive():
            time_left -= 1
            time.sleep(1)
            self.set_file_data(time=time_left)
            if time_left % 60 == 0:
                print("\n\nУ Вас осталось: {0:.1f} мин.\n".format(time_left/60.0))
        if p1.is_alive():
            print("Время вышло!")
        time.sleep(3)
        exit(0)

    def get_quit(self):
        sys.exit(0)

    def chek_authorization(self):
        while True:
            info = self.get_file_data()
            # print(info)
            # print(self.get_xor(self.current_machine_id, self.key))
            menu_items = []
            self.key = info[2]
            if info[2] is None or info[0] != self.get_xor(self.current_machine_id, self.key):
                menu_items.append(self.menu_items["set_key"])
                if info[3] > 0:
                    menu_items.append(self.menu_items["get_free"])
                menu_items.append(self.menu_items["get_quit"])
                self.get_choice_menu(menu_items)
            else:
                break
        self.program_process()

    def chek_key(self, key: str):
        if type(key) == str and len(key) == self.key_len:
            try:
                sock = socket.socket()
                sock.connect((self.HOST, self.PORT))
                data = json.dumps([self.current_machine_id, key]).encode("utf-8")
                sock.send(data)
                data = sock.recv(1024)
                sock.close()
                password = str(data, encoding="utf-8")
                if self.get_xor(self.current_machine_id, key) == password:
                    self.set_file_data(password=password, key=key)
                    return True
            except Exception as E:
                print(E.args)  # соединение разорвано
                return None
        return False

    def get_choice_menu(self, menu_items: list):
        try:
            while True:
                os.system('cls')
                size = 0
                for item in menu_items:
                    size += 1
                    print("{0} | {1}".format(size, item[0]))
                cin = input("Выберите пункт меню >> ")
                if int(cin) in range(0,size+1):
                    menu_items[int(cin)-1][1]()
                    return
        except Exception as e:
            return