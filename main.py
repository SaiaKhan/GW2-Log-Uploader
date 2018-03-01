print("---------- Starting GW2 Log Uploader ----------")

import sys
from PyQt5 import QtWidgets, Qt, QtGui
from mainwindow import Ui_MainWindow as MainWindow
#from log_uploader import log_uploader
import configparser


class MyMainWindow(QtWidgets.QMainWindow, MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        print("Loaded UI!")

        config = configparser.ConfigParser()
        config.read("options.ini")

        for widget in self.frame_bosses.children():
            if isinstance(widget, QtWidgets.QGroupBox):
                print(widget.objectName())
                #widget.setEnabled(True)


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

app.setPalette(dark_palette)

app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
#cb = app.clipboard()
#cb.setText("test", mode = cb.Clipboard)


Window = MyMainWindow()
Window.show()
sys.exit(app.exec_())
