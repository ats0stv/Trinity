#!/usr/bin/env python
"""     Script to convert a set of pot files into a 
        submittable format with .hashes extension
        Scalable Computing
"""
__author__ = "Arun Thundyill Saseendran"
__version__ = "0.0.1"
__maintainer__ = "Arun Thundyill Saseendran"
__email__ = "thundyia@tcd.ie"


import os
import argparse

ROOT = './'
OUTPUT_FILE = 'thundyia.broken'
INPUT_DIR = None

def processArgs():
    global OUTPUT_FILE
    global INPUT_DIR
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", "-d", help="The directory containing the pot files to be merged", required=True)
    parser.add_argument("--outputFile", "-o", help="The path of the output file. If not specified file called "
	   +OUTPUT_FILE+ "in CWD will be created", required=False)
    args = parser.parse_args()
    INPUT_DIR = args.dir
    if args.outputFile:
        OUTPUT_FILE = args.outputFile



def prepareOutputFromFile(inputFile,outputFile):
    with open(inputFile,'r') as inFile:
        print "Opened file "+ str(inFile)
        for line in inFile:
            if ':' in line:
                print "Processing Line "+ line
                splittedLine = line.split(':')
                formattedLine = ' '.join(splittedLine)
                appendToFile(outputFile,formattedLine)
            else:
                print "The line '"+ line + "' in file "+ inFile + " is of wrong format"


def appendToFile(outputFile, text):
    with open(outputFile, 'w') as outFile:
        outFile.write(text+'\n');

def processInput():
    try:
        for root, _, files in os.walk(INPUT_DIR):
            ROOT = root
            for file in files:
                if ".pot" in file:
                    print "Reading Pot file "+ str(file)
                    filePath = os.path.join(root,file)
                    prepareOutputFromFile(filePath, OUTPUT_FILE)

    except Exception as e:
        print e.message


def main():
    processArgs()
    processInput()


main()







