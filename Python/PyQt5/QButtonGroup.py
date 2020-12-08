from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import sys
import random

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 300)

        frame = QVBoxLayout()
        self.setLayout(frame)

        label = QLabel("[가위바위보 게임]\n준비가 되면 클릭하세요!")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QtGui.QFont('Noto Sans KR', 30))
        frame.addWidget(label)

        self.label = QLabel("")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QtGui.QFont('Noto Sans KR', 30))
        frame.addWidget(self.label)

        layout = QHBoxLayout()
        frame.addLayout(layout)

        self.btnGroup = QButtonGroup()
        self.btnGroup.setExclusive(False)
        self.btnGroup.buttonClicked[int].connect(self.button_clicked)

        button = QPushButton("가위")
        button.setFont(QtGui.QFont('Noto Sans KR', 20))
        self.btnGroup.addButton(button, 1)
        layout.addWidget(button)

        button = QPushButton("바위")
        button.setFont(QtGui.QFont('Noto Sans KR', 20))
        self.btnGroup.addButton(button, 2)
        layout.addWidget(button)

        button = QPushButton("보")
        button.setFont(QtGui.QFont('Noto Sans KR', 20))
        self.btnGroup.addButton(button, 3)
        layout.addWidget(button)

    def button_clicked(self, id):
        for btn in self.btnGroup.buttons():
            if btn is self.btnGroup.button(id):
                player = btn.text()
                self.RockPaperScissors(player)

    def RockPaperScissors(self, player):
        cpu_choice = random.choice(['가위','바위','보'])
        print("CPU는     [" + cpu_choice +"] 를 선택했다 -", end='')

        if player == "가위":
            print("\n플레이어는 [가위]를 선택했다 -")
            if cpu_choice == "가위":
                print("*비겼다.")
                self.label.setText("무승부 게임 -")
            elif cpu_choice == "바위":
                print("*졌다~~")
                self.label.setText("졌다~ ㅠㅠ;;;")
            else:
                print("*이겼다!!!")
                self.label.setText("당신의 승리!!")

        elif player == "바위":
            print("\n플레이어는 [바위]를 선택했다 -")
            if cpu_choice == "가위":
                print("*이겼다!!!")
                self.label.setText("당신의 승리!!")
            elif cpu_choice == "바위":
                print("*비겼다.")
                self.label.setText("무승부 게임 -")
            else:
                print("*졌다~~")
                self.label.setText("졌다~ ㅠㅠ;;;")

        elif player == "보":
            print("\n플레이어는 [보]를 선택했다 -")
            if cpu_choice == "가위":
                print("*졌다~~")
                self.label.setText("졌다~ ㅠㅠ;;;")
            elif cpu_choice == "바위":
                print("*이겼다!!!")
                self.label.setText("당신의 승리!!")
            else:
                print("*비겼다.")
                self.label.setText("무승부 게임 -")




app = QApplication(sys.argv)
screen = Window()
screen.show()

sys.exit(app.exec_())

