import time

import tweepy

from credentials import *
from web_scraper import devotional_content_retrieval

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def tweet_devotional():
    tweet_lines = devotional_content_retrieval()

    print(tweet_lines[0])
    try:
        last_tweet = api.update_status(tweet_lines[0])
    except tweepy.TweepError as e:
        print(e.reason)
        return [e.reason]

    # create a loop to iterate over lines
    for tweet_line in tweet_lines[1:]:
        try:
            print(tweet_line)
            last_tweet = api.update_status(tweet_line, last_tweet.id)
        except tweepy.TweepError as e:
            print(e.reason)
        time.sleep(10)

    return tweet_lines
