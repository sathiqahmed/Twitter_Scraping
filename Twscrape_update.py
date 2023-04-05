import streamlit as st
import pandas as pd
import snscrape.modules.twitter as sntwitter
from pymongo import MongoClient
from PIL import Image
import json
import base64

#Page Configuration:
st.set_page_config(page_title="My Streamlit Application", page_icon=":smiley:")

st.title("Twitter Scraping")

Twitter_Picture= Image.open(r"C:\Users\win10\Desktop\Twitterscrapping\Twitter-scraping.jpg")
st.image(Twitter_Picture)

st.markdown("""* Twitter scraping refers to the process of extracting data from Twitter using automated tools.
* Twitter data can be scraped for various purposes, such as sentiment analysis, social media monitoring, and marketing research.
* Twitter API provides a way to access and retrieve data from Twitter, but it has some limitations in terms of data volume and access restrictions.
* Third-party tools such as Twint, Tweepy, and Scrapy can be used for scraping Twitter data in a more efficient and customizable way.
* Twitter scraping can raise ethical and legal concerns, such as privacy and copyright infringement, and should be done responsibly and within the boundaries of the Twitter terms of service..""")

st.title("Snscrape:")

st.markdown("""Snscrape is another approach for scraping information from Twitter that does not require the use of an API. Snscrape allows you to scrape basic information such as a user's profile, tweet content, source, and so on.

Snscrape is not limited to Twitter, but can also scrape content from other prominent social media networks like Facebook, Instagram, and others.

Its advantages are that there are no limits to the number of tweets you can retrieve or the window of tweets (that is, the date range of tweets). So Snscrape allows you to retrieve old data.



""")

#function.py
def scraping_tweets(hashtag,start_date,end_date,tweet_limit):
  tweet_list=[]    
  for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'{hashtag} since:{start_date} until:{end_date}').get_items()):
    data=[tweet.date,tweet.id,tweet.user.username,tweet.user.verified,tweet.rawContent,tweet.lang,tweet.source,tweet.url,tweet.likeCount,tweet.retweetCount]
    tweet_list.append(data)
    if i==tweet_limit-1:
      break
    
  return tweet_list


def create_df(tweet_list):
  tweet_data = pd.DataFrame(tweet_list, columns=["Date","Id","Username","Verified","Raw Content","Language","Source","URL","LikeCount","Retweet Count"])
  return tweet_data



with st.sidebar.form("input_form"):
        st.write("Enter the #hashtag and the Date_range to Scrape:")
        keyword = st.text_input("Hashtag") 
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")
        tweet_limit= st.number_input("Enter the No of Tweets")
        submit_button = st.form_submit_button(" click to Scrape")
    
# Scrape tweets
tweet = scraping_tweets(keyword, start_date, end_date, tweet_limit)   
tweet_data = create_df(tweet)
st.dataframe(tweet_data)
 
 # Download as csv
st.write("Saving dataframe as csv")
csv = tweet_data.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()
href = f'<a href="data:file/csv;base64,{b64}" download="tweet_data.csv">Download CSV File</a>'
st.markdown(href, unsafe_allow_html=True)
 
 
 # Download as JSON
st.write("Saving dataframe as json")
json_string = tweet_data.to_json(indent=2)
b64 = base64.b64encode(json_string.encode()).decode()
href = f'<a href="data:file/json;base64,{b64}" download="tweet_data.json">Download json File</a>'
st.markdown(href, unsafe_allow_html=True)

# Upload to mongoDB
if st.button("upload to MongoDB"):
    tweet = scraping_tweets(keyword, start_date, end_date, tweet_limit)
    tweet_data = create_df(tweet)
    client =MongoClient('mongodb://localhost:27017')
    db = client["twitter_db_streamlit"]
    collection = db['tweet']
    tweet_data_json= json.loads(tweet_data.to_json(orient='records'))
    collection.insert_many(tweet_data_json)
    st.success(str(tweet_limit)+ ' tweets' + ' uploaded to MongoDB')  