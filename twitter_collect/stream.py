import tweepy
from tweepy.streaming import StreamListener
from twitter_collect import twitter_connection_setup


class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        if  str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True




def collect_by_streaming(query):

    connexion = twitter_connection_setup.twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    stream.filter(track=[query])

collect_by_streaming("trump")

