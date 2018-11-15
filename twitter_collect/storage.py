import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from twitter_collect import twitter_connection_setup
import json

#object Status: {Satutus...., _json: {....}}

#etape 1,on recupere le json sous la forme d'un dico
def collect_tweet(query):
    liste_tweet=[]
    connexion = twitter_connection_setup.twitter_setup()
    tweets = connexion.search(query,language="french",rpp=100)
    for tweet in tweets:
        liste_tweet.append(tweet._json)     #pour recuperer json
    #print(liste_tweet)
    return liste_tweet

#tweet_test=collect_tweet("macron")[0]
#print(type(tweet_test))


#entrée: un tweet json, nom du fichier qui va être créée et où on va stocker le json
#sortie: lefichier avec le json

def lavage(tweets):
    tweet_lave={}
    tweet_lave['text']=tweets.text
    tweet_lave['id']=tweets.id
    tweet_lave['retweeted']=tweets.retweeted
    tweet_lave['teweet_count']=tweets.retweet_count
    tweet_lave['created_at']=tweets.creeated_at
    tweet_lave['hastags']=tweets.hashtags
    return(json.dumps(tweet_lave))   #pour convertir dico en json



#entrée: tweets est un dico qui possede les attribut d'un tweet
def store_et_lavage_tweets(tweets, filename):
    #tweet_dico=json.load(tweets)  pour convertir json en dico
    tweets_lavé=lavage(tweets)
    fichier=open(filename,"w")
    json.dump(tweets_lavé,fichier)
    fichier.close()

#store_tweets(tweet_test, "test.json")
def dataframe(tweets):
    tweet_propre=lavage(tweets)
    Dataframe= pd.DataFrame(tweet_propre)
    return Dataframe
