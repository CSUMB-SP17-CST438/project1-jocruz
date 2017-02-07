import requests
import json 
# import llaves
import tweepy
import random
import os


class tweet:
    def __init__(self, tweet,user,link):
        self.t = tweet
        self.u = user
        self.l = "http://twitter.com/statuses/" + link
        
    def __str__(self):
        return "tweet: " + self.t +'\n' + "user: " + self.u + "\n" + "Link: " + self.l
        
def getTweet():
    auth = tweepy.OAuthHandler(os.environ['twitKey'],os.environ['twitSecret'])
    auth.set_access_token("571539197-KifHz80JlMf9gCWTHMIHPpeTlGAa60l2SOxdtsS7","qaucmJM9xtQKbZxHiNloaUBXhXXYGc8w5NRqb8iccgZle")

    api = tweepy.API(auth)
    new_tweets = api.search(q="puppers OR pups -filter:retweets AND -filter:replies AND -filter:links AND -filter:twimg", count = "100")
    size = len(new_tweets)
    i = random.randint(0,size)
    text = json.dumps(new_tweets[i].text)
    text = text[1:-1]
    user = json.dumps(new_tweets[i].user.screen_name)
    user = user[1:-1]
    link = json.dumps(new_tweets[i].id_str)
    link = link[1:-1]
    randomtweet = tweet(text,user,link)
    return randomtweet
    
    
tw = getTweet()
print(tw)