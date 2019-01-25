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

ARGS = None

if not os.path.exists('./logs'):
    os.makedirs('./logs')

logging.basicConfig(filename=LOG_FILENAME, level=DEBUG_LEVEL,
                    format=LOG_FORMAT)
logger = logging.getLogger('Parser')

def main():
    global ARGS
    try:
        logger.info('Starting the parsing of names')
        logger.debug('Parsing arguments')
        argParser = ArgsParser()
        ARGS = argParser.parseArguments()
        logger.debug(ARGS)
    except Exception as e:
        logger.error(f"Error in the start script. Error = {e}")
        exit(1)

if __name__ == "__main__":
    main()