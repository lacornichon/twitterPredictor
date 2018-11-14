from twitter_collect import search
from twitter_collect import twitter_connection_setup

twitter_api=twitter_connection_setup.twitter_setup()

""""étant donnée une liste queries de requêtes (de type search) et une instance de connexion twitter_api récupére et 
renvoie les tweets répondant aux différentes requêtes."""

def get_tweets_from_candidates_search_queries(queries,twitter_api):
    tweets={}
    try:
        for q in queries:
            tweets[q]=search.collect(q)
        return tweets
    except TweepError:
		print(TweepError.response.text)
	except RateLimitError:
        print("RateLimitError")

