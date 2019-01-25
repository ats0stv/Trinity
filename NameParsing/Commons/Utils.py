import os
import logging

logger = logging.getLogger('Utils')

class Utils:
    def __init__(self):
        logger.debug('Loading the util class')
    
    def isFile(self, filename):
        logger.debug(f'Checking if the file {filename} is present')
        return os.path.isfile(filename)