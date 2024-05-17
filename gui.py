import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow

from PIL.ImageQt import ImageQt

from card import card
from images import *
import pickle

testCard = card("ehfaiuwhfieahufahw", "karta jaka jest każdy widzi", ["2", "2", "2"], hatRomantic, bodyRomantic, accessoryRomantic, template, frontBg1, frontBand, backImg, 180)

testCardImage = testCard.renderCard()

# save card file
#
# testCard.saveCardEdit()


# read card file
#
# with open('agnieszka.card', 'rb') as handle:
#     b = pickle.load(handle)
# 
#     print(b)

image = ImageQt(testCardImage)
print(image)

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generator kart kapibar")
        self.setGeometry(0, 0, 1000, 500)

        self.initUI()

    def initUI(self):

        self.pixmap = QPixmap.fromImage(image)

        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 771, 401))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonSave = QtWidgets.QPushButton(parent=self.widget)
        self.buttonSave.setObjectName("buttonSave")
        self.gridLayout.addWidget(self.buttonSave, 7, 3, 1, 1)
        self.labelHealth = QtWidgets.QLabel(parent=self.widget)
        self.labelHealth.setObjectName("labelHealth")
        self.gridLayout.addWidget(self.labelHealth, 4, 2, 1, 1)
        self.labelDesc = QtWidgets.QLabel(parent=self.widget)
        self.labelDesc.setObjectName("labelDesc")
        self.gridLayout.addWidget(self.labelDesc, 2, 0, 1, 1)
        self.labelStamina = QtWidgets.QLabel(parent=self.widget)
        self.labelStamina.setObjectName("labelStamina")
        self.gridLayout.addWidget(self.labelStamina, 4, 1, 1, 1)
        self.buttonHat = QtWidgets.QPushButton(parent=self.widget)
        self.buttonHat.setObjectName("buttonHat")
        self.gridLayout.addWidget(self.buttonHat, 6, 0, 1, 1)
        self.labelName = QtWidgets.QLabel(parent=self.widget)
        self.labelName.setObjectName("labelName")
        self.gridLayout.addWidget(self.labelName, 0, 0, 1, 1)
        self.buttonGenerate = QtWidgets.QPushButton(parent=self.widget)
        self.buttonGenerate.setObjectName("buttonGenerate")
        self.gridLayout.addWidget(self.buttonGenerate, 7, 0, 1, 3)
        self.inputName = QtWidgets.QLineEdit(parent=self.widget)
        self.inputName.setObjectName("inputName")
        self.gridLayout.addWidget(self.inputName, 1, 0, 1, 3)
        self.inputMana = QtWidgets.QSpinBox(parent=self.widget)
        self.inputMana.setObjectName("inputMana")
        self.gridLayout.addWidget(self.inputMana, 5, 0, 1, 1)
        self.inputHealth = QtWidgets.QSpinBox(parent=self.widget)
        self.inputHealth.setObjectName("inputHealth")
        self.gridLayout.addWidget(self.inputHealth, 5, 2, 1, 1)
        self.buttonAccessory = QtWidgets.QPushButton(parent=self.widget)
        self.buttonAccessory.setObjectName("buttonAccessory")
        self.gridLayout.addWidget(self.buttonAccessory, 6, 2, 1, 1)
        self.buttonExport = QtWidgets.QPushButton(parent=self.widget)
        self.buttonExport.setObjectName("buttonExport")
        self.gridLayout.addWidget(self.buttonExport, 7, 4, 1, 1)

        self.labelImagePreview = QtWidgets.QLabel(parent=self.widget)
        self.labelImagePreview.setObjectName("labelImagePreview")
        self.labelImagePreview.setPixmap(self.pixmap)
        self.labelImagePreview.setScaledContents(True)

        self.gridLayout.addWidget(self.labelImagePreview, 0, 3, 7, 2)
        self.inputStamina = QtWidgets.QSpinBox(parent=self.widget)
        self.inputStamina.setObjectName("inputStamina")
        self.gridLayout.addWidget(self.inputStamina, 5, 1, 1, 1)
        self.inputDesc = QtWidgets.QTextEdit(parent=self.widget)
        self.inputDesc.setObjectName("inputDesc")
        self.gridLayout.addWidget(self.inputDesc, 3, 0, 1, 3)
        self.labelMana = QtWidgets.QLabel(parent=self.widget)
        self.labelMana.setObjectName("labelMana")
        self.gridLayout.addWidget(self.labelMana, 4, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 1, 1, 1)
        self.gridLayout.setColumnStretch(3, 10)
        self.gridLayout.setColumnStretch(4, 10)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Generator kart kapibar"))
        self.buttonSave.setText(_translate("MainWindow", "Zapisz plik edytowalny"))
        self.labelHealth.setText(_translate("MainWindow", "Zdrowie"))
        self.labelDesc.setText(_translate("MainWindow", "Opis"))
        self.labelStamina.setText(_translate("MainWindow", "Stamina"))
        self.buttonHat.setText(_translate("MainWindow", "Czapka"))
        self.labelName.setText(_translate("MainWindow", "Nazwa"))
        self.buttonGenerate.setText(_translate("MainWindow", "Generuj"))
        self.buttonAccessory.setText(_translate("MainWindow", "Akcesorium"))
        self.buttonExport.setText(_translate("MainWindow", "Eksportuj PNG"))
        self.labelMana.setText(_translate("MainWindow", "Mana"))
        self.pushButton.setText(_translate("MainWindow", "Wdzianko"))


def window():
    app = QApplication(sys.argv)
    win = mainWindow()

    win.show()
    sys.exit(app.exec())
