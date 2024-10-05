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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CaptionLabel, CardWidget, CheckBox,
    ImageLabel, PrimaryToolButton, StrongBodyLabel)

class Ui_MusicCardFrame(object):
    def setupUi(self, MusicCardFrame):
        if not MusicCardFrame.objectName():
            MusicCardFrame.setObjectName(u"MusicCardFrame")
        MusicCardFrame.resize(600, 80)
        MusicCardFrame.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout = QHBoxLayout(MusicCardFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CoverLabel = ImageLabel(MusicCardFrame)
        self.CoverLabel.setObjectName(u"CoverLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CoverLabel.sizePolicy().hasHeightForWidth())
        self.CoverLabel.setSizePolicy(sizePolicy)
        self.CoverLabel.setMinimumSize(QSize(64, 64))
        self.CoverLabel.setMaximumSize(QSize(64, 64))

        self.horizontalLayout.addWidget(self.CoverLabel)

        self.InfoLayout = QVBoxLayout()
        self.InfoLayout.setSpacing(0)
        self.InfoLayout.setObjectName(u"InfoLayout")
        self.TitleLayout = QHBoxLayout()
        self.TitleLayout.setSpacing(4)
        self.TitleLayout.setObjectName(u"TitleLayout")
        self.Title = StrongBodyLabel(MusicCardFrame)
        self.Title.setObjectName(u"Title")

        self.TitleLayout.addWidget(self.Title)

        self.TransTitle = BodyLabel(MusicCardFrame)
        self.TransTitle.setObjectName(u"TransTitle")

        self.TitleLayout.addWidget(self.TransTitle)

        self.Subtitle = CaptionLabel(MusicCardFrame)
        self.Subtitle.setObjectName(u"Subtitle")

        self.TitleLayout.addWidget(self.Subtitle)

        self.TitleLayoutSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.TitleLayout.addItem(self.TitleLayoutSpacer)


        self.InfoLayout.addLayout(self.TitleLayout)

        self.OtherInfoLayout = QHBoxLayout()
        self.OtherInfoLayout.setSpacing(4)
        self.OtherInfoLayout.setObjectName(u"OtherInfoLayout")
        self.ArtistIcon = BodyLabel(MusicCardFrame)
        self.ArtistIcon.setObjectName(u"ArtistIcon")

        self.OtherInfoLayout.addWidget(self.ArtistIcon)

        self.Artist = BodyLabel(MusicCardFrame)
        self.Artist.setObjectName(u"Artist")

        self.OtherInfoLayout.addWidget(self.Artist)

        self.AlbumIcon = BodyLabel(MusicCardFrame)
        self.AlbumIcon.setObjectName(u"AlbumIcon")

        self.OtherInfoLayout.addWidget(self.AlbumIcon)

        self.Album = BodyLabel(MusicCardFrame)
        self.Album.setObjectName(u"Album")

        self.OtherInfoLayout.addWidget(self.Album)

        self.OtherInfoLayoutSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.OtherInfoLayout.addItem(self.OtherInfoLayoutSpacer)


        self.InfoLayout.addLayout(self.OtherInfoLayout)


        self.horizontalLayout.addLayout(self.InfoLayout)

        self.Spacer = QSpacerItem(16777215, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.Spacer)

        self.CheckBox = CheckBox(MusicCardFrame)
        self.CheckBox.setObjectName(u"CheckBox")

        self.horizontalLayout.addWidget(self.CheckBox)

        self.DownloadButton = PrimaryToolButton(MusicCardFrame)
        self.DownloadButton.setObjectName(u"DownloadButton")

        self.horizontalLayout.addWidget(self.DownloadButton)


        self.retranslateUi(MusicCardFrame)

        QMetaObject.connectSlotsByName(MusicCardFrame)
    # setupUi

    def retranslateUi(self, MusicCardFrame):
        MusicCardFrame.setWindowTitle(QCoreApplication.translate("MusicCardFrame", u"Frame", None))
        self.CoverLabel.setText(QCoreApplication.translate("MusicCardFrame", u"Cover", None))
        self.Title.setText(QCoreApplication.translate("MusicCardFrame", u"Title", None))
        self.TransTitle.setText(QCoreApplication.translate("MusicCardFrame", u"TransTitle", None))
        self.Subtitle.setText(QCoreApplication.translate("MusicCardFrame", u"Subtitle", None))
        self.ArtistIcon.setText("")
        self.Artist.setText(QCoreApplication.translate("MusicCardFrame", u"Artist", None))
        self.AlbumIcon.setText("")
        self.Album.setText(QCoreApplication.translate("MusicCardFrame", u"Album", None))
        self.CheckBox.setText("")
        self.DownloadButton.setText("")
    # retranslateUi

