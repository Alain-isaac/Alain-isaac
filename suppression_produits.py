from charger_donnees import *
from sauvegarde_donnees import *

def supp (position):
    Liste_produits = chargerProduits()
    del Liste_produits[position]
    sauvegarde_produits(Liste_produits)
    print("Suppression réussie avec succès ")
    return
            