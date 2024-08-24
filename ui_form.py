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
        MainWindow.resize(1000, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1000, 600))
        self.centralwidget.setMaximumSize(QSize(1000, 600))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1000, 600))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 1001, 601))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.horizontalLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.lineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tableWidget = QTableWidget(self.horizontalLayoutWidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEdit_2 = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.lineEdit_2)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_3.addWidget(self.pushButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_5.addWidget(self.lineEdit_3)

        self.pushButton_4 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_5.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_5.addWidget(self.pushButton_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.tableWidget_2 = QTableWidget(self.horizontalLayoutWidget)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_2.addWidget(self.tableWidget_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.radioButton = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout_4.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout_4.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_4.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_4.addWidget(self.radioButton_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.checkBox = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_6.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_6.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_6.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.horizontalLayout_6.addWidget(self.checkBox_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.label_7 = QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.comboBox_2 = QComboBox(self.horizontalLayoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_8.addWidget(self.comboBox_2)

        self.label_8 = QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.spinBox = QSpinBox(self.horizontalLayoutWidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(100)
        self.spinBox.setMaximum(2000)
        self.spinBox.setSingleStep(100)

        self.horizontalLayout_8.addWidget(self.spinBox)

        self.label_9 = QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.lineEdit_4 = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_8.addWidget(self.lineEdit_4)

        self.toolButton = QToolButton(self.horizontalLayoutWidget)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_8.addWidget(self.toolButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)

        self.horizontalLayout_10.addWidget(self.label_10)

        self.progressBar = QProgressBar(self.horizontalLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy3)
        self.progressBar.setValue(0)

        self.horizontalLayout_10.addWidget(self.progressBar)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.label_11)

        self.progressBar_2 = QProgressBar(self.horizontalLayoutWidget)
        self.progressBar_2.setObjectName(u"progressBar_2")
        sizePolicy3.setHeightForWidth(self.progressBar_2.sizePolicy().hasHeightForWidth())
        self.progressBar_2.setSizePolicy(sizePolicy3)
        self.progressBar_2.setValue(0)

        self.horizontalLayout_11.addWidget(self.progressBar_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_9.addLayout(self.verticalLayout_6)

        self.pushButton_6 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy2.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy2)

        self.horizontalLayout_9.addWidget(self.pushButton_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NeteaseDownloader", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\u4f7f\u7528 NeteaseDownloader\uff01Copyright@CooooldWind", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6b4c\u66f2ID/Url", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6b4c\u5355ID/Url", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u6b4c\u66f2", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u6b4c\u5355", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u6807\u9898", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u624b", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u4e13\u8f91", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u591a\u9879\u9009\u62e9", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(accessibility)
        self.lineEdit_2.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u52fe\u9009", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5230\u4e0b\u8f7d\u5217\u8868", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u60a8\u5c1a\u672a\u767b\u5f55\uff01", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u5668\u6a21\u62df\u767b\u5f55", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u5217\u8868", None))
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u6807\u9898", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u624b", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u4e13\u8f91", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u8d28", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u6807\u51c6(standard)", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u8f83\u9ad8(higher)", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6781\u9ad8(exhigh)", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u635f(lossless)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5c5e\u6027", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u672c\u4fe1\u606f\u6dfb\u52a0", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u4e13\u8f91\u5c01\u9762\u6dfb\u52a0", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u8bcd\u4e0b\u8f7d", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u8bcd\u6dfb\u52a0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u8bcd\u7f16\u7801\u65b9\u5f0f", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"GBK", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"UTF-8", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Unicode", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u4e13\u8f91\u5c01\u9762\u5927\u5c0f", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u4fdd\u5b58\u4f4d\u7f6e", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u5217\u8868\u7684\u4e0b\u8f7d\u8fdb\u5ea6", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u6b4c\u66f2\u7684\u4e0b\u8f7d\u8fdb\u5ea6", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u4e0b\u8f7d\uff01", None))
    # retranslateUi

