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
    return tweets

tweets=collect("macron")
