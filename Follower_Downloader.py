import tweepy, time
import csv
# Consumer keys and access tokens, used for OAuth 
consumer_key = "xxxx"
consumer_secret = "xxxx"
access_token = "xxxx"
access_token_secret = "xxxx"

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the interface
api = tweepy.API(auth)

# creates cursor object
# insert the username of a person for whom you want followers and change datafile name
cursor = tweepy.Cursor(api.followers, screen_name="screenname", skip_status=True)
saveFile = open('followers.csv', 'a')

# write data in file as long as Twitter limit has not been reached
while True:
    try:
        for follower in cursor.items():       
            #print "follower = %s" % follower
            saveFile.write(str(follower.screen_name))
            saveFile.write('\n') 
        print "finished!"
        saveFile.close()
        break
    except tweepy.TweepError as e:
            print "error checking limits: %s" % e
            remain_search_limits = 0
            time.sleep(15*60)
