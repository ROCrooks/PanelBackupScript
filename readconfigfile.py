import configparser

def getconfiguration():
    config = configparser.ConfigParser()

    config.read('config.ini')

    #Read the source and the destination file formats from the config file
    sourceformat = config['folderpathformats']['sourceformat']
    destinationformat = config['folderpathformats']['destinationformat']

    #Get file extensions list
    extensions = config['fileextensions']['extensions']
    extensions = extensions.split(", ")

    configuration = {"sourceformat": sourceformat, "destinationformat": destinationformat, "extensions": extensions}
    return configuration
