from PyQt5 import QtWidgets

class customProgressBar(QtWidgets.QProgressBar):
    def __init__(self, parent=None):
        super(customProgressBar, self).__init__(parent=parent)

    def updateLabelFormat(self):
        print(self.value())
        if self.value() == self.maximum():
            self.setFormat("All uploads completed!")
        else:
            self.setFormat("%v of %m files uploaded")
