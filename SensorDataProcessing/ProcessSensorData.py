import os
import yaml
import logging
import logging.config

from IOOperations.PhoneSensorData import PhoneSensorData
from DataProcessor.JsonDataProcessor import JsonDataProcessor
from Configuration.AppConfig import (LOG_DIR, PHONE_URL, OUTPUT_CSV, JSON_DUMP_FILE)

LOGGER = logging.getLogger()


def init():
    """
    Method to initialize the application. Sets up logging.
    Returns: None
    """
    configureLogging()
    LOGGER.debug('Log Configuration Completed')


def configureLogging():
    """
    Method to configure logging
    Returns: None
    """
    global LOGGER
    try:
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)
        logging.config.dictConfig(yaml.load(open('configuration/logging.conf')))
        LOGGER.debug('Loggers initialized')
    except Exception as e:
        LOGGER.error(f"Error in the Log Configuration. Error = {e}")
        exit(1)


def processSensorData():
    """
    Get the data from Phone and convert it to a CSV
    :return: None
    """
    phoneSensorData = PhoneSensorData()
    data = phoneSensorData.collectPhoneSensorData(PHONE_URL)
    if data:
        LOGGER.info('Retrieved the sensor data. Processing it to CSV')
        jsonProcessor = JsonDataProcessor()
        if jsonProcessor.processJsonData(OUTPUT_CSV,jsonData=data):
            LOGGER.info(f'CSV file {OUTPUT_CSV} created successfully from the phone sensor data')
        else:
            LOGGER.error(f'Error in getting the Phone Sensor Data and creating a CSV file')
    else:
        LOGGER.error('Unable to get the Phone data. Check logs')
        exit(2)


def main():
    """
    Main Method. Inits the application and passes control to process Sensor data
    :return: None
    """
    init()
    processSensorData()


if __name__ == "__main__":
    main()
