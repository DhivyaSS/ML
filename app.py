import pandas as pd
import streamlit as st
import snscrape.modules.twitter as sntwitter

# Fetch Tweets
def fetch_tweets(query, max_tweets=100):
    tweets_list = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= max_tweets:
            break
        tweets_list.append([tweet.date, tweet.content])
    return pd.DataFrame(tweets_list, columns=["Date", "Tweet"])

# Streamlit App
st.title("Twitter Sentiment Analysis")
st.subheader("Search Tweets")

query = st.text_input("Enter a keyword or hashtag:")
max_tweets = st.slider("Number of Tweets to Fetch", 10, 500, 100)

if st.button("Fetch Tweets"):
    if query:
        df = fetch_tweets(query, max_tweets)
        st.write(f"Showing the latest {len(df)} tweets for **{query}**:")
        st.dataframe(df)
    else:
        st.error("Please enter a keyword or hashtag to search.")
      
