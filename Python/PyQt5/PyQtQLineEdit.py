from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.initialize()

    def initialize(self):
        self.setGeometry(300, 300, 400, 200)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.lineedit = QLineEdit("")
        self.lineedit.setFont(QtGui.QFont('Hack', 20))
        self.lineedit.returnPressed.connect(self.recturn_pressed)
        layout.addWidget(self.lineedit)

        self.label = QLabel("[LineEdit]")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QtGui.QFont('Hack', 25))
        layout.addWidget(self.label)

    def recturn_pressed(self):
        print(self.lineedit.text())
        self.label.setText(self.lineedit.text())

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
