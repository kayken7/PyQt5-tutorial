from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
app = QApplication(sys.argv)
mainScreen = QMainWindow()
QMainWindow.__init__(mainScreen)
mainScreen.show()
sys.exit(app.exec_())
