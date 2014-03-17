# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/list.ui'
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

class Ui_List(object):
    def setupUi(self, List):
        List.setObjectName(_fromUtf8("List"))
        List.resize(332, 398)
        self.centralwidget = QtGui.QWidget(List)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lst_files = QtGui.QListView(self.centralwidget)
        self.lst_files.setGeometry(QtCore.QRect(0, 40, 331, 361))
        self.lst_files.setObjectName(_fromUtf8("lst_files"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(7, 10, 281, 20))
        self.label.setObjectName(_fromUtf8("label"))
        List.setCentralWidget(self.centralwidget)

        self.retranslateUi(List)
        QtCore.QMetaObject.connectSlotsByName(List)

    def retranslateUi(self, List):
        List.setWindowTitle(QtGui.QApplication.translate("List", "File List", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("List", "File names that are on server:", None, QtGui.QApplication.UnicodeUTF8))

