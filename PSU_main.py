import sys
import serial
import time
from serial.tools import list_ports

from PyQt5.QtWidgets import QApplication, QMainWindow

from main_window_ui import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.ports = [p.name for p in list_ports.comports()]
        self.comboBox.addItems(self.ports)
        self.comboBox.setCurrentIndex(-1)
        self.connectSignalsSlots()
        
    
    def connectSignalsSlots(self):
        self.comboBox.currentIndexChanged.connect(self.MCU_serial_comm)
        self.pushButton.toggled.connect(self.enable_remote)
        self.pushButton_2.clicked.connect(self.start_remote)
        self.pushButton_3.clicked.connect(self.stop_remote)
        self.doubleSpinBox_1.valueChanged.connect(self.change_delays)
        self.doubleSpinBox_2.valueChanged.connect(self.change_delays)
        self.doubleSpinBox_3.valueChanged.connect(self.change_delays)
        self.doubleSpinBox_4.valueChanged.connect(self.change_delays)
        
    def MCU_serial_comm(self):
        self.MCU = serial.Serial(
            port = self.comboBox.currentText(), baudrate=115200, timeout=0.1
        )
        time.sleep(1)
        self.enable_remote()

    def change_delays(self):
        D1 = self.doubleSpinBox_1.value()
        D2 = self.doubleSpinBox_2.value()
        D3 = self.doubleSpinBox_3.value()
        D4 = self.doubleSpinBox_4.value()
        string = f'{int(D1*1000)},{int(D2*1000)},{int(D3*1000)},{int(D4*1000)}\n'
        encoded = str.encode(string)
        self.MCU.write(encoded)
    
    def enable_remote(self):
        if self.pushButton.isChecked() == True:
            self.MCU.write(b'Enable,0,0,0\n')
        if self.pushButton.isChecked() == False:
            self.MCU.write(b'Disable,0,0,0\n')

    def start_remote(self):
        self.MCU.write(b'Start,0,0,0\n')

    def stop_remote(self):
        self.MCU.write(b'Stop,0,0,0\n')

    # Execute this method when window is closed
    def closeEvent(self, *args, **kwargs):
        super(QMainWindow, self).closeEvent(*args, **kwargs)
        if self.comboBox.currentText() != "":
            self.MCU.close()
        print("Good-Bye!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())