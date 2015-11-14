#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import re
import time

#Twitter API credentials
access_key = "xxxx"
access_secret = "xxxx"
consumer_key = "xxxx"
consumer_secret = "xxxx"


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	print screen_name
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)

	#Fixes no tweet bug
	if len(alltweets) == 0:
		print "%s has no tweets" % (screen_name)
		return

	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["text"])
		writer.writerows(outtweets)
	

	pass

#iterates through a csv file of names 
with open('names.csv') as namescsv:
	namereader = csv.reader(namescsv)
	for row in namereader:
		for cell in row:
			#cleans non-alpha characters
			cell = re.sub(r'[^\w=]', '',cell)
			#executes function
        	get_all_tweets(cell)
        	print "Done with %s" % (cell)
        	#Pauses script for 60 sec
        	print "Waiting Period"
        	time.sleep(60)

print "Done downloading all tweets."
