# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionFile_Archiver_Help = QAction(MainWindow)
        self.actionFile_Archiver_Help.setObjectName(u"actionFile_Archiver_Help")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionSave_snapshot = QAction(MainWindow)
        self.actionSave_snapshot.setObjectName(u"actionSave_snapshot")
        self.actionLoad_snapshot = QAction(MainWindow)
        self.actionLoad_snapshot.setObjectName(u"actionLoad_snapshot")
        self.actionLanguage = QAction(MainWindow)
        self.actionLanguage.setObjectName(u"actionLanguage")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pendingPathEdit = QLineEdit(self.centralwidget)
        self.pendingPathEdit.setObjectName(u"pendingPathEdit")
        self.pendingPathEdit.setGeometry(QRect(140, 50, 591, 31))
        self.pendingSelectButton = QPushButton(self.centralwidget)
        self.pendingSelectButton.setObjectName(u"pendingSelectButton")
        self.pendingSelectButton.setGeometry(QRect(730, 50, 31, 31))
        self.pendingPathLabel = QLabel(self.centralwidget)
        self.pendingPathLabel.setObjectName(u"pendingPathLabel")
        self.pendingPathLabel.setGeometry(QRect(40, 50, 91, 31))
        self.processedPathEdit = QLineEdit(self.centralwidget)
        self.processedPathEdit.setObjectName(u"processedPathEdit")
        self.processedPathEdit.setGeometry(QRect(140, 120, 591, 31))
        self.processedSelectButton = QPushButton(self.centralwidget)
        self.processedSelectButton.setObjectName(u"processedSelectButton")
        self.processedSelectButton.setGeometry(QRect(730, 120, 31, 31))
        self.processedPathLabel = QLabel(self.centralwidget)
        self.processedPathLabel.setObjectName(u"processedPathLabel")
        self.processedPathLabel.setGeometry(QRect(40, 120, 91, 31))
        self.pendingFileList = QListWidget(self.centralwidget)
        self.pendingFileList.setObjectName(u"pendingFileList")
        self.pendingFileList.setGeometry(QRect(40, 320, 256, 192))
        self.processedFileList = QListWidget(self.centralwidget)
        self.processedFileList.setObjectName(u"processedFileList")
        self.processedFileList.setGeometry(QRect(500, 320, 256, 192))
        self.pendingListLabel = QLabel(self.centralwidget)
        self.pendingListLabel.setObjectName(u"pendingListLabel")
        self.pendingListLabel.setGeometry(QRect(40, 250, 80, 20))
        self.processedListLabel = QLabel(self.centralwidget)
        self.processedListLabel.setObjectName(u"processedListLabel")
        self.processedListLabel.setGeometry(QRect(500, 250, 91, 20))
        self.ruleComboBox = QComboBox(self.centralwidget)
        self.ruleComboBox.setObjectName(u"ruleComboBox")
        self.ruleComboBox.setGeometry(QRect(340, 370, 121, 22))
        self.processButton = QPushButton(self.centralwidget)
        self.processButton.setObjectName(u"processButton")
        self.processButton.setGeometry(QRect(340, 433, 121, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSave_snapshot)
        self.menuFile.addAction(self.actionLoad_snapshot)
        self.menuHelp.addAction(self.actionFile_Archiver_Help)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuSettings.addAction(self.actionLanguage)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "File Archiver", None))
        self.actionFile_Archiver_Help.setText(QCoreApplication.translate("MainWindow", "File Archiver Help", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", "About", None))
        self.actionSave_snapshot.setText(QCoreApplication.translate("MainWindow", "Save snapshot", None))
        self.actionLoad_snapshot.setText(QCoreApplication.translate("MainWindow", "Load snapshot", None))
        self.actionLanguage.setText(QCoreApplication.translate("MainWindow", "Language", None))
        self.pendingSelectButton.setText(QCoreApplication.translate("MainWindow", "...", None))
        self.pendingPathLabel.setText(QCoreApplication.translate("MainWindow", "Pending Path", None))
        self.processedSelectButton.setText(QCoreApplication.translate("MainWindow", "...", None))
        self.processedPathLabel.setText(QCoreApplication.translate("MainWindow", "Processed Path", None))
        self.pendingListLabel.setText(QCoreApplication.translate("MainWindow", "Pending Files", None))
        self.processedListLabel.setText(QCoreApplication.translate("MainWindow", "Processed Files", None))
        self.processButton.setText(QCoreApplication.translate("MainWindow", "Process", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "Help", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", "Settings", None))
    # retranslateUi

