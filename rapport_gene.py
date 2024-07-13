from charger_donnees import * 
from datetime import datetime

def rapport ():
    liste_produits = chargerProduits()
    liste_vente = chargerVente ()

    print("\nRapport journalier\n")
    print("pour achat\n")

    verf1 = 0
    verf2 = 0

    for produit in liste_produits:
            date = datetime.today().strftime('%d/%m/%y')
            if  produit['Date'] == date :
                print(f"Id : {produit['Id']}, Nom_produit : {produit['Nom_produit']} ,Prix_produit : {produit['Prix_produit']} , Quantite : {produit['Quantite']}, Date : {produit['Date']}, Heure : {produit['Heure']}")
                verf1 += 1
    if verf1 == 0: 
         print("jusque là il y a aucun achat qui a étais éffectuer aujourd'hui")

    print("\npour Vente\n")
    for vente in liste_vente:
            date = datetime.today().strftime('%d/%m/%y')
            if  vente['Date'] == date :
                print (f"id : {vente['id']} ,Nom_client :{vente['Nom_client']} , Nom_produit : {vente['nom_produit']} , Quantité : {vente['Quantite']}, mont_payer :{vente['Prix_payer']} , Date : {vente['Date']}, heure : {vente['heure']}")
                verf2 += 1
    if verf2 == 0: 
         print("jusque là il y a aucunne vente qui a étais éffectuée aujourd'hui")


