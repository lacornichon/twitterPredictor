# Fonctionnalité 11 : Votre première application avec Dash



[Dash](https://plot.ly/) est un framework pour prototyper rapidement des applications web de visualisation.

## Etape 1 : Installer Dash.

Pour l'installer il faut taper les commances ci-dessous:


```
pip install dash==0.29.0  # The core dash backend
pip install dash-html-components==0.13.2  # HTML components
pip install dash-core-components==0.38.0  # Supercharged components
pip install dash-table==3.1.5  # Interactive DataTable component (new!)

```
Vous pouvez tester votre application en regardant si la commande `import dash` fonctionne.


## Etape 2 : Créer un Dash Layout


Une application Dash est composée de deux parties. La première partie est le  **layout** de l'application et elle décrit à quoi ressemble l'application. La deuxième décrit les interactions avec l'application.

Pour créer votre première application Dash, nous allons suivre le manuel du site [ici](https://dash.plot.ly/getting-started).

Si vous recopiez et executez le code donné dans ce tutorial, vous allez obtenir cette visualisation à l'adresse mentionnée lors de l"execution, ici `http://127.0.0.1:8050/`.


![hellodash](./Images/dash.png)


C'est une application interactive. Essayez de passer votre souris dessus.
Regarder bien les différents types de graphes ou de visualisation proposées oar DASH en prenant le temps de faire le [tutoriel](https://dash.plot.ly/getting-started)).



## Etape 3 : Créer un dash layout pour l'analyse d'opinions.
L'objectif maintenant est de créer avec dash un layout pour votre application d'analyse d'opinions. C'est une étape ouverte qui vous nécessitera de regarder la documentation sur cette bibliothèque avant de commencer à écrire votre code. 

Nous vous conseillons donc de suivre la tutoriel de Dash avant de vous lancer dans ce travail [ici](https://dash.plot.ly/).

Nous allons maintenant utiliser une représentation sous forme de nuage de mots pour afficher le vocabulaire de nos tweets. Il s'agit de la fonctionnalité : [**Fonctionnalité 13** : Prise en main de WordCloud](./S6_wordcloud.md)











