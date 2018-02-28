from PyQt5 import QtWidgets

class ButtonGroupBox(QtWidgets.QGroupBox):
    def __init__(self, parent=None):
        super(ButtonGroupBox, self).__init__(parent=parent)
        #self.groupBox = QtWidgets.QGroupBox(self)
        self.button = QtWidgets.QPushButton("FOO", parent=self)
        #print(self.groupBox.width())
        self.button.move(150, -4)
