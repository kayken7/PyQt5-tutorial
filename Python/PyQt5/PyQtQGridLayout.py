from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QGridLayout
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 600, 500)

        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel("Label Grid 1 \n(row:0, col:0)")
        layout.addWidget(label, 0, 0)
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QtGui.QFont('Hack', 15))

        label = QLabel("Label Grid 2\n(row:0, col:1)")
        layout.addWidget(label, 0, 1)
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QtGui.QFont('Hack', 15))

        label = QLabel("Label Grid 3\n(row:1, col:0)")
        layout.addWidget(label, 1, 0)
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QtGui.QFont('Hack', 15))

        label = QLabel("Label Grid 4\n(row:1, col:1)")
        layout.addWidget(label, 1, 1)
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QtGui.QFont('Hack', 15))


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
