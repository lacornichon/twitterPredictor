from twitter_collect.search import collect

"""
  Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently"""

keywords=[]
hastag=[]

def get_candidate_(num_candidate, file_path):
    try:
        file_hashtag_candidate='/Users/valen/Documents/programmation/twitterPredictor/'+str(file_path)+'/hastag_candidate_'+str(num_candidate)+'.txt'
        file_keywords_candidate='/Users/valen/Documents/programmation/twitterPredictor/'+str(file_path)+'/keywords_candidate_'+str(num_candidate)+'.txt'
        fichier_hashtag = open(file_hashtag_candidate, "r")
        fichier_keywords = open(file_keywords_candidate, "r")
        for line in fichier_hashtag.readlines():
            line_str=str(line)
            hastag=line.split(" ")
            hastag.pop()
            #tweets=(collect(line))
            #for tweet in tweets:
                #print(tweet.text)
        for line in fichier_keywords.readlines():
            line_str=str(line)
            keywords=line.split(" ")
            keywords.pop()
            #tweets=(collect(line))
            #for tweet in tweets:
        return keywords, hastag
    except IOError as error:
        print(error)

print (get_candidate_(1,'CandidateData'))

#entrée num-candidate, file_path
#sortie : dico de clé:mot clé et associé aux 200 dernier tweets contenant mot clé

tweets_keywords={}
tweets_hastag={}

def get_candidate_queries(num_candidate, file_path):
    queries_hastag=[]
    queries_keywords=[]
    queries_keywords=get_candidate_(num_candidate,file_path)[0]
    queries_hastag=get_candidate_(num_candidate,file_path)[1]
    for k in queries_keywords:
       tweets_keywords[k]=collect(k)[1]
    for h in queries_hastag:
        tweets_hastag[h]=collect(h)[1]
    print(tweets_hastag)
    print(tweets_keywords)
    return tweets_keywords, tweets_hastag

print(get_candidate_queries(1,'CandidateData'))
