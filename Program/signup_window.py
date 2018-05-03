'''
-*- coding: utf-8 -*-

Form implementation generated from reading ui file 'signup_window.ui'

Created by: PyQt5 UI code generator 5.10.1
@author: Tejas Verghese

WARNING! All changes made in this file will be lost!
'''

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_SignUpDialog(object):
    def setupUi(self, SignUpDialog):
        # SignUp Window Settings
        SignUpDialog.setObjectName("SignUpDialog")
        SignUpDialog.resize(400, 300)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("../major_project-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SignUpDialog.setWindowIcon(self.icon)
        
        # Button Box Settings
        self.buttonBox = QtWidgets.QDialogButtonBox(SignUpDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.clicked.connect(SignUpDialog.accept)
        self.buttonBox.accepted.connect(self.insertUser)
        self.buttonBox.rejected.connect(SignUpDialog.reject)
        
        # SignUp Label Settings
        self.label = QtWidgets.QLabel(SignUpDialog)
        self.label.setGeometry(QtCore.QRect(110, 0, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        # Enter New Username Here
        self.newUserEdit = QtWidgets.QLineEdit(SignUpDialog)
        self.newUserEdit.setGeometry(QtCore.QRect(50, 80, 300, 20))
        self.newUserEdit.setObjectName("newUserEdit")
        
        # Enter New Email Here
        self.newEmailEdit = QtWidgets.QLineEdit(SignUpDialog)
        self.newEmailEdit.setGeometry(QtCore.QRect(50, 130, 300, 20))
        self.newEmailEdit.setObjectName("newEmailEdit")
        
        # Enter New Password Here
        self.newPassEdit = QtWidgets.QLineEdit(SignUpDialog)
        self.newPassEdit.setGeometry(QtCore.QRect(50, 180, 300, 20))
        self.newPassEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newPassEdit.setObjectName("newPassEdit")
        
        # To retranslate the UI window to create the Buttons, textinputs, etc.
        self.retranslateUi(SignUpDialog)
        self.buttonBox.accepted.connect(SignUpDialog.accept)
        self.buttonBox.rejected.connect(SignUpDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SignUpDialog)

    def retranslateUi(self, SignUpDialog):
        _translate = QtCore.QCoreApplication.translate
        SignUpDialog.setWindowTitle(_translate("SignUpDialog", "Sign Up"))
        self.label.setText(_translate("SignUpDialog", "Sign Up"))
        self.newUserEdit.setPlaceholderText(_translate("SignUpDialog", "Username"))
        self.newEmailEdit.setPlaceholderText(_translate("SignUpDialog", "Email Id"))
        self.newPassEdit.setPlaceholderText(_translate("SignUpDialog", "Password"))
        
    def insertUser(self):
        username = self.newUserEdit.text()
        email = self.newEmailEdit.text()
        password = self.newPassEdit.text()
        connection = sqlite3.connect("login.db")
        connection.execute("INSERT INTO USERS VALUES(?, ?, ?)", (username, email, password))
        connection.commit()
        connection.close()
        print("1 New User has been Added!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignUpDialog = QtWidgets.QDialog()
    ui = Ui_SignUpDialog()
    ui.setupUi(SignUpDialog)
    SignUpDialog.show()
    sys.exit(app.exec_())

