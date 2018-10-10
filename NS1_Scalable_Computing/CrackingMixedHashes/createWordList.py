#!/usr/bin/env python
"""     Script to create word lists for combinator attack
"""
__author__ = "Arun Thundyill Saseendran"
__version__ = "0.0.1"
__maintainer__ = "Arun Thundyill Saseendran"
__email__ = "thundyia@tcd.ie"


import os
import re
import argparse

OUTPUT_FILE = './output.txt'
LETTER_COUNT = 0
MODE = -1
MASTERFILE = './master.file'
TOTAL_PROCESSED = 0

def processArgs():
    global LETTER_COUNT
    global OUTPUT_FILE
    global MASTERFILE
    global MODE
    parser = argparse.ArgumentParser()
    parser.add_argument("--masterFile", "-mf", help="The path of the file containing all the files. Default: ./master.file", required=True)
    parser.add_argument("--outputFile", "-o", help="The path of the output file. If not specified file called (Should not be a hidden file) "
       +OUTPUT_FILE+ "in CWD will be created", required=False)
    parser.add_argument("--numberOfChars", "-n", help="The number of letters. Eg. 4", required=True)
    parser.add_argument("--convert", "-c", help="1 - Lower; 2 - Upper; 3 - As is", required=True)
    args = parser.parse_args()
    MASTERFILE = args.masterFile
    if args.outputFile:
        OUTPUT_FILE = args.outputFile
    try:
        LETTER_COUNT = int(args.numberOfChars)
    except Exception as e:
        print 'Unable to parse the number of characters'
        exit(1)
    try:
        MODE = int(args.convert)
        if not (MODE > 0 and MODE <= 3):
            print 'Mode should be within 1 and 3'
            exit(2)
    except Exception as e:
        print 'Unable to parse the mode'
        exit(1)


def emptyTheFile(filePath):
    if os.path.isfile(filePath):
        with open(filePath,'w') as file:
            file.write('')

def appendToFile(outputFile, text):
    with open(outputFile, 'a') as outFile:
        # print '---- ----- ----- ----- Writing {} to file {}'.format(text,outputFile)
        outFile.write(text+'\n')

def convertBasedOnMode(text, mode):
    if mode == 3:
        return text
    elif mode == 2:
        return text.upper()
    elif mode == 1:
        return text.lower()
    else:
        print 'Unacceptable text conversion mode'
        exit(2)

def processFile(masterFile, outputFile, convertMode, letterCount):
    global TOTAL_PROCESSED
    with open(masterFile,'r') as file:
        for line in file:
            # print 'Reading line {}'.format(line)
            if len(line.strip()) == letterCount:
                TOTAL_PROCESSED = TOTAL_PROCESSED + 1
                # print ' **** **** *** Word match for word {}'.format(line.strip())
                appendToFile(outputFile, convertBasedOnMode(line.strip(),convertMode))

def main():
    processArgs()
    emptyTheFile(OUTPUT_FILE)
    processFile(MASTERFILE, OUTPUT_FILE, MODE, LETTER_COUNT)
    print 'Processing Completed. \n{} words selected\n' \
          'Output file with {} chars and mode {} can be found in path {}'.format(str(TOTAL_PROCESSED), str(LETTER_COUNT), str(MODE), OUTPUT_FILE)

main()
