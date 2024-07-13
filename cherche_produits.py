
from charger_donnees import *
from suppression_produits import *
from Modification import * 

def recherche():
    liste_produits = chargerProduits()
    while True:    
        Menu = "Rechercher par :\n 1. Nom produit \n 2. Id produit \n 3. Quitter \n Votre choix :"
        
        reponde_utilisateur = input(Menu)
        if reponde_utilisateur == "1":
            par_nom(liste_produits)

        elif reponde_utilisateur == "2": 
            par_id(liste_produits)

        elif reponde_utilisateur == "3":
            print("vous venez d'arreter l'opération ...")
            return
         
def par_id(liste_parametre):
    Ct  = 0
    indice_trouv = 0
    rep_id = input("Entrez l'ID  du produit : ")
    for produit in liste_parametre :
        if str(produit['Id']) == rep_id:
            print(f"Id : {produit['Id']}, Nom_produit : {produit['Nom_produit']} ,Prix_produit : {produit['Prix_produit']} , Quantite : {produit['Quantite']}, Date : {produit['Date']}, Heure : {produit['Heure']}")
            Ct += 1
            
            while Ct != 0 :
                Menu = "1. Supprimer le produit\n2. Modifier\n3. Quitter\n Votre choix : "
                reponse = input(Menu)
                if reponse == "1":
                    supp(indice_trouv)
                elif reponse  == "2":
                    modification(produit['Id'],produit['Nom_produit'])
                elif reponse == "3":
                    print("Vous venez de quitter ... ")
                    Ct = 0
                else:
                    print("Mauvaise valeur ")
        indice_trouv += 1
                
    if Ct == 0 :
        print(f"il a aucun produit qui porte le nom {rep_id}")


def par_nom(liste_parametre):
    Ct  = 0
    indice_trouv = 0
    rep_nom = input("Entrez le nom du produit : ")
    for produit in liste_parametre :
        if produit['Nom_produit'].lower() == rep_nom.lower():
            print(f"Id : {produit['Id']}, Nom_produit : {produit['Nom_produit']} ,Prix_produit : {produit['Prix_produit']} , Quantite : {produit['Quantite']}, Date : {produit['Date']}, Heure : {produit['Heure']}")
            Ct += 1

            while Ct != 0 :
                Menu = "1. Supprimer le produit\n 2. Modifier\n 3. Quitter\n Votre choix : "
                reponse = input(Menu)
                if reponse == "1":
                    supp(indice_trouv)
                    return
                elif reponse  == "2":
                    modification(produit['Id'],produit['Nom_produit'])
                    return
                elif reponse == "3":
                    print("Vous venez de quitter ... ")
                    Ct = 1
                else:
                    print("Mauvaise valeur ")

        indice_trouv += 1

    if Ct == 0 :
        print(f"il a aucun produit qui porte le nom {rep_nom}")