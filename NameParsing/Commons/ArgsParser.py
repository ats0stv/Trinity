import logging
import argparse
from Commons.Utils import Utils
"""     
    Module to parse arguments
"""

logger = logging.getLogger('ArgsParser')

class ArgsParser:
    def __init__(self):
        logger.debug('Init ArgsParser')

    def parseArguments(self):
        logger.debug('Parsing the arguments')
        parser = argparse.ArgumentParser()
        parser.add_argument("--inputFile", "-i", help="Input file path with one name per line", required=True)
        parser.add_argument("--outputFile", "-o", help="If a file path is present, it writes the output to the file, else on console", required=False)
        outputTypeGroup = parser.add_mutually_exclusive_group(required=True)
        outputTypeGroup.add_argument('--xml', action='store_true')
        outputTypeGroup.add_argument('--json', action='store_true')
        args = parser.parse_args()
        self._validateArgs(args)
        return args

    def _validateArgs(self, args):
        util = Utils()
        if not util.isFile(args.inputFile):
            logger.error("Input file path not valid")
            print("Input file path not valid")
            exit(2)

        if args.outputFile:
            if not util.isFile(args.outputFile):
                logger.error("Output file path not valid")
                print("Output file path not valid")
                exit(2)



