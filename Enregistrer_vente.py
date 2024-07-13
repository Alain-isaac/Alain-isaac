from charger_donnees import *
from verification_sais_vente import *
from sauvegarde_donnees import *
import time
from datetime import datetime

def enregistrer_vente():
    liste_vente = chargerVente()
    liste_produit = chargerProduits()

    nom_client = input("Entrez le nom du client : ")
    nom_produit = input("Entrez le nom du produit : ")
    quant = input("Entrez la quantité vendue : ")

    valid,prix_payer = verification_sais_vente(nom_client,nom_produit,quant)
    
    if valid == 1:
        id_vente =  len(liste_vente)+1
        date = datetime.today().strftime('%d/%m/%y')
        heure = time.strftime('%H:%M:%S')
        nouveau_vente = {"id":id_vente,"Nom_client":nom_client,"nom_produit":nom_produit,"Quantite":int(quant),"Prix_payer":float(prix_payer*int(quant)),"Date":date,"heure":heure}
        print("\nLa vente est éffectuée avec succès")

        liste_vente.append(nouveau_vente)
        sauvegarde_vente(liste_vente)
    else:
        return