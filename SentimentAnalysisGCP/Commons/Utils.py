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


"""     
    Utilities Class
"""
import os
import logging
import json

logger = logging.getLogger('Utils')


class Utils:
    def __init__(self):
        logger.debug('Loading the util class')

    def isFile(self, filename):
        logger.debug(f'Checking if the file {filename} is present')
        return os.path.isfile(filename)

    def createDirIdenpotent(self, filename):
        try:
            logger.debug(f'Creating the directory for the filename {filename} if necessary')
            path = os.path.abspath(filename)
            directory = os.path.dirname(path)
            if not os.path.isdir(directory):
                os.makedirs(directory)
            return True
        except Exception as e:
            logger.error(f'Unable to createDirIdenpotent. Error = {e}')
            return False

    def printJson(self, sentiment, magnitude):
        outputObj = {
            "sentiment": sentiment,
            "magnitude": magnitude
        }
        logger.debug('Printing JSON response')
        outputString = json.dumps(
            outputObj, indent=4, separators=(',', ': '))
        return outputString