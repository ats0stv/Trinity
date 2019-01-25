import logging
import argparse

"""     
    Module to parse arguments
"""

logger = logging.getLogger('InputReader')

class InputReader:
    def __init__(self):
        logger.debug('Input Reader Init')

    def read(self, inputFilePath):
        logger.debug(f'Reading input from file {inputFilePath}')
        try:
            inputNames = []
            with open(inputFilePath, 'r') as fileObj:
                for line in fileObj:
                    inputNames.append(line.strip())
            return inputNames
        except Exception as e:
            logger.error(f'Error in reading file. Error = {e}')
            return None