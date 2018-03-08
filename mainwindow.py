# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/main_gui2.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(668, 860)
        MainWindow.setMinimumSize(QtCore.QSize(600, 860))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.fFooter = QtWidgets.QFrame(self.centralwidget)
        self.fFooter.setMaximumSize(QtCore.QSize(16777215, 30))
        self.fFooter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fFooter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fFooter.setObjectName("fFooter")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fFooter)
        self.horizontalLayout_2.setContentsMargins(-1, 3, -1, 3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lUploadStatus = QtWidgets.QLabel(self.fFooter)
        self.lUploadStatus.setObjectName("lUploadStatus")
        self.horizontalLayout_2.addWidget(self.lUploadStatus)
        self.progressBarUpload = customProgressBar(self.fFooter)
        self.progressBarUpload.setMinimumSize(QtCore.QSize(0, 0))
        self.progressBarUpload.setMaximum(1)
        self.progressBarUpload.setProperty("value", 0)
        self.progressBarUpload.setObjectName("progressBarUpload")
        self.horizontalLayout_2.addWidget(self.progressBarUpload)
        self.gridLayout_8.addWidget(self.fFooter, 1, 1, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setEnabled(True)
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Plain)
        self.splitter.setMidLineWidth(1)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(0)
        self.splitter.setObjectName("splitter")
        self.fRaidList = QtWidgets.QWidget(self.splitter)
        self.fRaidList.setObjectName("fRaidList")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fRaidList)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.fRaidList)
        self.treeWidget.setMinimumSize(QtCore.QSize(400, 0))
        self.treeWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setCascadingSectionResizes(True)
        self.horizontalLayout.addWidget(self.treeWidget)
        self.fOptions = QtWidgets.QFrame(self.splitter)
        self.fOptions.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fOptions.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fOptions.setObjectName("fOptions")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fOptions)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pbUploadSelection = QtWidgets.QPushButton(self.fOptions)
        self.pbUploadSelection.setObjectName("pbUploadSelection")
        self.verticalLayout.addWidget(self.pbUploadSelection)
        self.pbUploadRaids = QtWidgets.QPushButton(self.fOptions)
        self.pbUploadRaids.setObjectName("pbUploadRaids")
        self.verticalLayout.addWidget(self.pbUploadRaids)
        self.pbUploadFractals = QtWidgets.QPushButton(self.fOptions)
        self.pbUploadFractals.setObjectName("pbUploadFractals")
        self.verticalLayout.addWidget(self.pbUploadFractals)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.cbCustomList = QtWidgets.QComboBox(self.fOptions)
        self.cbCustomList.setObjectName("cbCustomList")
        self.verticalLayout.addWidget(self.cbCustomList)
        self.pbUploadCustomList = QtWidgets.QPushButton(self.fOptions)
        self.pbUploadCustomList.setObjectName("pbUploadCustomList")
        self.verticalLayout.addWidget(self.pbUploadCustomList)
        self.pbCreateCustomList = QtWidgets.QPushButton(self.fOptions)
        self.pbCreateCustomList.setObjectName("pbCreateCustomList")
        self.verticalLayout.addWidget(self.pbCreateCustomList)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pbCopyLatest = QtWidgets.QPushButton(self.fOptions)
        self.pbCopyLatest.setObjectName("pbCopyLatest")
        self.verticalLayout.addWidget(self.pbCopyLatest)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.pbTest = QtWidgets.QPushButton(self.fOptions)
        self.pbTest.setObjectName("pbTest")
        self.verticalLayout.addWidget(self.pbTest)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.label = QtWidgets.QLabel(self.fOptions)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.dteCutoffDate = QtWidgets.QDateTimeEdit(self.fOptions)
        self.dteCutoffDate.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.dteCutoffDate.setCalendarPopup(True)
        self.dteCutoffDate.setObjectName("dteCutoffDate")
        self.verticalLayout.addWidget(self.dteCutoffDate)
        self.gridLayout_8.addWidget(self.splitter, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 668, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lUploadStatus.setText(_translate("MainWindow", "upload status"))
        self.progressBarUpload.setFormat(_translate("MainWindow", "%v of %m files uploaded"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Raids"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "most recent run"))
        self.pbUploadSelection.setText(_translate("MainWindow", "upload selected bosses"))
        self.pbUploadRaids.setText(_translate("MainWindow", "upload latest raids"))
        self.pbUploadFractals.setText(_translate("MainWindow", "upload latest fractals"))
        self.pbUploadCustomList.setText(_translate("MainWindow", "upload custom list"))
        self.pbCreateCustomList.setText(_translate("MainWindow", "create custom list"))
        self.pbCopyLatest.setText(_translate("MainWindow", "copy latest upload \n"
" to clipboard"))
        self.pbTest.setText(_translate("MainWindow", "big red button"))
        self.label.setText(_translate("MainWindow", "Choose a cutoff date"))
        self.dteCutoffDate.setToolTip(_translate("MainWindow", "Any logs that were saved before this date will not be considered when looking for logs to upload!"))
        self.dteCutoffDate.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy HH:mm"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))

from customProgressBar import customProgressBar
