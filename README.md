Read Me

Twitter Study Tools

Author: Ian English

These tools are intended to be used to download data from Twitter in order to study for research purposes.

It is recommended that you use Linux when working with these programs as they have not been tested on other systems.

Setup

Install Python, Tweepy, and OAuth
Get access keys from Twitter (https://apps.twitter.com/)
jEdit (Recommended) - Edits csv files

Tweet_Downloader_Iterating.py

This program is based on Yanofsky’s program. 
https://gist.github.com/yanofsky/5436496

It will take a list of Twitter screen names and download the tweets of each to a separate file. At the end, it will print statistical information about the data. 

To use:
	Create a file called “names.csv” in your home directory that has the raw twitter user-names. No “@” symbols or numerical IDs.
	Enter the Twitter keys into the 4 strings.
	Run the program under administrator or sudo in a terminal.
	It will give information as to what it is working on.
	BE PATIENT. Because of Twitter’s use restrictions, after every user downloaded a 60 second time out will occur. 
	A csv file will be created in your home directory for each user you download.
	Once the program is done, it will offer statistics and exit.

Follower_Downloader.py

This program is an altered version of Karolina Slywester’s program, politicalFollowers.py.

It will download all of the followers of a Twitter user into a csv file. 

To use:
	Enter the Twitter keys into the 4 strings.
	Open the program in a text editor and change screen_name in line 20 to the user you want to use. Save.
	Run program.
	A csv file will be created that will be readable by  Tweet_Downloader_Iterating.py, be sure to change the name from “followers.csv” to “names.csv”. 
