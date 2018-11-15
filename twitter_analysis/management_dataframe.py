import numpy as np
from twitter_collect import storage

"""notre dataframe comorte 6 colonnes, dans l'ordre: 
text, id, retweets, retweet_count, created_at et hashtag"""

query="candidat"

data=storage.dataframe(query)   #on forme un dataframe
def analyser_info(data):
    rt_max  = np.max(data['retweet_count'])
    rt  = data[data.retweet_count == rt_max].index[0]
    print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
    print("Number of retweets: {}".format(rt_max))
    print("{} characters.\n".format(data['len'][rt]))
    hashtag_max=np.max(data['hasthag'].value_counts())
    hashtag=data[data.hashtag==hashtag_max].index[5]
    print("The most used hasthag is:" + hashtag )


