from PyQt5 import QtWidgets

class cErrorDlg(QtWidgets.QDialog):
	def __init__(self, parent = None):
		super(cErrorDlg, self).__init__(parent)
		self.errorMessageDialog = QtWidgets.QErrorMessage(self)

	def warningMessage(self, warning, title="Warning!!!"):
		msgBox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning,
				 title, warning,
				 QtWidgets.QMessageBox.NoButton, self)
		msgBox.addButton("Try &Again", QtWidgets.QMessageBox.AcceptRole)
		msgBox.addButton("&Continue", QtWidgets.QMessageBox.RejectRole)
		if msgBox.exec_() == QtWidgets.QMessageBox.AcceptRole:
			#action if accept was pressed
			return
		else:
			#action for rejection
			return

	def informationMessage(self, information, title="Information"):
		reply = QtWidgets.QMessageBox.information(self, title, information, QtWidgets.QMessageBox.Ok)
		if reply == QtWidgets.QMessageBox.Ok:
			#action if ok
			return False
		else:
			#action if not ok
			pass

	def questionMessage(self, title, question):
		reply = QtWidgets.QMessageBox.question(self, title, question,
				QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
		if reply == QtWidgets.QMessageBox.Yes:
			#action if yes
			return True
		elif reply == QtWidgets.QMessageBox.No:
			return False
		else:
			#action if cancel
			pass

	def criticalMessage(self, title, message):
		reply = QtWidgets.QMessageBox.critical(self, title, message,
                QtWidgets.QMessageBox.Abort | QtWidgets.QMessageBox.Retry | QtWidgets.QMessageBox.Ignore)
		if reply == QtWidgets.QMessageBox.Abort:
			#action if abort
			pass
		elif reply == QtWidgets.QMessageBox.Retry:
			#action if retry
			pass
		else:
			#action otherwise
			pass

	def errorMessage(self, error):
		self.errorMessageDialog.showMessage(error)

class cInputDlg(QtWidgets.QDialog):
	def __init__(self, parent = None):
		super(cInputDlg, self).__init__(parent)

	def getText(self, title, prompt, preset):
		text, ok = QtWidgets.QInputDialog.getText(self, title, prompt, QtWidgets.QLineEdit.Normal, preset)
		if ok and text != "":
			return text

	def getServer(self):
		items = ("BR", "EUNE", "EUW", "KR", "LAN", "LAS", "NA", "OCE", "RU", "TR")
		item, ok = QtWidgets.QInputDialog.getItem(self, "Choose a server!", "Server", items, 2, False)
		if ok and item:
			return str(item).lower()

	def getCombo(self,items):
		item, ok = QtWidgets.QInputDialog.getItem(self, "Choose a sheet!", "Sheet", items, 0, False)
		if ok and item:
			return item

	def getRole(self, items, name):
		item, ok = QtWidgets.QInputDialog.getItem(self, "Choose a role", name, items, 0, False)
		if ok and item:
			return str(item)

	def getDirectoryDlg(self):
		file = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
		return file

	def setOpenFileName(self):
		options = QtWidgets.QFileDialog.Options()
		options |= QtWidgets.QFileDialog.DontUseNativeDialog
		fileName = QtWidgets.QFileDialog.getOpenFileName(self,
				"Choose file for import",
				"","",
				"JSON Files (*.json)", options)
		if fileName:
			return fileName
