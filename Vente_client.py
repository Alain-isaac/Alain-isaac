from charger_donnees import *

def vente_client():
    liste_vente = chargerVente()
    nom_client = input("Entrez le nom du client : ")
    ct = 0

    for vente in liste_vente:
        if vente['Nom_client'].lower() == nom_client.lower():
            print (f"id : {vente['id']} ,Nom_client :{vente['Nom_client']} , Nom_produit : {vente['nom_produit']} , Quantité : {vente['Quantite']}, mont_payer :{vente['Prix_payer']} , Date : {vente['Date']}, heure : {vente['heure']}")
            ct +=1
    if  ct == 0 :
        print(f"il y a aucunne vente qui a été éffectuée sous nom du client {nom_client}")