from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("First Window PyQt5")


app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec_())
