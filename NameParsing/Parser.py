#!/usr/bin/python

"""     Script to parse Human names and output XML or JSON
        RC: 0-Good 1-Generic Error 2-I/O Error
"""
import os
import logging
import argparse

from Commons.Utils import Utils
from Commons.ArgsParser import ArgsParser
from Commons.Constants import (LOG_FILENAME, DEBUG_LEVEL,
                               LOG_FORMAT, TITLE_KEY_DICT)
from IoOperations.InputReader import InputReader
from IoOperations.OutputWriter import OutputWriter
from CoreLogic.NameParserLogic import NameParserLogic

ARGS = None
TITLE_DICT = {}
logger = None

def init():
    global TITLE_DICT
    global logger
    try:
        if not os.path.exists('./logs'):
            os.makedirs('./logs')
        logging.basicConfig(filename=LOG_FILENAME, level=DEBUG_LEVEL,
                            format=LOG_FORMAT)
        logger = logging.getLogger('Parser')
        logger.debug('Creating a quick ref title dict from the human readable title mappings')
        util = Utils()
        TITLE_DICT = util.createTitleDict(TITLE_KEY_DICT)
    except Exception as e:
        logger.error(f"Error in the init. Error = {e}")
        exit(1)

def parseArgs():
    global ARGS
    try:
        logger.debug('Parsing arguments')
        argParser = ArgsParser()
        ARGS = argParser.parseArguments()
        if not ARGS:
            logger.error('Error in parsing Arguments')
            exit(1)
        logger.debug(ARGS)
    except Exception as e:
        logger.error(f"Error in the parse logic. Error = {e}")
        exit(1)

def readInput(filename):
    logger.debug('Reading input')
    try:
        inputReader = InputReader()
        inputData = inputReader.read(filename)
        if not inputData:
            logger.error(f'Error in reading the input from the file {filename}')
            exit(2)
        else:
            logger.debug('Input file reading complete')
            return inputData
    except Exception as e:
        logger.error(f"Error in the file reading. Error = {e}")
        exit(2)

def parseNames(inputNames):
    logger.debug('Parsing Names')
    nameParser = NameParserLogic(TITLE_DICT)
    parsedNames = nameParser.parseListOfNames(inputNames)
    if parsedNames:
        logger.debug('Name Parsing completed')
        return parsedNames
    else:
        logger.error('Error in parsing names')
        print('Error in parsing names')
        exit(1)


def writeOutput(outputObjects):
    logger.info('Writing Output')
    outputWriter = OutputWriter(ARGS.outputFile, ARGS.xml, ARGS.json, ARGS.pretty)
    if not outputWriter.write(outputObjects):
        logger.error('Error in writing the output')
        print('Error in writing the output')
        exit(2)

def main():
    print('** Stating application')
    init()
    logger.info('** Starting the parsing of names')
    parseArgs()
    print('** Arguments parsed')
    inputData = readInput(ARGS.inputFile)
    print(f'** Input Read from file {os.path.abspath(ARGS.inputFile)}')
    outputData = parseNames(inputData)
    print('** Processing input')
    writeOutput(outputData)
    print('** Rendering output')
    print(f'Logs can be found in {os.path.abspath(LOG_FILENAME)}')


if __name__ == "__main__":
    main()