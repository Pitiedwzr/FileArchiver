from UI_mainWindow import Ui_MainWindow
from UI_loginDialog import Ui_Dialog

import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import QFile

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class Dialog(QDialog):
    def __init__(self):
        super(Dialog,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_slot()

    def init_slot(self):
        self.ui.signInButton.clicked.connect(self.jumpMain)

    def jumpMain(self):
        self.close()
        window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon(".\resource\images\icon.ico"))
    window = MainWindow()
    login = Dialog()
    login.show()

    sys.exit(app.exec())