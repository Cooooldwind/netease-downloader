# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'music_card_frame.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CheckBox, ImageLabel, StrongBodyLabel)

class Ui_MusicCardFrame(object):
    def setupUi(self, MusicCardFrame):
        if not MusicCardFrame.objectName():
            MusicCardFrame.setObjectName(u"MusicCardFrame")
        MusicCardFrame.resize(554, 64)
        self.horizontalLayout = QHBoxLayout(MusicCardFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CoverLabel = ImageLabel(MusicCardFrame)
        self.CoverLabel.setObjectName(u"CoverLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CoverLabel.sizePolicy().hasHeightForWidth())
        self.CoverLabel.setSizePolicy(sizePolicy)
        self.CoverLabel.setMinimumSize(QSize(48, 48))
        self.CoverLabel.setMaximumSize(QSize(48, 48))

        self.horizontalLayout.addWidget(self.CoverLabel)

        self.Layout = QVBoxLayout()
        self.Layout.setObjectName(u"Layout")
        self.Title = StrongBodyLabel(MusicCardFrame)
        self.Title.setObjectName(u"Title")

        self.Layout.addWidget(self.Title)

        self.Artist = BodyLabel(MusicCardFrame)
        self.Artist.setObjectName(u"Artist")

        self.Layout.addWidget(self.Artist)


        self.horizontalLayout.addLayout(self.Layout)

        self.Spacer = QSpacerItem(325, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.Spacer)

        self.CheckBox = CheckBox(MusicCardFrame)
        self.CheckBox.setObjectName(u"CheckBox")

        self.horizontalLayout.addWidget(self.CheckBox)


        self.retranslateUi(MusicCardFrame)

        QMetaObject.connectSlotsByName(MusicCardFrame)
    # setupUi

    def retranslateUi(self, MusicCardFrame):
        MusicCardFrame.setWindowTitle(QCoreApplication.translate("MusicCardFrame", u"Frame", None))
        self.CoverLabel.setText(QCoreApplication.translate("MusicCardFrame", u"Cover", None))
        self.Title.setText(QCoreApplication.translate("MusicCardFrame", u"TextLabel", None))
        self.Artist.setText(QCoreApplication.translate("MusicCardFrame", u"TextLabel", None))
        self.CheckBox.setText("")
    # retranslateUi

