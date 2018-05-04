'''
-*- coding: utf-8 -*-

Form implementation generated from reading ui file 'ann_window.ui'

Created by: PyQt5 UI code generator 5.10.1
@author: Tejas Verghese

WARNING! All changes made in this file will be lost!
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import pandas as pd
from delete_window import Ui_DeleteDialog
from update_window import Ui_UpdateDialog
from signup_window import Ui_SignUpDialog
import sqlite3
from about import AboutDeveloper, AboutProject
# Import the KAC_Predictor Class
from kac_predictor import KAC_Predictor

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

class Ui_MainWindow(object):  
    def setupUi(self, MainWindow, commodity, SelectorWindow):
        # Main Window Settings
        self.commodityName = commodity
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(687, 549)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("../major_project-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(self.icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        MainWindow.showMaximized()
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        MainWindow.move((resolution.width() / 2) - (MainWindow.frameSize().width() / 2),
                        (resolution.height() / 2) - (MainWindow.frameSize().height() / 2))
        
        # TableWidget Settings
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(['State',
                                                    'District',
                                                    'Market',
                                                    'Commodity',
                                                    'Arrival Date',
                                                    'Min Price',
                                                    'Max Price',
                                                    'Modal Price'])
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 3, 1)
        
        # TextBrowser Settings
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setObjectName("textBrowser")
        self.outputTextB('Commodity: %s' % commodity)
        
        self.gridLayout.addWidget(self.textBrowser, 4, 0, 4, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/mp_logo-100sq.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_1 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title_1.setFont(font)
        self.title_1.setObjectName("title_1")
        self.verticalLayout.addWidget(self.title_1)
        self.title_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title_2.setFont(font)
        self.title_2.setObjectName("title_2")
        self.verticalLayout.addWidget(self.title_2)
        self.title_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title_3.setFont(font)
        self.title_3.setObjectName("title_3")
        self.verticalLayout.addWidget(self.title_3)
        self.horizontalLayout.addWidget(self.frame)
        self.gridLayout.addWidget(self.frame_2, 1, 2, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        # Update Button Settings
        self.updateButton = QtWidgets.QPushButton(self.frame_4)
        self.updateButton.setObjectName("updateButton")
        self.updateButton.clicked.connect(self.showUpdateDialog)
        self.gridLayout_2.addWidget(self.updateButton, 0, 2, 1, 1)
        
        # Add Button Settings
        self.addButton = QtWidgets.QPushButton(self.frame_4)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/ADD.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon1)
        self.addButton.setObjectName("addButton")
        self.gridLayout_2.addWidget(self.addButton, 0, 1, 1, 1)
        self.addButton.clicked.connect(self.addAction)
        
        # Delete Button Settings
        self.deleteButton = QtWidgets.QPushButton(self.frame_4)
        self.deleteButton.setObjectName("deleteButton")
        self.deleteButton.clicked.connect(self.showDeleteDialog)
        self.gridLayout_2.addWidget(self.deleteButton, 0, 0, 1, 1)
        
        self.gridLayout.addWidget(self.frame_4, 6, 2, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_state = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_state.setFont(font)
        self.label_state.setAlignment(QtCore.Qt.AlignCenter)
        self.label_state.setObjectName("label_state")
        self.verticalLayout_2.addWidget(self.label_state)
        
        # State ComboBox Settings
        self.comboState = QtWidgets.QComboBox(self.frame_3)
        self.comboState.setCurrentText("")
        self.comboState.setObjectName("comboState")
        self.verticalLayout_2.addWidget(self.comboState)
        self.populateState(commodity)
        
        self.label_district = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_district.setFont(font)
        self.label_district.setAlignment(QtCore.Qt.AlignCenter)
        self.label_district.setObjectName("label_district")
        self.verticalLayout_2.addWidget(self.label_district)
        
        # District ComboBox Settings
        self.comboDistrict = QtWidgets.QComboBox(self.frame_3)
        self.comboDistrict.setCurrentText("")
        self.comboDistrict.setObjectName("comboDistrict")
        self.verticalLayout_2.addWidget(self.comboDistrict)
        self.comboDistrict.setEnabled(False)
        
        self.label_market = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_market.setFont(font)
        self.label_market.setAlignment(QtCore.Qt.AlignCenter)
        self.label_market.setObjectName("label_market")
        self.verticalLayout_2.addWidget(self.label_market)
        
        # Market ComboBox Settings
        self.comboMarket = QtWidgets.QComboBox(self.frame_3)
        self.comboMarket.setCurrentText("")
        self.comboMarket.setObjectName("comboMarket")
        self.verticalLayout_2.addWidget(self.comboMarket)
        self.comboMarket.setEnabled(False)
        
        self.label_date = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_date.setFont(font)
        self.label_date.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date.setObjectName("label_date")
        self.verticalLayout_2.addWidget(self.label_date)
        
        # DateEdit Settings
        self.dateEdit = QtWidgets.QDateEdit(self.frame_3)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDisplayFormat('dd/MM/yyyy')
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.dateEdit.setCalendarPopup(True)
        self.verticalLayout_2.addWidget(self.dateEdit)
        
        self.gridLayout.addWidget(self.frame_3, 3, 2, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        # Predict Button Settings
        self.predictButton = QtWidgets.QPushButton(self.frame_5)
        self.predictButton.setObjectName("predictButton")
        self.verticalLayout_3.addWidget(self.predictButton)
        self.predictButton.clicked.connect(self.makePrediction)
        
        self.gridLayout.addWidget(self.frame_5, 7, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 687, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuAbout.setTearOffEnabled(False)
        self.menuAbout.setObjectName("menuAbout")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuEdit_Data = QtWidgets.QMenu(self.menuEdit)
        self.menuEdit_Data.setObjectName("menuEdit_Data")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # Menu -> Edit -> Edit_Data -> Update(Row) Settings
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionUpdate.triggered.connect(self.showUpdateDialog)
        
        # Menu -> About -> About_Project Settings
        self.actionAbout_Project = QtWidgets.QAction(MainWindow)
        self.actionAbout_Project.setObjectName("actionAbout_Project")
        self.actionAbout_Project.triggered.connect(AboutProject)
        
        # Menu -> About -> About_Developer Settings
        self.actionAbout_Developer = QtWidgets.QAction(MainWindow)
        self.actionAbout_Developer.setObjectName("actionAbout_Developer")
        self.actionAbout_Developer.triggered.connect(AboutDeveloper)
        
        # Menu -> File -> Save Settings
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.showSaveDialog)
        
        # Menu -> File -> Back Settings
        self.actionBack = QtWidgets.QAction(MainWindow)
        self.actionBack.setObjectName("actionBack")
        self.actionBack.triggered.connect(partial(self.showSelectorWindow, MainWindow, SelectorWindow))
        
        # Menu -> File -> Sign_Up Settings
        self.actionSign_Up = QtWidgets.QAction(MainWindow)
        self.actionSign_Up.setObjectName("actionSign_Up")
        self.actionSign_Up.triggered.connect(self.showSignUp)
        
        # Menu -> File -> Quit Settings
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.triggered.connect(partial(self.closeApplication, MainWindow))
        
        # Menu -> File -> Open Settings
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.showFileDialog)
        
        # Menu -> Edit -> Clear Settings
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionClear.triggered.connect(self.clearAction)
        
        # Menu -> Edit -> Edit_Data -> Delete(Row) Settings
        self.actionDelete_Row = QtWidgets.QAction(MainWindow)
        self.actionDelete_Row.setObjectName("actionDelete_Row")
        self.actionDelete_Row.triggered.connect(self.showDeleteDialog)
        
        # Menu -> Edit -> Edit_Data -> Add(Row) Settings
        self.actionAdd_Row = QtWidgets.QAction(MainWindow)
        self.actionAdd_Row.setObjectName("actionAdd_Row")
        self.actionAdd_Row.triggered.connect(self.addAction)
        
        # Menu -> Edit -> Predict Settings
        self.actionPredict = QtWidgets.QAction(MainWindow)
        self.actionPredict.setObjectName("actionPredict")
        self.actionPredict.triggered.connect(self.makePrediction)
        
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionBack)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSign_Up)
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionAbout_Project)
        self.menuAbout.addAction(self.actionAbout_Developer)
        self.menuEdit_Data.addAction(self.actionAdd_Row)
        self.menuEdit_Data.addAction(self.actionUpdate)
        self.menuEdit_Data.addAction(self.actionDelete_Row)
        self.menuEdit.addAction(self.menuEdit_Data.menuAction())
        self.menuEdit.addAction(self.actionClear)
        self.menuEdit.addAction(self.actionPredict)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        
        # To retranslate the UI window to create the Buttons, textinputs, etc.
        self.retranslateUi(MainWindow)
        self.actionClear.triggered.connect(self.textBrowser.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Window"))
        self.title_1.setText(_translate("MainWindow", "\"Key-Agricultural Commodities"))
        self.title_2.setText(_translate("MainWindow", "Daily Market Price Prediction"))
        self.title_3.setText(_translate("MainWindow", "using Deep Neural Networks\""))
        self.updateButton.setText(_translate("MainWindow", "Update"))
        self.addButton.setText(_translate("MainWindow", "ADD"))
        self.deleteButton.setText(_translate("MainWindow", "Delete (Row)"))
        self.label_state.setText(_translate("MainWindow", "State :"))
        self.label_district.setText(_translate("MainWindow", "District :"))
        self.label_market.setText(_translate("MainWindow", "Market :"))
        self.label_date.setText(_translate("MainWindow", "Arrival Date :"))
        self.predictButton.setText(_translate("MainWindow", "Predict"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuEdit_Data.setTitle(_translate("MainWindow", "Edit Data"))
        self.actionUpdate.setText(_translate("MainWindow", "Update (Row)"))
        self.actionAbout_Project.setText(_translate("MainWindow", "About Project"))
        self.actionAbout_Developer.setText(_translate("MainWindow", "About Developer"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionBack.setText(_translate("MainWindow", "Back"))
        self.actionSign_Up.setText(_translate("MainWindow", "Sign Up"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionDelete_Row.setText(_translate("MainWindow", "Delete (Row)"))
        self.actionAdd_Row.setText(_translate("MainWindow", "Add (Row)"))
        self.actionPredict.setText(_translate("MainWindow", "Predict"))
    
    def outputTextB(self, text):
        self.textBrowser.append("\n >>>  %s" % text)
    
    def showFileDialog(self):
        fileDialog = QtWidgets.QFileDialog()
        self.file = fileDialog.getOpenFileName(caption="Open File", filter="csv(*.csv)")
        self.file = pd.read_csv(self.file[0])
        df1 = pd.DataFrame(self.file.iloc[:, :4].values)
        df2 = pd.DataFrame(self.file.iloc[:, 5].values)
        self.file = pd.concat([df1, df2], axis = 1)
        self.file.columns = ["STATE", "DISTRICT", "MARKET", "COMMODITY", "DATE"]
        connection = sqlite3.connect("combo_loader.db")
        connection.execute("DELETE FROM INPUT")
        self.file.to_sql(name='INPUT', con=connection, if_exists='append', index=False)
        connection.commit()
        connection.close()
        self.loadTableData()
        self.outputTextB("1 File Successfully Loaded!")
        
    def loadTableData(self):
        connection = sqlite3.connect("combo_loader.db")
        load_data = connection.execute("SELECT * FROM INPUT")
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(load_data):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()
        
################################ COMBO-BOX SETTINGS ###########################
    def populateState(self, commodity):
        connection = sqlite3.connect("combo_loader.db")
        results = connection.execute("SELECT DISTINCT STATE FROM BOX WHERE COMMODITY = ?", [commodity])
        for data in results:
            self.comboState.addItem(data[0])
        connection.close()
        self.comboState.activated[str].connect(self.choiceState)
        
    def populateDistrict(self, commodity, state):
        self.comboDistrict.clear()
        connection = sqlite3.connect("combo_loader.db")
        results = connection.execute("SELECT DISTINCT DISTRICT FROM BOX WHERE COMMODITY = ? AND STATE = ?", (commodity, state))
        for data in results:
            self.comboDistrict.addItem(data[0])
        connection.close()
        self.comboDistrict.activated[str].connect(self.choiceDistrict)
        
    def populateMarket(self, commodity, state, district):
        self.comboMarket.clear()
        connection = sqlite3.connect("combo_loader.db")
        results = connection.execute("SELECT DISTINCT MARKET FROM BOX WHERE COMMODITY = ? AND STATE = ? AND DISTRICT = ?", (commodity, state, district))
        for data in results:
            self.comboMarket.addItem(data[0])
        connection.close()
        self.comboMarket.activated[str].connect(self.choiceMarket)
        
    def choiceState(self, statename):
        self.stateChoice = statename
        self.outputTextB('State: %s' % self.stateChoice)
        self.comboDistrict.setEnabled(True)
        self.populateDistrict(self.commodityName, self.stateChoice)
        
    def choiceDistrict(self, districtname):
        self.districtChoice = districtname
        self.outputTextB('District: %s' % self.districtChoice)
        self.comboMarket.setEnabled(True)
        self.populateMarket(self.commodityName, self.stateChoice, self.districtChoice)
    
    def choiceMarket(self, marketname):
        self.marketChoice = marketname
        self.outputTextB('Market: %s' % self.marketChoice)
###############################################################################
    
    def addAction(self):
        self.date = self.dateEdit.date()
        self.date = self.date.toString('dd/MM/yyyy')
        connection = sqlite3.connect("combo_loader.db")
        connection.execute("INSERT INTO INPUT(STATE, DISTRICT, MARKET, COMMODITY, DATE) VALUES(?, ?, ?, ?, ?)", (self.stateChoice, self.districtChoice, self.marketChoice, self.commodityName, self.date))
        connection.commit()
        connection.close()
        self.loadTableData()
        self.outputTextB("1 Row Added!")
    
    def showUpdateDialog(self):
        dialog = QtWidgets.QDialog()
        ui = Ui_UpdateDialog()
        ui.setupUi(dialog, 'Amla')
        dialog.exec_()
        if(ui.checkPoint == 1):
            self.outputTextB("1 Row Updated!")
            self.loadTableData()
        
    def showDeleteDialog(self):
        dialog = QtWidgets.QDialog()
        ui = Ui_DeleteDialog()
        ui.setupUi(dialog)
        dialog.exec_()
        if(ui.checkPoint == 1):
            self.outputTextB("1 Row Deleted!")
            self.loadTableData()
        
    def showSignUp(self):
        dialog = QtWidgets.QDialog()
        ui = Ui_SignUpDialog()
        ui.setupUi(dialog)
        dialog.exec_()
        
    def clearAction(self):
        self.textBrowser.setText("")
        connection = sqlite3.connect("combo_loader.db")
        connection.execute("DELETE FROM INPUT")
        connection.commit()
        connection.close()
        self.loadTableData()
        
    def makePrediction(self):
        self.tableWidget.setRowCount(0)
        kac = KAC_Predictor()
        kac.predictor()
        connection = sqlite3.connect("combo_loader.db")
        dataset = connection.execute("SELECT * FROM OUTPUT")
        for row_number, row_data in enumerate(dataset):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()
        if(kac.checkPoint == 1):
            self.outputTextB("Prediction Completed!")
        
    def showSaveDialog(self):
        connection = sqlite3.connect("combo_loader.db")
        filename = QtWidgets.QFileDialog.getSaveFileName(caption="Save File", directory="../Untitled.csv", filter="csv(*.csv)", )
        df = pd.read_sql_query("SELECT * FROM OUTPUT", con=connection)
        df.to_csv(path_or_buf=filename[0], index=False)
        connection.close()
        msg="Output saved at:\n           \""+filename[0]+"\""
        self.outputTextB(msg)
        
    def showSelectorWindow(self, MainWindow, SelectorWindow):
        SelectorWindow.show()
        MainWindow.hide()
    
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

# Only for Developers...
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, "Amla", MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''
