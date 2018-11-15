from twitter_collect import twitter_connection_setup

 #entrée: user_id, càd l'id d'un compte twiteer
 #sortie:le tableau contenant tout les 200 dernier tweets de ce compte
def user(user_id):
    api=twitter_connection_setup.twitter_setup()
    statuses = api.user_timeline(id=user_id, count=200)
    for status in statuses:
        print(status.text)
    return statuses

user ("trump")
