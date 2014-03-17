############################
#                          #
#  Coded By: Saurabh Joshi #
#  Date Modified: 7/12/12  #
#                          #
#  File: Non UI stuff      #
############################

import ConfigParser
import os
Config = ConfigParser.ConfigParser()
ROOT = ''
ROOM = ''
BLOCK = ''


class Lib:
    
    
    def __init__(self):

        #SETTINGS
        self.FirstRun = False
        
        self.getSettings()

    def getSettings(self):

        if (os.path.isfile("settings/firstRun")):
            Config.read("settings/config")
            global ROOT 
            global ROOM 
            global BLOCK
            ROOT = Config.get('Settings','Root')
            BLOCK = Config.get('Settings','Block')
            ROOM = Config.get('Settings', 'Room')
            if (ROOT == "NA" or BLOCK == "NA" or ROOM == "NA"):
                print "NA value found!"
                self.FirstRun = True
            

        else:
            firstRun = open("settings/firstRun", 'w+')
            firstRun.close()
            self.FirstRun = True
            
        #Config File Structure
            cfgfile = open("settings/config",'w')
            Config.add_section('Settings')
            Config.set('Settings','Root',"NA")
            Config.set('Settings','Block', "NA")
            Config.set('Settings', 'Room' , "NA")
            Config.write(cfgfile)
            cfgfile.close()
            #Re-run function to get settings
            self.getSettings()
        return True
    
    

    #SAVE NEW SETTINGS
    def saveSettings(self,root,block,room):
        global ROOT 
        global ROOM 
        global BLOCK
        cfgfile = open("settings/config",'w')
        Config.set('Settings','Root',root)
        Config.set('Settings','Block', block)
        Config.set('Settings', 'Room' , room)
        Config.write(cfgfile)
        cfgfile.close()
        ROOT = root
        BLOCK = block
        ROOM = room
        return True

    #RETURN FUNCTIONS
    def isFirst(self):
        return self.FirstRun
    def getRoot(self):
        print "Returned: " + ROOT
        return ROOT
    def getRoom(self):
        return ROOM
    def getBlock(self):
        return BLOCK
            
