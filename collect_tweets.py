import json
import time
import tweepy

consumer_key =  'QvlNGKVPodDeDRIsJW4fEjd2H'
consumer_secret = 'QfKC7Xqb9GFT2X1zFFUg7zsRcC0bGsIqOFmP1yK890Y5YBBzrV'
access_token = '119028101-6DFJlu1MkQsxzfOj5Iy3EO4GFiYjYDYvI3CVHKd8'
access_token_secret = 'uzoZir60wbJEE318HV0G9GupMk39hePCZsKlw4Wru7I1H'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = []
save_file = open('tweets_english.json','a')

class StreamListener(tweepy.StreamListener):
	count=0
	
	def __init__(self, api):
		self.api = api
		super(tweepy.StreamListener, self).__init__()
		self.save_file = tweets
		self.start_time = time.time()
		self.time_limit = 7200
		self.count = 0

	def on_data(self, tweet):
		self.count+=1
		if self.count%10==0:
			time.sleep(5)
		if time.time()-self.start_time<=self.time_limit:
			self.save_file.append(json.loads(tweet))
			print(tweet)
			save_file.write(str(tweet))
			return True
		else:
			return False

		# self.count += 1
		# if self.count == 10:
		# 	self.count = 0
		# 	print("Sleeping")
		# 	time.sleep(10)

	def on_error(self, status_code):
		print("status_code = ",status_code)
		if status_code == 420:
			return False

stream_listener = StreamListener(api)
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(locations=[-180,-90,180,90])
