"""     
    Class to parse CLI arguments
"""

import logging
import argparse
from Commons.Utils import Utils

logger = logging.getLogger('ArgsParser')

class ArgsParser:
    def __init__(self):
        logger.debug('Init ArgsParser')

    def parseArguments(self):
        logger.debug('Parsing the arguments')
        parser = argparse.ArgumentParser()
        parser.add_argument("--inputFile", "-i", help="Input file path with one name per line", required=True)
        parser.add_argument("--outputFile", "-o", help="If a file path is present, it writes the output to the file, else on console", required=False)
        parser.add_argument('--pretty', '-p', help="Pretty print the JSON/XML output", action='store_true', required=False)
        outputTypeGroup = parser.add_mutually_exclusive_group(required=True)
        outputTypeGroup.add_argument('--xml', help="Render output as XML", action='store_true')
        outputTypeGroup.add_argument('--json', help="Render output as JSON", action='store_true')
        args = parser.parse_args()
        
        if self._validateArgs(args) and self._createOutputDirIdenpotent(args.outputFile):
            return args
        else:
            return None

    def _createOutputDirIdenpotent(self, outputFile):
        logger.debug(f'Creating directory idempotent for the file path {outputFile}')
        util = Utils()
        if outputFile:
            if util.createDirIdenpotent(outputFile):
                return True
            else:
                return False
        else:
            return True

    def _validateArgs(self, args):
        util = Utils()
        logger.debug('Validating arguments')
        if not util.isFile(args.inputFile):
            logger.error("Input file path not valid")
            print("Input file path not valid")
            return False
        else:
            return True



