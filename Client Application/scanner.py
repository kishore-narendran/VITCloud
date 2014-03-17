################################
#                              #
#  Coded By: Saurabh Joshi     #
#  Date Modified: 7/12/12      #
#                              #
#  File: File Scanner & Sender #
################################

import os
from PyQt4 import QtCore

import json
import urllib2
import sys

                    
class WorkThread(QtCore.QThread):
    def __init__(self,mssg,room,block , t = 0):
        QtCore.QThread.__init__(self)
        self.msg = mssg
        self.room = room
        self.block = block
        self.t = t
        
    def run(self):
        self.scan(self.msg,self.block,self.room , self.t)
        return

    def sorter(self,seq):
        seen = set()
        seen_add = seen.add
        return [ x for x in seq if x not in seen and not seen_add(x)]

    def final_msg(self):
        #make tags remove dots etc
        pass

    def scan(self,d,block,room , t):
        f = open('settings/Files', 'w+')
        m = open('settings/Sizes', 'w+')
        try:
            for dirname, dirnames, filenames in os.walk(d):
                for filename in filenames:
                    temp_file = os.path.join(dirname, filename)
                    self.emit( QtCore.SIGNAL('scanned(QString)'), filename)
                    if (os.path.getsize(temp_file) > 104857600):
                        f.write(filename + '\n')
                        f.write(str(os.path.getsize(temp_file)) + '\n')

        except:
            pass
        f.close()
        m.close()

        self.emit( QtCore.SIGNAL('scanned(QString)'), "DONE")

        url = 'http://vitcloud-collegecode.rhcloud.com/interface'

        self.emit( QtCore.SIGNAL('scanned(QString)'), "Checking for duplicates..")        
        
        self.emit( QtCore.SIGNAL('scanned(QString)'), "Connecting..")

        #Read data
        with open('settings/Files') as g:
            data = g.readlines()
        g.close()

        #Convert to JSON
        inf = [room,block]
        data = json.dumps(inf + data)

        self.emit( QtCore.SIGNAL('scanned(QString)'), "Sending..")

        #Send this shit
        try:
            req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
            k = urllib2.urlopen(req)
            response = k.read()
            print response
            k.close()
        except Exception as e:
            print "Awesome error:", e

        self.emit( QtCore.SIGNAL('scanned(QString)'), "Idle")

        if (t!=0):
            sys.exit(0)


#Service for /s arg
def startService(msg):
    workThread = WorkThread(msg)
    workThread.start()







