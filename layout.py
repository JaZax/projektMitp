# Form implementation generated from reading ui file 'testui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        MainWindow.resize(789, 438)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Generator kart kapibar"))
        self.buttonSave.setText(_translate("MainWindow", "Save edit file"))
        self.labelHealth.setText(_translate("MainWindow", "Zdrowie"))
        self.labelDesc.setText(_translate("MainWindow", "Opis"))
        self.labelStamina.setText(_translate("MainWindow", "Stamina"))
        self.buttonHat.setText(_translate("MainWindow", "czapka"))
        self.labelName.setText(_translate("MainWindow", "Nazwa"))
        self.buttonGenerate.setText(_translate("MainWindow", "Generuj"))
        self.buttonAccessory.setText(_translate("MainWindow", "Akcesorium"))
        self.buttonExport.setText(_translate("MainWindow", "Export PNG"))
        self.labelImagePreview.setText(_translate("MainWindow", "TextLabel"))
        self.labelMana.setText(_translate("MainWindow", "Mana"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())