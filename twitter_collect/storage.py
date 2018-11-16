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
    tweets = connexion.search(query,language="french",rpp=1)
    for tweet in tweets:
        liste_tweet.append(tweet._json)     #pour recuperer json
    #print(liste_tweet)
    return liste_tweet

#tweet_test=collect_tweet("macron")[0]
#print(type(tweet_test))


#entrée: un tweet json, nom du fichier qui va être créée et où on va stocker le json
#sortie: lefichier avec le json




#entrée: tweets est un dico qui possede les attribut d'un tweet
def store_et_lavage_tweets(query,filename):                                   #pour enregistrer
    connexion = twitter_connection_setup.twitter_setup()
    tweets = connexion.search(query,language="french",rpp=1)               #on recupère juste un tweet
    tweet_lave={}
    tweet_lave['text']=tweets.text
    tweet_lave['id']=tweets.id
    tweet_lave['retweeted']=tweets.retweeted
    tweet_lave['teweet_count']=tweets.retweet_count
    tweet_lave['created_at']=tweets.creeated_at
    tweet_lave['hastags']=tweets.hashtags
    fichier=open(filename,"w")
    json.dump(tweet_lave,fichier)
    fichier.close()

#store_tweets(tweet_test, "test.json")
"""
def dataframe(query):
    connexion = twitter_connection_setup.twitter_setup()
    tweets = connexion.search(query,language="french",rpp=1)
    tweet_lave={}
    tweet_lave['text']=tweets.text
    tweet_lave['id']=tweets.id
    tweet_lave['retweeted']=tweets.retweeted
    tweet_lave['teweet_count']=tweets.retweet_count
    tweet_lave['created_at']=tweets.creeated_at
    tweet_lave['hastags']=tweets.hashtags
    Dataframe= pd.DataFrame(tweet_lave)
    return Dataframe

dataframe("président")
"""

#correction prof pour storage

def dataframe(query):
    connexion = twitter_connection_setup.twitter_setup()
    tweets = connexion.search(query,language="fr",rpp=100)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    data['len']= np.array([len(tweet.text) for tweet in tweets])
    data['ID']   = np.array([tweet.id for tweet in tweets])
    data['created_at'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['retweet_count']    = np.array([tweet.retweet_count for tweet in tweets])
    return data

