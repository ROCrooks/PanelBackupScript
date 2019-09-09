#Import required modules
import os
import re

#Get the configuration from the config file
from readconfigfile import getconfiguration
configurations = getconfiguration()

#Get the configurations
backupfileextensions = configurations['extensions']
sourceformat = configurations['sourceformat']
destinationformat = configurations['destinationformat']

#Make source and destination folders
from selectfolder import choosefolder, makedestination
sourcefiles = choosefolder()
destinationfiles = makedestination(sourcefiles,sourceformat,destinationformat)

#List the files in the directory
fileslist = os.listdir(sourcefiles)

#Create folder if not already existing
if not os.path.exists(destinationfiles):
    os.mkdir(destinationfiles)

for file in fileslist:

    #Check the file extension of each file and only move if it is on the list
    move = False
    for extension in backupfileextensions:
        regex = ".*" + extension + "$"

        #Match to the file extensions list and prevent duplication caused by vcf
        if (bool(re.match(regex,file)) == True):
            move = True

    #Move files if they are
    if (move == True):
        from movefile import movefile
        movefile(sourcefiles,destinationfiles,file)
