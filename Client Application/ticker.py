#####################
#                                          #
#  Coded By: Saurabh Joshi     #
#  Date Modified: 7/12/12       #
#                                        #
#  File: 2SEC Ticker               #
####################
import os
from PyQt4 import QtCore

import json
import urllib2
import time
import sys

                    
class Ticker(QtCore.QThread):
    def __init__(self,tok):
        QtCore.QThread.__init__(self)
        self.token = tok
    def run(self):
        self.startTick()
        return

    def startTick(self):
        try:
            while (True):
                time.sleep(3)
                url = "http://vitcloud-collegecode.rhcloud.com/response?token=" + str(self.token)
                req = urllib2.Request(url)
                k = urllib2.urlopen(req)
                response = k.read()
                print "Ticker:startTick(): RESPONSE: " + response
                
                if (response == "waiting"):
                    self.emit(QtCore.SIGNAL('ticked(QString)'), "waiting")
                    
                elif (response == "error"):
                    self.emit(QtCore.SIGNAL('ticked(QString)'), "error")
                    break
                
                else:
                    self.emit(QtCore.SIGNAL('ticked(QString)'), response)
                    break
                    
                k.close()
                
        except:
            self.emit(QtCore.SIGNAL('ticked(QString)'), "error")
            print "Awesome error:", sys.exc_info()[0]

class TempTok(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
        
    def run(self):
        self.getTok()
        return

    def getTok(self):
        try:
            tok = "http://vitcloud-collegecode.rhcloud.com/prechallenge"
            req = urllib2.Request(tok)
            k = urllib2.urlopen(req)
            print k
            token = k.read()
            self.emit(QtCore.SIGNAL('token(QString)'), token)
        except:
             self.emit(QtCore.SIGNAL('token(QString)'), "error")
            

    
            
