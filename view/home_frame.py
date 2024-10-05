# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_frame.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QListView,
    QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, PasswordLineEdit, PrimaryPushButton, PushButton,
    StrongBodyLabel, TitleLabel)

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(593, 399)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Home.sizePolicy().hasHeightForWidth())
        Home.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(Home)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.WelcomeLabel = TitleLabel(Home)
        self.WelcomeLabel.setObjectName(u"WelcomeLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.WelcomeLabel.sizePolicy().hasHeightForWidth())
        self.WelcomeLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.WelcomeLabel)

        self.InfoLabel = BodyLabel(Home)
        self.InfoLabel.setObjectName(u"InfoLabel")

        self.verticalLayout_2.addWidget(self.InfoLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.CookieLabel = StrongBodyLabel(Home)
        self.CookieLabel.setObjectName(u"CookieLabel")

        self.horizontalLayout.addWidget(self.CookieLabel)

        self.CookieLineEdit = PasswordLineEdit(Home)
        self.CookieLineEdit.setObjectName(u"CookieLineEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.CookieLineEdit.sizePolicy().hasHeightForWidth())
        self.CookieLineEdit.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.CookieLineEdit)

        self.LoginButton = PrimaryPushButton(Home)
        self.LoginButton.setObjectName(u"LoginButton")

        self.horizontalLayout.addWidget(self.LoginButton)

        self.QRCodeLoginButton = PushButton(Home)
        self.QRCodeLoginButton.setObjectName(u"QRCodeLoginButton")

        self.horizontalLayout.addWidget(self.QRCodeLoginButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.ListView = QListView(Home)
        self.ListView.setObjectName(u"ListView")
        self.ListView.setFlow(QListView.Flow.LeftToRight)

        self.verticalLayout_2.addWidget(self.ListView)


        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"Frame", None))
        self.WelcomeLabel.setText(QCoreApplication.translate("Home", u"\u6b22\u8fce\u4f7f\u7528 NeteaseDownloader!", None))
        self.InfoLabel.setText(QCoreApplication.translate("Home", u"\u767b\u5f55\u7f51\u6613\u4e91\u97f3\u4e50\u8d26\u6237\u83b7\u5f97\u66f4\u597d\u7684\u4f53\u9a8c\u2193\u6211\u4eec\u4fdd\u8bc1\u7edd\u4e0d\u6cc4\u9732\u60a8\u7684\u4e2a\u4eba\u4fe1\u606f!", None))
        self.CookieLabel.setText(QCoreApplication.translate("Home", u"\u7528\u6237\u51ed\u8bc1 (MUSIC_U): ", None))
        self.LoginButton.setText(QCoreApplication.translate("Home", u"\u767b\u5f55", None))
        self.QRCodeLoginButton.setText(QCoreApplication.translate("Home", u"\u4e8c\u7ef4\u7801\u767b\u5f55", None))
    # retranslateUi

