from charger_donnees import *
from sauvegarde_donnees import *

def verification_sais_vente(nomcl,nompro,quantite):
    Ct = 0
    position =  0 
    liste_produits = chargerProduits()
    for produit in liste_produits:
        if produit['Nom_produit'].lower() == nompro.lower():
            Ct += 1
            if nomcl == "" or nompro == "" or quantite == "":
                print("toute les cases sont obligatoires veuillez les remplires")
                return 0,0
            try: 
                nomcl = int(nompro)
            except:
            
                try: 
                    quantite = int(quantite)
                except: 
                    print("saisissez les entiers pour la case (quantité ) ")
                    return 0,0
                else:
                    if quantite <= 0 :
                        print("veuillez saisir un nombre supérieur à 0 pour (la quantité et le prix)")
                        return 0,0
                    elif quantite > produit['Quantite']:
                        print("la quantité vendue doit être inférière ou égale à la quantité du produit en stock")
                        return 0,0
            else :
                print("le nom du produit doit être une chaîne de caractères")
                return 0,0
            liste_produits[position]['Quantite'] -= quantite
            sauvegarde_produits(liste_produits)
            return 1,produit['Prix_produit']
        position +=1

    if Ct == 0:
        print("Le produit n'est pas dans le stock ")
        return 0,0