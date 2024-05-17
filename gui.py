from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

import PIL
from PIL import Image

from card import card 
from images import *

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()

        self.setGeometry(0, 0, 1000, 600)
        self.setWindowTitle("Generator kart kapibar")

        self.initUI()
    
    def initUI(self):
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("test")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.b1.setText("test")
       
    
def window():
    app = QApplication(sys.argv)
    win = App()

    win.show()
    sys.exit(app.exec_())