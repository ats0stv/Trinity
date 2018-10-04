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
import re
import argparse


CONFIG_SORT_PWD_BY_LENGTH = True

ROOT = './'
OUTPUT_FILE = 'thundyia.broken'
COMBINED_POT_FILE = 'thundyia.pot'
UNIQUE_PASSWORD_LIST = 'thundyia.password'
INPUT_DIR = None
DESCRYPT_FILE_IDENTIFIER = 'descrypt' # Just for getting submitty to accept the use
PASSWORD_TYPE_DICT = {'num':[],'lower':[],'upper':[],'alnum':[],'other':[]}
REGEX_LOWER = '^[a-z]+$'
REGEX_UPPER = '^[A-Z]+$'
SEPERATOR_STRING = '**** -=-=-=-=-=-=-=-==-=-=-= ****'
PASSWORD_STATS_DICT = {'num':{'count':0,'percent':0,'minimum_length':100, 'maximum_length':0},
                       'lower':{'count':0,'percent':0,'minimum_length':100, 'maximum_length':0},
                       'upper':{'count':0,'percent':0,'minimum_length':100, 'maximum_length':0},
                       'alnum':{'count':0,'percent':0,'minimum_length':100, 'maximum_length':0},
                       'other':{'count':0,'percent':0,'minimum_length':100, 'maximum_length':0}}
TOTAL_PASSWORD_COUNT = 0


def formatOutputFileNames(outputFile):
    if '/' in outputFile:
        firstSplit = outputFile.split('/')
        if '.' in outputFile:
            outputFileSplit = firstSplit[-1].split('.')
            return str(outputFileSplit[0])+'.broken', str(outputFileSplit[0])+'.pot', str(outputFileSplit[0])+'.password'
    else:
        if '.' in outputFile:
            outputFileSplit = outputFile.split('.')
            return str(outputFileSplit[0])+'.broken', str(outputFileSplit[0])+'.pot', str(outputFileSplit[0])+'.password'


def emptyTheFile(filePath):
    if os.path.isfile(filePath):
        with open(filePath,'w') as file:
            file.write('')


def formatAsHeader(text):
    return '\n' + SEPERATOR_STRING + '\n' + text.center(len(SEPERATOR_STRING))+ '\n' + SEPERATOR_STRING + '\n\n'


def initializeOutputFiles():
    emptyTheFile(OUTPUT_FILE)
    emptyTheFile(COMBINED_POT_FILE)
    emptyTheFile(UNIQUE_PASSWORD_LIST)


def processArgs():
    global OUTPUT_FILE
    global INPUT_DIR
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", "-d", help="The directory containing the pot files to be merged", required=True)
    parser.add_argument("--outputFile", "-o", help="The path of the output file. If not specified file called (Should not be a hidden file) "
	   +OUTPUT_FILE+ "in CWD will be created", required=False)
    args = parser.parse_args()
    INPUT_DIR = args.dir
    if args.outputFile:
        OUTPUT_FILE, COMBINED_POT_FILE, UNIQUE_PASSWORD_LIST = formatOutputFileNames(args.outputFile)


def segregatePasswordType(password):
    global PASSWORD_TYPE_DICT
    global TOTAL_PASSWORD_COUNT
    global PASSWORD_STATS_DICT
    TOTAL_PASSWORD_COUNT = TOTAL_PASSWORD_COUNT + 1
    passwordLength = len(password.strip())
    if unicode(password.strip()).isnumeric():
        PASSWORD_TYPE_DICT['num'].append(password)
        updatePasswordStats('num',passwordLength)
    elif re.match(REGEX_LOWER.strip(), password):
        PASSWORD_TYPE_DICT['lower'].append(password)
        updatePasswordStats('lower',passwordLength)
    elif re.match(REGEX_UPPER.strip(), password):
        PASSWORD_TYPE_DICT['upper'].append(password)
        updatePasswordStats('upper',passwordLength)
    elif unicode(password.strip()).isalnum():
        PASSWORD_TYPE_DICT['alnum'].append(password)
        updatePasswordStats('alnum',passwordLength)
    else:
        PASSWORD_TYPE_DICT['other'].append(password)
        updatePasswordStats('other',passwordLength)


def updatePasswordStats(passwordType,passwordLength):
    PASSWORD_STATS_DICT[passwordType]['count'] = PASSWORD_STATS_DICT[passwordType]['count'] + 1
    if passwordLength < PASSWORD_STATS_DICT[passwordType]['minimum_length']:
            PASSWORD_STATS_DICT[passwordType]['minimum_length'] = passwordLength
    if passwordLength > PASSWORD_STATS_DICT[passwordType]['maximum_length']:
            PASSWORD_STATS_DICT[passwordType]['maximum_length'] = passwordLength
        
def computerPasswordTypePercentage():
    global PASSWORD_STATS_DICT
    for key, value in PASSWORD_STATS_DICT.items():
        percent = float(PASSWORD_STATS_DICT[key]['count']) / TOTAL_PASSWORD_COUNT * 100;
        # print 'tot = {}, key = {}, count = {}, percent = {}'.format(str(TOTAL_PASSWORD_COUNT),key,str(PASSWORD_STATS_DICT[key]['count']), str(percent))
        PASSWORD_STATS_DICT[key]['percent'] = percent

def prepareOutputFromFile(inputFile,outputFile):
    addedLines = []
    passwords = []
    with open(inputFile,'r') as inFile:
        for line in inFile:
            if ':' in line:
                splittedLine = line.split(':')
                segregatePasswordType(splittedLine[1])
                if DESCRYPT_FILE_IDENTIFIER in str(inFile): # To handle the submitty issue
                    splittedLine[1] = splittedLine[1][:7].strip()
                    formattedLine = ' '.join(splittedLine)+'\n'
                else:
                    formattedLine = ' '.join(splittedLine)
                if not line in addedLines: # to avoid any duplicates by mistake
                    appendToFile(outputFile,formattedLine)
                    appendToFile(COMBINED_POT_FILE,line)
                    addedLines.append(line)
            else:
                print "The line '"+ line + "' in file "+ inFile + " is not in pot format"


def writePasswordsByTypeToFile():
    appendToFile(UNIQUE_PASSWORD_LIST,formatAsHeader('Stats'))
    writeStatsToFile()
    for dictkey, value in PASSWORD_TYPE_DICT.items():
        appendToFile(UNIQUE_PASSWORD_LIST,formatAsHeader(dictkey))
        if CONFIG_SORT_PWD_BY_LENGTH:
            writeLinesToFile(UNIQUE_PASSWORD_LIST,list(sorted(set(value),key=len)))
        else:
            writeLinesToFile(UNIQUE_PASSWORD_LIST,list(sorted(set(value))))

def writeStatsToFile():
    computerPasswordTypePercentage()
    for key, value in PASSWORD_STATS_DICT.items():
        appendToFile(UNIQUE_PASSWORD_LIST,"\n-- "+key)
        for k, v in value.items():
            appendToFile(UNIQUE_PASSWORD_LIST, "\n"+k+": "+str(v))
        appendToFile(UNIQUE_PASSWORD_LIST, "\n")
    appendToFile(UNIQUE_PASSWORD_LIST, "\n")

def writeLinesToFile(outputFile,lines):
    with open(outputFile,'a') as outFile:
        outFile.writelines(lines)


def appendToFile(outputFile, text):
    with open(outputFile, 'a') as outFile:
        outFile.write(text);


def processInput():
    try:
        for root, _, files in os.walk(INPUT_DIR):
            ROOT = root
            for file in files:
                if ".pot" in file:
                    print "Reading Pot file "+ str(file)
                    filePath = os.path.join(root,file)
                    prepareOutputFromFile(filePath, OUTPUT_FILE)
        writePasswordsByTypeToFile()

    except Exception as e:
        print e.message


def displaySuccessMessage():
    print 'The output file can be found in {}'.format(OUTPUT_FILE)
    print 'The combined pot file can be found in {}'.format(COMBINED_POT_FILE)
    print 'The unique passwords file can be found in {}'.format(UNIQUE_PASSWORD_LIST)


def main():
    processArgs()
    initializeOutputFiles()
    processInput()
    displaySuccessMessage()

main()







