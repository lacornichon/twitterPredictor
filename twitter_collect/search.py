from twitter_collect import twitter_connection_setup

def collect(query):
    api= twitter_connection_setup.twitter_setup()
    tweets=api.search(query,rpp=5)  #rpp max 100
    for tweet in tweets:
        print(tweet.text)

collect("@Emmanuelmacron")

