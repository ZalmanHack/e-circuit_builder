import socket
import json
import os
import string
import random
from threading import Thread

class Server():

    def __init__(self):
        self.file_name = "keys_data.json"
        self.folder_path = os.path.expanduser('~') + "\\.E-Circuit Server"
        # если файла конфига нет
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
        # --------------------------------------------------------------------------------------------------------------
        self.sock = socket.socket()
        self.sock.bind(('', 8888))

    def read_file_json(self):
        try:
            file = open('{0}\\{1}.json'.format(self.folder_path, self.file_name), 'r', encoding="utf-8")
            return json.load(file)
        except Exception as E:
            return {}

    def write_file_json(self, data_json):
        try:
            file = open('{0}\\{1}.json'.format(self.folder_path, self.file_name), 'w', encoding="utf-8")
            return json.dump(data_json, file, indent=4)
        except Exception as E:
            return {}

    def get_xor(self, A: str, B: str):
        password: str = ""
        if len(A) > 0 and len(B) > 1:
            index_b = -1
            for index_a in range(0, len(A)):
                index_b += 1
                if index_b == len(B):
                    index_b = 0
                password += chr(ord(A[index_a]) ^ ord(B[index_b]))
            return password
        return "-1"

    def generation_key(self):
        file_keys = self.read_file_json()
        while True:
            key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(36))
            if key not in file_keys:
                file_keys[key] = {"is_used": True, "machine_id": None}
                self.write_file_json(file_keys)
                return key


    def menu_process(self):
        input("Для получения нового ключа нажмите любую кнопку.")
        while True:
            input()
            print(self.generation_key())


    def server_process(self):
        os.system('cls')

        while True:
            data = None
            try:
                self.sock.listen()
                conn, addr = self.sock.accept()
                print('connected:', addr)
                data = conn.recv(1024)
                if not data:
                    conn.close()
                else:
                    data = json.loads(data)
                    key = data[1]
                    machine_id = data[0]

                    keys_file = self.read_file_json()
                    xor_data = "-1"
                    activation = False
                    if key in keys_file:
                        if keys_file[key]["is_used"] is True:
                            if keys_file[key]["machine_id"] == machine_id or keys_file[key]["machine_id"] is None:
                                activation = True
                                keys_file[key]["machine_id"] = machine_id
                                self.write_file_json(keys_file)
                                xor_data = self.get_xor(machine_id, key)
                    conn.send(bytes(xor_data, encoding="utf-8"))
                    # answer = json.dumps(xor_data).encode("utf-8")
                    print("    Серийный номер компьютера: ", machine_id)
                    print("    Введенный ключ активации:  ", key)
                    print("    Активация продукта:        ", activation)
                conn.close()
            except Exception as E:
                print("    data: ", data)
                print("    Error:", E.args)


if __name__ == "__main__":
    server = Server()
    # server.generation_keys(100)
    p1 = Thread(target=server.server_process)
    p2 = Thread(target=server.menu_process)
    p1.start()
    p2.start()