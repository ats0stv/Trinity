#!/usr/bin/python

# Copyright (C) 2019, Arun Thundyill Saseendran | ats0stv@gmail.com, thundyia@tcd.ie
#
# Permission is hereby granted, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software with restriction, that the software shall not be used without
# explicit written permission from the author. It is forbidden to be sold, used
# in products for commercial use, as-is, or translated.
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""     Core Module to calls the GCP API and get the response
  
"""

import logging

logger = logging.getLogger('SentimentAnalysis')

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


class SentimentAnalysis:

	def __init__(self, text):
		logger.debug('Init Sentiment Analysis')
		self.text = text

	def analyseSentiment(self):
		logger.info('Performing sentiment analysis')
		logger.debug('Creating document')
		try:
			client = language.LanguageServiceClient()
			document = types.Document(
				content=self.text,
				type=enums.Document.Type.PLAIN_TEXT)
			logger.debug('Performing sentiment analysis')
			sentiment = client.analyze_sentiment(document=document).document_sentiment
			logger.debug(f'Returning the sentiment score '+
				'{sentiment.score} and magnitude {sentiment.magnitude}')
			return sentiment.score, sentiment.magnitude
		except Exception as e:
			logger.error(f'Unable to perform sentiment analysis. Error = {e}')
			return None, None

	def offlineAnalysis(self):
		logger.debug('Performing offline analysis')
		lengthOfText = 0
		if self.text is not None:
			lengthOfText = len(self.text)
			logger.debug(f'The length of the text is {lengthOfText}')
		return lengthOfText

