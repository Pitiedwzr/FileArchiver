# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signUpDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_signUpDialog(object):
    def setupUi(self, signUpDialog):
        if not signUpDialog.objectName():
            signUpDialog.setObjectName(u"signUpDialog")
        signUpDialog.resize(393, 263)
        self.gridLayout = QGridLayout(signUpDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.signUpButton = QPushButton(signUpDialog)
        self.signUpButton.setObjectName(u"signUpButton")

        self.gridLayout.addWidget(self.signUpButton, 8, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.usernameLabel = QLabel(signUpDialog)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.verticalLayout_2.addWidget(self.usernameLabel)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.passwordLabel = QLabel(signUpDialog)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.verticalLayout_2.addWidget(self.passwordLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.usernameLineEdit = QLineEdit(signUpDialog)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.verticalLayout.addWidget(self.usernameLineEdit)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.passwordLineEdit = QLineEdit(signUpDialog)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.passwordLineEdit)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 3)

        self.passRequestNumberLabel = QLabel(signUpDialog)
        self.passRequestNumberLabel.setObjectName(u"passRequestNumberLabel")

        self.gridLayout.addWidget(self.passRequestNumberLabel, 7, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 8, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 48, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 9, 2, 1, 1)

        self.skipButton = QPushButton(signUpDialog)
        self.skipButton.setObjectName(u"skipButton")
        font = QFont()
        font.setKerning(True)
        self.skipButton.setFont(font)
        self.skipButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.skipButton.setFlat(False)

        self.gridLayout.addWidget(self.skipButton, 8, 3, 1, 1)

        self.passRequestCharacterLabel = QLabel(signUpDialog)
        self.passRequestCharacterLabel.setObjectName(u"passRequestCharacterLabel")

        self.gridLayout.addWidget(self.passRequestCharacterLabel, 4, 2, 1, 1)

        self.passRequestLowercaseLabel = QLabel(signUpDialog)
        self.passRequestLowercaseLabel.setObjectName(u"passRequestLowercaseLabel")

        self.gridLayout.addWidget(self.passRequestLowercaseLabel, 6, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(17, 49, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 2, 1, 1)

        self.passRequestCapitalLabel = QLabel(signUpDialog)
        self.passRequestCapitalLabel.setObjectName(u"passRequestCapitalLabel")

        self.gridLayout.addWidget(self.passRequestCapitalLabel, 5, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.passRequestTitleLabel = QLabel(signUpDialog)
        self.passRequestTitleLabel.setObjectName(u"passRequestTitleLabel")

        self.gridLayout.addWidget(self.passRequestTitleLabel, 3, 2, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.gridLayout.addLayout(self.verticalLayout_4, 2, 2, 1, 1)


        self.retranslateUi(signUpDialog)

        QMetaObject.connectSlotsByName(signUpDialog)
    # setupUi

    def retranslateUi(self, signUpDialog):
        signUpDialog.setWindowTitle(QCoreApplication.translate("signUpDialog", "Register", None))
        self.signUpButton.setText(QCoreApplication.translate("signUpDialog", "Sign Up", None))
        self.usernameLabel.setText(QCoreApplication.translate("signUpDialog", "Username", None))
        self.passwordLabel.setText(QCoreApplication.translate("signUpDialog", "Password", None))
        self.passwordLineEdit.setInputMask("")
        self.passwordLineEdit.setPlaceholderText("")
        self.passRequestNumberLabel.setText(QCoreApplication.translate("signUpDialog", "- One number", None))
        self.skipButton.setText(QCoreApplication.translate("signUpDialog", "Skip", None))
        self.passRequestCharacterLabel.setText(QCoreApplication.translate("signUpDialog", "- Six characters", None))
        self.passRequestLowercaseLabel.setText(QCoreApplication.translate("signUpDialog", "- One lowercase letter", None))
        self.passRequestCapitalLabel.setText(QCoreApplication.translate("signUpDialog", "- One capital letter", None))
        self.passRequestTitleLabel.setText(QCoreApplication.translate("signUpDialog", "Password should contain at least:", None))
    # retranslateUi

