from twitter_collect import search
from twitter_collect import storage
from pytest import *



def test_collect():
    tweets = search.collect("macron")[0]
    data = storage.dataframe(tweets)
    assert 'tweet_textual_content' in data.columns
