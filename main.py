from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        #Window Properties
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.center()

        #Load UIs
        self.loadStart()

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()