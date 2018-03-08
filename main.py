print("---------- Starting GW2 Log Uploader ----------")

import sys
import ast
from PyQt5 import QtWidgets, QtCore, QtGui, Qt
from mainwindow import Ui_MainWindow as MainWindow
import log_uploader
import configparser
import messages


class MyMainWindow(QtWidgets.QMainWindow, MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        print("Loaded UI!")

        self.config = configparser.ConfigParser()
        self.config.read("options.ini")
        self.style_ui()
        self.populate_treeview()

        self.log_uploader = log_uploader.log_uploader()
        self.messages = messages.cErrorDlg()


        # button connections
        self.pbUploadSelection.clicked.connect(self.upload_checked_items)


    def populate_treeview(self):
        # load boss- and wingnames from the options file
        data = ast.literal_eval(self.config["bosslists"]["bosses"])
        for wing in data.keys():
            parent = QtWidgets.QTreeWidgetItem(self.treeWidget)
            parent.setText(0, wing)
            parent.setText(1, "something something modify date")
            parent.setFlags(QtCore.Qt.ItemIsAutoTristate | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            for boss in data[wing]:
                child = QtWidgets.QTreeWidgetItem(parent)
                child.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
                child.setText(0, boss)
                child.setCheckState(0, QtCore.Qt.Checked)

        self.treeWidget.expandAll()
        c_width = round(self.treeWidget.width()/2)
        self.treeWidget.setColumnWidth(0, c_width)
        self.treeWidget.setColumnWidth(1, c_width)


    def make_bosslist(self):
        root = self.treeWidget.invisibleRootItem()
        result = []
        for childnum in range(root.childCount()):
            child = root.child(childnum)
            for bossnum in range(child.childCount()):
                if child.child(bossnum).checkState(0):
                    #print(child.child(bossnum).text(0))
                    result.append(child.child(bossnum).text(0))
        return result

    def upload_checked_items(self):
        bosses = self.make_bosslist()
        if len(bosses) > 0:
            self.log_uploader.upload_parts(bosses)
        else:
            self.messages.informationMessage("Please select some bosses to upload!")


    def style_ui(self):
        # This makes the checkbox border light-blue
        treePalette = QtGui.QPalette()
        treePalette.setColor(QtGui.QPalette.Window, QtGui.QColor(85, 170, 255))
        self.treeWidget.setPalette(treePalette)


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
