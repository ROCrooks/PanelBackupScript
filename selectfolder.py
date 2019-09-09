#Import the tkinter module
import tkinter as tk
from tkinter import filedialog

#sourceformat = "D:\Illumina\MiSeqAnalysis\<runID>\data\intensities\BaseCalls\Alignment"
sourceformat = "D:/Illumina/MiSeqAnalysis/<runID>/data/intensities/BaseCalls/Alignment"
#sourceformat = sourceformat.replace("\","\\")
#destinationformat = "Z:\Illumina\MiSeqOutput\<runID>"
destinationformat = "Z:/Illumina/MiSeqOutput/<runID>"

def choosefolder():
    #Choose folder
    root = tk.Tk()
    root.withdraw()

    folder_path=filedialog.askdirectory()

    return folder_path

def makedestination(folder_path,sourceformat,destinationformat):
    sourceformat = sourceformat.split("/")
    destinationformat = destinationformat.split("/")
    folder_path = folder_path.split("/")

    #Get location of the run ID from the source folder path
    sourcefindbatch = ""
    i = -1;
    while sourcefindbatch != "<runID>":
        i+=1
        sourcefindbatch = sourceformat[i]
    sourcekey = i

    #Get the location of the run ID from the destination folder path
    destinationfindbatch = ""
    i = -1;
    while destinationfindbatch != "<runID>":
        i+=1
        destinationfindbatch = destinationformat[i]
    destinationkey = i

    #Get RunID
    runid = folder_path[sourcekey]

    folder_path = destinationformat
    folder_path[destinationkey] = runid
    slash = "/"
    folder_path = slash.join(folder_path)
    return folder_path
