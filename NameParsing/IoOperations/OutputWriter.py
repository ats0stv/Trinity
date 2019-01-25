"""     
    Class to Write Operations
"""
import os
import json
import logging
import dicttoxml
from xml.dom.minidom import parseString

from Commons.Constants import (XML_PRINT_TYPE, XML_ROOT_NAME)

logger = logging.getLogger('OutputWriter')

class OutputWriter:
	def __init__(self, outputFilePath, isXml, isJson, isPretty):
		logger.debug(f'Init Output writer with outputfilePath = {outputFilePath}, isXML = {isXml}, isJson = {isJson}')
		self.outputFilePath = outputFilePath
		self.isXml = isXml
		self.isJson = isJson
		self.isPretty = isPretty

	def write(self, dataObjects):
		logger.debug('Creating output')
		outputString = ""
		if self.isJson:
			outputString = self._renderJson(dataObjects)
		else:
			outputString = self._renderXML(dataObjects)
		if outputString:
			return self._displayOutput(outputString)
		else:
			logger.error("Error in rendering output to the desired format")
			return False

	def _renderJson(self, dataObjects):
		logger.debug('Rendering output as JSON')
		try:
			if self.isPretty:
				outputString = json.dumps(dataObjects, indent=4, separators=(',', ': '))
			else:
				outputString = json.dumps(dataObjects)
			return outputString
		except Exception as e:
			logger.error(f'JSON Rendering failed. Error = {e}')
			return None

	def _renderXML(self, dataObjects):
		logger.debug('Rendering output as XML')
		rootName = XML_ROOT_NAME
		if rootName == "":
			rootName = "root"
		try:
			outputString = dicttoxml.dicttoxml(dataObjects, custom_root=rootName,
										       attr_type=XML_PRINT_TYPE)
			if self.isPretty:		
				dom = parseString(outputString)
				outputString = dom.toprettyxml()
			return outputString
		except Exception as e:
			logger.error(f'XML Rendering failed. Error = {e}')
			return None

	def _displayOutput(self, outputString):
		if self.outputFilePath:
			logger.debug('Writing output to file')
			return self._writeToFile(outputString)
		else:
			return self._writeToConsole(outputString)


	def _writeToConsole(self, message):
		logger.debug('Displaying output in console')
		seperator = "* ~ * ~ * ~ * ~ * ~ * ~  Parsed Names * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * "
		print(seperator)
		print()
		print(message)
		print()
		print(seperator)
		return True

	def _writeToFile(self, message):
		try:
			with open(self.outputFilePath, 'w') as writeFileObj:
				writeFileObj.write(message)
				print(f'Output file available in path {os.path.abspath(self.outputFilePath)}')
			return True
		except Exception as e:
			logger.error(f'Error in writing to file. Error = {e}')
			return False





