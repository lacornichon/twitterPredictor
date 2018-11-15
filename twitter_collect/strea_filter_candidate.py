from twitter_collect import stream
#pour convertir @Id en id_user utiliser l'url  https://tweeteri

def ecoute_candidate(candidate):
    return print(stream.collect_by_streaming(candidate))

#ne sais pas comment faire pour les reponses
