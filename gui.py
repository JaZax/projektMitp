import sys
from PyQt6 import QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow

from PIL.ImageQt import ImageQt

from card import card
from images import *

testCard = card("agnieszka", "fajny ten pimpek", [0, 0, 100], hatMag, bodyKnight, accessoryRomantic, template, frontBg2, frontBand, backImg, 129)

testCardImage = testCard.renderCard()
image = ImageQt(testCardImage)
print(image)

class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setWindowTitle("Generator kart kapibar")
        self.setGeometry(0, 0, 1000, 500)

        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.pixmap = QPixmap.fromImage(image)

        self.label.setPixmap(self.pixmap)
        self.setCentralWidget(self.label)
        self.resize(self.pixmap.width(), self.pixmap.height())

def window():
    app = QApplication(sys.argv)
    win = mainWindow()

    win.show()
    sys.exit(app.exec())
