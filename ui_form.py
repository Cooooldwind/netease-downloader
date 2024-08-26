# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(1100, 600))
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setMinimumSize(QSize(1100, 600))
        self.centralWidget.setMaximumSize(QSize(1100, 600))
        self.mainFrame = QFrame(self.centralWidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setGeometry(QRect(0, 0, 1100, 600))
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setMaximumSize(QSize(1100, 600))
        self.mainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget = QWidget(self.mainFrame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 1101, 601))
        self.mainHorizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.mainHorizontalLayout.setSpacing(5)
        self.mainHorizontalLayout.setObjectName(u"mainHorizontalLayout")
        self.mainHorizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.leftVerticalLayout = QVBoxLayout()
        self.leftVerticalLayout.setSpacing(5)
        self.leftVerticalLayout.setObjectName(u"leftVerticalLayout")
        self.leftVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.welcomeLayout = QVBoxLayout()
        self.welcomeLayout.setObjectName(u"welcomeLayout")
        self.welcomeLayout.setContentsMargins(0, 0, 0, 0)
        self.welcomeLabel = QLabel(self.horizontalLayoutWidget)
        self.welcomeLabel.setObjectName(u"welcomeLabel")

        self.welcomeLayout.addWidget(self.welcomeLabel)


        self.leftVerticalLayout.addLayout(self.welcomeLayout)

        self.searchLayout = QHBoxLayout()
        self.searchLayout.setSpacing(5)
        self.searchLayout.setObjectName(u"searchLayout")
        self.searchLayout.setContentsMargins(0, 0, 0, 0)
        self.searchComboBox = QComboBox(self.horizontalLayoutWidget)
        self.searchComboBox.addItem("")
        self.searchComboBox.addItem("")
        self.searchComboBox.addItem("")
        self.searchComboBox.addItem("")
        self.searchComboBox.setObjectName(u"searchComboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.searchComboBox.sizePolicy().hasHeightForWidth())
        self.searchComboBox.setSizePolicy(sizePolicy1)

        self.searchLayout.addWidget(self.searchComboBox)

        self.searchLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        sizePolicy1.setHeightForWidth(self.searchLineEdit.sizePolicy().hasHeightForWidth())
        self.searchLineEdit.setSizePolicy(sizePolicy1)

        self.searchLayout.addWidget(self.searchLineEdit)

        self.searchButton = QPushButton(self.horizontalLayoutWidget)
        self.searchButton.setObjectName(u"searchButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy2)

        self.searchLayout.addWidget(self.searchButton)


        self.leftVerticalLayout.addLayout(self.searchLayout)

        self.resultTableWidget = QTableWidget(self.horizontalLayoutWidget)
        if (self.resultTableWidget.columnCount() < 4):
            self.resultTableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.resultTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.resultTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.resultTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.resultTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.resultTableWidget.setObjectName(u"resultTableWidget")

        self.leftVerticalLayout.addWidget(self.resultTableWidget)

        self.selectionLayout = QHBoxLayout()
        self.selectionLayout.setSpacing(5)
        self.selectionLayout.setObjectName(u"selectionLayout")
        self.selectionLayout.setContentsMargins(0, 0, 0, 0)
        self.selectionLabel = QLabel(self.horizontalLayoutWidget)
        self.selectionLabel.setObjectName(u"selectionLabel")

        self.selectionLayout.addWidget(self.selectionLabel)

        self.selectionLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.selectionLineEdit.setObjectName(u"selectionLineEdit")
        self.selectionLineEdit.setMinimumSize(QSize(0, 0))

        self.selectionLayout.addWidget(self.selectionLineEdit)

        self.selectAllButton = QPushButton(self.horizontalLayoutWidget)
        self.selectAllButton.setObjectName(u"selectAllButton")

        self.selectionLayout.addWidget(self.selectAllButton)

        self.addToDownloadListButton = QPushButton(self.horizontalLayoutWidget)
        self.addToDownloadListButton.setObjectName(u"addToDownloadListButton")

        self.selectionLayout.addWidget(self.addToDownloadListButton)


        self.leftVerticalLayout.addLayout(self.selectionLayout)


        self.mainHorizontalLayout.addLayout(self.leftVerticalLayout)

        self.rightVerticalLayout = QVBoxLayout()
        self.rightVerticalLayout.setObjectName(u"rightVerticalLayout")
        self.rightVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.loginLayout = QHBoxLayout()
        self.loginLayout.setSpacing(5)
        self.loginLayout.setObjectName(u"loginLayout")
        self.loginLayout.setContentsMargins(0, 0, 0, 0)
        self.loginLabel = QLabel(self.horizontalLayoutWidget)
        self.loginLabel.setObjectName(u"loginLabel")

        self.loginLayout.addWidget(self.loginLabel)

        self.loginLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.loginLineEdit.setObjectName(u"loginLineEdit")

        self.loginLayout.addWidget(self.loginLineEdit)

        self.loginButton = QPushButton(self.horizontalLayoutWidget)
        self.loginButton.setObjectName(u"loginButton")

        self.loginLayout.addWidget(self.loginButton)

        self.browserLoginButton = QPushButton(self.horizontalLayoutWidget)
        self.browserLoginButton.setObjectName(u"browserLoginButton")

        self.loginLayout.addWidget(self.browserLoginButton)


        self.rightVerticalLayout.addLayout(self.loginLayout)

        self.downloadListTitleLayout = QVBoxLayout()
        self.downloadListTitleLayout.setObjectName(u"downloadListTitleLayout")
        self.downloadListTitleLayout.setContentsMargins(0, 0, 0, 0)
        self.downloadListLabel = QLabel(self.horizontalLayoutWidget)
        self.downloadListLabel.setObjectName(u"downloadListLabel")

        self.downloadListTitleLayout.addWidget(self.downloadListLabel)


        self.rightVerticalLayout.addLayout(self.downloadListTitleLayout)

        self.downloadListTableWidget = QTableWidget(self.horizontalLayoutWidget)
        if (self.downloadListTableWidget.columnCount() < 4):
            self.downloadListTableWidget.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.downloadListTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.downloadListTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.downloadListTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.downloadListTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.downloadListTableWidget.setObjectName(u"downloadListTableWidget")

        self.rightVerticalLayout.addWidget(self.downloadListTableWidget)

        self.downloadSettingsLayout = QVBoxLayout()
        self.downloadSettingsLayout.setObjectName(u"downloadSettingsLayout")
        self.downloadSettingsLayout.setContentsMargins(0, 0, 0, 0)
        self.qualityLayout = QHBoxLayout()
        self.qualityLayout.setSpacing(5)
        self.qualityLayout.setObjectName(u"qualityLayout")
        self.qualityLayout.setContentsMargins(5, 5, 5, 5)
        self.qualityLabel = QLabel(self.horizontalLayoutWidget)
        self.qualityLabel.setObjectName(u"qualityLabel")

        self.qualityLayout.addWidget(self.qualityLabel)

        self.standardRadioButton = QRadioButton(self.horizontalLayoutWidget)
        self.standardRadioButton.setObjectName(u"standardRadioButton")

        self.qualityLayout.addWidget(self.standardRadioButton)

        self.higherRadioButton = QRadioButton(self.horizontalLayoutWidget)
        self.higherRadioButton.setObjectName(u"higherRadioButton")

        self.qualityLayout.addWidget(self.higherRadioButton)

        self.exhighRadioButton = QRadioButton(self.horizontalLayoutWidget)
        self.exhighRadioButton.setObjectName(u"exhighRadioButton")

        self.qualityLayout.addWidget(self.exhighRadioButton)

        self.losslessRadioButton = QRadioButton(self.horizontalLayoutWidget)
        self.losslessRadioButton.setObjectName(u"losslessRadioButton")

        self.qualityLayout.addWidget(self.losslessRadioButton)


        self.downloadSettingsLayout.addLayout(self.qualityLayout)

        self.filePropertiesLayout = QHBoxLayout()
        self.filePropertiesLayout.setSpacing(5)
        self.filePropertiesLayout.setObjectName(u"filePropertiesLayout")
        self.filePropertiesLayout.setContentsMargins(5, 5, 5, 5)
        self.filePropertiesLabel = QLabel(self.horizontalLayoutWidget)
        self.filePropertiesLabel.setObjectName(u"filePropertiesLabel")

        self.filePropertiesLayout.addWidget(self.filePropertiesLabel)

        self.basicInfoCheckBox = QCheckBox(self.horizontalLayoutWidget)
        self.basicInfoCheckBox.setObjectName(u"basicInfoCheckBox")

        self.filePropertiesLayout.addWidget(self.basicInfoCheckBox)

        self.albumCoverCheckBox = QCheckBox(self.horizontalLayoutWidget)
        self.albumCoverCheckBox.setObjectName(u"albumCoverCheckBox")

        self.filePropertiesLayout.addWidget(self.albumCoverCheckBox)

        self.lyricsDownloadCheckBox = QCheckBox(self.horizontalLayoutWidget)
        self.lyricsDownloadCheckBox.setObjectName(u"lyricsDownloadCheckBox")

        self.filePropertiesLayout.addWidget(self.lyricsDownloadCheckBox)

        self.lyricsAddCheckBox = QCheckBox(self.horizontalLayoutWidget)
        self.lyricsAddCheckBox.setObjectName(u"lyricsAddCheckBox")

        self.filePropertiesLayout.addWidget(self.lyricsAddCheckBox)


        self.downloadSettingsLayout.addLayout(self.filePropertiesLayout)

        self.lyricsEncodingLayout = QHBoxLayout()
        self.lyricsEncodingLayout.setSpacing(5)
        self.lyricsEncodingLayout.setObjectName(u"lyricsEncodingLayout")
        self.lyricsEncodingLayout.setContentsMargins(5, 5, 5, 5)
        self.lyricsEncodingLabel = QLabel(self.horizontalLayoutWidget)
        self.lyricsEncodingLabel.setObjectName(u"lyricsEncodingLabel")

        self.lyricsEncodingLayout.addWidget(self.lyricsEncodingLabel)

        self.lyricsEncodingComboBox = QComboBox(self.horizontalLayoutWidget)
        self.lyricsEncodingComboBox.addItem("")
        self.lyricsEncodingComboBox.addItem("")
        self.lyricsEncodingComboBox.addItem("")
        self.lyricsEncodingComboBox.setObjectName(u"lyricsEncodingComboBox")

        self.lyricsEncodingLayout.addWidget(self.lyricsEncodingComboBox)

        self.albumCoverSizeLabel = QLabel(self.horizontalLayoutWidget)
        self.albumCoverSizeLabel.setObjectName(u"albumCoverSizeLabel")

        self.lyricsEncodingLayout.addWidget(self.albumCoverSizeLabel)

        self.albumCoverSizeSpinBox = QSpinBox(self.horizontalLayoutWidget)
        self.albumCoverSizeSpinBox.setObjectName(u"albumCoverSizeSpinBox")
        self.albumCoverSizeSpinBox.setMinimum(100)
        self.albumCoverSizeSpinBox.setMaximum(2000)
        self.albumCoverSizeSpinBox.setSingleStep(100)

        self.lyricsEncodingLayout.addWidget(self.albumCoverSizeSpinBox)

        self.fileSaveLocationLabel = QLabel(self.horizontalLayoutWidget)
        self.fileSaveLocationLabel.setObjectName(u"fileSaveLocationLabel")

        self.lyricsEncodingLayout.addWidget(self.fileSaveLocationLabel)

        self.fileSaveLocationLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.fileSaveLocationLineEdit.setObjectName(u"fileSaveLocationLineEdit")

        self.lyricsEncodingLayout.addWidget(self.fileSaveLocationLineEdit)

        self.fileSaveLocationToolButton = QToolButton(self.horizontalLayoutWidget)
        self.fileSaveLocationToolButton.setObjectName(u"fileSaveLocationToolButton")

        self.lyricsEncodingLayout.addWidget(self.fileSaveLocationToolButton)

        self.filenameFormatLabel = QLabel(self.horizontalLayoutWidget)
        self.filenameFormatLabel.setObjectName(u"filenameFormatLabel")

        self.lyricsEncodingLayout.addWidget(self.filenameFormatLabel)

        self.filenameFormatLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.filenameFormatLineEdit.setObjectName(u"filenameFormatLineEdit")

        self.lyricsEncodingLayout.addWidget(self.filenameFormatLineEdit)


        self.downloadSettingsLayout.addLayout(self.lyricsEncodingLayout)


        self.rightVerticalLayout.addLayout(self.downloadSettingsLayout)

        self.downloadingLayout = QHBoxLayout()
        self.downloadingLayout.setObjectName(u"downloadingLayout")
        self.downloadingLayout.setContentsMargins(0, 0, 0, -1)
        self.downloadListProgressLayout = QVBoxLayout()
        self.downloadListProgressLayout.setObjectName(u"downloadListProgressLayout")
        self.downloadListProgressLayout.setContentsMargins(0, 0, 0, 0)
        self.downloadListProgressInnerLayout = QHBoxLayout()
        self.downloadListProgressInnerLayout.setObjectName(u"downloadListProgressInnerLayout")
        self.downloadListProgressLabel = QLabel(self.horizontalLayoutWidget)
        self.downloadListProgressLabel.setObjectName(u"downloadListProgressLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.downloadListProgressLabel.sizePolicy().hasHeightForWidth())
        self.downloadListProgressLabel.setSizePolicy(sizePolicy3)

        self.downloadListProgressInnerLayout.addWidget(self.downloadListProgressLabel)

        self.downloadListProgressBar = QProgressBar(self.horizontalLayoutWidget)
        self.downloadListProgressBar.setObjectName(u"downloadListProgressBar")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.downloadListProgressBar.sizePolicy().hasHeightForWidth())
        self.downloadListProgressBar.setSizePolicy(sizePolicy4)
        self.downloadListProgressBar.setValue(0)

        self.downloadListProgressInnerLayout.addWidget(self.downloadListProgressBar)


        self.downloadListProgressLayout.addLayout(self.downloadListProgressInnerLayout)

        self.currentSongProgressLayout = QHBoxLayout()
        self.currentSongProgressLayout.setObjectName(u"currentSongProgressLayout")
        self.currentSongProgressLayout.setContentsMargins(0, 0, 0, 0)
        self.currentSongProgressLabel = QLabel(self.horizontalLayoutWidget)
        self.currentSongProgressLabel.setObjectName(u"currentSongProgressLabel")
        sizePolicy3.setHeightForWidth(self.currentSongProgressLabel.sizePolicy().hasHeightForWidth())
        self.currentSongProgressLabel.setSizePolicy(sizePolicy3)

        self.currentSongProgressLayout.addWidget(self.currentSongProgressLabel)

        self.currentSongProgressBar = QProgressBar(self.horizontalLayoutWidget)
        self.currentSongProgressBar.setObjectName(u"currentSongProgressBar")
        sizePolicy4.setHeightForWidth(self.currentSongProgressBar.sizePolicy().hasHeightForWidth())
        self.currentSongProgressBar.setSizePolicy(sizePolicy4)
        self.currentSongProgressBar.setValue(0)

        self.currentSongProgressLayout.addWidget(self.currentSongProgressBar)


        self.downloadListProgressLayout.addLayout(self.currentSongProgressLayout)


        self.downloadingLayout.addLayout(self.downloadListProgressLayout)

        self.startDownloadButton = QPushButton(self.horizontalLayoutWidget)
        self.startDownloadButton.setObjectName(u"startDownloadButton")
        sizePolicy3.setHeightForWidth(self.startDownloadButton.sizePolicy().hasHeightForWidth())
        self.startDownloadButton.setSizePolicy(sizePolicy3)

        self.downloadingLayout.addWidget(self.startDownloadButton)


        self.rightVerticalLayout.addLayout(self.downloadingLayout)


        self.mainHorizontalLayout.addLayout(self.rightVerticalLayout)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NeteaseDownloader", None))
        self.welcomeLabel.setText(QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\u4f7f\u7528 NeteaseDownloader\uff01Copyright@CooooldWind", None))
        self.searchComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6b4c\u66f2 ID/Url", None))
        self.searchComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6b4c\u5355 ID/Url", None))
        self.searchComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u6b4c\u66f2", None))
        self.searchComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u6b4c\u5355", None))

        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        ___qtablewidgetitem = self.resultTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.resultTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u6807\u9898", None));
        ___qtablewidgetitem2 = self.resultTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u624b", None));
        ___qtablewidgetitem3 = self.resultTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u4e13\u8f91", None));
        self.selectionLabel.setText(QCoreApplication.translate("MainWindow", u"\u591a\u9879\u9009\u62e9", None))
#if QT_CONFIG(tooltip)
        self.selectionLineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.selectionLineEdit.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.selectAllButton.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u52fe\u9009", None))
        self.addToDownloadListButton.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5230\u4e0b\u8f7d\u5217\u8868", None))
        self.loginLabel.setText(QCoreApplication.translate("MainWindow", u"\u60a8\u5c1a\u672a\u767b\u5f55\uff01", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.browserLoginButton.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u5668\u6a21\u62df\u767b\u5f55", None))
        self.downloadListLabel.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u5217\u8868", None))
        ___qtablewidgetitem4 = self.downloadListTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem5 = self.downloadListTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u6807\u9898", None));
        ___qtablewidgetitem6 = self.downloadListTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u624b", None));
        ___qtablewidgetitem7 = self.downloadListTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u4e13\u8f91", None));
        self.qualityLabel.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u8d28", None))
        self.standardRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u6807\u51c6(standard)", None))
        self.higherRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u8f83\u9ad8(higher)", None))
        self.exhighRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u6781\u9ad8(exhigh)", None))
        self.losslessRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u635f(lossless)", None))
        self.filePropertiesLabel.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5c5e\u6027", None))
        self.basicInfoCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u672c\u4fe1\u606f\u6dfb\u52a0", None))
        self.albumCoverCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u4e13\u8f91\u5c01\u9762\u6dfb\u52a0", None))
        self.lyricsDownloadCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u8bcd\u4e0b\u8f7d", None))
        self.lyricsAddCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u8bcd\u6dfb\u52a0", None))
        self.lyricsEncodingLabel.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u8bcd\u7f16\u7801\u65b9\u5f0f", None))
        self.lyricsEncodingComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"GBK", None))
        self.lyricsEncodingComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"UTF-8", None))
        self.lyricsEncodingComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Unicode", None))

        self.albumCoverSizeLabel.setText(QCoreApplication.translate("MainWindow", u"\u4e13\u8f91\u5c01\u9762\u5927\u5c0f", None))
        self.fileSaveLocationLabel.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u4fdd\u5b58\u4f4d\u7f6e", None))
        self.fileSaveLocationToolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.filenameFormatLabel.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u683c\u5f0f", None))
        self.downloadListProgressLabel.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u5217\u8868\u7684\u4e0b\u8f7d\u8fdb\u5ea6", None))
        self.currentSongProgressLabel.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u6b4c\u66f2\u7684\u4e0b\u8f7d\u8fdb\u5ea6", None))
        self.startDownloadButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u4e0b\u8f7d\uff01", None))
    # retranslateUi

