from UI_mainWindow import Ui_MainWindow
from UI_loginDialog import Ui_loginDialog
from UI_signUpDialog import Ui_signUpDialog
import account_handling
import file_handling
import sys
import atexit
from settings import config
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QFileDialog
from PySide6.QtCore import QFile, QTranslator, QLocale

class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_slot()

    def init_slot(self):
        self.ui.pendingSelectButton.clicked.connect(self.selectPendingPath)
        self.ui.processedSelectButton.clicked.connect(self.selectProcessedPath)

    def selectPendingPath(self):
        path_pending = QFileDialog.getExistingDirectory(self,"Select the pending folder")
        self.ui.pendingPathEdit.clear()
        self.ui.pendingPathEdit.insert(path_pending)
        full_pending, name_pending = file_handling.goThroughFiles(path_pending)
        self.ui.pendingFileList.clear()
        self.ui.pendingFileList.addItems(name_pending)

    def selectProcessedPath(self):
        path_processed = QFileDialog.getExistingDirectory(self,"Select the processed folder")
        self.ui.processedPathEdit.clear()
        self.ui.processedPathEdit.insert(path_processed)
        # full_processed, name_processed = 
        # self.ui.processedFileList.clear()
        # self.ui.processedFileList.addItems(name_processed)

class signUpDialog(QDialog):
    def __init__(self):
        super(signUpDialog,self).__init__()
        self.ui = Ui_signUpDialog()
        self.ui.setupUi(self)
        self.init_slot()

    def init_slot(self):
        self.ui.signUpButton.clicked.connect(self.add_account)
        self.ui.skipButton.clicked.connect(self.skipRegister)

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

    def skipRegister(self):
        skip = QMessageBox.question(None," ","Skip only for this time or from now on? ",QMessageBox.Yes | QMessageBox.No)
        if skip == QMessageBox.Yes:
            config.common.skipSignIn = True
            config.save()
            self.close()
            window.show()
        else:
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
    translator = QTranslator()

    locale = QLocale.system().name()

    if locale != config.common.language and config.common.firstRun:
        config.common.language = locale
        config.save()
    
    locale = config.common.language

    if translator.load(f"translations/{locale}.qm"):
        app.installTranslator(translator)

    # app.setWindowIcon(QIcon(".\resource\images\icon.ico")) # It doesn't work...
    window = mainWindow()
    login = loginDialog()
    signUp = signUpDialog()

    if config.common.firstRun:
        config.common.firstRun = False
        config.save()
        relpy = QMessageBox.question(None," ","Do you want to Register a account?",QMessageBox.Yes | QMessageBox.No)
        if relpy == QMessageBox.Yes:
            signUp.show()
        else:
            login.show()
    elif config.common.skipSignIn:
        window.show()
    else:
        login.show()

    atexit.register(account_handling.exitDB)
    sys.exit(app.exec())