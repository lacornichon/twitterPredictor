# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from twitter_analysis import prise_en_compte_opinion

"""
ici on crée un tableau qui comparre tweet positif negatif et neutre pour les 2 mots en queries (test et tu comprendra)
"""

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
"""on def un object app avec un constructeur Dash, puis on lui aplliquera des methodes et on utlisiera ces propriétés"""

queries=["Homme","Femme"]

app.layout = html.Div(children=[                                   #comme en html, balise Div et H1, imbriquées
    html.H1(children='Hello my name is winner'),

    html.Div(children='''
        Dash: A cool way to make funny twitter.
    '''),

    dcc.Graph(
        id='popularity_compare',
        figure={
            'data': [
                {'x': ["pos", "neg", "neutre"], 'y': prise_en_compte_opinion.collect_opinion(queries[0]), 'type': 'bar', 'name': queries[0]},
                {'x': ["pos", "neg", "neutre"], 'y': prise_en_compte_opinion.collect_opinion(queries[1]), 'type': 'bar', 'name': queries[1]},
            ],
            'layout': {
                'title': 'who is the best?'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
