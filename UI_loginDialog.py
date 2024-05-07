# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginDialog.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(381, 285)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(17, 49, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.usernameLabel = QLabel(Dialog)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.verticalLayout_2.addWidget(self.usernameLabel)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.passwordLabel = QLabel(Dialog)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.verticalLayout_2.addWidget(self.passwordLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.usernameLineEdit = QLineEdit(Dialog)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")

        self.verticalLayout.addWidget(self.usernameLineEdit)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.passwordLineEdit = QLineEdit(Dialog)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")

        self.verticalLayout.addWidget(self.passwordLineEdit)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 3)

        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(17, 17, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer, 2, 2, 1, 1)

        self.signUpButton = QPushButton(Dialog)
        self.signUpButton.setObjectName(u"signUpButton")

        self.gridLayout.addWidget(self.signUpButton, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.signInButton = QPushButton(Dialog)
        self.signInButton.setObjectName(u"signInButton")

        self.gridLayout.addWidget(self.signInButton, 3, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 48, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 2, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.usernameLabel.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.passwordLabel.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.signUpButton.setText(QCoreApplication.translate("Dialog", u"Sign Up", None))
        self.signInButton.setText(QCoreApplication.translate("Dialog", u"Sign In", None))
    # retranslateUi

