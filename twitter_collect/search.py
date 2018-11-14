from twitter_collect import twitter_connection_setup

def collect():
    api= twitter_connection_setup.twitter_setup()
    tweets=api.search("macron",language="french",rpp=10)
    for tweet in tweets:
        print(tweet.text)

collect()

