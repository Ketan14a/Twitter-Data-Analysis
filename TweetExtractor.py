# Importing Tweepy Library
from tweepy import Stream, OAuthHandler, streaming
import sys
TweetListener = streaming.StreamListener

'''

A reference of an analogous Twitter task has been taken from a YouTube video. But the program has not been copied entirely
Reference Link: https://youtu.be/wlnx-7cm4Gg

'''



#Class for Twitter Authentication and connection verification
class TweetsExtractor():

	def stream_tweets(self, file_name, hash_tag_list):
		listener = MyListener(file_name)
		auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
		
		auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

		stream = Stream(auth, listener)
		stream.filter(track=hash_tag_list)

# Class for retrieving Tweets from Tweepy
class MyListener(TweetListener):

	def __init__(self, file_name1):
		self.file_name = file_name1
		self.count=0

	def check_count(self):
		if self.count>2000:
			return
		else:
			print(self.count)
			self.count+=1


	def on_data(self, data):
		try:
			self.check_count()
			with open(self.file_name,'a') as f:
				f.write(data)
		except BaseException as e:
			print(e)

		return True
		
       
	

ACCESS_TOKEN = "1222330761723961344-MWiZ8rjxrV1IAjKUP9cvNLSbGzmAKN"
ACCESS_TOKEN_SECRET = "23hWAHUgti8SHIv8ZupAzE5RtkeZ7c96zsSZJvcliWrkS"
CONSUMER_KEY = "9xxKEK21NVEQ5MoURYoLhKuj6"
CONSUMER_SECRET = "74iSEWetMNU4PhLk13dBXbzehM0nIlXBBZQT6PfpWomeDc0jQ2"




def getTweets(filter_strings):
	myFile = 'Extracted_Tweets_File.json'
	Tweet_counter=0
	ts = TweetsExtractor()
	ts.stream_tweets(myFile,filter_strings)


