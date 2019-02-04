# GCP Sentiment Analysis
The application determines the sentiment and magnitude of it using the GCP language API

# Credentials File for API
Download the API from 
```
https://cloud.google.com/natural-language/docs/quickstart?refresh=1#set_up_a_project
```
The important part is to download the JSON file with credentials and configure it in the Configuration.py file

# Folder Structure
```
.
├── Analyser.py
├── Commons
│   ├── ArgsParser.py
│   ├── Utils.py
│   └── __init__.py
├── Config
│   ├── Configuration.py
│   └── __init__.py
├── Core
│   ├── SentimentAnalysis.py
│   └── __init__.py
├── IOOperations
│   ├── InputOperations.py
│   └── __init__.py
├── README.md
├── gcpCreds.json
├── requirements.txt
├── sampleInput
│   └── sample1.txt
└── setup.py
```

# Configuration
Configure the Configuration File from the path `Config/Configuration.py` based on the description below.

```
# Logging configuration
LOG_DIRECTORY = '<Path to Log Directory. Will be created if not present>'
LOG_FILENAME = '<Log File Name>'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
DEBUG_LEVEL = logging.DEBUG

# Google Creds
CREDS_FILE = '<Path to GCP Credentials file>'
```

# Usage
Script Usage 
```
$ python Analyser.py --help
usage: Analyser.py [-h] --inputFile INPUTFILE [--json]

optional arguments:
  -h, --help            show this help message and exit
  --inputFile INPUTFILE, -i INPUTFILE
                        Input file path with one name per line
  --json                Render output as JSON
```

## Sample Input
**sample1.txt**
```
Customer complaints are not always a sign that something is wrong. Be that as it may, great feedback can be buried within the vitriol. You need to give credence to every message that customers send. Oftentimes, a negative experience can be salvaged and turned into an opportunity.
```

## Example 1
Blunt Output
```
$ python Analyser.py -i sampleInput/sample1.txt
Number of units is 1
The sentiment is -0.30000001192092896 and the magnitude is 2.0999999046325684
```

## Example 2
JSON Output
```
$ python Analyser.py -i sampleInput/sample1.txt --json
Number of units is 1
The sentiment is -0.30000001192092896 and the magnitude is 2.0999999046325684
JSON Output
{
    "sentiment": -0.30000001192092896,
    "magnitude": 2.0999999046325684
}
```