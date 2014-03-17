# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/welcome2.ui'
#
# Created: Fri Jul 12 14:18:39 2013
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Welcome2(object):
    def setupUi(self, Welcome2):
        Welcome2.setObjectName(_fromUtf8("Welcome2"))
        Welcome2.resize(444, 150)
        self.centralwidget = QtGui.QWidget(Welcome2)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(5, 3, 431, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.lbl_dir = QtGui.QLabel(self.centralwidget)
        self.lbl_dir.setGeometry(QtCore.QRect(10, 80, 331, 20))
        self.lbl_dir.setObjectName(_fromUtf8("lbl_dir"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(350, 80, 87, 62))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btn_browse = QtGui.QPushButton(self.widget)
        self.btn_browse.setObjectName(_fromUtf8("btn_browse"))
        self.verticalLayout.addWidget(self.btn_browse)
        self.btn2 = QtGui.QPushButton(self.widget)
        self.btn2.setObjectName(_fromUtf8("btn2"))
        self.verticalLayout.addWidget(self.btn2)
        Welcome2.setCentralWidget(self.centralwidget)

        self.retranslateUi(Welcome2)
        QtCore.QMetaObject.connectSlotsByName(Welcome2)

    def retranslateUi(self, Welcome2):
        Welcome2.setWindowTitle(QtGui.QApplication.translate("Welcome2", "Step 1", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("Welcome2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Select a folder where you store all your </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">downloaded files. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">This list of files will be sent to the server :D </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">You can chage this directory later :) </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_dir.setText(QtGui.QApplication.translate("Welcome2", "Select directory", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_browse.setText(QtGui.QApplication.translate("Welcome2", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.btn2.setText(QtGui.QApplication.translate("Welcome2", "Continue", None, QtGui.QApplication.UnicodeUTF8))

