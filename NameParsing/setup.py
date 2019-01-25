#!/usr/bin/env python
import io
from setuptools import setup, find_packages


readme = open('README.md').read()

requirements = [
    'nameparser',
    'dicttoxml'
]


setup(

    # Metadata
    name='Parser',
    version='0.1',
    author='Arun Thundyill Saseendran',
    author_email='thundyia@tcd.ie',
    url='https://github.com/ats0stv/Trinity/tree/master/NameParsing',
    description='Script to parse names into JSON or XML',
    long_description=readme,

    # Package info
    packages=find_packages(exclude=('test',)),

    # Requirements
    install_requires=requirements
)
