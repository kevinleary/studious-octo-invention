# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 21:09:39 2022

@author: twolf, mattheidelbaugh, kevinleary
burnerbot22
"""

import tweepy
import os
import json
import logging

with open("creds.json", "r") as f:
    creds = json.load(f)

access_token = creds["access_token"]
access_token_secret = creds["access_token_secret"]
consumer_key = creds["consumer_key"]
consumer_secret = creds["consumer_secret"]

client = tweepy.Client(access_token=access_token, access_token_secret=access_token_secret, consumer_key=consumer_key, consumer_secret=consumer_secret)
client.create_tweet(text="wolf eats farts")
        