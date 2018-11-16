from textblob import TextBlob
from twitter_collect import twitter_connection_setup


"""# Each word in the lexicon has scores for:
# 1)     polarity: negative vs. positive    (-1.0 => +1.0)
# 2) subjectivity: objective vs. subjective (+0.0 => +1.0)
# 3)    intensity: modifies next word?      (x0.5 => x2.0)"""


def collect(query):
    liste_tweet_text=[]
    liste_tweet=[]
    connexion = twitter_connection_setup.twitter_setup()
    tweets = connexion.search(query,language="french",rpp=10)
    for tweet in tweets:
        liste_tweet_text.append(tweet.text)
    return liste_tweet_text

#pb de genre
tweets=collect("macron")
print(tweets)
print(type(tweets))
str_tweets=",".join(tweets)
print(str_tweets)
print(type(str_tweets))
#list_tweets=str_tweets.split(" ")
#print(list_tweets)
#print(type(list_tweets))
""" il faut tous convertir en un tableau de mots car sinon on ne peut pas utiliser les modules de textblob"""

tweets_polarity=[]
for tweet in str_tweets.sentences:
    tweets_polarity.append(tweet.sentiment.polarity)
moyenne=sum(tweets_polarity)/len(tweets_polarity)

""""on def, tweet positif pour polarité>0.3, négatifs pour polarité<-0.3"""
positifs=[]
negatifs=[]
neutres=[]
for sentiment in tweets_polarity:
    if sentiment<-0.3:
        negatifs.append(sentiment)
    elif sentiment>0.3:
        positifs.append(sentiment)
    else:
        neutres.append(sentiment)

pourcentage_positif=len(positifs)/len(tweets_polarity)
pourcentage_negatif=len(negatifs)/len(tweets_polarity)
pourcentage_neutre=len(neutres)/len(tweets_polarity)

print("Percentage of positive tweets: {}%".format(pourcentage_positif*100))
print("Percentage of neutral tweets: {}%".format(pourcentage_negatif*100))
print("Percentage de negative tweets: {}%".format(pourcentage_neutre*100))
