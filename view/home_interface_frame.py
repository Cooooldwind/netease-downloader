# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_interface_frame.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLayout,
    QListView, QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import (ComboBox, PushButton, SearchLineEdit, TitleLabel)

class Ui_HomeInterface(object):
    def setupUi(self, HomeInterface):
        if not HomeInterface.objectName():
            HomeInterface.setObjectName(u"HomeInterface")
        HomeInterface.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HomeInterface.sizePolicy().hasHeightForWidth())
        HomeInterface.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QWidget(HomeInterface)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-1, -1, 401, 301))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.WelcomeLabel = TitleLabel(self.verticalLayoutWidget)
        self.WelcomeLabel.setObjectName(u"WelcomeLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.WelcomeLabel.sizePolicy().hasHeightForWidth())
        self.WelcomeLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.WelcomeLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(5, -1, 5, -1)
        self.SearchTypeComboBox = ComboBox(self.verticalLayoutWidget)
        self.SearchTypeComboBox.addItem("")
        self.SearchTypeComboBox.addItem("")
        self.SearchTypeComboBox.addItem("")
        self.SearchTypeComboBox.addItem("")
        self.SearchTypeComboBox.setObjectName(u"SearchTypeComboBox")

        self.horizontalLayout.addWidget(self.SearchTypeComboBox)

        self.SearchKeyLineEdit = SearchLineEdit(self.verticalLayoutWidget)
        self.SearchKeyLineEdit.setObjectName(u"SearchKeyLineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.SearchKeyLineEdit.sizePolicy().hasHeightForWidth())
        self.SearchKeyLineEdit.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.SearchKeyLineEdit)

        self.LoginButton = PushButton(self.verticalLayoutWidget)
        self.LoginButton.setObjectName(u"LoginButton")

        self.horizontalLayout.addWidget(self.LoginButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.listView = QListView(self.verticalLayoutWidget)
        self.listView.setObjectName(u"listView")

        self.verticalLayout.addWidget(self.listView)


        self.retranslateUi(HomeInterface)

        QMetaObject.connectSlotsByName(HomeInterface)
    # setupUi

    def retranslateUi(self, HomeInterface):
        HomeInterface.setWindowTitle(QCoreApplication.translate("HomeInterface", u"Frame", None))
        self.WelcomeLabel.setText(QCoreApplication.translate("HomeInterface", u"\u6b22\u8fce\u4f7f\u7528 NeteaseDownloader!", None))
        self.SearchTypeComboBox.setItemText(0, QCoreApplication.translate("HomeInterface", u"\u6b4c\u66f2ID/Url", None))
        self.SearchTypeComboBox.setItemText(1, QCoreApplication.translate("HomeInterface", u"\u6b4c\u5355ID/Url", None))
        self.SearchTypeComboBox.setItemText(2, QCoreApplication.translate("HomeInterface", u"\u641c\u7d22\u6b4c\u66f2", None))
        self.SearchTypeComboBox.setItemText(3, QCoreApplication.translate("HomeInterface", u"\u641c\u7d22\u6b4c\u5355", None))

        self.LoginButton.setText(QCoreApplication.translate("HomeInterface", u"\u767b\u5f55", None))
    # retranslateUi

