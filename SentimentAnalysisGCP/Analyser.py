#!/usr/bin/python

# Copyright (C) 2019, Arun Thundyill Saseendran | ats0stv@gmail.com, thundyia@tcd.ie
#
# Permission is hereby granted, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software with restriction, that the software shall not be used without
# explicit written permission from the author. It is forbidden to be sold, used
# in products for commercial use, as-is, or translated.
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""     Script to Analyze Sentiment and Magnitude of Emotion in a given text
  
"""

import os
import math
import logging

from Commons.Utils import Utils
from Commons.ArgsParser import ArgsParser
from Core.SentimentAnalysis import SentimentAnalysis
from IOOperations.InputOperations import InputOperations
from Config.Configuration import (
    LOG_FILENAME, DEBUG_LEVEL, LOG_FORMAT, LOG_DIRECTORY,
    CREDS_FILE)

LOGGER = None

def init():
    """ Initialization of the log directory and logger """
    global LOGGER
    try:
        if not os.path.exists(LOG_DIRECTORY):
            os.makedirs(LOG_DIRECTORY)
        logging.basicConfig(filename=str(os.path.join(os.path.abspath(LOG_DIRECTORY), LOG_FILENAME)), 
                            level=DEBUG_LEVEL, format=LOG_FORMAT)
        LOGGER = logging.getLogger('Sentiment Analysis Init')
        LOGGER.debug(f'Setting credentials file with path {CREDS_FILE}')
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = CREDS_FILE
    except Exception as e:
        LOGGER.error(f"Error in the init. Error = {e}")
        exit(1)

def parseArgs():
    argsParser = ArgsParser()
    args = argsParser.parseArguments()
    if args:
        LOGGER.debug('Parsed the input arguments')
        return args
    else:
        LOGGER.error('Invalid Input')
        print("Invalid Input")
        exit(2)

def readInput(filename):
    LOGGER.debug('Reading input')
    inputOperations = InputOperations()
    return inputOperations.readText(filename)

def performSentimentAnalysis(inputText):
    LOGGER.debug('Performing sentiment Analysis')
    sentimentAnalysis = SentimentAnalysis(inputText)
    LOGGER.debug(f'Input text length is {sentimentAnalysis.offlineAnalysis()}')
    print(f'Number of units is {math.ceil(sentimentAnalysis.offlineAnalysis()/1000)}')
    sentiment, magnitude = sentimentAnalysis.analyseSentiment()
    if sentiment:
        LOGGER.debug(f'The sentiment is {sentiment} and the magnitude is {magnitude}')
        return sentiment, magnitude
    else:
        return None, None


def main():
    """ Main Method to get the application running """
    init()
    LOGGER.debug('Starting application')
    args = parseArgs()
    util = Utils()
    inputText = readInput(args.inputFile)
    sentiment, magnitude = performSentimentAnalysis(inputText)
    print(f'The sentiment is {sentiment} and the magnitude is {magnitude}')
    print('JSON Output')
    if args.json:
        print(util.printJson(sentiment, magnitude))


if __name__ == "__main__":
    main()












