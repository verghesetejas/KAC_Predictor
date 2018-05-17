'''
-*- coding: utf-8 -*-

Form implementation generated from reading ui file 'main_window.ui'

Created by: PyQt5 UI code generator 5.10.1

    KAC Predictor (Key-Agricultural Commodities Daily Market Price Prediction using Deep Neural Networks)
    Copyright (C) 2018  Tejas Verghese

    This file is part of KAC Predictor.

    KAC Predictor is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    KAC Predictor is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with KAC Predictor.  If not, see <http://www.gnu.org/licenses/>.

@author: Tejas Verghese

WARNING! All changes made in this file will be lost!
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from signup_window import Ui_SignUpDialog
from about_window import Ui_About
from main_window import Ui_MainWindow
from about import AboutDeveloper, AboutProject
import sqlite3

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SelectorWindow(object):
    def setupUi(self, MainWindow, username):
        # Selector Window Settings
        self.user = username
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 445)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("../major_project-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(self.icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 683, 1118))
        self.scrollAreaWidgetContents.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        MainWindow.move((resolution.width() / 2) - (MainWindow.frameSize().width() / 2),
                        (resolution.height() / 2) - (MainWindow.frameSize().height() / 2))
        
        # Raddish Button Settings
        self.buttonRaddish = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.buttonRaddish.setStyleSheet("#buttonRaddish {\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}")
        self.buttonRaddish.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/Raddish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonRaddish.setIcon(icon1)
        self.buttonRaddish.setIconSize(QtCore.QSize(200, 267))
        self.buttonRaddish.setObjectName("buttonRaddish")
        self.buttonRaddish.clicked.connect(partial(self.showMainWindow, MainWindow, "Raddish"))
        self.gridLayout.addWidget(self.buttonRaddish, 4, 2, 1, 1)
        
        # Persimmon Button Settings
        self.buttonPersimmon = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.buttonPersimmon.setStyleSheet("#buttonPersimmon {\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}")
        self.buttonPersimmon.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/Persimmon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPersimmon.setIcon(icon2)
        self.buttonPersimmon.setIconSize(QtCore.QSize(200, 267))
        self.buttonPersimmon.setObjectName("buttonPersimmon")
        self.buttonPersimmon.clicked.connect(partial(self.showMainWindow, MainWindow, "Persimon(Japani Fal)"))
        self.gridLayout.addWidget(self.buttonPersimmon, 4, 1, 1, 1)
        
        # Mint Button Settings
        self.buttonMint = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.buttonMint.setStyleSheet("#buttonMint {\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}")
        self.buttonMint.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/Mint.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonMint.setIcon(icon3)
        self.buttonMint.setIconSize(QtCore.QSize(200, 267))
        self.buttonMint.setObjectName("buttonMint")
        self.buttonMint.clicked.connect(partial(self.showMainWindow, MainWindow, "Mint(Pudina)"))
        self.gridLayout.addWidget(self.buttonMint, 3, 2, 1, 1)
        
        # Lentils Button Settings
        self.buttonLentils = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.buttonLentils.setStyleSheet("#buttonLentils {\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}")
        self.buttonLentils.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/Lentils.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonLentils.setIcon(icon4)
        self.buttonLentils.setIconSize(QtCore.QSize(200, 267))
        self.buttonLentils.setObjectName("buttonLentils")
        self.buttonLentils.clicked.connect(partial(self.showMainWindow, MainWindow, "Lentil(Masur)"))
        self.gridLayout.addWidget(self.buttonLentils, 3, 1, 1, 1)
        
        # CumminSeeds Button Settings
        self.buttonCumminSeeds = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.buttonCumminSeeds.setStyleSheet("#buttonCumminSeeds {\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}")
        self.buttonCumminSeeds.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Images/CumminSeeds.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonCumminSeeds.setIcon(icon5)
        self.buttonCumminSeeds.setIconSize(QtCore.QSize(200, 267))
        self.buttonCumminSeeds.setObjectName("buttonCumminSeeds")
        self.buttonCumminSeeds.clicked.connect(partial(self.showMainWindow, MainWindow, "Cummin Seed(Jeera)"))
        self.gridLayout.addWidget(self.buttonCumminSeeds, 2, 0, 1, 1)
        
        # Paddy Button Settings
        self.buttonPaddy = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.buttonPaddy.setStyleSheet("#buttonPaddy {\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}")
        self.buttonPaddy.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Images/Paddy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPaddy.setIcon(icon6)
        self.buttonPaddy.setIconSize(QtCore.QSize(200, 267))
        self.buttonPaddy.setObjectName("buttonPaddy")
        self.buttonPaddy.clicked.connect(partial(self.showMainWindow, MainWindow, "Paddy(Dhan)"))
        self.gridLayout.addWidget(self.buttonPaddy, 4, 0, 1, 1)
        
        # Amla Button Settings
        self.buttonAmla = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.buttonAmla.setStyleSheet("#buttonAmla {\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}")
        self.buttonAmla.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Images/Amla.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonAmla.setIcon(icon7)
        self.buttonAmla.setIconSize(QtCore.QSize(200, 267))
        self.buttonAmla.setObjectName("buttonAmla")
        self.buttonAmla.clicked.connect(partial(self.showMainWindow, MainWindow, "Amla"))
        self.gridLayout.addWidget(self.buttonAmla, 1, 0, 1, 1)
        
        # Lemon Button Settings
        self.buttonLemon = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.buttonLemon.setStyleSheet("#buttonLemon {\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}")
        self.buttonLemon.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Images/Lemon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonLemon.setIcon(icon8)
        self.buttonLemon.setIconSize(QtCore.QSize(200, 267))
        self.buttonLemon.setObjectName("buttonLemon")
        self.buttonLemon.clicked.connect(partial(self.showMainWindow, MainWindow, "Galgal(Lemon)"))
        self.gridLayout.addWidget(self.buttonLemon, 3, 0, 1, 1)
        
        # Ladiesfinger Button Settings
        self.buttonLadiesFinger = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.buttonLadiesFinger.setStyleSheet("#buttonLadiesFinger {\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}")
        self.buttonLadiesFinger.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Images/LadiesFinger.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonLadiesFinger.setIcon(icon9)
        self.buttonLadiesFinger.setIconSize(QtCore.QSize(200, 267))
        self.buttonLadiesFinger.setObjectName("buttonLadiesFinger")
        self.buttonLadiesFinger.clicked.connect(partial(self.showMainWindow, MainWindow, "Bhindi(Ladies Finger)"))
        self.gridLayout.addWidget(self.buttonLadiesFinger, 2, 2, 1, 1)
        
        # BlackGrams Button Settings
        self.buttonBlackGrams = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.buttonBlackGrams.setStyleSheet("#buttonBlackGrams {\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}")
        self.buttonBlackGrams.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("Images/BlackGrams.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonBlackGrams.setIcon(icon10)
        self.buttonBlackGrams.setIconSize(QtCore.QSize(200, 267))
        self.buttonBlackGrams.setObjectName("buttonBlackGrams")
        self.buttonBlackGrams.clicked.connect(partial(self.showMainWindow, MainWindow, "Black Grams (Urd Beans)"))
        self.gridLayout.addWidget(self.buttonBlackGrams, 1, 1, 1, 1)
        
        # Chickpeas Button Settings
        self.buttonChickpeas = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.buttonChickpeas.setStyleSheet("#buttonChickpeas {\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}")
        self.buttonChickpeas.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("Images/Chickpeas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonChickpeas.setIcon(icon11)
        self.buttonChickpeas.setIconSize(QtCore.QSize(200, 267))
        self.buttonChickpeas.setObjectName("buttonChickpeas")
        self.buttonChickpeas.clicked.connect(partial(self.showMainWindow, MainWindow, "Kabuli Chana(Chickpeas-White)"))
        self.gridLayout.addWidget(self.buttonChickpeas, 1, 2, 1, 1)
        
        # DryPeas Button Settings
        self.buttonDryPeas = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.buttonDryPeas.setStyleSheet("#buttonDryPeas {\n"
"background-color: transparent;\n"
"background: none;\n"
"border: none;\n"
"background-repeat: none;\n"
"}")
        self.buttonDryPeas.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("Images/DryPeas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonDryPeas.setIcon(icon12)
        self.buttonDryPeas.setIconSize(QtCore.QSize(200, 267))
        self.buttonDryPeas.setObjectName("buttonDryPeas")
        self.buttonDryPeas.clicked.connect(partial(self.showMainWindow, MainWindow, "Peas(Dry)"))
        self.gridLayout.addWidget(self.buttonDryPeas, 2, 1, 1, 1)
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.userLabel = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        self.userLabel.setFont(font)
        self.userLabel.setAlignment(QtCore.Qt.AlignLeft)
        self.userLabel.setText("Active User: %s" % self.user)
        self.statusbar.addWidget(self.userLabel)
        
        # Menu -> Quit Button Settings
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.triggered.connect(partial(self.closeApplication, MainWindow))
        
        # Menu -> About Developer Button Settings
        self.actionAbout_Developer = QtWidgets.QAction(MainWindow)
        self.actionAbout_Developer.setObjectName("actionAbout_Developer")
        self.actionAbout_Developer.triggered.connect(AboutDeveloper)
        
        # Menu -> About Copyright Button Settings
        self.actionAbout_Gpl = QtWidgets.QAction(MainWindow)
        self.actionAbout_Gpl.setObjectName("actionAbout_Gpl")
        self.actionAbout_Gpl.triggered.connect(self.showGpl)
        
        # Menu -> Sign Up Button Settings
        self.actionSign_Up = QtWidgets.QAction(MainWindow)
        self.actionSign_Up.setObjectName("actionSign_Up")
        self.actionSign_Up.triggered.connect(self.showSignUp)
        
        # Menu -> About Project Button Settings
        self.actionAbout_Project = QtWidgets.QAction(MainWindow)
        self.actionAbout_Project.setObjectName("actionAbout_Project")
        self.actionAbout_Project.triggered.connect(AboutProject)
        
        self.menuFile.addAction(self.actionSign_Up)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionAbout_Project)
        self.menuAbout.addAction(self.actionAbout_Developer)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout_Gpl)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        
        # To retranslate the UI window to create the Buttons, textinputs, etc.
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Selector Window"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAbout_Developer.setText(_translate("MainWindow", "About Developer"))
        self.actionSign_Up.setText(_translate("MainWindow", "Sign Up"))
        self.actionAbout_Project.setText(_translate("MainWindow", "About Project"))
        self.actionAbout_Gpl.setText(_translate("MainWindow", "About"))
    
    def showGpl(self):
        about = QtWidgets.QDialog()
        ui = Ui_About()
        ui.setupUi(about)
        about.exec_()
    
    def showSignUp(self):
        dialog = QtWidgets.QDialog()
        ui = Ui_SignUpDialog()
        ui.setupUi(dialog)
        dialog.exec_()
        
    def showMainWindow(self, MainWindow, commodity):
        mainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(mainWindow, commodity, MainWindow, self.user)
        mainWindow.show()
        MainWindow.hide()
        
    def closeApplication(self, MainWindow):
        '''
            This Function will Exit/Quit the Application.
            It will also ask for confirmation before exit. 
        '''
        connection = sqlite3.connect("combo_loader.db")
        connection.execute("DELETE FROM INPUT")
        connection.execute("DELETE FROM OUTPUT")
        connection.commit()
        connection.close()
        ret = QtWidgets.QMessageBox.Yes
        choice = QtWidgets.QMessageBox()
        choice.setWindowTitle("Quit Application!")
        choice.setWindowIcon(self.icon)
        choice.setText("Are you sure you want to Quit?")
        choice.setIcon(QtWidgets.QMessageBox.Warning)
        choice.setStandardButtons(QtWidgets.QMessageBox.Yes  | QtWidgets.QMessageBox.No)
        choice.setDefaultButton(QtWidgets.QMessageBox.No)
        ret = choice.exec_()
        if ret == QtWidgets.QMessageBox.Yes:
            MainWindow.close()
        else:
            pass

# Only for Developers...
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SelectorWindow = QtWidgets.QMainWindow()
    ui = Ui_SelectorWindow()
    ui.setupUi(SelectorWindow, "Test")
    SelectorWindow.show()
    sys.exit(app.exec_())
'''
