# Importing the Tweet Processing Python File
import TweetExtractor

# Declaring the required filtering strings for Tweets
hash_tags = ['Dalhousie University','Canada','University','Halifax','Canada Education','Moncton','Toronto']

# Fetching Tweets into a local file 
TweetExtractor.getTweets(hash_tags)