#Dump and load convert between files and objects, while dumps and loads convert between strings and objects.
#options de dump intéréssantes ==> indent=None, separators=None, 


#serialisation:
#Exemple:
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

#Il est important d'arriver à sauvegarder des données

import json
#méthode 1, retourne un fichier où le json est stocker
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)                                     
#méthode 2, retourne une chaine de caractères dans laqeulle le json est stocké
json_string = json.dumps(data)      

#deserialisation:
import json
#methode 1 si le json est stocké dans un fichier
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
#methode 2 pour convertir une chaine de cara en json
data = json.loads(json_string)
