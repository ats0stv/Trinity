import json
import logging
import requests

from Configuration.AppConfig import JSON_DUMP_FILE

LOGGER = logging.getLogger('Phone Sensor Data')


class PhoneSensorData:
    def __init__(self):
        LOGGER.debug('Init Phone Sensor Data Module')

    def collectPhoneSensorData(self, URL):
        """
        Collect the Sensor Data from Phone
        :param URL: The URL exposed by the Phone Sensor App
        :return: Returns the json data retrieved else None
        """
        LOGGER.info(f'Collecting data from {URL}')
        response = requests.get(URL)
        if response.status_code == 200:
            LOGGER.debug('Retrieved JSON DATA from phone')
            jsonData = response.json()
            with open(JSON_DUMP_FILE, 'w') as jsonFile:
                jsonFile.write(json.dumps(jsonData))
                LOGGER.info(f'Dumped the JSON Data to the file {JSON_DUMP_FILE}')
            LOGGER.info('Returning JSON Data')
            return jsonData
        else:
            LOGGER.error(f'Error in retrieving the sensor data. Error code = {response.status_code}')
            return None
