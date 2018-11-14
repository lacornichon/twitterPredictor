import tweepy
from twitterPredictor import credentials

print(credentials.CONSUMER_KEY)

def twitter_setup():
    auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_SECRET)
    api = tweepy.API(auth)
    return (api)


twitter_setup()
