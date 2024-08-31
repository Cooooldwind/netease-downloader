# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'music_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_musicWidget(object):
    def setupUi(self, musicWidget):
        if not musicWidget.objectName():
            musicWidget.setObjectName(u"musicWidget")
        musicWidget.resize(400, 64)
        self.coverLabel = QLabel(musicWidget)
        self.coverLabel.setObjectName(u"coverLabel")
        self.coverLabel.setGeometry(QRect(8, 8, 48, 48))
        self.titleLabel = QLabel(musicWidget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(64, 8, 328, 24))
        self.artistLabel = QLabel(musicWidget)
        self.artistLabel.setObjectName(u"artistLabel")
        self.artistLabel.setGeometry(QRect(64, 40, 328, 16))

        self.retranslateUi(musicWidget)

        QMetaObject.connectSlotsByName(musicWidget)
    # setupUi

    def retranslateUi(self, musicWidget):
        musicWidget.setWindowTitle(QCoreApplication.translate("musicWidget", u"Form", None))
        self.coverLabel.setText(QCoreApplication.translate("musicWidget", u"cover", None))
        self.titleLabel.setText(QCoreApplication.translate("musicWidget", u"title", None))
        self.artistLabel.setText(QCoreApplication.translate("musicWidget", u"artist", None))
    # retranslateUi

