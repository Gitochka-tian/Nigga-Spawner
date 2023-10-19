import sys
import socket
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


sock = socket.socket()
sock.connect(('10.193.157.129', 8090))
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("Nigga Swapper")

        self.button = QPushButton("Swap Niggas!")
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_released)
        self.button.setChecked(self.button_is_checked)
        self.button.setFixedSize(400,300)
        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.button.setText("Niggas Already Swapped")
        HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
        content = 'ON'.encode('utf-8')
        sock.send(HDRS.encode('utf-8') + content)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

sock.close()