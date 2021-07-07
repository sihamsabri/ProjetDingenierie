import matplotlib.pyplot as plt
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

df = pd.read_csv('Traffic.csv')
def Stat_Address():
    Adresses = df['Source']
    Add0 = list(Adresses)
    Add = []
    for i in Add0:
        if i not in Add:
            Add.append(i)
    print("La liste des adresses detectees dans ce traffic est: ")
    print(Add)
    # On donne la main a l'utilisateur pour saisir l<adresse
    Adress = input("veuillez choisir une adresse!")
    print('L\'adresse que vous avez choisi est ', Adress)
    df_r = df[df.Source == Adress]
    # Preparer les datasets des protocoles pour l'adresse choisie par l'utilisateur
    A = df[df.Source == Adress]
    Listes_des_protocoles0 = []
    Listes_des_protocoles0 = list(A['Protocol'])
    Listes_des_protocoles = []
    # Preparer la liste qui va contenir les protocoles qu'on a collcte du dataset
    for i in Listes_des_protocoles0:
        if i not in Listes_des_protocoles:
            Listes_des_protocoles.append(i)
    l = len(Listes_des_protocoles)
    x2 = [0] * l
    # Calculer le nombre de paquets dans le traffic pour chaque protocole
    for i in range(0, l):
        x2[i] = Listes_des_protocoles0.count(Listes_des_protocoles[i])
    ############################################################
    some = sum(x2)
    # Liste qui va contenir le pourcentage de chaque protocole
    x3 = [0] * l
    for i in range(0, l):
        j = (x2[i] / some) * 100
        x3[i] = j
    ######################################################

    ######################################################
    # On va afficher chaque protocole avec son pourcentage dans le traffic
    print('Voici le pourcentage de chaque protocole pour l\'adresse ', Adress)
    for i in range(0, l):
        print(Listes_des_protocoles[i], ' : ', x3[i], '%')
    print(Listes_des_protocoles)
    # Présentation graphique
    plt.bar(Listes_des_protocoles, x3)
    plt.title('Pourcentage de chaque protocole pour l\'adresse ' + Adress)
    plt.xlabel('Les protocoles')
    plt.ylabel('(%)')
    plt.show()
    # Affichage Web
    # -*- coding: utf-8 -*-
    # visit http://127.0.0.1:8050/ in your web browser.
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    df0 = pd.DataFrame({
        "Les protocoles": Listes_des_protocoles,
        "Le poucentage": x3,
        "Proto": Listes_des_protocoles
    })

    fig = px.bar(df0, x="Les protocoles", y="Le poucentage", color="Proto", barmode="group")
    app.layout = html.Div(children=[
        html.H1(children='Classification par protocole  pour l\'adresse ' + Adress),
        html.Div(children='''
                    Dash: Taux d'une adresse.
                '''),
        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])
    if __name__ == '__main__':
        app.run_server(debug=True)
Stat_Address()