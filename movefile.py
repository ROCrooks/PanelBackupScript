from shutil import copyfile

def movefile(sourcefiles,destinationfiles,file):
    sourcefile = sourcefiles + "/" + file
    destinationfile = destinationfiles + "/" + file
    copyfile(sourcefile,destinationfile)
