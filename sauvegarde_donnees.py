import json

def sauvegarde_produits(liste_produits):
    with open('Produits.json','w+') as FICHIER:
         json.dump(liste_produits,FICHIER)
    

def sauvegarde_vente(liste_vente):
     with open('vente.json','w+') as FICHIER:
          json.dump(liste_vente,FICHIER)