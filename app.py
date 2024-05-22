import sys
import PyQt6
from PyQt6 import uic, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow

from PIL.ImageQt import ImageQt

from card import card
from images import *
import pickle


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./ui.ui", self)

        self.cardData = {
            "name": "",
            "description": "",
            "stats": [],
            "hat": "",
            "body": "",
            "accessory": "",
            "template": template,
            "frontBg": "",
            "frontBand": frontBand,
            "backImg": backImg,
            "hue": 0,
        }

        self.syncColorInputs()

        self.labelImagePreview.setScaledContents(True)
        self.menuOtworz.triggered.connect(self.openSaveFile)
        self.menuSave.triggered.connect(self.saveFile)
        self.buttonGenerate.clicked.connect(self.generate)


    def syncColorInputs(self):
        self.inputColorNumber.valueChanged.connect(lambda: self.inputColor.setValue(self.inputColorNumber.value()))
        self.inputColor.valueChanged.connect(lambda: self.inputColorNumber.setValue(self.inputColor.value()))


    def generate(self):
        try:
            self.testCard = card(self.inputName.text(), 
                            self.inputDesc.toPlainText(), 
                            [self.inputMana.value(), self.inputStamina.value(), self.inputHealth.value()], 
                            hatRomantic, 
                            bodyRomantic, 
                            accessoryRomantic, 
                            template, 
                            frontBg1, 
                            frontBand, 
                            backImg, 
                            self.inputColorNumber.value())

            testCardImage = self.testCard.renderCard()
            image = ImageQt(testCardImage)

            self.pixmap = QPixmap.fromImage(image)
            self.labelImagePreview.setPixmap(self.pixmap)

            self.labelStatus.setText('Wygenerowano :)')
            self.labelStatus.setStyleSheet('background-color: #a8ff66') 

        except Exception as error:
            self.labelStatus.setText(fr'Nie udało sie :(')
            self.labelStatus.setStyleSheet('background-color: #ff6b66') 

    
    def openSaveFile(self):
        # 🔥
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Wybierz plik.', '', '*.card')

        with open(path, 'rb') as handle:
            openedCard = pickle.load(handle)

            openedCardImage = openedCard.renderCard()

            image = ImageQt(openedCardImage)
            self.pixmap = QPixmap.fromImage(image)

            self.labelImagePreview.setPixmap(self.pixmap)


    def saveFile(self):
        # 🔥
        # path = str(QFileDialog.getExistingDirectory(self, "Wybierz lokalizacje."))
        
        self.testCard.saveCardEdit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())