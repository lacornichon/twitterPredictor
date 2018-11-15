from twitter_collect import twitter_connection_setup

#entrer : une requete
#sortie: un tableau des texts des 100 derniers tweets ou apprarrait la requete, et les tweet avec toutes les info
def collect(query):
    api= twitter_connection_setup.twitter_setup()
    tweets=api.search(query,rpp=100)  #rpp max 100
    liste_tweet=[]
    tweets=[]
    for tweet in tweets:
        liste_tweet.append(tweet.text)
        print(liste_tweet)
    return liste_tweet, tweets

collect("@Emmanuelmacron")

