#!/usr/bin/env python
"""     Try and crack pbkdf2 and argon2i
"""
__author__ = "Arun Thundyill Saseendran"
__version__ = "0.0.1"
__maintainer__ = "Arun Thundyill Saseendran"
__email__ = "thundyia@tcd.ie"

import os
import re
import datetime
import argparse
import threading
from passlib.hash import pbkdf2_sha256
from timeit import default_timer as timer



INPUTFILE = None
WORDLIST = None
OUTPUTFILE = './arunHashCrack.pot'
MODE = 1
HASHES = []
WORDS = []
THREADCOUNT = 5 
CHUNKS = None
TOTAL = 0
CURRENT = 0
PROFILEINTERVAL = 1000
STARTTIME = timer()

class myThread (threading.Thread):
   def __init__(self, chunk, hashes, outputFile, name):
      threading.Thread.__init__(self)
      self.chunk = chunk
      self.hashes = hashes
      self.outputFile = outputFile
      self.name = name

   def run(self):
      verifyHash(self.chunk, self.hashes, self.outputFile,self.name)
      print("Thread {} competed execution".format(str(self.name)))

def processArgs():
    global INPUTFILE
    global WORDLIST
    global OUTPUTFILE
    global MODE
    global THREADCOUNT
    parser = argparse.ArgumentParser()
    parser.add_argument("--hashFile", "-hF", help="The path of the hash file", required=True)
    parser.add_argument("--wordList", "-w", help="The path of the wordlist file", required=True)
    parser.add_argument("--outputFile", "-o", help="The path of the output file. If not specified file called (Should not be a hidden file) "
       +OUTPUTFILE+ "in CWD will be created", required=False)
    parser.add_argument("--mode", "-m", help="1 - pbkdf2 | 2 - argon2i", required=False)
    parser.add_argument("--threadCount", "-t", help="Number of threads. Default: 5", required=False)
    args = parser.parse_args()
    INPUTFILE = args.hashFile
    WORDLIST = args.wordList
    if args.outputFile:
        OUTPUTFILE = args.outputFile
    if args.mode:
        try:
            MODE = int(args.mode)
        except Exception as e:
            print('Unable to parse the mode. Use 1 or 2 alone')
            exit(2)
    if args.threadCount:
        try:
            print('Thread count to be overridden from {} to {}. Hope you have know your computer!'.format(str(THREADCOUNT),str(args.threadCount)))
            THREADCOUNT = int(args.threadCount)
        except Exception as e:
            print('Unable to parse the threadCount. Defaulting to {}'.format(str(THREADCOUNT)))

def loadWordlist(inputFile):
    global WORDS
    with open(inputFile,'r') as inFile:
        for line in inFile:
            WORDS.append(str(line).strip())

def prepareChunks(words):
    global CHUNKS
    chunkSize = len(words)/THREADCOUNT
    chunkSize = int(chunkSize) if chunkSize > 0 else 1
    CHUNKS = [words[x:x+chunkSize] for x in range(0,len(words),chunkSize)]

def readHashes(inputFile):
    with open(inputFile,'r') as inFile:
        for line in inFile:
            HASHES.append(str(line).strip())

def appendToFile(outputFile, text):
    with open(outputFile, 'a') as outFile:
        outFile.write(text)


def verifyHash(chunk, hashes, outputFile, threadName):
    global CURRENT
    for candidate in chunk:
        for hashValue in hashes:
            CURRENT = CURRENT + 1
            if (CURRENT % PROFILEINTERVAL) == 0:
                now = timer()
                secs = (now - STARTTIME)
                rate = CURRENT / secs
                remaining = TOTAL - CURRENT
                estimate = remaining / rate
                print('{} -- {}/{} - Elapsed {} - Rate {} H/s - ETA {}'.format(threadName,str(CURRENT),str(TOTAL),str(datetime.timedelta(seconds=round(secs))),str(round(rate,2)),str(datetime.timedelta(seconds=round(estimate)))))
            if pbkdf2_sha256.verify(candidate, hashValue):
                appendToFile(outputFile,hashValue+":"+candidate+'\n')
                print('**************************************** '+hashValue+":"+candidate)

def multiThreadHashVerification(chunks, outputFile):
    global HASHES
    threadList = []
    for i in range(len(chunks)):
        threadList.append(myThread(chunks[i],HASHES, outputFile, 'T'+str((i+1))))

    for thread in threadList:
        thread.start()


def main():
    global TOTAL
    processArgs()
    if MODE == 2: # Since argon2i is not implemented
        print('Argon2i Not implemented yet')
        exit(1)
    readHashes(INPUTFILE)
    loadWordlist(WORDLIST)
    TOTAL = len(HASHES) * len(WORDS)
    prepareChunks(WORDS)
    multiThreadHashVerification(CHUNKS, OUTPUTFILE)

main()
