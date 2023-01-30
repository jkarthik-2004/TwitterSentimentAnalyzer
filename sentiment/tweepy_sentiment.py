from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import tweepy
import numpy as np
import pandas as pd

class Import_tweet_sentiment:

	consumer_key="rILEjaK09uWxjmZWrXpQJFcQD"
	consumer_secret="pc0iYX5FpgSWLCdQ8fQTa7n3YFeH4Bev24aQ8W7DbVKj3KZCu6"
	access_token="989488945158209537-TrwI8liMDKKmzanHbWGLu50abBrj1Pt"
	access_token_secret="a7G4io1Kbd1GyRdmjHsI8LUekK82V0Fh8McNyu3j45yzk"

	def tweet_to_data_frame(self, tweets):
		df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
		return df

	def get_tweets(self, handle):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		api = API(auth)

		account = handle
		item = api.user_timeline(id=account,count=200)
		df = self.tweet_to_data_frame(item)

		all_tweets = []
		for j in range(20):
			all_tweets.append(df.loc[j]['Tweets'])
		return all_tweets

	def get_hashtag(self, hashtag):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		api = API(auth)

		account = hashtag
		all_tweets = []

		for tweet in tweepy.Cursor(api.search_tweets, q=account, lang='en').items(200):
			all_tweets.append(tweet.text)

		return all_tweets
