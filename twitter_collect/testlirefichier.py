from twitter_collect.search import collect

"""Extrait les tweets à l'aide de la fonction collect à partir des hashtags et des mots-clés du candidat en question
  Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently"""

def get_candidate_queries(num_candidate, file_path):
    try:
        file_hashtag_candidate='/Users/valen/Documents/programmation/twitterPredictor/'+str(file_path)+'/hastag_candidate_'+str(num_candidate)+'.txt'
        file_keywords_candidate='/Users/valen/Documents/programmation/twitterPredictor/'+str(file_path)+'/keywords_candidate_'+str(num_candidate)+'.txt'
        fichier_hashtag = open(file_hashtag_candidate, "r")
        fichier_keywords = open(file_keywords_candidate, "r")
        for line in fichier_hashtag.readlines():
            print("")
            print(line)
            #tweets=(collect(line))
            #for tweet in tweets:
                #print(tweet.text)
        keywords=[]
        for line in fichier_keywords.readlines():
            print("")
            print(line)
            line_str=str(line)
            print(line.split(" "))
            #tweets=(collect(line))
            #for tweet in tweets:
        print(keywords)       #print(tweet.text)
    except IOError as error:
        print(error)

print (get_candidate_queries(1,'CandidateData'))


#for tweet in tweets:
#    print(tweet.text)
