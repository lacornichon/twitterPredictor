import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from twitter_collect import twitter_connection_setup
import json

query="macron"

def collect_tweet(query):
    liste_tweet=[]
    connexion = twitter_connection_setup.twitter_setup()
    tweets = connexion.search(query,language="french",rpp=100)
    for tweet in tweets:
        liste_tweet.append(tweet._json)     #pour recuperer json
    print(liste_tweet)
    return liste_tweet

tweet_test=collect_tweet("macron")[0]


#entrée: un tweet json, nom du fichier qui va être créée et où on va stocker le json
#sortie: lefichier avec le json

def store_tweets(tweets,filename):
    fichier=open(filename,"w")
    json.dump(tweets,fichier)
    fichier.close()

store_tweets(tweet_test, "test.json")
