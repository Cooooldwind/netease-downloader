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
from PySide6.QtWidgets import (QApplication, QFrame, QSizePolicy, QWidget)

from qfluentwidgets import (BodyLabel, ImageLabel, StrongBodyLabel)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(400, 64)
        self.coverLabel = ImageLabel(Frame)
        self.coverLabel.setObjectName(u"coverLabel")
        self.coverLabel.setGeometry(QRect(8, 8, 48, 48))
        self.coverLabel.setStyleSheet(u"")
        self.coverLabel.setFrameShape(QFrame.Shape.StyledPanel)
        self.coverLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titleLabel = StrongBodyLabel(Frame)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(64, 12, 328, 16))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.artistLabel = BodyLabel(Frame)
        self.artistLabel.setObjectName(u"artistLabel")
        self.artistLabel.setGeometry(QRect(64, 36, 328, 16))
        self.artistLabel.setStyleSheet(u"")

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.coverLabel.setText(QCoreApplication.translate("Frame", u"Cover", None))
        self.titleLabel.setText(QCoreApplication.translate("Frame", u"Title", None))
        self.artistLabel.setText(QCoreApplication.translate("Frame", u"Artist", None))
    # retranslateUi

