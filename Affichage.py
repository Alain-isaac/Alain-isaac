from charger_donnees import * 

def affichage_produits():
    liste_produits = chargerProduits()
    if liste_produits == []:
        print("\nLe stock est vide")
    else : 
        print("\nLes produits en stock\n")
        for produit in liste_produits: 
            print(f"Id : {produit['Id']}, Nom_produit : {produit['Nom_produit']} ,Prix_produit : {produit['Prix_produit']} , Quantite : {produit['Quantite']}, Date : {produit['Date']}, Heure : {produit['Heure']}")
