#!/usr/bin/env python
import io
from setuptools import setup, find_packages


readme = open('README.md').read()

requirements = [
    'google-cloud-language'
]


setup(

    # Metadata
    name='Analyser',
    version='0.1',
    author='Arun Thundyill Saseendran',
    author_email='tsarun9@gmail.com',
    url='https://github.com/ats0stv/Trinity/tree/master/SentimentAnalysisGCP',
    description='Script to analyse sentiment and magnitude of it using the GCP Language APIs',
    long_description=readme,

    # Package info
    packages=find_packages(exclude=('test',)),

    # Requirements
    install_requires=requirements
)