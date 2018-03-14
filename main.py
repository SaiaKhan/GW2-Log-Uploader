print("---------- Starting GW2 Log Uploader ----------")

import sys
import ast
import os
from PyQt5 import QtWidgets, QtCore, QtGui, Qt
from mainwindow import Ui_MainWindow as MainWindow
import log_uploader
import configparser
import messages
import datetime


class MyMainWindow(QtWidgets.QMainWindow, MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        print("Loaded UI!")
        self.logFolderExists = False

        self.log_uploader = log_uploader.log_uploader()
        self.messages = messages.cErrorDlg()
        self.dialogs = messages.cInputDlg()
        self.cb = app.clipboard()

        self.config = configparser.ConfigParser()
        self.config.read("options.ini")
        self.checkLogFolders()
        self.style_ui()
        self.populate_treeview()


        # button connections
        self.pbUploadSelection.clicked.connect(self.upload_checked_items)
        self.progressBarUpload.valueChanged.connect(self.progressBarUpload.updateLabelFormat)
        self.pbCopyLatest.clicked.connect(self.copyResults)
        self.log_uploader.uploaded_signal.connect(self.update_progressbar)
        self.pbChooseFolder.clicked.connect(self.choose_log_folder)
        self.pbRefresh.clicked.connect(self.populate_treeview)
        self.pbTest.clicked.connect(self.find_bosses)
        #self.log_uploader.uploaded_signal.connect(self.on_upload)


    def populate_treeview(self):
        # load boss- and wingnames from the options file
        self.treeWidget.clear()
        # the data should not be read from the config file but rather be gained
        # from crawling the subdirs of the chosen log directory
        data = ast.literal_eval(self.config["bosslists"]["bosses"])
        for wing in data.keys():
            parent = QtWidgets.QTreeWidgetItem(self.treeWidget)
            parent.setText(0, wing)
            parent.setFlags(QtCore.Qt.ItemIsAutoTristate | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            for boss in data[wing]:
                child = QtWidgets.QTreeWidgetItem(parent)
                child.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
                child.setText(0, boss)
                text = self.log_uploader.format_date(self.log_uploader.get_latest_file(boss=boss)[1])
                if text == 0:
                    child.setCheckState(0, QtCore.Qt.Unchecked)
                    child.setText(1, "No file found")
                else:
                    child.setCheckState(0, QtCore.Qt.Checked)
                    child.setText(1, text)
        self.treeWidget.expandAll()


    def make_bosslist(self):
        root = self.treeWidget.invisibleRootItem()
        result = []
        for childnum in range(root.childCount()):
            child = root.child(childnum)
            for bossnum in range(child.childCount()):
                if child.child(bossnum).checkState(0):
                    result.append(child.child(bossnum).text(0))
        return result

    def upload_checked_items(self):
        bosses = self.make_bosslist()
        #print("uploading {0} bosses".format(len(bosses)))
        if self.logFolderExists:
            if len(bosses) > 0:
                self.progressBarUpload.setMinimum(0)
                self.progressBarUpload.setMaximum(len(bosses))
                self.progressBarUpload.setValue(0)
                self.progressBarUpload.setTextVisible(True)
                self.log_uploader.upload_parts(bosses)
                self.cb.setText(self.log_uploader.formattedResponse, mode = self.cb.Clipboard)
            else:
                self.messages.informationMessage("Please select at least one boss to upload!")
        else:
            self.messages.informationMessage("Please choose a log folder first!")


    def style_ui(self):
        # This makes the checkbox border light-blue
        treePalette = QtGui.QPalette()
        treePalette.setColor(QtGui.QPalette.Window, QtGui.QColor(85, 170, 255))
        self.treeWidget.setPalette(treePalette)
        self.treeWidget.setCurrentItem(None, 0)
        c_width = round(self.treeWidget.width()/3)
        self.treeWidget.setColumnWidth(0, c_width*2)
        self.treeWidget.setColumnWidth(1, c_width)

        self.statusbar.setVisible(False)


        self.progressBarUpload.setTextVisible(False)
        cutofftime = datetime.timedelta(hours=8)
        self.dteCutoffDate.setDateTime(datetime.datetime.now()-cutofftime)

    def checkLogFolders(self):
        self.log_uploader.log_folder = self.config["options"]["logfolder"]
        if os.path.isdir(self.log_uploader.log_folder):
            self.logFolderExists = True

    def copyResults(self):
        if self.log_uploader.formattedResponse != "":
            self.cb.setText(self.log_uploader.formattedResponse, mode = self.cb.Clipboard)
        else:
            self.messages.informationMessage("No logs were uploaded yet! Please upload some logs and try again!")

    def update_progressbar(self):
        self.progressBarUpload.setValue(self.progressBarUpload.value()+1)

    def choose_log_folder(self):
        self.log_uploader.log_folder = self.dialogs.getDirectoryDlg()
        self.config["options"]["logfolder"] = self.log_uploader.log_folder
        self.logFolderExists = True
        with open("options.ini", "w") as c:
            self.config.write(c)
        self.populate_treeview()
        return self.log_uploader.log_folder

    def find_bosses(self):
        """This walks through the log directory to find bosses"""
        if os.path.isdir(self.log_uploader.log_folder):
            for dirname, subdirs, files in os.walk(self.log_uploader.log_folder):
                print(os.path.split(dirname)[-1])

app = QtWidgets.QApplication(sys.argv)
app.setStyle("fusion")
dark_palette = QtGui.QPalette()

dark_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
dark_palette.setColor(QtGui.QPalette.WindowText, Qt.QColor(255, 255, 255))
dark_palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
dark_palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
dark_palette.setColor(QtGui.QPalette.ToolTipBase, Qt.QColor(255, 255, 255))
dark_palette.setColor(QtGui.QPalette.ToolTipText, Qt.QColor(255, 255, 255))
dark_palette.setColor(QtGui.QPalette.Text, Qt.QColor(255, 255, 255))
dark_palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
dark_palette.setColor(QtGui.QPalette.ButtonText, Qt.QColor(255, 255, 255))
dark_palette.setColor(QtGui.QPalette.BrightText, Qt.QColor(255, 0, 0))
dark_palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
dark_palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
dark_palette.setColor(QtGui.QPalette.HighlightedText, Qt.QColor(0, 0, 0))

dark_palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Button, QtGui.QColor(55, 0, 0))
dark_palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, QtGui.QColor(100, 100, 100))
#dark_palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Button, QtGui.QColor(25, 0, 0))

#dark_palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142,45,197).lighter())
dark_palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(85, 170, 255).lighter())
dark_palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)

app.setPalette(dark_palette)

app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
#cb = app.clipboard()
#cb.setText("test", mode = cb.Clipboard)


Window = MyMainWindow()
Window.show()
sys.exit(app.exec_())
