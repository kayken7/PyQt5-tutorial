from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("Python PyQt5")

        self.label = QLabel("Hello World, PyQt5!\nWelcome to the App!")
        self.label.setFont(QtGui.QFont('Hack', 20))

        layout = QVBoxLayout()
        layout.addWidget(self.label, alignment=Qt.AlignCenter)
        self.setLayout(layout)


app = QApplication(sys.argv)
root = Window()
root.show()

sys.exit(app.exec_())
