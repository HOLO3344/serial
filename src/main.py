import sys

try:
    sys.path.append("../ui")
    sys.path.append("../image")
    from main_ui import Ui_MainWindow
except Exception as e:
    print(e)
finally:
    pass

import serial
import threading
import serial.tools.list_ports
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal


class my_app(QMainWindow, Ui_MainWindow):
    """docstring for my_app"""

    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.serial = serial.Serial()

        baudrate_list = ["9600", "115200"]
        for item in baudrate_list:
            self.combobox_seial_baudrate.addItem(item)

        self.button_fresh.clicked.connect(self.fresh_port)
        self.action_fresh.setShortcut("F5")
        self.action_fresh.triggered.connect(self.fresh_port)
        self.fresh_port()

        self.button_open_close.clicked.connect(self.on_click_button_open_close)

        self.recive_process = my_thread(self.recive_process_callback)
        self.recive_process.signal_trigger.connect(self.on_updata_text_output)
        self.alive = threading.Event()

    def fresh_port(self):
        print("fresh_port")
        self.combobox_serial_port.clear()
        port_list = list(serial.tools.list_ports.comports())
        port_list.sort()
        for item in port_list:
            self.combobox_serial_port.addItem(item[0])

    def on_click_button_open_close(self):
        if not self.serial.isOpen():
            try:
                self.serial.baudrate = int(self.combobox_seial_baudrate.currentText())
                self.serial.port = self.combobox_serial_port.currentText()
                self.serial.open()
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
            finally:
                if self.serial.isOpen():
                    self.button_open_close.setText("Close")
                    self.alive.set()
                    self.recive_process.start()
        else:
            self.alive.clear()
            self.recive_process.exit()
            self.serial.close()
            self.button_open_close.setText("Open")

    def on_updata_text_output(self, text):
        self.text_output.append(text)

    def recive_process_callback(self):
        while self.alive.isSet():
            if self.serial.isOpen():
                count = self.serial.inWaiting()
                if count > 0:
                    bytes_data = self.serial.read(count)
                    self.recive_process.signal_trigger.emit(bytes_data.decode("ascii"))
                self.recive_process.msleep(100)


class my_thread(QThread):
    """docstring for my_thread"""

    signal_trigger = pyqtSignal(str)

    def __init__(self, callback):
        super(my_thread, self).__init__()
        self.callback = callback

    def run(self):
        self.callback()


if __name__ == '__main__':
    print("App start...")
    app = QApplication(sys.argv)
    window = my_app()
    window.show()
    sys.exit(app.exec_())
