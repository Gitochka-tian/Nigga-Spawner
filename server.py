import socket, sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtGui import QPixmap
import threading


class Display(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nigga Swaper")
        self.setFixedSize(720,480)
        self.label = QLabel(self)
        self.label.setFixedSize(720,480)
        image = QPixmap('first_picture.jpg')
        self.label.setPixmap(image)
    def changeImage(self):
        image2 = QPixmap('second_picture.jpg')
        self.label.setPixmap(image2)

app = QApplication(sys.argv)
window = Display()
window.show()


MainSocket = socket.socket()
MainSocket.bind(('127.0.0.1', 8090))
MainSocket.listen(1)
connection, addr = MainSocket.accept()


data = connection.recv(1024).decode('utf-8')
content = 'aboba'.encode('utf-8')
HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
connection.send(HDRS.encode('utf-8') + content)

print(data)

if data == 'ON'.encode('utf-8') :
    window.changeImage()


connection.close()
app.exec()