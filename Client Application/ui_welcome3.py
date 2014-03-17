# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/welcome3.ui'
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

class Ui_Welcome3(object):
    def setupUi(self, Welcome3):
        Welcome3.setObjectName(_fromUtf8("Welcome3"))
        Welcome3.resize(487, 128)
        self.centralwidget = QtGui.QWidget(Welcome3)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 491, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.btnFb = QtGui.QPushButton(self.centralwidget)
        self.btnFb.setGeometry(QtCore.QRect(110, 50, 261, 61))
        self.btnFb.setObjectName(_fromUtf8("btnFb"))
        Welcome3.setCentralWidget(self.centralwidget)

        self.retranslateUi(Welcome3)
        QtCore.QMetaObject.connectSlotsByName(Welcome3)

    def retranslateUi(self, Welcome3):
        Welcome3.setWindowTitle(QtGui.QApplication.translate("Welcome3", "Step 2", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("Welcome3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\">Login with your</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:600;\"> FaceBook</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt;\"> account to continue</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFb.setText(QtGui.QApplication.translate("Welcome3", "Login with FaceBook", None, QtGui.QApplication.UnicodeUTF8))

