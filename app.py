import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic, QtWidgets
from PyQt6.QtGui import QPixmap

from PIL.ImageQt import ImageQt

from card import card
from translateAtts import *

from pathlib import Path  
from threading import *
import pickle

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # Załadowanie UI z wygenerowanego przez designer pliku
        uic.loadUi("./ui.ui", self)

        self.cardData = {
            "name": "",
            "desc": "",
            "stats": [0, 0, 0,],
            "hat": "",
            "body": "",
            "accessory": "",
            "template": "",
            "frontBg": "",
            "frontBand": "",
            "backImg": "",
            "hue": 0
        }

        self.inputHat.setItemData(0, None)
        self.inputHat.setItemData(1, fr"img\hatMag.png")
        self.inputHat.setItemData(2, fr"img\hatKnight.png")
        self.inputHat.setItemData(3, fr"img\hatRomantic.png")

        self.inputBody.setItemData(0, None)
        self.inputBody.setItemData(1, fr"img\bodyMag.png")
        self.inputBody.setItemData(2, fr"img\bodyKnight.png")
        self.inputBody.setItemData(3, fr"img\bodyRomantic.png")

        self.inputAccessory.setItemData(0, None)
        self.inputAccessory.setItemData(1, fr"img\accessoryMag.png")
        self.inputAccessory.setItemData(2, fr"img\accessoryKnight.png")
        self.inputAccessory.setItemData(3, fr"img\accessoryRomantic.png")

        self.inputBackground.setItemData(0, None)
        self.inputBackground.setItemData(1, fr"img\frontBg1.png")
        self.inputBackground.setItemData(2, fr"img\frontBg2.png")

        self.inputHatOther.clicked.connect(lambda: self.customAttr("hat"))
        self.inputBodyOther.clicked.connect(lambda: self.customAttr("body"))
        self.inputAccessoryOther.clicked.connect(lambda: self.customAttr("accessory"))
        self.inputBackgroundOther.clicked.connect(lambda: self.customAttr("frontBg"))

        # ustawianie obu inputów od koloru (suwak i pole) na te same wartości
        self.inputColorNumber.valueChanged.connect(lambda: self.inputColor.setValue(self.inputColorNumber.value()))
        self.inputColor.valueChanged.connect(lambda: self.inputColorNumber.setValue(self.inputColor.value()))

        # Podpinanie funkcji do menu i przycisku
        self.menuOtworz.triggered.connect(self.openSaveFile)
        self.menuSave.triggered.connect(self.saveFile)
        self.menuExport.triggered.connect(self.exportFile)
        self.buttonGenerate.clicked.connect(self.thread)

        # Skalowanie obrazka pod label
        self.labelImagePreview.setScaledContents(True)


    def alert(self, message, color):
        self.labelStatus.setText(message)
        self.labelStatus.setStyleSheet(f'background-color: {color}')


    def customAttr(self, attr):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Wybierz plik.', '', '*.png')

        self.cardData[attr] = path

        print(self.cardData)

    def thread(self): 
        self.alert('generowanie', '#ffe645')

        t1=Thread(target=self.generate) 
        t1.start() 


    def generate(self):
        try:
            self.testCard = card(self.inputName.text(), 
                            self.inputDesc.toPlainText(), 
                            [self.inputMana.value(), self.inputStamina.value(), self.inputHealth.value()], 
                            self.inputHat.currentData(), 
                            self.inputBody.currentData(),
                            self.inputAccessory.currentData(), 
                            fr"img\template1.png", 
                            self.inputBackground.currentData(), 
                            fr"img\frontBand1.png", 
                            fr"img\backImg1.png", 
                            self.inputColorNumber.value())


            # Renderowanie karty, zmiana obiektu karty PIL na ImageQt, zrobienie z obrazka pixmapy, umieszczenie pixmapy w labelu
            testCardImage = self.testCard.renderCard()
            image = ImageQt(testCardImage)
            self.pixmap = QPixmap.fromImage(image)
            self.labelImagePreview.setPixmap(self.pixmap)

            self.alert('Wygenerowano', '#a8ff66')

        except Exception as error:
            self.alert(error, '#ff6b66')

    
    def openSaveFile(self):
        try:
            path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Wybierz plik.', '', '*.card')

            with open(path, 'rb') as handle:
                openedCard = pickle.load(handle)

                # Uzyskanie nazw plików atrybutów bez ścieżki i rozszerzenia
                hatName = Path(openedCard.hatName).stem
                bodyName = Path(openedCard.bodyName).stem
                accessoryName = Path(openedCard.accessoryName).stem
                frontBgName = Path(openedCard.frontBgName).stem

                # "Przetłumaczenie" uzyskanej nazwy pliku na nazwe która może być w comboboxie (nameTranslate -> translateAtts.py), później kolejne przetłumaczenie tym razem do odpowiedniego indexu w comboboxie
                indexHat = self.inputHat.findText(nameTranslate[hatName])
                indexBody = self.inputBody.findText(nameTranslate[bodyName])
                indexAccessory = self.inputAccessory.findText(nameTranslate[accessoryName])
                indexFrontBg = self.inputBackground.findText(nameTranslate[frontBgName])

                # Aktualizowanie wszystkich pól zgodnie z otworzonym plikiem
                self.inputName.setText(openedCard.name)
                self.inputDesc.setPlainText(openedCard.desc)
                self.inputMana.setValue(int(openedCard.stats[0]))
                self.inputStamina.setValue(int(openedCard.stats[1]))
                self.inputHealth.setValue(int(openedCard.stats[2]))
                self.inputHat.setCurrentIndex(indexHat)
                self.inputBody.setCurrentIndex(indexBody)
                self.inputAccessory.setCurrentIndex(indexAccessory)
                self.inputBackground.setCurrentIndex(indexFrontBg)
                self.inputColor.setValue(openedCard.hue)
                self.inputColorNumber.setValue(openedCard.hue)

                self.alert('Otworzono plik', '#a8ff66')
                
        except Exception as error:
            self.alert('Nie udało się otworzyć pliku', '#ff6b66')


    def saveFile(self):
        try:
            path = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Wybierz lokalizacje."))
            self.testCard.saveCardEdit(path)

            self.alert('Zapisano', '#a8ff66')
        except:
            self.alert('Nie udało się zapisać pliku', '#ff6b66') 

    
    def exportFile(self):
        try:
            path = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Wybierz lokalizacje."))
            self.testCard.exportCardToPNG(path)

            self.alert('Wyeksportowano', '#a8ff66')
        except:
            self.alert('Nie udało się eksportować pliku', '#ff6b66') 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())