from twitter_collect import user
from twitter_collect import twitter_connection_setup
api= twitter_connection_setup.twitter_setup()

#pour convertir @Id en id_user utiliser l'url  https://tweeterid.com/

#dico contient
def get_retweets_of_candidate(num_candidate):
    screen_name_candidat = recuperer_candidate(num_candidate)  #verif screen
    tweets=api.user_timeline(screen_name=screen_name_candidat, count=200)
    for tweet in tweets:
        if tweet.retweeted:
            retweets=api.retweets(tweet.id)
    return retweets



def recuperer_candidate(num_candidate):
    path_keyword= "C:/Users/valen/Documents/programmation/twitterPredictor/CandidateData/keywords_candidate_" + str(num_candidate) +".txt"
    fichier_keyword = open("path_keyword","r")
    contenu_keyword=fichier_keyword.read()
    keyword= contenu_keyword.split(" ")
    return keyword[0] + keyword[1]                                       #le premier mot de chquaque fichier est le prenom puis nom





public_tweets = api.search("stackoverflow")
for tweet in public_tweets:
    print(api.retweets(tweet.id))
