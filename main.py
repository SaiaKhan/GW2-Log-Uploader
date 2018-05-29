print("---------- Starting GW2 Log Uploader ----------")

import sys
import json
import os
from PyQt5 import QtWidgets, QtCore, QtGui, Qt
from mainwindow import Ui_MainWindow as MainWindow
import log_uploader
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

        with open("options.json") as f:
            self.options = json.load(f)

        self.checkLogFolders()
        self.style_ui()
        self.populate_treeview()
        self.cbChannelSelect.addItems(list(self.options["hook_urls"].keys()))


        # button connections
        self.pbUploadSelection.clicked.connect(self.upload_checked_items)
        self.progressBarUpload.valueChanged.connect(self.progressBarUpload.updateLabelFormat)
        self.pbCopyLatest.clicked.connect(self.copyResults)
        self.log_uploader.uploaded_signal.connect(self.update_progressbar)
        self.pbChooseFolder.clicked.connect(self.choose_log_folder)
        self.pbRefresh.clicked.connect(self.populate_treeview)
        #self.log_uploader.uploaded_signal.connect(self.on_upload)


    def populate_treeview(self):
        self.treeWidget.clear()
        wing_data = self.log_uploader.get_wing_data()
        # Go through the wing ids and create a node for each wing
        for wing_id in wing_data.keys():
            parent = QtWidgets.QTreeWidgetItem(self.treeWidget)
            parent.setText(0, self.options["wings"].get(wing_id, "oops"))
            parent.setFlags(QtCore.Qt.ItemIsAutoTristate\
                          | QtCore.Qt.ItemIsUserCheckable\
                          | QtCore.Qt.ItemIsEnabled)
            # for the current wing, iterate through the bosses
            # and create a child with the bossname
            for boss_id in wing_data[wing_id].keys():
                child = QtWidgets.QTreeWidgetItem(parent)
                child.setFlags(QtCore.Qt.ItemIsEnabled \
                             | QtCore.Qt.ItemIsUserCheckable)
                bossname = wing_data[wing_id].get(boss_id)
                child.setText(0, self.log_uploader.convert_bossname(bossname))
                text = self.log_uploader.format_date(self.log_uploader.get_latest_file(boss=bossname)[1])
                if text == 0:
                    child.setCheckState(0, QtCore.Qt.Unchecked)
                    child.setText(1, "No file found")
                    child.setText(2, boss_id)
                else:
                    child.setCheckState(0, QtCore.Qt.Checked)
                    child.setText(1, text)
                    child.setText(2, boss_id)
        self.treeWidget.expandAll()

    def send_test_message(self):
        self.log_uploader.test_message()


    def make_bosslist(self):
        root = self.treeWidget.invisibleRootItem()
        result = []
        for childnum in range(root.childCount()):
            child = root.child(childnum)
            for bossnum in range(child.childCount()):
                if child.child(bossnum).checkState(0):
                    boss_id = child.child(bossnum).text(2)
                    bossname = self.log_uploader.get_bossname_by_id(boss_id)
                    result.append(bossname)
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
                self.log_uploader.upload_logs(bosses, self.options["hook_urls"].get(self.cbChannelSelect.itemText(self.cbChannelSelect.currentIndex())))
                #self.cb.setText(self.log_uploader.formatted_response, mode = self.cb.Clipboard)
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
        #self.treeWidget.hideColumn(2)

        self.statusbar.setVisible(False)


        self.progressBarUpload.setTextVisible(False)
        cutofftime = datetime.timedelta(hours=8)
        self.dteCutoffDate.setDateTime(datetime.datetime.now()-cutofftime)

    def checkLogFolders(self):
        self.log_uploader.log_folder = self.options.get("logfolder", "")
        if os.path.isdir(self.log_uploader.log_folder):
            self.logFolderExists = True

    def copyResults(self):
        if self.log_uploader.formatted_response != "":
            self.cb.setText(self.log_uploader.formatted_response, mode = self.cb.Clipboard)
        else:
            self.messages.informationMessage("No logs were uploaded yet! Please upload some logs and try again!")

    def update_progressbar(self):
        self.progressBarUpload.setValue(self.progressBarUpload.value()+1)

    def choose_log_folder(self):
        self.log_uploader.log_folder = self.dialogs.getDirectoryDlg()
        self.options["logfolder"] = self.log_uploader.log_folder
        self.logFolderExists = True
        with open("options.json", "w") as f:
            json.dump(self.options, f)
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
