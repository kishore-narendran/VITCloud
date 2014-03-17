# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created: Fri Jul 12 14:18:38 2013
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName(_fromUtf8("Main"))
        Main.resize(495, 180)
        Main.setMinimumSize(QtCore.QSize(408, 150))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../resources/icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(Main)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 50, 171, 19))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lbl_status = QtGui.QLabel(self.layoutWidget)
        self.lbl_status.setObjectName(_fromUtf8("lbl_status"))
        self.horizontalLayout_2.addWidget(self.lbl_status)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(12, 22, 481, 17))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label = QtGui.QLabel(self.splitter)
        self.label.setObjectName(_fromUtf8("label"))
        self.lbl_dir = QtGui.QLabel(self.splitter)
        self.lbl_dir.setObjectName(_fromUtf8("lbl_dir"))
        self.btn_browse = QtGui.QPushButton(self.splitter)
        self.btn_browse.setObjectName(_fromUtf8("btn_browse"))
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(170, 150, 317, 29))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_website = QtGui.QPushButton(self.layoutWidget1)
        self.btn_website.setObjectName(_fromUtf8("btn_website"))
        self.horizontalLayout.addWidget(self.btn_website)
        self.btn_files = QtGui.QPushButton(self.layoutWidget1)
        self.btn_files.setObjectName(_fromUtf8("btn_files"))
        self.horizontalLayout.addWidget(self.btn_files)
        self.btn_save = QtGui.QPushButton(self.layoutWidget1)
        self.btn_save.setObjectName(_fromUtf8("btn_save"))
        self.horizontalLayout.addWidget(self.btn_save)
        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 80, 226, 52))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(self.layoutWidget2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.txt_room = QtGui.QTextEdit(self.layoutWidget2)
        self.txt_room.setMaximumSize(QtCore.QSize(171, 21))
        self.txt_room.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_room.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.txt_room.setObjectName(_fromUtf8("txt_room"))
        self.verticalLayout_2.addWidget(self.txt_room)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        Main.setWindowTitle(QtGui.QApplication.translate("Main", "VITCloud", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Main", "Status:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_status.setText(QtGui.QApplication.translate("Main", "Idle", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Main", "Current Directory:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_dir.setText(QtGui.QApplication.translate("Main", "Choose your root directory", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_browse.setText(QtGui.QApplication.translate("Main", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_website.setText(QtGui.QApplication.translate("Main", "Open Website", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_files.setText(QtGui.QApplication.translate("Main", "Show Files", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_save.setText(QtGui.QApplication.translate("Main", "Save and Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Main", "ID: ", None, QtGui.QApplication.UnicodeUTF8))

