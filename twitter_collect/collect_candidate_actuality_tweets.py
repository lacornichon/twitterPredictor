from twitter_collect import search
from twitter_collect import twitter_connection_setup

twitter_api=twitter_connection_setup.twitter_setup()

def get_tweets_from_candidates_search_queries(queries,twitter_api):
    tweets=[]
    for q in queries:
        tweets.append(search.collect(q))
    return tweets


