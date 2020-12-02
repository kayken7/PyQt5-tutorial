from PyQt5.QtWidgets import QWidget, QApplication, \
    QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setUp()

    def setUp(self):
        label = QLabel("Good Question 1")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QtGui.QFont('Hack', 20))

        label2 = QLabel("slept well?")
        label2.setAlignment(Qt.AlignCenter)
        label2.setFont(QtGui.QFont('Hack', 20))

        label3 = QLabel("if not, go get some sleep!")
        label3.setAlignment(Qt.AlignCenter)
        label3.setFont(QtGui.QFont('Hack', 20))

        button = QPushButton("no I want to play~")
        button.setFont(QtGui.QFont('Hack', 20))

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(button)

        self.setLayout(layout)
        self.setWindowTitle("First Window PyQt5")
        self.setGeometry(300, 300, 500, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = Window()
    sys.exit(app.exec_())
