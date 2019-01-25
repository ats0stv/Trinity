import logging

from Commons.Constants import (TITLE, FORENAME,
                       SURNAME)

logger = logging.getLogger('Name')

class Name:
    def __init__(self, title, forename, surname)
        logger.debug(f'Name init with title={title}, forename={forename}, surname={surname}')
        self.title = title
        self.forename = forename
        self.surname = surname

    def getNameDict(self):
        logger.debug(f'Returning name dict for name object with forename {self.forename}')
        return {TITLE:self.title, FORENAME:self.forename,
                SURNAME:self.surname}