from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5 import QtGui
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        uic.loadUi("interfaces/untitled.ui", self)
        
        self.setWindowIcon(QtGui.QIcon("assets/icon_1000x1000.png"))
        self.setWindowTitle("Van Gogh - Alpha")

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()