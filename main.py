import tweepy 
import time
import os
from os import environ

#Access token & access token secret
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

#Consumer API keys
CONSUMER_KEY =  environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)


api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify=True)


user = api.me()


search = 'Kenya'
nrTweets = 500 #number of tweets you wanna pull back


for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
	try:
		
		tweet.retweet()
		print("tweet retweet")

		time.sleep(5)

		tweet.favorite()
		print("tweet liked")
		time.sleep(36)


	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break
