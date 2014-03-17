###############################
#                             #
#  Coded By: Saurabh Joshi    #
#  Date Modified: 8/12/12     #
#                             #
#  File: File List            #
###############################


import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


from ui_list import Ui_List

class FileList (QMainWindow):

    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.parent = parent
        self.setWindowFlags(Qt.Dialog)
        self.ui = Ui_List()
        self.ui.setupUi(self)
        self.lst = self.ui.lst_files
        self.populate()

    def populate(self):
        model = QStandardItemModel()
        
        f = open('settings/Files')
        line = f.readline()
        
        while line:
            size = int(f.readline())

            size = size / 1048576
            
            item = QStandardItem(line + "\nSize:" + str(size) + "MB\n\n")

            line = f.readline()

            
            
            item.setEditable(False)
            model.appendRow(item)
            
        f.close()

        self.lst.setModel(model)



        
