import tweepy 
import time
import os
from os import environ

#Access token & access token secret
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = environ['ACCESS_TOKEN_SECRET']

#Consumer API keys
API_KEY =  environ['API_KEY']
API_SECRET = environ['API_SECRET']

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify=True)


user = api.me()


search = 'Kenya'
nrTweets = 500 #number of tweets you wanna pull back


for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
	try:
		
		tweet.retweet()
		print("tweet retweet")

		time.sleep(10)

		tweet.favorite()
		print("tweet liked")
		time.sleep(10)


	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break
