#Locations of the source and destination files
sourcefiles = "../TestPanelBackup/filesfrom"
destinationfiles = "../TestPanelBackup/filesto"

#List of file extensions to backup
backupfileextensions = ['genome.vcf','vcf','bam','bai']

#Import required modules
import os
import re

#List the files in the directory
fileslist = os.listdir(sourcefiles)

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
