# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_frame.ui'
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
    QSizePolicy, QSpacerItem, QTableWidgetItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (BodyLabel, ComboBox, PrimaryPushButton, ProgressBar,
    PushButton, SearchLineEdit, TableWidget, TitleLabel)

class Ui_Search(object):
    def setupUi(self, Search):
        if not Search.objectName():
            Search.setObjectName(u"Search")
        Search.resize(667, 621)
        self.verticalLayout = QVBoxLayout(Search)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TitleLabel = TitleLabel(Search)
        self.TitleLabel.setObjectName(u"TitleLabel")

        self.verticalLayout.addWidget(self.TitleLabel)

        self.SearchHorizontalLayout = QHBoxLayout()
        self.SearchHorizontalLayout.setObjectName(u"SearchHorizontalLayout")
        self.SearchTypeComboBox = ComboBox(Search)
        self.SearchTypeComboBox.addItem("")
        self.SearchTypeComboBox.addItem("")
        self.SearchTypeComboBox.addItem("")
        self.SearchTypeComboBox.addItem("")
        self.SearchTypeComboBox.setObjectName(u"SearchTypeComboBox")

        self.SearchHorizontalLayout.addWidget(self.SearchTypeComboBox)

        self.SearchKeyLineEdit = SearchLineEdit(Search)
        self.SearchKeyLineEdit.setObjectName(u"SearchKeyLineEdit")

        self.SearchHorizontalLayout.addWidget(self.SearchKeyLineEdit)


        self.verticalLayout.addLayout(self.SearchHorizontalLayout)

        self.SearchResultLabel = BodyLabel(Search)
        self.SearchResultLabel.setObjectName(u"SearchResultLabel")

        self.verticalLayout.addWidget(self.SearchResultLabel)

        self.ProgressBar = ProgressBar(Search)
        self.ProgressBar.setObjectName(u"ProgressBar")
        self.ProgressBar.setValue(24)

        self.verticalLayout.addWidget(self.ProgressBar)

        self.SearchResultTable = TableWidget(Search)
        if (self.SearchResultTable.columnCount() < 1):
            self.SearchResultTable.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.SearchResultTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.SearchResultTable.setObjectName(u"SearchResultTable")
        self.SearchResultTable.horizontalHeader().setVisible(False)
        self.SearchResultTable.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.SearchResultTable)

        self.DownloadHorizontalLayout = QHBoxLayout()
        self.DownloadHorizontalLayout.setObjectName(u"DownloadHorizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.DownloadHorizontalLayout.addItem(self.horizontalSpacer)

        self.DownloadPushButton = PrimaryPushButton(Search)
        self.DownloadPushButton.setObjectName(u"DownloadPushButton")

        self.DownloadHorizontalLayout.addWidget(self.DownloadPushButton)

        self.AddDownloadListPushButton = PushButton(Search)
        self.AddDownloadListPushButton.setObjectName(u"AddDownloadListPushButton")

        self.DownloadHorizontalLayout.addWidget(self.AddDownloadListPushButton)


        self.verticalLayout.addLayout(self.DownloadHorizontalLayout)


        self.retranslateUi(Search)

        QMetaObject.connectSlotsByName(Search)
    # setupUi

    def retranslateUi(self, Search):
        Search.setWindowTitle(QCoreApplication.translate("Search", u"Frame", None))
        self.TitleLabel.setText(QCoreApplication.translate("Search", u"\u641c\u7d22", None))
        self.SearchTypeComboBox.setItemText(0, QCoreApplication.translate("Search", u"\u6b4c\u66f2\u94fe\u63a5/ID", None))
        self.SearchTypeComboBox.setItemText(1, QCoreApplication.translate("Search", u"\u6b4c\u5355\u94fe\u63a5/ID", None))
        self.SearchTypeComboBox.setItemText(2, QCoreApplication.translate("Search", u"\u641c\u7d22\u6b4c\u66f2", None))
        self.SearchTypeComboBox.setItemText(3, QCoreApplication.translate("Search", u"\u641c\u7d22\u6b4c\u5355", None))

        self.SearchResultLabel.setText(QCoreApplication.translate("Search", u"\u8bf7\u70b9\u51fb\u201c\u641c\u7d22\u201d\u3002\u5728\u70b9\u51fb\u201c\u641c\u7d22\u201d\u4e4b\u540e\u4e0d\u4e45\uff0c\u5e95\u4e0b\u7684\u5217\u8868\u5c06\u4f1a\u663e\u793a\u7ed3\u679c\u3002", None))
        ___qtablewidgetitem = self.SearchResultTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Search", u"\u65b0\u5efa\u5217", None));
        self.DownloadPushButton.setText(QCoreApplication.translate("Search", u"\u76f4\u63a5\u4e0b\u8f7d", None))
        self.AddDownloadListPushButton.setText(QCoreApplication.translate("Search", u"\u6dfb\u52a0\u81f3\u4e0b\u8f7d\u5217\u8868", None))
    # retranslateUi

