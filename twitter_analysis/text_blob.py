from textblob import TextBlob
from twitter_collect import twitter_connection_setup

def collect(query):
    liste_tweet_text=[]
    liste_tweet=[]
    connexion = twitter_connection_setup.twitter_setup()
    tweets = connexion.search(query,language="french",rpp=10)
    for tweet in tweets:
        liste_tweet_text.append(tweet.text)
    return liste_tweet_text

list_tweet_text=collect("macron")
print(type(list_tweet_text))
str_tweets=",".join(list_tweet_text)
print(str_tweets)
print(type(str_tweets))

wordlist=TextBlob(str_tweets)
print(wordlist.words)
wordlist_unique=set(wordlist)
                #on veut les mots qui n'apparaissent qu'une fois

