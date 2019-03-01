import json
import pandas
import logging

LOGGER = logging.getLogger('JsonDataProcessor')


class JsonDataProcessor:
    def __init__(self):
        LOGGER.info('Init JSON Data processor')

    def processJsonData(self, outputCSVFile, jsonData=None, jsonFile=None):
        """
        Method to process the JSON data to a CSV file
        :param outputCSVFile: The name of the output CSV file
        :param jsonData: The json Data to be parsed
        :param jsonFile: The JSON file which is to be parsed. Ideally for debug
        :return: True if successfull, False Otherwise
        """
        LOGGER.info(f'Processing the JSON data to convert to CSV')
        tempJsonData = None
        if jsonData is None and jsonFile is None:
            LOGGER.error('No input provided for processing. Erroring out')
            return False
        elif jsonData is not None:
            LOGGER.info('Processing provided JSON data')
            tempJsonData = jsonData
        else:
            try:
                with open(jsonFile, 'r', encoding='utf8') as jFile:
                    tempJsonData = json.load(jFile)
                    LOGGER.info(f'Data read from the JSON file {jsonFile}')
            except Exception as e:
                LOGGER.error(f'Error in retrieving the JSON file {jsonFile}. Error = {e}')
        if self._writeToCSV(tempJsonData, outputCSVFile):
            LOGGER.info('JSON Data Processing completed')
            return True
        else:
            LOGGER.error('Error in JSON Data Processing')
            return None

    def _writeToCSV(self, jsonData, csvFile):
        """
        The method to write a jsonData to a CSV file. Uses Pandas
        :param jsonData: JSON data to be parsed
        :param csvFile: The output CSV file
        :return: True is success, False otherwise
        """
        LOGGER.info(f'Writing the provided json data to the CSV file {csvFile}')
        timestamp = []
        dataSource = []
        displayName = []
        displayValue = []
        rawValue = []
        if 'entries' in jsonData:
            for entry in jsonData['entries']:
                tempTimeStamp = entry['timestamp']
                tempSource = entry['dataSource']
                if 'data' in entry:
                    for record in entry['data']:
                        timestamp.append(tempTimeStamp)
                        dataSource.append(tempSource)
                        displayName.append(record['displayName'])
                        displayValue.append(record['displayValue'])
                        rawValue.append(record['rawValue'])

            csvData = {'Timestamp': timestamp,
                       'Data Source': dataSource,
                       'Display Name': displayName,
                       'Display Valule': displayValue,
                       'Raw Value': rawValue}
            dataFrame = pandas.DataFrame(data=csvData)
            LOGGER.info('CSV Data Frame Created')
            dataFrame.to_csv(csvFile)
            LOGGER.info(f'CSV Data written to CSV file {csvFile}')
            return True
        else:
            LOGGER.error('Could not find the entries array in the JSON data. Data is not in expected format')
            return False
