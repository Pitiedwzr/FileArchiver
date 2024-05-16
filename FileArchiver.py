from UI_mainWindow import Ui_MainWindow
from UI_loginDialog import Ui_loginDialog
from UI_signUpDialog import Ui_signUpDialog
import account_handling
import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PySide6.QtCore import QFile

class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class signUpDialog(QDialog):
    def __init__(self):
        super(signUpDialog,self).__init__()
        self.ui = Ui_signUpDialog()
        self.ui.setupUi(self)
        self.init_slot()

    def init_slot(self):
        self.ui.signUpButton.clicked.connect(self.add_account)

    def add_account(self):
        username = self.ui.usernameLineEdit.text().strip()
        password = self.ui.passwordLineEdit.text().strip()
        if username == "" or password == "":
            QMessageBox.critical(None,"Error","Username or password can not be empty.")
        else:
            account_handling.add(username,password)
            QMessageBox.information(None,"Success","Your account has been created.")
            self.close()
            login.show()



class loginDialog(QDialog):
    def __init__(self):
        super(loginDialog,self).__init__()
        self.ui = Ui_loginDialog()
        self.ui.setupUi(self)
        self.init_slot()

    def init_slot(self):
        self.ui.signInButton.clicked.connect(self.check_account)
        self.ui.signUpButton.clicked.connect(self.jumpSignUp)

    def check_account(self):
        username = self.ui.usernameLineEdit.text().strip()
        password = self.ui.passwordLineEdit.text().strip()
        if username == "" or password == "":
            QMessageBox.critical(None,"Error","Username or password can not be empty.")
        else:
            correct = account_handling.check(username,password)
            if correct:
                self.jumpMain()
            else:
                QMessageBox.critical(None,"Error","Incorrect user name or password.")

    def jumpMain(self):
        self.close()
        window.show()

    def jumpSignUp(self):
        self.close()
        signUp.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon(".\resource\images\icon.ico"))
    window = mainWindow()
    login = loginDialog()
    signUp = signUpDialog()
    login.show()

    sys.exit(app.exec())