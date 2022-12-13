# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 21:09:39 2022

@author: twolf
burnerbot22
"""

import tweepy
import os
import requests
import logging
import time
from keys import consumer_key, consumer_secret, access_token , access_token_secret , bearer_token

auth = tweepy.OAuthHandler(consumer_key, consumer_secret )
auth.set_access_token(access_token, access_token_secret )
api  = tweepy.API(auth)
print(api.verify_credentials().screen_name)  

# def create_api():
#     consumer_key = os.getenv("CONSUMER_KEY")
#     consumer_secret = os.getenv("CONSUMER_SECRET")
#     access_token = os.getenv("ACCESS_TOKEN")
#     access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

#     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token, access_token_secret)
#     api = tweepy.API(auth, wait_on_rate_limit=True, 
#         wait_on_rate_limit_notify=True)
#     try:
#         api.verify_credentials()
#     except Exception as e:
#         logger.error("Error creating API", exc_info=True)
#         raise e
#     logger.info("API created")
#     return api

#client = tweepy.Client(bearer_token=bearer_token)

# client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

# client.create_tweet(text="This Tweet was Tweeted using Tweepy and Twitter API v2!")


# # api = tweepy.API(client)
# # print(api.verify_credentials().screen_name)

# response = client.create_tweet(
#     text="This Tweet was Tweeted using Tweepy and Twitter API v2!")
# #print(f"https://twitter.com/user/status/{response.data['id']}")




# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")

# user = api.get_user(screen_name='twitter')
# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
#    print(friend.screen_name)
   
   
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
    
    
# def tweetme(tweet):
    

        