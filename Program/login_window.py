'''
-*- coding: utf-8 -*-

Form implementation generated from reading ui file 'login_window.ui'

Created by: PyQt5 UI code generator 5.10.1
@author: Tejas Verghese

WARNING! All changes made in this file will be lost!
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from selector_window import Ui_SelectorWindow
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

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        # Main Window Settings
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        MainWindow.setMaximumSize(QtCore.QSize(500, 300))
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("../major_project-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(self.icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bgView = QtWidgets.QGraphicsView(self.centralwidget)
        self.bgView.setGeometry(QtCore.QRect(0, 0, 500, 300))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.bgView.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.bgView.setBackgroundBrush(brush)
        self.bgView.setObjectName("bgView")
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        MainWindow.move((resolution.width() / 2) - (MainWindow.frameSize().width() / 2),
                        (resolution.height() / 2) - (MainWindow.frameSize().height() / 2))
        
        # Username Edit Settings
        self.userEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.userEdit.setGeometry(QtCore.QRect(100, 125, 300, 20))
        self.userEdit.setStatusTip("")
        self.userEdit.setWhatsThis("")
        self.userEdit.setInputMask("")
        self.userEdit.setText("")
        self.userEdit.setObjectName("userEdit")
        
        # Password Edit Settings
        self.passEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passEdit.setGeometry(QtCore.QRect(100, 175, 300, 20))
        self.passEdit.setStatusTip("")
        self.passEdit.setWhatsThis("")
        self.passEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.passEdit.setInputMask("")
        self.passEdit.setText("")
        self.passEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passEdit.setObjectName("passEdit")
        
        # Login Button Settings
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(0, 250, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setCheckable(False)
        self.loginButton.setObjectName("loginButton")
        self.loginButton.setDefault(True)
        self.loginButton.clicked.connect(partial(self.loginApplication, MainWindow))
        
        # Cancel Button Settings
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(250, 250, 250, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.cancelButton.clicked.connect(partial(self.closeApplication, MainWindow))
        
        # Label for the Project Icon
        self.label_icon = QtWidgets.QLabel(self.centralwidget)
        self.label_icon.setGeometry(QtCore.QRect(5, 5, 100, 100))
        self.label_icon.setText("")
        self.label_icon.setPixmap(QtGui.QPixmap(_fromUtf8("Images/mp_logo-100sq.png")))
        self.label_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.label_icon.setObjectName("label_icon")
        
        # Label for Text part-1
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 10, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(100, 0, 20, 110))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        # Label for Text part-2
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 40, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        
        # Label for Text part-3
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 70, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        
        # To retranslate the UI window to create the Buttons, textinputs, etc.
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login Window"))
        self.userEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.passEdit.setPlaceholderText(_translate("MainWindow", "Password"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.label_2.setText(_translate("MainWindow", "\" Key Agricultural Commodities"))
        self.label_3.setText(_translate("MainWindow", "Daily Market Price Prediction"))
        self.label_4.setText(_translate("MainWindow", "using Deep Neural Networks \""))
        
    def showSelectorWindow(self):
        selectorWindow = QtWidgets.QMainWindow()
        ui = Ui_SelectorWindow()
        ui.setupUi(selectorWindow)
        selectorWindow.show()
        
    def showLoginWarning(self):
        ret = QtWidgets.QMessageBox.Ok
        choice = QtWidgets.QMessageBox()
        choice.setWindowTitle("Warning!!")
        choice.setWindowIcon(self.icon)
        choice.setText("Invalid Username and Password!")
        choice.setIcon(QtWidgets.QMessageBox.Warning)
        choice.setStandardButtons(QtWidgets.QMessageBox.Ok)
        choice.setDefaultButton(QtWidgets.QMessageBox.Ok)
        ret = choice.exec_()
        if ret == QtWidgets.QMessageBox.Ok:
            pass
        
    def loginApplication(self, MainWindow):
        '''
            This Function will Login the user to the Main Window
            If and only if the Username and Password are Registered.
        '''
        username = self.userEdit.text()
        password = self.passEdit.text()
        connection = sqlite3.connect("login.db")
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?", (username, password))
        if(len(result.fetchall()) > 0):
            print("User Found!")
            self.showSelectorWindow()
            MainWindow.hide()
        else:
            print("User Not Found!")
            self.showLoginWarning()
        connection.close()
    
    def closeApplication(self, MainWindow):
        '''
            This Function will Exit/Quit the Application.
            It will also ask for confirmation before exit. 
        '''
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())

