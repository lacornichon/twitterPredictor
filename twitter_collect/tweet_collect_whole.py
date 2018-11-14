"""Un premier travail pour initier la collecte est de définir l'ensemble des mots clés que vous allez utiliser pour votre collecte
via l'API search. Nous allons considérer que cette liste de mots clés vous est fournie par votre client sous la forme de fichiers
keywords_candidate_n.txt avec un mot clé (ou un ensemble de mots clés) par ligne. De la même manière, votre client vous fournira
une liste de hashtag_candidate_n.txt qui sont les hastags associés à chaque candidat.
Ces fichiers seront stockés dans un répertoire CandidateData à la racine de votre projet.
Il s'agit maintennant d'écrire une fonction get_candidate_queries(num_candidate,file_path) qui permet de créer et de renvoyer un
ensemble de requêtes destinées à l'API search pour le candidat num_candidate à partir des fichiers keywords_candidate_num_candidate.txt
et hastag_candidate_num_candidate.txt."""
from twitter_collect import search


def get_candidate_queries(num_candidate, file_path):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    try:
        path_keyword= file_path + "keyword_candidate_" + str(num_candidate) +".txt"
        path_hastag= file_path +"hastag_candidate_" + str(num_candidate) + ".txt"
        fichier_keyword = open("path_keyword","r")
        fichier_hastag = open("path_hastag","r")
        contenu_keyword=fichier_keyword.read()
        contenu_hastag=fichier_hastag.read()
        keyword= contenu_keyword.split()
        hastag= contenu_hastag.split()
        print (keyword)
        print(hastag)
        return keyword, hastag





    except IOError:
        # TO COMPLETE



