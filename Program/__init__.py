# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 22:12:00 2018

@author: Tejas Verghese
"""
from PyQt5 import QtWidgets
from login_window import Ui_LoginWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())