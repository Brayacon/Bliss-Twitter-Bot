import tweepy 
import time
import os
import config
from os import environ


#Cloud Deploy
#Access token & access token secret
# ACCESS_KEY = environ['ACCESS_KEY']
# ACCESS_SECRET = environ['ACCESS_SECRET']

# #Consumer API keys
# CONSUMER_KEY =  environ['CONSUMER_KEY']
# CONSUMER_SECRET = environ['CONSUMER_SECRET']

# auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
# auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)




# Local Host 
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)






api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify=True)
user = api.me()


search = 'Kenya'
nrTweets = 500 #number of tweets you wanna pull back


FILE_NAME = 'last_seen_id.txt'
 
def ChangeSearch(i):
	search = get_trend()
	my_tags = ['GeeksyR', 'GeeksyNerd', 'brad_yalo']
	return my_tags[i]



def like_n_retweet():
	my_tags = ['GeeksyR', 'GeeksyNerd', 'brad_yalo',]

	for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
		try:
			# print(search) 
			# Reply
			reply_to_tweets(tweet.user.screen_name, tweet.id)
			time.sleep(5)


			#like
			tweet.favorite()
			print("liked")
			time.sleep(5)

			#retweet
			tweet.retweet()
			print("retweeted")
			time.sleep(100)

			


		except tweepy.TweepError as e:
			print("error:",e.reason)
		except StopIteration:
			break




def get_trends():
	trends1 = api.trends_place(1) # from the end of your code
	# trends1 is a list with only one element in it, which is a 
	# dict which we'll put in data.
	data = trends1[0] 
	# grab the trends
	trends = data['trends']
 	# grab the name from each trend
	names = [trend['name'] for trend in trends]
	# put all the names together with a ' ' separating them
	trendsName = ' '.join(names)
	print(name)


def get_trend():
	trends1 = api.trends_place(1) # from the end of your code
	# trends1 is a list with only one element in it, which is a 
	# dict which we'll put in data.
	data = trends1[0] 
	# grab the trends
	trends = data['trends']
 	# grab the name from each trend
	names = [trend['name'] for trend in trends]
	# put all the names together with a ' ' separating them
	trendsName = ' '.join(names)
	print(names[0])


def tweet_reply(file_name):
	f_read = open(file_name, 'r')
	tweet = int(f_read.read().strip())
	f_read.close()
	return tweet




def retrieve_promo_handles(file_name):
	f_read = open(file_name, 'r')
	promo_handles = int(f_read.read().strip())
	f_read.close()
	return promo_handles



def retrieve_last_seen_id(file_name):
	f_read = open(file_name, 'r')
	last_seen_id = int(f_read.read().strip())
	f_read.close()
	return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
	f_write = open(file_name, 'w')
	f_write.write(str(last_seen_id))
	f_write.close()
	return

# def reply_to_tweets():
# 	print('retrieving and replying to tweets', flush = True)

# 	last_seen_id = retrieve_last_seen_id(FILE_NAME)

# 	mentions  = api.mentions_timeline(last_seen_id, tweet_mode = 'extended')
# 	print("mentions: " + str(mentions))
# 	print("last_seen_id: " + str(last_seen_id))
# 	for mention in reversed(mentions):
# 		print(str(mention.id) + '-' + mention.full_text, flush = True)
# 		last_seen_id = mention.id
# 		store_last_seen_id(last_seen_id, FILE_NAME)

# 		if search in mention.full_text.lower():
# 			print("found " + search, flush = True)
# 			print( "responding back to " + mention.user.screen_name + "..." , flush = True)
# 			replyee =  mention.user.screen_name 
# 			api.update_status('@', +replyee + "Hey Please follow me for daily retweets " + "@"+user + "@GeeksyR", mention.id)

def reply_to_tweets(screen_name, tweet_id):
	print(screen_name)
	print('retrieving and replying to tweets', flush = True)
	api.update_status('@'+ screen_name +' '+ 'Hey Please follow me for daily retweets and likes \n FOLLOW  @GeeksyR too. \n Use #GeeksyNerd for likes and retweets ', tweet_id)





while True:
	like_n_retweet()