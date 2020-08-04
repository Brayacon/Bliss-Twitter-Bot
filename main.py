import tweepy 
import time


auth = tweepy.OAuthHandler('7SG8RO9FDjOJKxZjawbLQXPkH', 'N6CsGk8MvutJhpztMW2oXEIsed0juMPbjwuKgj31SK3KpUNebT')
auth.set_access_token('1264775524775313414-u5lCUak36CY2Eoj6CM9NyKVxgsWmTo', '6S4JuZlB666kRXoqmdKI8UGkJONSXiRRztzGtPTBsHaKX')


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
