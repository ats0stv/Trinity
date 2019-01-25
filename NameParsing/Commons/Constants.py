import logging

# Logging configuration
LOG_FILENAME = 'logs/Parser.log'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
DEBUG_LEVEL = logging.DEBUG

# JSON/XML element names
TITLE = "title"
FORENAME = "forename"
SURNAME = "surname"

# Default Title if title could not be detemined
DEFAULT_TITLE = ""


# Lowercase list of possible title representations
TITLE_KEY_DICT = {
    "Mr.": ["male", "m", "man", "guy"],
    "Ms.": ["female", "f", "woman", "girl"],
    "Dr.": ["doctor", "doc"],
    "Prof.": ["professor", "prof"],
    "Sir.": ['british knight', 'dame', 'sir']
}
