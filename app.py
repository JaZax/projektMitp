import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic, QtWidgets
from PyQt6.QtGui import QPixmap

from PIL.ImageQt import ImageQt

from card import card
from images import *

from pathlib import Path  
from threading import *
import pickle

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # Załadowanie UI z wygenerowanego przez designer pliku
        uic.loadUi("./ui.ui", self)

        self.inputHat.setItemData(0, None)
        self.inputHat.setItemData(1, hatMag)
        self.inputHat.setItemData(2, hatKnight)
        self.inputHat.setItemData(3, hatRomantic)

        self.inputBody.setItemData(0, None)
        self.inputBody.setItemData(1, bodyMag)
        self.inputBody.setItemData(2, bodyKnight)
        self.inputBody.setItemData(3, bodyRomantic)

        self.inputAccessory.setItemData(0, None)
        self.inputAccessory.setItemData(1, accessoryMag)
        self.inputAccessory.setItemData(2, accessoryKnight)
        self.inputAccessory.setItemData(3, accessoryRomantic)

        self.inputBackground.setItemData(0, None)
        self.inputBackground.setItemData(1, frontBg1)
        self.inputBackground.setItemData(2, frontBg2)

        self.syncColorInputs()

        # Skalowanie obrazka pod label
        self.labelImagePreview.setScaledContents(True)

        # Podpinanie funkcji do menu i przycisku
        self.menuOtworz.triggered.connect(self.openSaveFile)
        self.menuSave.triggered.connect(self.saveFile)
        self.menuExport.triggered.connect(self.exportFile)
        self.buttonGenerate.clicked.connect(self.thread)


    def syncColorInputs(self):
        # ustawianie obu inputów od koloru (suwak i pole) na te same wartości
        self.inputColorNumber.valueChanged.connect(lambda: self.inputColor.setValue(self.inputColorNumber.value()))
        self.inputColor.valueChanged.connect(lambda: self.inputColorNumber.setValue(self.inputColor.value()))


    def thread(self): 
        self.labelStatus.setText('Generowanie...')
        self.labelStatus.setStyleSheet('background-color: #ffe645') 

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
                            template, 
                            self.inputBackground.currentData(), 
                            frontBand, 
                            backImg, 
                            self.inputColorNumber.value())


            # Renderowanie karty, zmiana obiektu karty PIL na ImageQt, zrobienie z obrazka pixmapy, umieszczenie pixmapy w labelu
            testCardImage = self.testCard.renderCard()
            image = ImageQt(testCardImage)
            self.pixmap = QPixmap.fromImage(image)
            self.labelImagePreview.setPixmap(self.pixmap)

            self.labelStatus.setText('Wygenerowano :)')
            self.labelStatus.setStyleSheet('background-color: #a8ff66') 

        except Exception as error:
            print(error)

            self.labelStatus.setText(str(error))
            self.labelStatus.setStyleSheet('background-color: #ff6b66') 

    
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

                # "Przetłumaczenie" uzyskanej nazwy pliku na nazwe która może być w comboboxie (nameTranslate -> images.py), później kolejne przetłumaczenie tym razem do odpowiedniego indexu w comboboxie
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

                self.labelStatus.setText('Otworzono zapisany plik :)')
                self.labelStatus.setStyleSheet('background-color: #5dbbe3')
                
        except Exception as error:
            print(error)

            self.labelStatus.setText(fr'Nie udało się otworzyć pliku')
            self.labelStatus.setStyleSheet('background-color: #ff6b66') 


    def saveFile(self):
        path = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Wybierz lokalizacje."))
        self.testCard.saveCardEdit(path)

    
    def exportFile(self):
        path = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Wybierz lokalizacje."))
        self.testCard.exportCardToPNG(path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())