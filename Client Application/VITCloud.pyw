############################
#                                                         #
#  Coded By: Saurabh Joshi                    #
#  Date Modified: 28/05/13                    #
#                                                        #
#  File: Main Screen                              #
###########################

import sys
from PyQt4 import QtCore, QtGui

#Include required folders (New trick I learned :P)
sys.path.insert(0,'ui')
sys.path.insert(0,'resources')
sys.path.insert(0,'lib')

IS_WORKING = 0

#Import UI Files
from ui_main import Ui_Main
import webbrowser
from ui_welcome1 import Ui_Welcome1
from ui_welcome2 import Ui_Welcome2
from ui_welcome3 import Ui_Welcome3

#Import non-ui components
from vals import Lib
from list import FileList
from scanner import WorkThread
from ticker import *
from update import Updater

#Import Values
Vals = Lib()


class Main(QtGui.QMainWindow):

    #INITIALIZE WINDOW
    def __init__(self , parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('resources/icon.ico'))  
        self.count = 0
        self.boo = 0

        #Start the scanner onStart
        self.workThread = WorkThread(Vals.getRoot() , Vals.getRoom() , Vals.getBlock())
        self.connect(self.workThread, QtCore.SIGNAL("finished()"), self.scDone)
        self.connect(self.workThread, QtCore.SIGNAL("scanned(QString)"), self.state)
        self.ui.btn_save.setEnabled(False)

        #Define variable to check if background worker is running
        global IS_WORKING
        IS_WORKING = 1
        self.workThread.start()

        #Check for application updates
        self.upd = Updater()
        self.connect(self.upd, QtCore.SIGNAL("update(QString)"), self.update)
        self.upd.start()

        #UI Tweaks
        self.center()
        self.lblDir = self.ui.lbl_dir
        self.txtRoom = self.ui.txt_room
        #self.txtBlock = self.ui.txt_block
        self.setValues()
        
        #Connect Buttons with functions
        self.ui.btn_browse.clicked.connect(self.browse)
        self.ui.btn_website.clicked.connect(self.opnweb)
        self.ui.btn_save.clicked.connect(self.save)
        self.ui.btn_files.clicked.connect(self.shwFiles)
        return
    
    
    #Get Data from worker
    def state(self,dat):
        if (dat == "DONE"):
            self.boo = 1
            
        if (self.boo == 0):
            if (self.count > 100):
                self.count = 1
            if ((self.count % 10) == 0 ):
                self.ui.lbl_status.setText(dat)
            self.count  += 1
        else:
            self.ui.lbl_status.setText(dat)
        return
    


    #Override the close button in case worker is working
    def closeEvent(self, event):
        if (IS_WORKING == 1):
            quit_msg = "Please wait till the upload finishes"
            reply = QtGui.QMessageBox.question(self, 'Message', quit_msg, QtGui.QMessageBox.AcceptRole)
            event.ignore()
        else:
            event.accept()
        return

    #Show update message
    def update(self):
        quit_msg = "A new version of VITCloud is available!"
        reply = QtGui.QMessageBox.question(self, 'Message', quit_msg, QtGui.QMessageBox.AcceptRole)

    #Show list of files
    def shwFiles(self):
        self.l = FileList(self)
        self.l.show()
        return

    
    
    #Called when worker is finished
    def scDone(self):
        global IS_WORKING
        IS_WORKING = 0
        self.boo = 0
        self.Notify("File list synced")
        self.ui.lbl_status.setText("Idle")
        self.ui.btn_save.setEnabled(True)
                      

    def end(self):
        sys.exit()
        return
    def opnweb(self):
        webbrowser.open("https://vitcloud-biocross.rhcloud.com/search?thesearchbox=" , 2 , True)
        

    def browse(self):
        try:
           root = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
           if (root==''):
               return
           self.lblDir.setText(root)
        except:
            pass
        return

    def Notify(self,msg):
        try:
            Vals.saveSettings(str(self.lblDir.text()),str(self.txtBlock.toPlainText()),str(self.txtRoom.toPlainText()))
            self.setValues()
            self.notification = Notification(msg,self)
            #self.notification.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Dialog)
            self.notification.show()
        except:
            pass
        

    def save(self):
        try:
            Vals.saveSettings(str(self.lblDir.text()),"BLOCK",str(self.txtRoom.toPlainText()))
            #self.setValues()
            self.Notify("Settings Saved!")

            #Start the scanner after save
            global IS_WORKING
            IS_WORKING = 1
            self.ui.btn_save.setEnabled(False)
            self.workThread = WorkThread(Vals.getRoot() , Vals.getRoom() , Vals.getBlock(),1)
            self.connect(self.workThread, QtCore.SIGNAL("finished()"), self.scDone)
            self.connect(self.workThread, QtCore.SIGNAL("scanned(QString)"), self.state)
            self.workThread.start()
        except:
            pass

    #PUT THE SCREEN IN CENTER
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setValues(self):
        self.lblDir.setText(Vals.getRoot())
        self.txtRoom.setText(Vals.getRoom())
        self.txtRoom.setEnabled(False) 
        #self.txtBlock.setText(Vals.getBlock())

class FirstRun(QtGui.QMainWindow):

    #INITIALIZE WINDOW
    def __init__(self , parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Welcome1()
        self.ROOT = "NA"
        self.ROOM = "NA"
        self.BLOCK = "NA"
        self.center()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('resources/icon.ico'))

        self.ui.btn1.clicked.connect(self.step1)

    def step1(self):
        try:
            self.ui = Ui_Welcome2()
            self.ui.setupUi(self)
            self.ui.btn_browse.clicked.connect(self.browse)
            self.ui.btn2.clicked.connect(self.step2)
        except:
            self.msgBox("Error occured please check value!")
            

    def step2(self):
        self.ui = Ui_Welcome3()
        self.ui.setupUi(self)
        self.ui.btnFb.clicked.connect(self.getTok)


    def openBrowser(self,tok):
        if (tok == "error"):
            print "Error!"
            self.msgBox("Error occured! Please try again.")
            self.ui.btnFb.setEnabled(True)
            self.ui.btnFb.setText("Login with Facebook")

        else:
            print tok
            url = "http://vitcloud-collegecode.rhcloud.com/challenge?token=" + tok
            webbrowser.open(url)
            self.tick = Ticker(tok)
            self.connect(self.tick, QtCore.SIGNAL("ticked(QString)"), self.complt)
            self.tick.start()

    def complt(self,dat):
        if (dat == "waiting"):
            print str(dat)
        elif (dat == "error"):
            print "Error!"
            self.msgBox("Error occured! Please try again.")
            self.ui.btnFb.setEnabled(True)
            self.ui.btnFb.setText("Login with Facebook")
            
        else:
            print "Verified User!"
            self.ROOM = str(dat)
            self.BLOCK = "BLOCK"
            Vals.saveSettings(self.ROOT,self.BLOCK,self.ROOM)
            self.myapp = Main()
            self.myapp.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
            self.myapp.show()
            self.hide()

    def getTok(self):
        self.ui.btnFb.setEnabled(False)
        self.ui.btnFb.setText("Waiting for permission...")
        self.t = TempTok()
        self.connect(self.t, QtCore.SIGNAL("token(QString)"), self.openBrowser)
        self.t.start()
        
                   

    def msgBox(self,msg):
        reply = QtGui.QMessageBox.question(self, 'Info', msg, QtGui.QMessageBox.AcceptRole)
        return

    def browse(self):
        try:
           root = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
           self.ROOT = root
           self.ui.lbl_dir.setText(self.ROOT)
           if (root == ''):
               raise NameError("Err")
        except:
            self.msgBox("Error occured please check value!")
        return
        
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
    


        
        

#SHOW ON THE SCREEN
def startIt():
    if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        myapp = Main()
        myapp.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        myapp.show()
        sys.exit(app.exec_())

#FIRST RUN
def firstRun():
    if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        myapp = FirstRun()
        #myapp.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        myapp.show()
        sys.exit(app.exec_())




    
#Check if silent call
try:
    a = str(sys.argv[1])
except:
    a = "/g"
    pass

if ( a == '/s'):
    print Vals.isFirst()
    #Check if first run cant run in silent if not
    if (Vals.isFirst() == False):
        print "Starting silent scanner!"
        workThread = WorkThread(Vals.getRoot() , Vals.getRoom() , Vals.getBlock() , 1)
        workThread.start()
        while True:
            a = True
    else:
        firstRun()
else:
    if (Vals.isFirst() == False):
        print "No args starting UI"
        startIt()
    else:
        firstRun()

   




