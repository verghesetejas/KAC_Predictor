'''
-*- coding: utf-8 -*-

Form implementation generated from reading ui file 'delete_window.ui'

Created by: PyQt5 UI code generator 5.10.1
@author: Tejas Verghese

WARNING! All changes made in this file will be lost!
'''

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import sqlite3

class Ui_DeleteDialog(object):
    def setupUi(self, DeleteDialog):
        # Delete Dialog Window Settings
        self.checkPoint = 0
        DeleteDialog.setObjectName("DeleteDialog")
        DeleteDialog.resize(405, 79)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../major_project-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DeleteDialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(DeleteDialog)
        self.gridLayout.setObjectName("gridLayout")
        
        # Button Box Settings
        self.buttonBox = QtWidgets.QDialogButtonBox(DeleteDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 0, 1, 1, 1)
        self.buttonBox.clicked.connect(DeleteDialog.accept)
        self.buttonBox.accepted.connect(self.deleteAction)
        self.buttonBox.rejected.connect(DeleteDialog.reject)
        
        self.frame = QtWidgets.QFrame(DeleteDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_heading = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_heading.setFont(font)
        self.label_heading.setObjectName("label_heading")
        self.verticalLayout.addWidget(self.label_heading)
        
        # Row Number Field Settings
        self.rowNoEdit = QtWidgets.QLineEdit(self.frame)
        self.rowNoEdit.setObjectName("rowNoEdit")
        self.onlyInt = QtGui.QIntValidator()
        self.rowNoEdit.setValidator(self.onlyInt)
        self.verticalLayout.addWidget(self.rowNoEdit)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        
        # To retranslate the UI window to create the Buttons, textinputs, etc.
        self.retranslateUi(DeleteDialog)
        self.buttonBox.accepted.connect(DeleteDialog.accept)
        self.buttonBox.rejected.connect(DeleteDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DeleteDialog)

    def retranslateUi(self, DeleteDialog):
        _translate = QtCore.QCoreApplication.translate
        DeleteDialog.setWindowTitle(_translate("DeleteDialog", "Delete(Row) Dialog"))
        self.label_heading.setText(_translate("DeleteDialog", "\"The Entered Row of Records will be removed\""))
        self.rowNoEdit.setPlaceholderText(_translate("DeleteDialog", "Enter Row Number"))
    
    def deleteAction(self):
        row_num = int(self.rowNoEdit.text())
        row_num = row_num - 1
        connection = sqlite3.connect("combo_loader.db")
        df = pd.read_sql_query("SELECT * FROM INPUT", con=connection)
        df = df.drop(df.index[row_num])
        connection.execute("DELETE FROM INPUT")
        df.to_sql(name='INPUT', con=connection, if_exists='append', index=False)
        connection.commit()
        connection.close()
        self.checkPoint = 1
        
# Only for Developers...
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeleteDialog = QtWidgets.QDialog()
    ui = Ui_DeleteDialog()
    ui.setupUi(DeleteDialog)
    DeleteDialog.show()
    sys.exit(app.exec_())
'''
