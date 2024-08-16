from UI_mainWindow import Ui_MainWindow
from UI_loginDialog import Ui_loginDialog
from UI_signUpDialog import Ui_signUpDialog
from settings import config
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QFileDialog
from PySide6.QtCore import QTranslator, QLocale, QCoreApplication
import account_handling
import file_handling
import atexit
import sys
import os


# Main window of the File Archiver application
# Handles file selection, processing, and user interface interactions
class MainWindow(QMainWindow):
    # Inital the UI and functions
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initSlot()
        self.setupLanguageActions()


    # Connect functions to the UI
    def initSlot(self):
        self.ui.pendingSelectButton.clicked.connect(self.selectPendingPath)
        self.ui.processedSelectButton.clicked.connect(self.selectProcessedPath)
        self.ui.processButton.clicked.connect(self.processCategory)
        self.directory = "rules"
        rules_files = file_handling.readRulesFiles(self.directory)
        self.ui.ruleComboBox.addItems(rules_files)
        self.ui.ruleComboBox.currentIndexChanged.connect(self.getCurrentRulesFile)
        self.ui.actionLoad_snapshot.triggered.connect(self.loadSnapshot)
        self.ui.snapshotCheckBox.stateChanged.connect(self.sscbStateChanged)
        self.ui.actionEnableLogin.triggered.connect(self.enableLogin)
        self.ui.actionDisableLogin.triggered.connect(self.disableLogin)


    def enableLogin(self):
        config.common.skipSignIn = False
        config.save()
        QMessageBox.information(
            None,
            QCoreApplication.translate("MainWindow", "Success"),
            QCoreApplication.translate("MainWindow", f"Login will display on next startup.")
        )

    def disableLogin(self):
        config.common.skipSignIn = True
        config.save()
        QMessageBox.information(
            None,
            QCoreApplication.translate("MainWindow", "Success"),
            QCoreApplication.translate("MainWindow", f"Login won't display on next startup.")
        )

    # Get the snapshot file from user input and pass it to the function
    def loadSnapshot(self):
        snapshots, _ = QFileDialog.getOpenFileNames(
            self,
            QCoreApplication.translate("mainWindow", "Open snapshot file"),
            "snapshots",
            QCoreApplication.translate("mainWindow", "Snapshot file (*.yaml)"),
        )
        
        if len(snapshots) != 1: # Check if user choose more than one file
            QMessageBox.warning(
                None,
                QCoreApplication.translate("mainWindow", "Error"),
                QCoreApplication.translate("mainWindow", f"You can only select one snapshot for loading.")
            )
            
        else:
            snapshot_path = snapshots[0]
            snapshot_name = os.path.basename(snapshot_path)
            confirm = QMessageBox.question(
                None,
                QCoreApplication.translate("mainWindow", "Warning"),
                QCoreApplication.translate("mainWindow", f"Are you sure you want to load the snapshot {snapshot_name}? This will undo all changes in that process."),
                QMessageBox.Yes | QMessageBox.No
            )
            
            if confirm == QMessageBox.Yes:
                if file_handling.loadSnapshot(snapshot_path):
                    QMessageBox.information(
                        None,
                        QCoreApplication.translate("mainWindow", "Success"),
                        QCoreApplication.translate("mainWindow", f"The snapshot {snapshot_name} has been loaded, undo all changes.")
                    )
    

    # Generate snapshot if user want
    def sscbStateChanged(self):
        self.save_snapshot = False
        if self.ui.snapshotCheckBox.isChecked():
            self.save_snapshot = True
        else:
            self.save_snapshot = False
            

    # Initial a dictionary and tuple for language changing
    def setupLanguageActions(self):
        language_actions = {
            "zh_CN": (self.ui.actionChinese_CN, QCoreApplication.translate("MainWindow", "Simplified Chinese (China)")),
            "zh_TW": (self.ui.actionChinese_TW, QCoreApplication.translate("MainWindow", "Traditional Chinese (Taiwan)")),
            "zh_HK": (self.ui.actionChinese_HK, QCoreApplication.translate("MainWindow", "Traditional Chinese (Hongkong)")),
            "en_US": (self.ui.actionEnglish_US, QCoreApplication.translate("MainWindow", "English (American)")),
            "en_GB": (self.ui.actionEnglish_GB, QCoreApplication.translate("MainWindow", "English (Britain)")),
            "es_ES": (self.ui.actionSpanish, QCoreApplication.translate("MainWindow", "Spanish")),
            "fr_FR": (self.ui.actionFrench, QCoreApplication.translate("MainWindow", "French")),
            "de_DE": (self.ui.actionGerman, QCoreApplication.translate("MainWindow", "German")),
            "pr_BR": (self.ui.actionPortuguese, QCoreApplication.translate("MainWindow", "Portuguese")),
            "ru_RU": (self.ui.actionRussian, QCoreApplication.translate("MainWindow", "Russian")),
            "jp_JP": (self.ui.actionJapanese, QCoreApplication.translate("MainWindow", "Japanese")),
            "ar_AE": (self.ui.actionArabic, QCoreApplication.translate("MainWindow", "Arabic")),
            "hi_IN": (self.ui.actionHindi, QCoreApplication.translate("MainWindow", "Hindi")),
            "ko_KR": (self.ui.actionKorean, QCoreApplication.translate("MainWindow", "Korean")),
            "it_IT": (self.ui.actionItalian, QCoreApplication.translate("MainWindow", "Italian")),
            "tr_TR": (self.ui.actionTurkish, QCoreApplication.translate("MainWindow", "Turkish")),
            "nl_NL": (self.ui.actionDutch, QCoreApplication.translate("MainWindow", "Dutch")),
            "sv_SE": (self.ui.actionSwedish, QCoreApplication.translate("MainWindow", "Swedish"))
        }

        for lang_code, (action, lang_name) in language_actions.items():
            action.triggered.connect(lambda lc=lang_code, ln=lang_name: self.changeLanguage(lc, ln)) # Use lambda function to avoid run it when connect it


    # Change languages to the passed one 
    def changeLanguage(self, lang_code, lang_name):
        config.common.language = lang_code
        config.save()
        
        QMessageBox.information(
            None,
            QCoreApplication.translate("mainWindow", "Success"),
            QCoreApplication.translate("mainWindow", f"Language will change to {lang_name} on next startup.")
        )

    # Execute process
    def processCategory(self):
        try:
            file_handling.moveFilesToCategories(self.categorized_files, self.path_processed, self.save_snapshot)
            QMessageBox.information(
                None,
                QCoreApplication.translate("mainWindow", "Success"),
                QCoreApplication.translate("mainWindow", "Category complete.")
            )
        except NameError and AttributeError: # Check if user doesn't choose a path
            QMessageBox.critical(
                None,
                QCoreApplication.translate("MainWindow", "Error"),
                QCoreApplication.translate("MainWindow", "Please select a valid path.")
            )


    # Get the files in the pending path, add them to the list
    def selectPendingPath(self):
        self.path_pending = QFileDialog.getExistingDirectory(
            self,
            QCoreApplication.translate("mainWindow", "Select the pending folder")
        )
        if not self.path_pending: # If not a avaliable path then return
            return

        self.ui.pendingPathEdit.clear()
        self.ui.pendingPathEdit.insert(self.path_pending)
        self.pending_files = file_handling.goThroughFiles(self.path_pending)
        paths_pending_file = []
        for file in self.pending_files:
            path_pending_file = file.path.replace(self.path_pending, '.', 1)
            paths_pending_file.append(path_pending_file)

        self.ui.pendingFileList.clear()
        self.ui.pendingFileList.addItems(paths_pending_file)


    # Get the files in the processed path, pre-processed them and show them in the list
    def selectProcessedPath(self):
        self.path_processed = QFileDialog.getExistingDirectory(
            self,
            QCoreApplication.translate("mainWindow", "Select the processed folder")
        )
        if not self.path_processed:
            return
    
        self.ui.processedPathEdit.clear()
        self.ui.processedPathEdit.insert(self.path_processed)
        map_file = self.getCurrentRulesFile()
        extension_mapping = file_handling.loadMapping(map_file)
        self.categorized_files = file_handling.categorizeByExt(self.pending_files, extension_mapping)
        categorized_name = []

        for category, files in self.categorized_files.items():
            categorized_name.append(category)
            for file in files:
                categorized_name.append("- "+file.name)
                
        self.ui.processedFileList.clear()
        self.ui.processedFileList.addItems(categorized_name)


    # Get the rule file that user selected
    def getCurrentRulesFile(self):
        map_file = self.ui.ruleComboBox.currentText()
        return map_file


class SignUpDialog(QDialog):
    # Inital the UI and functions
    def __init__(self):
        super(SignUpDialog,self).__init__()
        self.ui = Ui_signUpDialog()
        self.ui.setupUi(self)
        self.initSlot()


    # Connect functions to the UI
    def initSlot(self):
        self.ui.signUpButton.clicked.connect(self.addAccount)
        self.ui.skipButton.clicked.connect(self.skipRegister)


    # Get user input and pass to the function
    def addAccount(self):
        username = self.ui.usernameLineEdit.text().strip()
        password = self.ui.passwordLineEdit.text().strip()
        if username == "" or password == "": # If user input nothing then ask them input again
            QMessageBox.critical(
                None,
                QCoreApplication.translate("signUpDialog", "Error"),
                QCoreApplication.translate("signUpDialog", "Username or password can not be empty.")
            )

        elif not account_handling.checkLegalPassword(password): # If user input a not legal password then ask them input again
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


    # If user don't want to use login system, diable the login part and add to the settings
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


class LoginDialog(QDialog):
    # Inital the UI and functions
    def __init__(self):
        super(LoginDialog,self).__init__()
        self.ui = Ui_loginDialog()
        self.ui.setupUi(self)
        self.initSlot()


    # Connect functions to the UI
    def initSlot(self):
        self.ui.signInButton.clicked.connect(self.checkAccount)
        self.ui.signUpButton.clicked.connect(self.jumpSignUp)


    # Pass the username and password to the function and get a boolean, jump to main window if is True
    def checkAccount(self):
        username = self.ui.usernameLineEdit.text().strip()
        password = self.ui.passwordLineEdit.text().strip()
        if username == "" or password == "": # If user input nothing then ask them input again
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


    # Jump to main window and close the correct windows
    def jumpMain(self):
        self.close()
        window.show()


    # Jump to sing up window and close the correct windows
    def jumpSignUp(self):
        self.close()
        signUp.show()


# Main program running
if __name__ == "__main__":
    app = QApplication(sys.argv)
    translator = QTranslator() # Initial the translator
    locale = QLocale.system().name() # Get the system language which the user use

    # Change the default language (English) to the system language
    if locale != config.common.language and config.common.firstRun:
        config.common.language = locale
        config.save()
    
    locale = config.common.language # Change the language in the settings

    # Load translation
    if translator.load(f"translations/{locale}.qm"):
        app.installTranslator(translator)

    app.setWindowIcon(QIcon(".\Resource\images\icon.ico"))
    app.setStyle("fusion")
    
    # Inital all windows
    window = MainWindow()
    login = LoginDialog()
    signUp = SignUpDialog()

    # Ask the user who first run the program want to sign up or not
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
            
    # If user disable the login system them just show the main window
    elif config.common.skipSignIn:
        window.show()
        
    # Normallly show the login window
    else:
        login.show()
        
    # Close the database when exit the program
    atexit.register(account_handling.exitDB)
    sys.exit(app.exec())