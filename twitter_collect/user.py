from twitter_collect import twitter_connection_setup

def user(user_id):
    api=twitter_connection_setup.twitter_setup()
    statuses = api.user_timeline(id=user_id, count=200)
    for status in statuses:
        print(status.txt)
    return statuses

