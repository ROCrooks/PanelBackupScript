import configparser

def getconfiguration():
    config = configparser.ConfigParser()

    config.read('config.ini')

    #Read the source and the destination file formats from the config file
    sourceformat = config['folderpathformats']['sourceformat']
    destinationformat = config['folderpathformats']['destinationformat']

    configuration = {"Source": sourceformat, "destination": destinationformat}
    return configuration
