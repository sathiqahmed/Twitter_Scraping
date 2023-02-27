!pip install -q snscrape

#Import the Modulus Tools for Scraping
import snscrape.modules.twitter as sntwitter
import pandas as pd


#Give Which Tweets we want & how many
Username = "prime video IN"
Numbers= int(input())

#reate a Empty list for storing the items
Tweets_Data=[]

#Iterate the Collecting Items from there by using some Key words..
#When stop the collection if condition becomes satisfied

for tweet in sntwitter.TwitterSearchScraper(Username).get_items():
 if len(Tweets_Data)==Numbers:
     break
  
 Tweets_Data.append ([tweet.date,tweet.id,tweet.url,tweet.content,tweet.user,tweet.replyCount,tweet.retweetCount,tweet.lang,tweet.source,tweet.likeCount])  

#Convert a list into data frame by using Pandas Lib..
df = pd.DataFrame(Tweets_Data, columns = ["DATE","ID","URL","CONTENT","USER","REPLYCOUNT","RETWEETCOUNT","LANGUAGE","SOURCE","LIKECOUNT"])  
print(df)
df.to_csv('Twitter Scraping->prime video IN .csv', index = False)
