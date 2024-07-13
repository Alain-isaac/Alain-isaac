from charger_donnees import *
from sauvegarde_donnees import * 
import time
from datetime import datetime
from Verification_saisies import *


def doublons (liste_parametre,nompro):
    
    for produit in liste_parametre:
        if produit['Nom_produit'] == nompro:
            print("le produit existe déjà")
            return 0 
    return 1 


def ajouter_produits():
    liste_produits = chargerProduits()
   

    nom_produit = input("entrez le nom du produit : ")
    prix = input("Entrez le prix du produit : ") 
    Quantite = input("Entrez la quantite du produit : ")

    Ver = doublons(liste_produits,nom_produit)
    ver_saisie = verification(nom_produit,prix,Quantite)

    if ver_saisie == 0:
        return
    else:
        if Ver == 1:

            if liste_produits == []:
                id_produit = len(liste_produits)+1
            else:
                id_produit = liste_produits[-1]['Id']+1

            date = datetime.today().strftime('%d/%m/%y')
            heure = time.strftime('%H:%M:%S')
            nouveau_produit = {"Id":id_produit,"Nom_produit":nom_produit,"Prix_produit":float(prix),"Quantite":int(Quantite),"Date":date,"Heure":heure}
                
            liste_produits.append(nouveau_produit)
            sauvegarde_produits(liste_produits)
            print("Le produit est bel bien enregistrer !!")
        