# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Kittiphat\Documents\CAI_C\GUI\2.0.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import datetime
from multiprocessing.connection import wait
from unittest import skip
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QFileDialog, QVBoxLayout
import sys, os, time, re, utils, time

import InvoiceExtract as Ie

output = ''

class Ui_Main(object):
    
    
    def setupUi(self, Main):
        
        Main.setObjectName("Main")
        Main.setWindowModality(QtCore.Qt.ApplicationModal)
        Main.resize(640, 480)
        Main.setMinimumSize(QtCore.QSize(640, 480))
        Main.setMaximumSize(QtCore.QSize(640, 480))
        
        self.output = ''
        
        self.exportButton = QtWidgets.QPushButton(Main)
        self.exportButton.setEnabled(False)
        self.exportButton.setGeometry(QtCore.QRect(530, 430, 93, 28))
        self.exportButton.setObjectName("exportButton")
        self.exportButton.clicked.connect(self.whenClick)
        
        self.io = QtWidgets.QGroupBox(Main)
        self.io.setEnabled(True)
        self.io.setGeometry(QtCore.QRect(10, 20, 621, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(129)
        sizePolicy.setVerticalStretch(66)
        sizePolicy.setHeightForWidth(self.io.sizePolicy().hasHeightForWidth())
        self.io.setSizePolicy(sizePolicy)
        self.io.setObjectName("io")
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.io)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(120, 30, 491, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.inputEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.inputEdit.setObjectName("inputEdit")
        self.horizontalLayout.addWidget(self.inputEdit)
        self.inputButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.inputButton.setObjectName("inputButton")
        self.inputFileLists =self.inputButton.clicked.connect(self.getFileNamesInput)
        self.horizontalLayout.addWidget(self.inputButton)
        
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.io)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 111, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.io)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(120, 70, 491, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.outputEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.outputEdit.setEnabled(True)
        self.outputEdit.setObjectName("outputEdit")
        self.horizontalLayout_2.addWidget(self.outputEdit)
        self.outputButtion = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.outputButtion.setObjectName("outputButtion")
        self.outputFolder = self.outputButtion.clicked.connect(self.getFileNamesOutput)
        self.horizontalLayout_2.addWidget(self.outputButtion)
        self.groupBox = QtWidgets.QGroupBox(Main)
        self.groupBox.setGeometry(QtCore.QRect(10, 180, 621, 239))
        self.groupBox.setObjectName("groupBox")
        self.statusScrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.statusScrollArea.setGeometry(QtCore.QRect(9, 26, 601, 201))
        self.statusScrollArea.setWidgetResizable(True)
        self.statusScrollArea.setObjectName("statusScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 599, 199))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.statusScrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 601, 201))
        self.textBrowser.setObjectName("textLog")
        self.statusScrollArea.setWidget(self.scrollAreaWidgetContents)
        
    
        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "DocJuice! 2.0"))
        self.exportButton.setText(_translate("Main", "Export"))
        self.io.setTitle(_translate("Main", "File location"))
        self.inputButton.setText(_translate("Main", "Browse..."))
        self.label.setText(_translate("Main", "PDF flie to export:"))
        self.label_2.setText(_translate("Main", "Output :"))
        self.outputButtion.setText(_translate("Main", "Browse..."))
        self.groupBox.setTitle(_translate("Main", "Status"))
        self.textBrowser.setText(_translate("Main", r"%s : Welcome to DocJuice 2.0! "%datetime.datetime.now().strftime("%H:%M:%S")))
        
    def getFileNamesInput(self):
        file_filter = 'PDF File (*.pdf)'
        response = QFileDialog.getOpenFileNames(
            caption='Select a data file',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='PDF File (*.pdf)')
        print(response[0])
        if response[0] :
            if len(response[0]) > 1 :
                self.inputEdit.setText(str(response[0]).replace("'", "").replace("[", "").replace("]", ""))
                self.textBrowser.append("%s : You have selected %d files."%(datetime.datetime.now().strftime("%H:%M:%S"), len(response[0])))
                return response[0]
            elif len(response[0]) == 1 :
                self.inputEdit.setText(response[0][0])
                self.textBrowser.append(QtCore.QCoreApplication.translate("Main", r"%s : Set select file at %s "%(datetime.datetime.now().strftime("%H:%M:%S"),response[0][0])))
                return response[0][0]
            self.dataCheck()
        
    def getFileNamesOutput(self):
        response = QFileDialog.getExistingDirectory(
            caption='Select a folder',
            directory=os.getcwd(),
            )
        print(response)
        if response[0] :
            self.outputEdit.setText(response)
            self.dataCheck()
            self.textBrowser.append(QtCore.QCoreApplication.translate("Main", r"%s : Save file at %s "%(datetime.datetime.now().strftime("%H:%M:%S"),response)))

    def dataCheck(self):
        if self.inputEdit.text() != '' and self.outputEdit.text() != '':
            self.exportButton.setEnabled(True)
            print('output is : ', self.outputEdit.text())
    
    def getTime(self):
        named_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%H:%M:%S", named_tuple)
        return time_string
    
    def whenClick(self):
        global output
        self.exportButton.setEnabled(False)
        self.textBrowser.append(QtCore.QCoreApplication.translate("Main", r"%s : Start export "%(self.getTime())))
        
        
        ### Start export ###
        # export script here 
        # input file destination at 'self.inputEdit.text()'
        # output file destination at 'self.outputEdit.text()'
        
        
        input = list(self.inputEdit.text().split(', '))
        Ie.output = self.outputEdit.text()
        
        len_file = len(input)
        file_scaned = 0
        skipped = 0
        for file in input :
            cur_file = os.path.basename(file)
            print(cur_file)
            print(f"Processing {cur_file} ...")
            if file.endswith(".pdf"):
                if all(x in utils.ie_extract_text(file) for x in Ie.KBANK_KEYWORDS):
                    inv = Ie.KBANKInvoice(file)
                    self.textBrowser.append(QtCore.QCoreApplication.translate("Main", r"%s : %s is a KBANK invoice "%(self.getTime(), cur_file)))
                    print (f"{cur_file} is a KBANK invoice")
                elif all(x in utils.ie_extract_text(file) for x in Ie.BBL_KEYWORDS):
                    inv = Ie.BBLInvoice(file)
                    self.textBrowser.append(QtCore.QCoreApplication.translate("Main", r"%s : %s is a BBL invoice "%(self.getTime(), cur_file)))
                    print (f"{cur_file} is a BBL invoice")
                elif all(x in utils.ie_extract_text(file) for x in Ie.SCB_KEYWORDS):
                    inv = Ie.SCBInvoice(file)
                    self,textBrowser.append(QtCore.QCoreApplication.translate("Main", r"%s : %s is a SCB invoice "%(self.getTime(), cur_file)))
                    print (f"{cur_file} is a SCB invoice")
                else:
                    skipped += 1
                    continue 
                try:
                    inv.get_invoice_info()
                    inv.to_excel()
                except:
                    self.textBrowser.append(QtCore.QCoreApplication.translate("Main", r"%s : Skipped file %s "%(self.getTime(), cur_file)))
                finally:
                    inv.close()
                    self.scriptFinish()
                    file_scaned += 1
                    self.textBrowser.append(QtCore.QCoreApplication.translate("Main", r"%s : %s is done %d/%d "%(self.getTime(), cur_file, file_scaned, len_file)))

                    
                    
        
    def scriptFinish(self):
        self.textBrowser.append(QtCore.QCoreApplication.translate("Main", r"%s : Finish export "%(self.getTime())))
        time.sleep(2)
        self.exportButton.setEnabled(True)
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QWidget()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
    