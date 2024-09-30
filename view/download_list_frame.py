# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'download_list_frame.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QSizePolicy, QTableWidgetItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, PushButton, TableWidget, TitleLabel)

class Ui_DownloadList(object):
    def setupUi(self, DownloadList):
        if not DownloadList.objectName():
            DownloadList.setObjectName(u"DownloadList")
        DownloadList.resize(535, 522)
        self.verticalLayout = QVBoxLayout(DownloadList)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TitleLabel = TitleLabel(DownloadList)
        self.TitleLabel.setObjectName(u"TitleLabel")

        self.verticalLayout.addWidget(self.TitleLabel)

        self.ResultLabel = BodyLabel(DownloadList)
        self.ResultLabel.setObjectName(u"ResultLabel")

        self.verticalLayout.addWidget(self.ResultLabel)

        self.DownloadListTable = TableWidget(DownloadList)
        self.DownloadListTable.setObjectName(u"DownloadListTable")

        self.verticalLayout.addWidget(self.DownloadListTable)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.DownloadButton = PushButton(DownloadList)
        self.DownloadButton.setObjectName(u"DownloadButton")

        self.horizontalLayout.addWidget(self.DownloadButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(DownloadList)

        QMetaObject.connectSlotsByName(DownloadList)
    # setupUi

    def retranslateUi(self, DownloadList):
        DownloadList.setWindowTitle(QCoreApplication.translate("DownloadList", u"Frame", None))
        self.TitleLabel.setText(QCoreApplication.translate("DownloadList", u"\u4e0b\u8f7d\u5217\u8868", None))
        self.ResultLabel.setText(QCoreApplication.translate("DownloadList", u"\u8fd8\u6ca1\u6709\u641c\u7d22\u6b4c\u66f2\u5e76\u6dfb\u52a0\u81f3\u4e0b\u8f7d\u5217\u8868\uff01\u8bf7\u5148\u5207\u6362\u5230\u201c\u641c\u7d22\u201d\u9875\u9762\u641c\u7d22\u70b9\u4ec0\u4e48\u5e76\u6dfb\u52a0\u81f3\u4e0b\u8f7d\u5217\u8868\u3002", None))
        self.DownloadButton.setText(QCoreApplication.translate("DownloadList", u"\u4e0b\u8f7d", None))
    # retranslateUi

