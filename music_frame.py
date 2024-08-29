# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'music_frame.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(400, 80)
        self.coverLabel = QLabel(Frame)
        self.coverLabel.setObjectName(u"coverLabel")
        self.coverLabel.setGeometry(QRect(10, 10, 60, 60))
        self.coverLabel.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid black;")
        self.coverLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titleLabel = QLabel(Frame)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(80, 10, 310, 25))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.aritstLabel = QLabel(Frame)
        self.aritstLabel.setObjectName(u"aritstLabel")
        self.aritstLabel.setGeometry(QRect(80, 55, 310, 15))
        font1 = QFont()
        font1.setPointSize(10)
        self.aritstLabel.setFont(font1)
        self.aritstLabel.setStyleSheet(u"opacity: 0.7;")
        self.subtitleLabel = QLabel(Frame)
        self.subtitleLabel.setObjectName(u"subtitleLabel")
        self.subtitleLabel.setGeometry(QRect(80, 37, 310, 15))
        self.subtitleLabel.setFont(font1)
        self.subtitleLabel.setStyleSheet(u"opacity: 0.7;")

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.coverLabel.setText(QCoreApplication.translate("Frame", u"Cover", None))
        self.titleLabel.setText(QCoreApplication.translate("Frame", u"Title", None))
        self.aritstLabel.setText(QCoreApplication.translate("Frame", u"Artist", None))
        self.subtitleLabel.setText(QCoreApplication.translate("Frame", u"Subtitle", None))
    # retranslateUi

