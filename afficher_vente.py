from charger_donnees import * 
def afficher_vente():
    liste_vente = chargerVente()
    if liste_vente == []:
        print("aucunne vente est déjà éffectuée")
        return
    else:
        print("\nInfos sur les ventes\n")
        for vente in liste_vente:
            print (f"id : {vente['id']} ,Nom_client :{vente['Nom_client']} , Nom_produit : {vente['nom_produit']} , Quantité : {vente['Quantite']}, mont_payer :{vente['Prix_payer']} , Date : {vente['Date']}, heure : {vente['heure']}")
