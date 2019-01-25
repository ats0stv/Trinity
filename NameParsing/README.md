# Name Parser Application

## Description
The app will enable to parse a set of Human names from an input text file which contains one name per line and output it as json or xml on the screen or write the output to a file.

## Requirements
Python 3.6+. Not compatible with Python 2.x

## Installation
```bash
pip install -r requirements.txt
```

## Configuration
Look into Commons/Constants.py

** Important **
If title is not detected by norm, then the following following dictionary is used to match the appropriate title. New titles can be added and exiting ones can be updated.
```
TITLE_KEY_DICT = {
    "Mr.": ["male", "m", "man", "guy"],
    "Ms.": ["female", "f", "woman", "girl"],
    "Dr.": ["doctor", "doc"],
    "Prof.": ["professor", "prof"],
    "Sir.": ['british knight', 'dame', 'sir']
}
```

## App Usage
To know the usage of the application, use the following command
```python
python NameParser.py --help
```
Ref:
```
usage: Parser.py [-h] --inputFile INPUTFILE [--outputFile OUTPUTFILE]
                 [--pretty] (--xml | --json)

optional arguments:
  -h, --help            show this help message and exit
  --inputFile INPUTFILE, -i INPUTFILE
                        Input file path with one name per line
  --outputFile OUTPUTFILE, -o OUTPUTFILE
                        If a file path is present, it writes the output to the
                        file, else on console
  --pretty, -p          Pretty print the JSON/XML output
  --xml                 Render output as XML
  --json                Render output as JSON
```

### Sample Input File
sampleInput.txt
```
Dr. Gilles Deleuze
Michel Foucault (Male)
Hannah Arendt (Professor)
John Locke (male)
Judith Butler (Female)
Francis Bacon (British knight)
```

## Examples
** JSON Output on Console **
```bash
python Parser.py -i ./sampleInput.txt --json --pretty
```
Output
```
** Stating application
** Arguments parsed
** Input Read from file /Users/arun/git/Trinity/NameParsing/sampleInput.txt
** Input Processed
* ~ * ~ * ~ * ~ * ~ * ~  Parsed Names * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ *

[
    {
        "title": "Dr.",
        "forename": "Gilles",
        "surname": "Deleuze"
    },
    {
        "title": "Mr.",
        "forename": "Michel",
        "surname": "Foucault"
    },
    {
        "title": "Prof.",
        "forename": "Hannah",
        "surname": "Arendt"
    },
    {
        "title": "Mr.",
        "forename": "John",
        "surname": "Locke"
    },
    {
        "title": "Ms.",
        "forename": "Judith",
        "surname": "Butler"
    },
    {
        "title": "Sir.",
        "forename": "Francis",
        "surname": "Bacon"
    }
]

* ~ * ~ * ~ * ~ * ~ * ~  Parsed Names * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ *
** Output Rendered
Logs can be found in /Users/arun/git/Trinity/NameParsing/logs/Parser.log
```


** XML Output on Console **
```bash
python Parser.py -i ./sampleInput.txt --xml --pretty
```
Output
```
** Stating application
** Arguments parsed
** Input Read from file /Users/arun/git/Trinity/NameParsing/sampleInput.txt
** Input Processed
* ~ * ~ * ~ * ~ * ~ * ~  Parsed Names * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ *

<?xml version="1.0" ?>
<names>
	<item>
		<title>Dr.</title>
		<forename>Gilles</forename>
		<surname>Deleuze</surname>
	</item>
	<item>
		<title>Mr.</title>
		<forename>Michel</forename>
		<surname>Foucault</surname>
	</item>
	<item>
		<title>Prof.</title>
		<forename>Hannah</forename>
		<surname>Arendt</surname>
	</item>
	<item>
		<title>Mr.</title>
		<forename>John</forename>
		<surname>Locke</surname>
	</item>
	<item>
		<title>Ms.</title>
		<forename>Judith</forename>
		<surname>Butler</surname>
	</item>
	<item>
		<title>Sir.</title>
		<forename>Francis</forename>
		<surname>Bacon</surname>
	</item>
</names>


* ~ * ~ * ~ * ~ * ~ * ~  Parsed Names * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ *
** Output Rendered
```


** JSON Output on File Non Pretty**
Creates the output directory if required
```bash
python Parser.py -i ./sampleInput.txt -o ./test/sample.json --json
```

** XML Output on File Non Pretty**
Creates the output directory if required
```bash
python Parser.py -i ./sampleInput.txt -o ./test/sample.xml --xml
```
