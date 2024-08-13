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
from PySide6.QtCore import QTranslator, QLocale, QCoreApplication
import account_handling
import file_handling
import atexit
import sys


class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_slot()

    def init_slot(self):
        self.ui.pendingSelectButton.clicked.connect(self.selectPendingPath)
        self.ui.processedSelectButton.clicked.connect(self.selectProcessedPath)
        self.ui.processButton.clicked.connect(self.processCategory)
        self.directory = "rules"
        rules_files = file_handling.readRulesFiles(self.directory)
        self.ui.ruleComboBox.addItems(rules_files)
        self.ui.ruleComboBox.currentIndexChanged.connect(
        self.ui.actionChinese_CN.triggered.connect(self.languageApplyZHCN)
        self.ui.actionEnglish_US.triggered.connect(self.languageApplyENUS)

    def languageApplyZHCN(self):
        config.common.language = "zh_CN"
        config.save()
        QMessageBox.information(
            None,
            QCoreApplication.translate("mainWindow", "Success"),
            QCoreApplication.translate("mainWindow", "Language will change to Chinese (China) on next startup.")
        )
        
    def languageApplyENUS(self):
        config.common.language = "en_US"
        config.save()
        QMessageBox.information(
            None,
            QCoreApplication.translate("mainWindow", "Success"),
            QCoreApplication.translate("mainWindow", "Language will change to English (America) on next startup.")
        )
        
    def processCategory(self):
        file_handling.copyFilesToCategories(categorized_files, path_processed, save_snapshot)
        QMessageBox.information(
            None,
            QCoreApplication.translate("mainWindow", "Success"),
            QCoreApplication.translate("mainWindow", "Category complete.")
        )

    def selectPendingPath(self):
        path_pending = QFileDialog.getExistingDirectory(
            self,
            QCoreApplication.translate("mainWindow", "Select the pending folder")
        )
        if not path_pending:
            return

        self.ui.pendingPathEdit.clear()
        self.ui.pendingPathEdit.insert(path_pending)
        global pending_files
        pending_files = file_handling.goThroughFiles(path_pending)
        paths_pending_file = []
        for file in pending_files:
            path_pending_file = file.path.replace(path_pending, '.', 1)
            paths_pending_file.append(path_pending_file)

        self.ui.pendingFileList.clear()
        self.ui.pendingFileList.addItems(paths_pending_file)

    def selectProcessedPath(self):
        global path_processed
        path_processed = QFileDialog.getExistingDirectory(
            self,
            QCoreApplication.translate("mainWindow", "Select the processed folder")
        )
        if not path_processed:
            return
    
        self.ui.processedPathEdit.clear()
        self.ui.processedPathEdit.insert(path_processed)
        
        map_file = self.getCurrentRulesFile()

        extension_mapping = file_handling.loadMapping(map_file)
        
        global categorized_files
        categorized_files = file_handling.categorizeByExt(pending_files, extension_mapping)
        
        categorized_name = []

        for category, files in categorized_files.items():
            categorized_name.append(category)
            for file in files:
                categorized_name.append("- "+file.name)
                
        self.ui.processedFileList.clear()
        self.ui.processedFileList.addItems(categorized_name)

    def getCurrentRulesFile(self):
        map_file = self.ui.ruleComboBox.currentText()
        return map_file

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
            QMessageBox.critical(
                None,
                QCoreApplication.translate("signUpDialog", "Error"),
                QCoreApplication.translate("signUpDialog", "Username or password can not be empty.")
            )

        elif not account_handling.check_legal_password(password):
            QMessageBox.critical(
                None,
                QCoreApplication.translate("signUpDialog", "Error"),
                QCoreApplication.translate("signUpDialog", "Password should contain at least:\n- Six characters\n- One capital letter\n- One lowercase letter\n- One number")
            )

        else:
            account_handling.add(username,password)
            QMessageBox.information(
                None,
                QCoreApplication.translate("signUpDialog", "Success"),
                QCoreApplication.translate("signUpDialog", "Your account has been created.")
            )
            self.close()
            login.show()

    def skipRegister(self):
        skip = QMessageBox.question(
            None,
            QCoreApplication.translate("signUpDialog", " "),
            QCoreApplication.translate("signUpDialog", "Do you want to skip login and register from now on?"),
            QMessageBox.Yes | QMessageBox.No
        )
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
            QMessageBox.critical(
                None,
                QCoreApplication.translate("loginDialog", "Error"),
                QCoreApplication.translate("loginDialog", "Username or password can not be empty.")
            )
        else:
            correct = account_handling.check(username,password)
            if correct:
                self.jumpMain()
            else:
                QMessageBox.critical(
                    None,
                    QCoreApplication.translate("loginDialog", "Error"),
                    QCoreApplication.translate("loginDialog", "Incorrect user name or password.")
                )

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

    app.setWindowIcon(QIcon(".\Resource\images\icon.ico"))
    app.setStyle("fusion")
    window = mainWindow()
    login = loginDialog()
    signUp = signUpDialog()

    if config.common.firstRun:
        config.common.firstRun = False
        config.save()
        reply = QMessageBox.question(
            None,
            QCoreApplication.translate("app", " "),
            QCoreApplication.translate("app", "Do you want to Register a account?"),
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            signUp.show()
        else:
            login.show()
    elif config.common.skipSignIn:
        window.show()
    else:
        login.show()

    atexit.register(account_handling.exitDB)
    sys.exit(app.exec())