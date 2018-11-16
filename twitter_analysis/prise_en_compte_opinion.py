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

""""on def, tweet positif pour polarité>0.1, négatifs pour polarité<-0.1"""
def collect_opinion(query):
    #pb de genre
    tweets=collect(query)
    tweets_blob=TextBlob('.'.join(tweets))

    tweets_polarity=[]
    for sentences in tweets_blob.sentences:
        tweets_polarity.append(sentences.sentiment.polarity)
    moyenne=sum(tweets_polarity)/len(tweets_polarity)
    pos,neg,neutre=0,0,0
    for sentiment in tweets_polarity:
        if sentiment<-0.1:
            neg+=1
        elif sentiment>0.1:
            pos+=1
        else:
            neutre+=1
    pourcentage_positif=pos/len(tweets_polarity)*100
    pourcentage_negatif=neg/len(tweets_polarity)*100
    pourcentage_neutre=neutre/len(tweets_polarity)*100
    return([pourcentage_positif,pourcentage_negatif,pourcentage_neutre])
