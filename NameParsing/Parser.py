#!/usr/bin/python

"""     Script to parse Human names and output XML or JSON
        RC: 0-Good 1-Generic Error 2-I/O Error
"""
import os
import logging
import argparse

from Commons.ArgsParser import ArgsParser
from Commons.Constants import (LOG_FILENAME, DEBUG_LEVEL,
                               LOG_FORMAT)
from IoOperations.InputReader import InputReader

ARGS = None

if not os.path.exists('./logs'):
    os.makedirs('./logs')

logging.basicConfig(filename=LOG_FILENAME, level=DEBUG_LEVEL,
                    format=LOG_FORMAT)
logger = logging.getLogger('Parser')


def parseArgs():
    global ARGS
    try:
        logger.info('Starting the parsing of names')
        logger.debug('Parsing arguments')
        argParser = ArgsParser()
        ARGS = argParser.parseArguments()
        if not ARGS:
            logger.error('Error in parsing Arguments')
            exit(1)
        logger.debug(ARGS)
    except Exception as e:
        logger.error(f"Error in the start script. Error = {e}")
        exit(1)

def readInput(filename):
    inputReader = InputReader()
    inputData = inputReader.read(filename)
    if not inputData:
        logger.error(f'Error in reading the input from the file {filename}')
        exit(2)
    else:
        logger.debug('Input file reading complete')
        return inputData

def main():
    parseArgs()
    inputData = readInput(ARGS.inputFile)
    print(inputData)



if __name__ == "__main__":
    main()