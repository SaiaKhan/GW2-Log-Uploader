# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui2.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 842)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.fRaidList = QtWidgets.QWidget(self.splitter)
        self.fRaidList.setObjectName("fRaidList")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fRaidList)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.fRaidList)
        self.treeWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.treeWidget.setObjectName("treeWidget")
        self.horizontalLayout.addWidget(self.treeWidget)
        self.fOptions = QtWidgets.QFrame(self.splitter)
        self.fOptions.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fOptions.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fOptions.setObjectName("fOptions")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fOptions)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.fOptions)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout_8.addWidget(self.splitter, 1, 1, 1, 1)
        self.fFooter = QtWidgets.QFrame(self.centralwidget)
        self.fFooter.setMaximumSize(QtCore.QSize(16777215, 30))
        self.fFooter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fFooter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fFooter.setObjectName("fFooter")
        self.gridLayout_8.addWidget(self.fFooter, 2, 1, 1, 1)
        self.fHeader = QtWidgets.QWidget(self.centralwidget)
        self.fHeader.setMaximumSize(QtCore.QSize(16777215, 30))
        self.fHeader.setObjectName("fHeader")
        self.gridLayout_8.addWidget(self.fHeader, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 568, 21))
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
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Raids"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))

