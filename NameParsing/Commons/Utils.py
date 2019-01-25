import os
import logging

logger = logging.getLogger('Utils')

class Utils:
    def __init__(self):
        logger.debug('Loading the util class')
    
    def isFile(self, filename):
        logger.debug(f'Checking if the file {filename} is present')
        return os.path.isfile(filename)

    def createTitleDict(self, titleKeyDict):
        titleDict = {}
        logger.debug('Creating title dict')
        for title, options in titleKeyDict.items():
            for option in options:
                titleDict[option] = title
        logger.debug('Returning title dict')
        return titleDict
