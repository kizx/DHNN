# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hopui.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(628, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.groupBox_3 = QGroupBox(self.splitter)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lcdNumber = QLCDNumber(self.groupBox_3)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setMinimumSize(QSize(0, 80))
        self.lcdNumber.setDigitCount(10)

        self.verticalLayout_3.addWidget(self.lcdNumber)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.start = QPushButton(self.groupBox_3)
        self.start.setObjectName(u"start")
        self.start.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.start)

        self.next = QPushButton(self.groupBox_3)
        self.next.setObjectName(u"next")
        self.next.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.next)

        self.play = QPushButton(self.groupBox_3)
        self.play.setObjectName(u"play")
        self.play.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.play)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.groupBox_2 = QGroupBox(self.groupBox_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        font = QFont()
        font.setFamily(u"Adobe \u9ed1\u4f53 Std R")
        font.setPointSize(28)
        self.lineEdit.setFont(font)

        self.verticalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.groupBox_3)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        font1 = QFont()
        font1.setFamily(u"Adobe \u9ed1\u4f53 Std R")
        font1.setPointSize(26)
        self.textEdit.setFont(font1)

        self.verticalLayout.addWidget(self.textEdit)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.splitter.addWidget(self.groupBox_3)
        self.print = QPlainTextEdit(self.splitter)
        self.print.setObjectName(u"print")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.print.sizePolicy().hasHeightForWidth())
        self.print.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font2.setPointSize(16)
        self.print.setFont(font2)
        self.splitter.addWidget(self.print)

        self.horizontalLayout_2.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 628, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DHNN", None))
        self.groupBox_3.setTitle("")
        self.start.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.next.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0", None))
        self.play.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u5165", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6837\u672c", None))
    # retranslateUi

