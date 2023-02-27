#IMPORT MATERIAL TOOLS:
import streamlit as st
import pandas as pd
from PIL import Image
import snscrape.modules.twitter as sntwitter
from datetime import datetime
import numpy as np
import json
import base64
from pymongo import MongoClient

#INTRODUCTION:
st.set_page_config(page_title="My Streamlit Application", page_icon=":smiley:")

Twitter_Picture= Image.open(r"C:\Users\win10\Desktop\Twitterscrapping\twtscr.jpg")
st.image(Twitter_Picture)

st.title("TWITTER SCRAPING")

st.header("Twitter Scraping:")

st.markdown("""* Twitter scraping refers to the process of extracting data from Twitter using automated tools.

* Twitter data can be scraped for various purposes, such as sentiment analysis, social media monitoring, and marketing research.

* Twitter API provides a way to access and retrieve data from Twitter, but it has some limitations in terms of data volume and access restrictions.

* Third-party tools such as Twint, Tweepy, and Scrapy can be used for scraping Twitter data in a more efficient and customizable way.

* Twitter scraping can raise ethical and legal concerns, such as privacy and copyright infringement, and should be done responsibly and within the boundaries of the Twitter terms of service..""")

st.subheader("Prime video IN Tweets:")

st.markdown("""* Prime Video is a video streaming service offered by Amazon that allows users to watch movies, TV shows, and original content.
* Prime Video has its official Twitter account (@PrimeVideo) which shares updates, recommendations, and behind-the-scenes content related to its offerings.
* Users can also tweet about their experience with Prime Video using the hashtag #PrimeVideo or by mentioning the official account.
* Prime Video also engages with its audience on Twitter by responding to queries, addressing complaints, and running social media campaigns.
* Prime Video's Twitter presence plays a significant role in its marketing and customer engagement strategies, as Twitter is a popular platform for entertainment-related discussions and recommendations.""")

#IMPORT SCRAPED DATA SET OF TWITTER(primevideo IN):


st.subheader("Scraping Tweets From Twitter By Using Snscrape: ")

df = pd.read_csv('Twitter Scraping-_prime video IN .csv')
submit = st.button('**Click to show the Dataset**')
if submit:
    st.dataframe(df)
    

#DOWNLOAD SCRAPED DATASET:
st.subheader("Download The Scraped Tweets Dataset: ")

Twitter_Picture1= Image.open(r"C:\Users\win10\Desktop\Twitterscrapping\scraping.jpg")
st.image(Twitter_Picture1)


st.download_button("**Download CSV File**",df.to_csv(),
                   file_name='SCRAPED DATA',mime='csv')
st.download_button("**Download json File**",df.to_json(),
                   file_name='SCRAPED DATA',mime='json')

#FILTERED BY HASHTAG:

st.subheader("HASHTAG FILTER:")


Twitter_Picture2= Image.open(r"C:\Users\win10\Desktop\Twitterscrapping\twitter-hashtag.jpg")
st.image(Twitter_Picture2)


hashtag = st.text_input('**Enter Hashtag:**')

def filter_data(hashtag, df):
    filtered_df = df[df['CONTENT'].str.contains(hashtag, na=False)]
    return filtered_df

if hashtag:
    filtered_df = filter_data(hashtag,df)
    st.write(filtered_df)
    
  
#DOWNLOAD HASHTAG FILTERED DATA:
    
st.text("Download Filtered Data Given Below")  

if st.button('**Download as CSV**'):
   
   csv = filtered_df.to_csv(index=False)
   b64 = base64.b64encode(csv.encode()).decode()
   href = f'<a href="data:file/csv;base64,{b64}" download="Hashtag Filtered Dataset.csv">Download CSV File</a>'
   st.markdown(href, unsafe_allow_html=True)

if st.button("**Download as JSON**"):
    filtered_data_json = filtered_df.to_json(orient='records')
    b64 = base64.b64encode(filtered_data_json.encode()).decode() 
    href = f'<a href="data:application/json;base64,{b64}" download="Hashtag Filtered Dataset.json">Download JSON File</a>'
    st.markdown(href, unsafe_allow_html=True)

#DATE RANGE FILTERING PROCESS:

st.header('Date Range Filter')


Twitter_Picture3= Image.open(r"C:\Users\win10\Desktop\Twitterscrapping\date.jpg")
st.image(Twitter_Picture3)

#CHANGE THE DATE FORMAT:

df['DATE'] = pd.to_datetime(df['DATE'])
Start_Date = st.date_input('**Enter The Start Date**:',value= df["DATE"].min().date())
Start_Date = pd.to_datetime(Start_Date).strftime("%Y-%m-%d %H:%M:%S")


End_Date = st.date_input('**Enter the End date**:',value= df["DATE"].max().date())
End_Date = pd.to_datetime(End_Date).strftime("%Y-%m-%d %H:%M:%S")

#DATE FILTERING PROCESS:

filtered_date = df[(df["DATE"] >= Start_Date) & (df["DATE"] <= End_Date)]
st.write("Number of tweets:",filtered_date.shape[0])
st.dataframe(filtered_date)



#ADDING DOWNLOAD OPTION AS CSV FILE:

if st.button("**Download Filtered as CSV**"):
   
   csv = filtered_date.to_csv(index=False)
   b64 = base64.b64encode(csv.encode()).decode()
   href = f'<a href="data:file/csv;base64,{b64}" download="Date_Filtered_Twitter_Scrape.csv">Download CSV File</a>'
   st.markdown(href, unsafe_allow_html=True)

#ADDING DOWNLOAD OPTION AS JSON FILE:

if st.button("**Download Filtered as JSON**"):
    filtered_data_json = filtered_date.to_json(orient='records')
    b64 = base64.b64encode(filtered_data_json.encode()).decode() 
    href = f'<a href="data:application/json;base64,{b64}" download="Date_Filtered_Twitter_Scrape.json">Download JSON File</a>'
    st.markdown(href, unsafe_allow_html=True)














  


    

















   


    
















    
