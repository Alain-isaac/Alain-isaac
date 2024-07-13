from charger_donnees import * 
from Verification_saisies import * 
from sauvegarde_donnees import * 
import time
from datetime import datetime

def modification(id_parametre, nomproduit):
    liste_produits = chargerProduits()
    position =  0 
    for produit in liste_produits: 
        if nomproduit == produit ['Nom_produit'] or produit['Id'] == id_parametre:
            print("\nEntrez les nouvelles informations \n")
            
            nom_produit = input("entrez le nom du produit : ")
            prix = input("Entrez le prix du produit : ") 
            Quantite = input("Entrez la quantite du produit : ")

            ver_saisie = verification(nom_produit,prix,Quantite)
            if ver_saisie == 0:
                    return
            else:
                date = datetime.today().strftime('%d/%m/%y')
                heure = time.strftime('%H:%M:%S')
                liste_produits[position]['Nom_produit'] = nom_produit
                liste_produits[position]['Prix_produit'] = prix
                liste_produits[position]['Quantite'] = Quantite
                liste_produits[position]['Date'] = date
                liste_produits[position]['Heure'] = heure

                sauvegarde_produits(liste_produits)
                print("modification terminer ")
            

        position += 1