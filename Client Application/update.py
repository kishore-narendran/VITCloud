import os
from PyQt4 import QtCore

class Updater(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        try:
            self.check()
        except:
            print "Error: Update failed!"
        return

    def check(self):
        with open('settings/Version') as g:
            curver = g.readline()
        g.close()

        print "####\n\nUPDATER STARTED###\n\n"
        print "LOCAL VERSION: " + curver
        curver = int(curver[0])
        
        import urllib

        urllib.urlretrieve ("http://dl.dropbox.com/u/37268256/VITCloud/Version", "settings/Curversion")

        with open('settings/Curversion') as h:
            ver = h.readline()
        h.close()

        print "SERVER VERSION: " + ver
        ver = int(ver[0])

        if (ver > curver):
            print "Update required!"
            self.emit( QtCore.SIGNAL('update(QString)'), "Update")

            
        
