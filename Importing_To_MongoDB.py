# importing pymongo for feeding Tweets in MongoDB
from pymongo import MongoClient
import json

# Eastablishing the Connection 
db_client = MongoClient('localhost', 27017)

# Creating a Fresh Database for Storing Tweets
db = db_client['tweets_db']

# Creating a Fresh Collection which acts analogous to a table in Relational DBMS
Tweets_Collection = db['my_tweet_collection']


# Importing Tweets from JSON file into a list of dictionaries
tweets = []
for line in open('Cleaned_Tweets.json', 'r'):
    tweets.append(json.loads(line))


# Refershing the Collection Values
Tweets_Collection.remove()

# Stotring the Tweets into MongoDB
result = Tweets_Collection.insert_many(tweets)


# Closing the MongoDB Connection
db_client.close()