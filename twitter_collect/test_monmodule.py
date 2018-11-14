import pytest
from twitter_collect import twitter_connection_setup
#il faut importer le fichier à tester

def test_connect():
    assert twitter_connection_setup.twitter_setup() != None
#sythaxe, on a nom fichier.fonction ()
