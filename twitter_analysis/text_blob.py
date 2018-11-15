from textblob import TextBlob
from twitter_collect import twitter_connection_setup

def collect(query):
    liste_tweet_text=[]
    liste_tweet=[]
    connexion = twitter_connection_setup.twitter_setup()
    tweets = connexion.search(query,language="french",rpp=10)
    return tweets

tweets=collect("macron")

wordlist=[]
for word in tweets.words:
    wordlist.append(word)
word_unique=set(wordlist)                #on veut les mots qui n'apparaissent qu'une fois

