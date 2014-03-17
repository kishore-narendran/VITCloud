# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/welcome1.ui'
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

class Ui_Welcome1(object):
    def setupUi(self, Welcome1):
        Welcome1.setObjectName(_fromUtf8("Welcome1"))
        Welcome1.resize(443, 137)
        Welcome1.setMinimumSize(QtCore.QSize(443, 119))
        self.centralwidget = QtGui.QWidget(Welcome1)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 0, 115, 28))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 431, 61))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.btn1 = QtGui.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(350, 100, 85, 27))
        self.btn1.setObjectName(_fromUtf8("btn1"))
        Welcome1.setCentralWidget(self.centralwidget)

        self.retranslateUi(Welcome1)
        QtCore.QMetaObject.connectSlotsByName(Welcome1)

    def retranslateUi(self, Welcome1):
        Welcome1.setWindowTitle(QtGui.QApplication.translate("Welcome1", "VITCloud Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Welcome1", "VITCloud", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("Welcome1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Welcome to VIT Cloud ! :) </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">This setup will only be required </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">once</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"> and we will </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\">never</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"> bother you again.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btn1.setText(QtGui.QApplication.translate("Welcome1", "Continue", None, QtGui.QApplication.UnicodeUTF8))

