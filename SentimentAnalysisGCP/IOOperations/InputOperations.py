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

"""     Operations related to reading the input data
  
"""

import logging

logger = logging.getLogger('InputOperations')

class InputOperations:
	def __init__(self):
		logger.debug('Init InputOperations')

	def readText(self, filename):
		lines = []
		try:
			with open(filename, 'r') as filePointer:
				for line in filePointer:
					lines.append(line)
			return "\n".join(lines)
		except Exception as e:
			logger.error(f'Unable to read the file {filename}. Error = {e}')

