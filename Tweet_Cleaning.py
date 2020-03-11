# Importing required data processing libraries
import pandas as pd
import re

# Reading the JSON file in column oriented fashion
tweets_data = pd.read_json('Extracted_Tweets.json',orient='columns',lines=True)

# Dividing the data into column lists for flexible processing
Created_at = list(tweets_data['created_at'].values)
IDs = list(tweets_data['id'].values)
Texts = list(tweets_data['text'].values)
Truncated = list(tweets_data['truncated'].values)
In_reply_to_user_id = list(tweets_data['in_reply_to_user_id'].values)
In_reply_to_screen_name = list(tweets_data['in_reply_to_screen_name'].values)
Reply_Count = list(tweets_data['reply_count'].values)
Retweet_Count = list(tweets_data['retweet_count'].values)
Favourite_Count = list(tweets_data['favorite_count'].values)
Favourited = list(tweets_data['favorited'].values)
Retweeted = list(tweets_data['retweeted'].values)
Language = list(tweets_data['lang'].values)
Geo = list(tweets_data['geo'].values)
Place = list(tweets_data['place'].values)




# Cleaning the date by removing the timestamp
loop_len = len(Created_at)
for i in range(loop_len):
        temp = str(Created_at[i])
        Created_at[i] = temp[:10]
        
# Defining a method for removing the URL of Tweet
def remove_URL(mystr):
    while "https" in mystr or "http" in mystr:
        if 'https' in mystr:
            i = mystr.find('https')
            mystr_refined = mystr[:i]
            stop=i
            for i in range(i,len(mystr)):
                if mystr[i]!=' ':
                    stop+=1
                else:
                    break
            mystr = mystr_refined + mystr[stop:]

        elif 'http' in mystr:
            i = mystr.find('http')
            mystr_refined = mystr[:i]
            stop=i
            for i in range(i,len(mystr)):
                if mystr[i]!=' ':
                    stop+=1
                else:
                    break
            mystr = mystr_refined + mystr[stop:]
    
    return mystr
 
# Method for eliminating Imogis       
# Emoticons ASCII value taken from https://altcodeunicode.com/alt-codes-emoticons-cat-faces-gesture-symbols/       
def eliminate_emoticons(tweet):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"  
        u"\U0001F1E0-\U0001F1FF"  
        u"\U00002500-\U00002BEF"  
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f" 
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', tweet)
            
            

# Method for cleaning the Tweets 
for i in range(loop_len):
    temp = str(Texts[i])
    temp = temp.replace('#','')
    temp = temp.replace('@','')
    temp = remove_URL(temp)
    temp = eliminate_emoticons(temp)
    Texts[i] = temp
    



# Declaring the final list to be saved
Tweet_list = []

loop_length = len(IDs)

# Populating the final list with cleaned data
for index in range(loop_length):
    temp = []
    temp.append(Created_at[index])
    temp.append(IDs[index])
    temp.append(Texts[index])
    temp.append(Truncated[index])
    temp.append(In_reply_to_user_id[index])
    temp.append(In_reply_to_screen_name[index])
    temp.append(Reply_Count[index])
    temp.append(Retweet_Count[index])
    temp.append(Favourite_Count[index])
    temp.append(Favourited[index])
    temp.append(Retweeted[index])
    temp.append(Language[index])
    temp.append(Geo[index])
    temp.append(Place[index])
    
    Tweet_list.append(temp)  



# Saving Tweets along with their MetaData in another JSON file
cols = ['Created_at','Tweet_ID','Tweet','Truncated','In_reply_to_user_id','In_reply_to_screen_name','Reply_Count','Retweet_Count','Favourite_Count','Favourited','Retweeted','Language','Geo','Place']
Tweets_df = pd.DataFrame(Tweet_list,columns=cols)

Tweets_df.to_json('Cleaned_Tweets.json',orient='records',lines=True)
        







