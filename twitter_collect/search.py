from twitter_collect import twitter_connection_setup

liste_tweet_text=[]
liste_tweet=[]

#entrer : une requete
#sortie: un tableau des texts des 100 derniers tweets ou apprarrait la requete, et les tweet avec toutes les info(json
def collect(query):
    connexion = twitter_connection_setup.twitter_setup()
    tweets = connexion.search(query,language="french",rpp=1)
    for tweet in tweets:
        liste_tweet_text.append(tweet.text)
        print(tweet.text)
        liste_tweet.append(tweet._json)
    print(tweets)
    return liste_tweet, liste_tweet_text


print(collect("@Emmanuelmacron"))


