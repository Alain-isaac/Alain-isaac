import json

def chargerProduits():
    with open('Produits.json','r+') as FICHIER:
        liste_produits = json.load(FICHIER)
    return liste_produits

def chargerVente():
    with open('vente.json','r+') as FICHIER:
        liste_vente = json.load(FICHIER)
    return liste_vente