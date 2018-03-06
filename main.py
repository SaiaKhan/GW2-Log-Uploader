print("---------- Starting GW2 Log Uploader ----------")

import sys
from PyQt5 import QtWidgets, QtCore, QtGui, Qt
from mainwindow import Ui_MainWindow as MainWindow
#from log_uploader import log_uploader
import configparser


class MyMainWindow(QtWidgets.QMainWindow, MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        print("Loaded UI!")

        config = configparser.ConfigParser()
        self.options = config.read("options.ini")

        self.populate_treeview()

        # This makes the checkbox border light-blue
        treePalette = QtGui.QPalette()
        treePalette.setColor(QtGui.QPalette.Window, QtGui.QColor(85, 170, 255))
        self.treeWidget.setPalette(treePalette)

        #for widget in self.frame_bosses.children():
        #    if isinstance(widget, QtWidgets.QGroupBox):
        #        print(widget.objectName())

    def populate_treeview(self):
        # load boss- and wingnames from the options file
        data = {"Spirit Vale": ["VG", "Gorseval", "Sabetha"], "Hall of Chains": ["Soulless Horror", "Dhuum"]}
        for wing in data.keys():
            parent = QtWidgets.QTreeWidgetItem(self.treeWidget)
            parent.setText(0, wing)
            parent.setFlags(QtCore.Qt.ItemIsAutoTristate | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            for boss in data[wing]:
                child = QtWidgets.QTreeWidgetItem(parent)
                child.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
                child.setText(0, boss)
                child.setCheckState(0, QtCore.Qt.Checked)


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
