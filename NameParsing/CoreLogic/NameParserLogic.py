"""     
    Class to parse human names
"""

import logging

from nameparser import HumanName
from Commons.Constants import DEFAULT_TITLE
from Model.Name import Name
logger = logging.getLogger('NameParserLogic')


class NameParserLogic:
    def __init__(self, titleDict):
        logger.debug('Name Parser Init')
        self.titleDict = titleDict

    def parseListOfNames(self, namesList):
        try:
            logger.info('Parsing the provided list of names to Objects')
            parsedNameList = []
            for name in namesList:
                humanName = HumanName(name)
                title, surname, forename = self.processHumanName(humanName)
                logger.debug(f'Title = {title}, Surname = {surname}, Forename = {forename}')
                parsedName = Name(title, forename, surname)
                parsedNameList.append(parsedName.getNameDict())
            logger.info('Parsing completed')
            return parsedNameList
        except Exception as e:
            logger.error(f'Error in parsing the input names. Error = {e}')
            return None

    def processHumanName(self, humanName):
        forename = humanName.first
        surname = humanName.middle + humanName.last + humanName.suffix
        title = self.processTitle(humanName)
        return title, surname, forename

    def processTitle(self, humanName):
        title = ""
        if humanName.title != "":
            title = humanName.title
        elif humanName.nickname != "":
            tempTitle = self.getTitleFromNickname(humanName.nickname)
            if tempTitle:
                logger.debug(f'Title determined as {tempTitle}')
                title = tempTitle
            else:
                logger.warn(f'Unable to determine the title. Setting title as {DEFAULT_TITLE}')
                title = DEFAULT_TITLE
        else:
            title = DEFAULT_TITLE
        return title

    def getTitleFromNickname(self, nickname):
        nickname = nickname.lower()
        if nickname in self.titleDict:
            return self.titleDict[nickname]
        else:
            return None
