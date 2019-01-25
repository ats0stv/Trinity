#!/usr/bin/python

"""     Script to parse Human names and output XML or JSON
        RC: 0-Good 1-Generic Error 2-I/O Error
"""
import os
import logging
import argparse

from Commons.Constants import (LOG_FILENAME, DEBUG_LEVEL)

if not os.path.exists('./logs'):
    os.makedirs('./logs')

logging.basicConfig(filename=LOG_FILENAME, level=DEBUG_LEVEL)
logger = logging.getLogger('Parser')

def main():
    logging.info('Starting the parsing of names')
    logging.debug('Parsing arguments')
    

if __name__ == "__main__":
    main()