'''
-*- coding: utf-8 -*-

Form implementation generated from reading ui file 'update_window.ui'

Created by: PyQt5 UI code generator 5.10.1
@author: Tejas Verghese

WARNING! All changes made in this file will be lost!
'''

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import sqlite3

class Ui_UpdateDialog(object):
    def setupUi(self, UpdateDialog, commodity):
        self.commodityName = commodity
        self.checkPoint = 0
        # Update Dialog Window Settings
        UpdateDialog.setObjectName("UpdateDialog")
        UpdateDialog.resize(465, 276)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../major_project-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UpdateDialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(UpdateDialog)
        self.gridLayout.setObjectName("gridLayout")
        
        # Button Box Settings
        self.buttonBox = QtWidgets.QDialogButtonBox(UpdateDialog)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)
        self.buttonBox.clicked.connect(UpdateDialog.accept)
        self.buttonBox.accepted.connect(self.updateAction)
        self.buttonBox.rejected.connect(UpdateDialog.reject)
        
        self.frame = QtWidgets.QFrame(UpdateDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Row Number Edit Settings
        self.rowNoEdit = QtWidgets.QLineEdit(self.frame)
        self.rowNoEdit.setObjectName("rowNoEdit")
        self.onlyInt = QtGui.QIntValidator()
        self.rowNoEdit.setValidator(self.onlyInt)
        self.verticalLayout.addWidget(self.rowNoEdit)
        
        self.label_state = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_state.setFont(font)
        self.label_state.setObjectName("label_state")
        self.verticalLayout.addWidget(self.label_state)
        
        # State Combo Box Settings
        self.stateCombo = QtWidgets.QComboBox(self.frame)
        self.stateCombo.setObjectName("stateCombo")
        self.verticalLayout.addWidget(self.stateCombo)
        self.populateState(self.commodityName)
        
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        
        # District Combo Box Settings
        self.districtCombo = QtWidgets.QComboBox(self.frame)
        self.districtCombo.setObjectName("districtCombo")
        self.verticalLayout.addWidget(self.districtCombo)
        self.districtCombo.setEnabled(False)
        
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        
        # Market Combo Box Settings
        self.marketCombo = QtWidgets.QComboBox(self.frame)
        self.marketCombo.setObjectName("marketCombo")
        self.verticalLayout.addWidget(self.marketCombo)
        self.marketCombo.setEnabled(False)
        
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        
        # Date Edit Settings
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDisplayFormat('dd/MM/yyyy')
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEdit.setCalendarPopup(True)
        self.verticalLayout.addWidget(self.dateEdit)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        
        # To retranslate the UI window to create the Buttons, textinputs, etc.
        self.retranslateUi(UpdateDialog)
        self.buttonBox.accepted.connect(UpdateDialog.accept)
        self.buttonBox.rejected.connect(UpdateDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(UpdateDialog)

    def retranslateUi(self, UpdateDialog):
        _translate = QtCore.QCoreApplication.translate
        UpdateDialog.setWindowTitle(_translate("UpdateDialog", "Update(Row) Dialog"))
        self.rowNoEdit.setPlaceholderText(_translate("UpdateDialog", "Enter Row Number"))
        self.label_state.setText(_translate("UpdateDialog", "State :"))
        self.label_2.setText(_translate("UpdateDialog", "District :"))
        self.label_3.setText(_translate("UpdateDialog", "Market :"))
        self.label_4.setText(_translate("UpdateDialog", "Date :"))
        
################################ COMBO-BOX SETTINGS ###########################
    def populateState(self, commodity):
        connection = sqlite3.connect("combo_loader.db")
        results = connection.execute("SELECT DISTINCT STATE FROM BOX WHERE COMMODITY = ?", [commodity])
        for data in results:
            self.stateCombo.addItem(data[0])
        connection.close()
        self.stateCombo.activated[str].connect(self.choiceState)
        
    def populateDistrict(self, commodity, state):
        self.districtCombo.clear()
        connection = sqlite3.connect("combo_loader.db")
        results = connection.execute("SELECT DISTINCT DISTRICT FROM BOX WHERE COMMODITY = ? AND STATE = ?", (commodity, state))
        for data in results:
            self.districtCombo.addItem(data[0])
        connection.close()
        self.districtCombo.activated[str].connect(self.choiceDistrict)
        
    def populateMarket(self, commodity, state, district):
        self.marketCombo.clear()
        connection = sqlite3.connect("combo_loader.db")
        results = connection.execute("SELECT DISTINCT MARKET FROM BOX WHERE COMMODITY = ? AND STATE = ? AND DISTRICT = ?", (commodity, state, district))
        for data in results:
            self.marketCombo.addItem(data[0])
        connection.close()
        self.marketCombo.activated[str].connect(self.choiceMarket)
        
    def choiceState(self, statename):
        self.stateChoice = statename
        self.districtCombo.setEnabled(True)
        self.populateDistrict(self.commodityName, self.stateChoice)
        
    def choiceDistrict(self, districtname):
        self.districtChoice = districtname
        self.marketCombo.setEnabled(True)
        self.populateMarket(self.commodityName, self.stateChoice, self.districtChoice)
    
    def choiceMarket(self, marketname):
        self.marketChoice = marketname
###############################################################################
    
    def updateAction(self):
        self.date = self.dateEdit.date()
        self.date = self.date.toString('dd/MM/yyyy')
        row_num = int(self.rowNoEdit.text())
        row_num = row_num - 1
        connection = sqlite3.connect("combo_loader.db")
        df = pd.read_sql_query("SELECT * FROM INPUT", con=connection)
        df.iloc[row_num] = [self.stateChoice, self.districtChoice, self.marketChoice, self.commodityName, self.date]
        df = df.sort_index()
        connection.execute("DELETE FROM INPUT")
        df.to_sql(name='INPUT', con=connection, if_exists='append', index=False)
        connection.commit()
        connection.close()
        self.checkPoint = 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UpdateDialog = QtWidgets.QDialog()
    ui = Ui_UpdateDialog()
    ui.setupUi(UpdateDialog, "Amla")
    UpdateDialog.show()
    sys.exit(app.exec_())

