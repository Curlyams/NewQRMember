# This Python file uses the following encoding: utf-8
import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox
from PySide6 import QtCore, QtWidgets
from main import main
from ui_form import Ui_MainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py


class Worker(QtCore.QObject):
    finished =QtCore.Signal()
    error = QtCore.Signal(str)

    def __init__(self, export_path,master_path,clinic_address):
        super().__init__()
        self.clinic_address = clinic_address
        self.export_path = export_path
        self.master_path = master_path
    def run(self):
        result = main(self.export_path,self.master_path,self.clinic_address)
        if result is None:
            self.finished.emit()
        else:
            message = result
            self.error.emit(message)





class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.browseButton_1.clicked.connect(self.select_export_file)
        self.ui.browseButton_2.clicked.connect(self.select_master_file)
        self.ui.runButton.clicked.connect(self.run_script)

    def select_export_file(self):
        #open a file dialog and get the selecte file path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select File")

        # Update the file path in the form
        self.ui.export_path.setText(file_path)
    def select_master_file(self):
        #open a file dialog and get the selecte file path
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select File")

        # Update the file path in the form
        self.ui.master_path.setText(file_path)
    def run_script(self):
        # Get the export path and master path from the UI form
        export_path = self.ui.export_path.text()
        master_path = self.ui.master_path.text()

        try:
            # Check file extensions and create a new Worker instance if they are valid
            export_extension = os.path.splitext(export_path)[1]
            master_extension = os.path.splitext(master_path)[1]
            if export_extension == ".csv" and master_extension == ".xlsx":
                clinic_address_string, ok = QInputDialog.getText(self, "Input Dialog", "Please enter all paticipating address street numbers, seperated by a comma.")
                clinic_address = clinic_address_string.split(",")
                if ok:
                    self.worker = Worker(export_path, master_path,clinic_address)
                    self.worker_thread = QtCore.QThread()
                    self.worker.moveToThread(self.worker_thread)
                    self.worker.finished.connect(self.on_script_finished)
                    self.worker.error.connect(self.on_script_error)
                    self.worker_thread.started.connect(self.worker.run)
                    self.worker_thread.start()
            else:
                QtWidgets.QMessageBox.information(self,"Error: One of the files is the wrong file type.")
        except Exception as e:
            # Display an error message if an exception is raised
            QtWidgets.QMessageBox.critical(self, "Error", str(e))


    def on_script_finished(self):
        QtWidgets.QMessageBox.information(self,"QR Member Detect", "The members have been added to the Master Member List\n you can close the program")

    def on_script_error(self, message):

        QtWidgets.QMessageBox.critical(self, "Error", f"{message}: Close QR Member Detect")  # Display an error




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
