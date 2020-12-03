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
        self.setGeometry(300, 300, 500, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.checkbox1 = QCheckBox("CPU")
        self.checkbox1.setChecked(False)
        self.checkbox1.setFont(QtGui.QFont('Hack', 15))
        self.checkbox1.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox1)

        self.checkbox2 = QCheckBox("Graphic Card")
        self.checkbox2.setChecked(False)
        self.checkbox2.setFont(QtGui.QFont('Hack', 15))
        self.checkbox2.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox2)

        self.checkbox3 = QCheckBox("Mainboard")
        self.checkbox3.setChecked(False)
        self.checkbox3.setFont(QtGui.QFont('Hack', 15))
        self.checkbox3.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox3)

        self.label = QLabel("[CHECKBOX]")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QtGui.QFont('Hack', 20))
        layout.addWidget(self.label)


    def checkbox_toggled(self):
        checked = []
        items = ""

        if self.checkbox1.isChecked():
            checked.append("CPU")

        if self.checkbox2.isChecked():
            checked.append("Graphic Card")

        if self.checkbox3.isChecked():
            checked.append("Mainboard")

        print("* Selected: %s" % ", ".join(checked))

        for item in checked:
            items += "*checked : " + item + "\n"
            self.label.setText(items)


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
