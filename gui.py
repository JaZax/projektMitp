import sys
import PyQt6
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow

from PIL.ImageQt import ImageQt

from card import card
from images import *
import pickle

# save card file
#
# testCard.saveCardEdit()


# read card file
#
# with open('agnieszka.card', 'rb') as handle:
#     b = pickle.load(handle)
# 
#     print(b)

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generator kart kapibar")
        self.setGeometry(0, 0, 1160, 700)

        self.initUI()

    def generate(self):
        testCard = card(self.inputName.text(), 
                        self.inputDesc.toPlainText(), 
                        [self.inputMana.value(), self.inputStamina.value(), self.inputHealth.value()], 
                        hatRomantic, 
                        bodyRomantic, 
                        accessoryRomantic, 
                        template, 
                        frontBg1, 
                        frontBand, 
                        backImg, 
                        self.colorInputNumber.value())
        
        testCardImage = testCard.renderCard()
        image = ImageQt(testCardImage)
        self.pixmap = QPixmap.fromImage(image)

        self.labelImagePreview.setPixmap(self.pixmap)

    def initUI(self):

        self.centralwidget = QtWidgets.QWidget(parent=self)
        font = PyQt6.QtGui.QFont()
        font.setPointSize(11)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")

        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 1137, 642))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.line2 = QtWidgets.QFrame(parent=self.widget)
        self.line2.setMinimumSize(QtCore.QSize(0, 10))
        self.line2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line2.setObjectName("line2")
        self.gridLayout.addWidget(self.line2, 5, 0, 1, 3)

        self.labelImagePreview = QtWidgets.QLabel(parent=self.widget)
        self.labelImagePreview.setMinimumSize(QtCore.QSize(800, 640))
        self.labelImagePreview.setMaximumSize(QtCore.QSize(800, 640))
        self.labelImagePreview.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.labelImagePreview.setObjectName("labelImagePreview")
        self.gridLayout.addWidget(self.labelImagePreview, 0, 3, 19, 1)
        self.labelImagePreview.setScaledContents(True)

        self.line1 = QtWidgets.QFrame(parent=self.widget)
        self.line1.setMinimumSize(QtCore.QSize(0, 10))
        self.line1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line1.setObjectName("line1")
        self.gridLayout.addWidget(self.line1, 2, 0, 1, 3)

        self.line4 = QtWidgets.QFrame(parent=self.widget)
        self.line4.setMinimumSize(QtCore.QSize(0, 10))
        self.line4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line4.setObjectName("line4")
        self.gridLayout.addWidget(self.line4, 15, 0, 1, 3)

        self.labelName = QtWidgets.QLabel(parent=self.widget)
        self.labelName.setObjectName("labelName")
        self.gridLayout.addWidget(self.labelName, 0, 0, 1, 1)

        self.colorInputNumber = QtWidgets.QSpinBox(parent=self.widget)
        self.colorInputNumber.setMinimumSize(QtCore.QSize(80, 0))
        self.colorInputNumber.setMaximum(360)
        self.colorInputNumber.setObjectName("colorInputNumber")
        self.colorInputNumber.valueChanged.connect(lambda: self.inputColor.setValue(self.colorInputNumber.value()))
        self.gridLayout.addWidget(self.colorInputNumber, 14, 2, 1, 1)

        self.labelColor = QtWidgets.QLabel(parent=self.widget)
        self.labelColor.setObjectName("labelColor")
        self.gridLayout.addWidget(self.labelColor, 14, 0, 1, 1)

        self.inputHat = QtWidgets.QComboBox(parent=self.widget)
        self.inputHat.setObjectName("inputHat")
        self.inputHat.addItem("")
        self.inputHat.setItemText(0, "")
        self.inputHat.addItem("")
        self.inputHat.addItem("")
        self.inputHat.addItem("")
        self.inputHat.addItem("")
        self.gridLayout.addWidget(self.inputHat, 10, 1, 1, 2)

        self.inputColor = QtWidgets.QSlider(parent=self.widget)
        self.inputColor.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.inputColor.setObjectName("inputColor")
        self.inputColor.setMaximum(360)
        self.inputColor.valueChanged.connect(lambda: self.colorInputNumber.setValue(self.inputColor.value()))
        self.gridLayout.addWidget(self.inputColor, 14, 1, 1, 1)

        self.labelBody = QtWidgets.QLabel(parent=self.widget)
        self.labelBody.setObjectName("labelBody")
        self.gridLayout.addWidget(self.labelBody, 11, 0, 1, 1)

        self.labelMana = QtWidgets.QLabel(parent=self.widget)
        self.labelMana.setObjectName("labelMana")
        self.gridLayout.addWidget(self.labelMana, 6, 0, 1, 1)

        self.labelDesc = QtWidgets.QLabel(parent=self.widget)
        self.labelDesc.setObjectName("labelDesc")
        self.gridLayout.addWidget(self.labelDesc, 3, 0, 1, 1)

        self.buttonSave = QtWidgets.QPushButton(parent=self.widget)
        self.buttonSave.setObjectName("buttonSave")
        self.gridLayout.addWidget(self.buttonSave, 17, 0, 1, 3)

        self.line3 = QtWidgets.QFrame(parent=self.widget)
        self.line3.setMinimumSize(QtCore.QSize(0, 10))
        self.line3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line3.setObjectName("line3")
        self.gridLayout.addWidget(self.line3, 9, 0, 1, 3)

        self.labelAccessory = QtWidgets.QLabel(parent=self.widget)
        self.labelAccessory.setObjectName("labelAccessory")
        self.gridLayout.addWidget(self.labelAccessory, 12, 0, 1, 1)

        self.labelBackground = QtWidgets.QLabel(parent=self.widget)
        self.labelBackground.setObjectName("labelBackground")
        self.gridLayout.addWidget(self.labelBackground, 13, 0, 1, 1)

        self.inputBackground = QtWidgets.QComboBox(parent=self.widget)
        self.inputBackground.setObjectName("inputBackground")
        self.inputBackground.addItem("")
        self.inputBackground.setItemText(0, "")
        self.inputBackground.addItem("")
        self.inputBackground.addItem("")
        self.inputBackground.addItem("")
        self.gridLayout.addWidget(self.inputBackground, 13, 1, 1, 2)

        self.inputName = QtWidgets.QLineEdit(parent=self.widget)
        self.inputName.setMaxLength(23)
        self.inputName.setObjectName("inputName")
        self.gridLayout.addWidget(self.inputName, 1, 0, 1, 3)

        self.inputAccessory = QtWidgets.QComboBox(parent=self.widget)
        self.inputAccessory.setObjectName("inputAccessory")
        self.inputAccessory.addItem("")
        self.inputAccessory.setItemText(0, "")
        self.inputAccessory.addItem("")
        self.inputAccessory.addItem("")
        self.inputAccessory.addItem("")
        self.inputAccessory.addItem("")
        self.gridLayout.addWidget(self.inputAccessory, 12, 1, 1, 2)

        self.labelHat = QtWidgets.QLabel(parent=self.widget)
        self.labelHat.setObjectName("labelHat")
        self.gridLayout.addWidget(self.labelHat, 10, 0, 1, 1)

        self.buttonGenerate = QtWidgets.QPushButton(parent=self.widget)
        self.buttonGenerate.setObjectName("buttonGenerate")
        self.gridLayout.addWidget(self.buttonGenerate, 16, 0, 1, 3)
        self.buttonGenerate.clicked.connect(self.generate)

        self.inputDesc = QtWidgets.QPlainTextEdit(parent=self.widget)
        self.inputDesc.setMaximumSize(QtCore.QSize(16777215, 115))
        self.inputDesc.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.inputDesc.setPlainText("")
        self.inputDesc.setObjectName("inputDesc")
        self.gridLayout.addWidget(self.inputDesc, 4, 0, 1, 3)

        self.buttonExport = QtWidgets.QPushButton(parent=self.widget)
        self.buttonExport.setObjectName("buttonExport")
        self.gridLayout.addWidget(self.buttonExport, 18, 0, 1, 3)

        self.inputBody = QtWidgets.QComboBox(parent=self.widget)
        self.inputBody.setObjectName("inputBody")
        self.inputBody.addItem("")
        self.inputBody.setItemText(0, "")
        self.inputBody.addItem("")
        self.inputBody.addItem("")
        self.inputBody.addItem("")
        self.inputBody.addItem("")
        self.gridLayout.addWidget(self.inputBody, 11, 1, 1, 2)

        self.labelStamina = QtWidgets.QLabel(parent=self.widget)
        self.labelStamina.setObjectName("labelStamina")
        self.gridLayout.addWidget(self.labelStamina, 7, 0, 1, 1)

        self.labelHealth = QtWidgets.QLabel(parent=self.widget)
        self.labelHealth.setObjectName("labelHealth")
        self.gridLayout.addWidget(self.labelHealth, 8, 0, 1, 1)

        self.inputMana = QtWidgets.QSpinBox(parent=self.widget)
        self.inputMana.setMaximum(100)
        self.inputMana.setObjectName("inputMana")
        self.gridLayout.addWidget(self.inputMana, 6, 1, 1, 1)

        self.inputStamina = QtWidgets.QSpinBox(parent=self.widget)
        self.inputStamina.setMaximum(100)
        self.inputStamina.setObjectName("inputStamina")
        self.gridLayout.addWidget(self.inputStamina, 7, 1, 1, 1)

        self.inputHealth = QtWidgets.QSpinBox(parent=self.widget)
        self.inputHealth.setMaximum(100)
        self.inputHealth.setObjectName("inputHealth")
        self.gridLayout.addWidget(self.inputHealth, 8, 1, 1, 1)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1140, 26))

        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Generator kart kapibar"))
        self.labelImagePreview.setText(_translate("MainWindow", ""))
        self.labelName.setText(_translate("MainWindow", "Nazwa"))
        self.labelColor.setText(_translate("MainWindow", "Kolor"))
        self.inputHat.setItemText(1, _translate("MainWindow", "Mag"))
        self.inputHat.setItemText(2, _translate("MainWindow", "Rycerz"))
        self.inputHat.setItemText(3, _translate("MainWindow", "Romantyk"))
        self.inputHat.setItemText(4, _translate("MainWindow", "Inne"))
        self.labelBody.setText(_translate("MainWindow", "Wdzianko"))
        self.labelMana.setText(_translate("MainWindow", "Mana"))
        self.labelDesc.setText(_translate("MainWindow", "Opis"))
        self.buttonSave.setText(_translate("MainWindow", "Zapisz plik edytowalny"))
        self.labelAccessory.setText(_translate("MainWindow", "Akcesorium"))
        self.inputName.setText(_translate("MainWindow", ""))
        self.inputAccessory.setItemText(1, _translate("MainWindow", "Mag"))
        self.inputAccessory.setItemText(2, _translate("MainWindow", "Rycerz"))
        self.inputAccessory.setItemText(3, _translate("MainWindow", "Romantyk"))
        self.inputAccessory.setItemText(4, _translate("MainWindow", "Inne"))
        self.labelHat.setText(_translate("MainWindow", "Czapka"))
        self.buttonGenerate.setText(_translate("MainWindow", "Generuj"))
        self.buttonExport.setText(_translate("MainWindow", "Eksportuj PNG"))
        self.inputBody.setItemText(1, _translate("MainWindow", "Mag"))
        self.inputBody.setItemText(2, _translate("MainWindow", "Rycerz"))
        self.inputBody.setItemText(3, _translate("MainWindow", "Romantyk"))
        self.inputBody.setItemText(4, _translate("MainWindow", "Inne"))
        self.labelStamina.setText(_translate("MainWindow", "Stamina"))
        self.labelHealth.setText(_translate("MainWindow", "Zdrowie"))
        self.labelBackground.setText(_translate("MainWindow", "Tło"))
        self.inputBackground.setItemText(1, _translate("MainWindow", "Niebo"))
        self.inputBackground.setItemText(2, _translate("MainWindow", "Ogień"))
        self.inputBackground.setItemText(3, _translate("MainWindow", "Inne"))


def window():
    app = QApplication(sys.argv)
    win = mainWindow()

    win.show()
    sys.exit(app.exec())
