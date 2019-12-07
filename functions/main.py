import sys
import os
import time
import json
import pickle
import socket
import subprocess
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot, QTimer
from PyQt5.Qt import QApplication, QMessageBox

from interfaces.activationWindow import ActivationWindow
from interfaces.mainWindow import MainWindow

class MainProcess(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.key_len = 36
        self.time_left = 300
        self.key = None
        self.folder_path = os.path.expanduser('~') + "\\.E-Circuit builder"
        self.file_name = "authorization.bin"
        self.current_machine_id = self.get_current_machine_id()
        # --------------------------------------------------------------------------------------------------------------
        self.HOST = str('109.254.54.221')  # '127.0.0.1'  # Standard loopback interface address (localhost)
        self.PORT = 8888  # 65432  # Port to listen on (non-privileged ports are > 1023)
        # таймер -------------------------------------------------------------------------------------------------------
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timeout)
        # --------------------------------------------------------------------------------------------------------------
        if self.is_activated():
            self.mainWindow = MainWindow()
            self.mainWindow.show()
        else:
            self.start_activationWindow()

    def start_activationWindow(self):
        time_left = self.get_activation()[3]
        self.activationWindow = ActivationWindow(time_left=time_left, key_len=self.key_len)
        self.activationWindow.send_key.connect(self.send_key_to_server)
        self.activationWindow.pushFree.clicked.connect(self.startFreePeriod)
        self.activationWindow.show()

    def mainWindow_closed(self):
        self.activationWindow.show()
        self.timer.stop()

    def startFreePeriod(self):
        self.timer.start(1000)
        self.activationWindow.close()
        self.mainWindow = MainWindow()
        self.mainWindow.closed.connect(self.mainWindow_closed)
        self.mainWindow.show()

    def timeout(self):
        time_left = self.get_activation()[3]
        time_left -= 1
        if time_left < 0:
            time_left = 0
        self.set_activation(time_left=time_left)
        self.activationWindow.set_label_time(time_left)
        if time_left % 60 == 0 and time_left != 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("У Вас осталось времени: {0} мин. {1} сек.".format(int(time_left/60), time_left % 60))
            msg.setWindowTitle("Активация")
            msg.exec_()
        if time_left <= 0:
            self.timer.stop()
            self.activationWindow.pushFree.setEnabled(False)
            self.activationWindow.show()
            self.mainWindow.close()


    def get_current_machine_id(self):
        return subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

    def exit_program(self):
        print("1234567")

    # работа с файлом активации ________________________________________________________________________________________
    def get_activation(self):
        # если файла конфига нет
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
        if not os.path.isfile(self.folder_path + "\\" + self.file_name):
            self.set_activation()
        with open("{0}\\{1}".format(self.folder_path, self.file_name), 'rb') as file:
            info = pickle.load(file)
        return info

    def set_activation(self, password=None, key=None, time_left: int = 300):
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)
        with open("{0}\\{1}".format(self.folder_path, self.file_name), 'wb') as file:
            info = [password, self.current_machine_id, key, time_left]
            pickle.dump(info, file)

    # активация ________________________________________________________________________________________________________
    def xor(self, A=None, B=None):
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

    def is_activated(self):
        info = self.get_activation()
        password = info[0]
        current_machine_id = info[1]
        key = info[2]
        if key is None:
            return False
        if current_machine_id != self.current_machine_id:
            return False
        if password != self.xor(self.current_machine_id, key):
            return False
        return True

    @pyqtSlot(str)
    def send_key_to_server(self, key: str):
        check = False
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        try:
            sock = socket.socket()
            sock.settimeout(2)
            sock.connect((self.HOST, self.PORT))
            data = json.dumps([self.current_machine_id, key]).encode("utf-8")
            sock.send(data)
            data = sock.recv(1024)
            sock.close()
            password = str(data, encoding="utf-8")
            if self.xor(self.current_machine_id, key) == password:
                self.set_activation(password=password, key=key, time_left=self.time_left)
                msg.setText("Активация успешно пройдена")
                check = True
            else:
                msg.setText("Ключ не верен или не действителен!")
        except Exception as E:
            print(E.args)  # соединение разорвано
            msg.setText("Не удалось подключиться к серверу")
        msg.setWindowTitle("Активация")
        msg.exec_()
        if check is True:
            self.activationWindow.close()
            self.mainWindow = MainWindow()
            self.mainWindow.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    obj = MainProcess()
    sys.exit(app.exec())
