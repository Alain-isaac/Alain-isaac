
import sys
from charger_donnees import *
from ajouter_produits import *
from cherche_produits import * 
from Affichage import *
from Enregistrer_vente import * 
from afficher_vente import *
from Vente_client import *
from rapport_gene import * 

LISTE_PRODUITS = [] 
LISTE_PRODUITS =  chargerProduits()

MENU = "\n \t\t\t\t MENU PRINCIPAL\n 1.  Ajouter produit\n 2.  Afficher produits\n 3.  Rechercher produit\n 4.  Enregistrer vente\n 5.  Afficher ventes\n 6.  Ventes par client\n 7.  Générer rapport de ventes\n 8.  Charger données\n 9.  Quitter\n Votre choix : "

MENU_CHOICES = ["1","2","3","4","5","6","7","8","9"] 


while True:    
        CHOIX_UTILISATEUR = "" 
        while CHOIX_UTILISATEUR not in MENU_CHOICES:
            CHOIX_UTILISATEUR = input(MENU)
            if CHOIX_UTILISATEUR not in MENU_CHOICES:
                print("Veuillez Choisir une option valide...")
        if CHOIX_UTILISATEUR == "1":  
            ajouter_produits()
        elif CHOIX_UTILISATEUR =="2":
            affichage_produits()
        elif CHOIX_UTILISATEUR == "3":
            recherche()
        elif CHOIX_UTILISATEUR =="4":
            enregistrer_vente()
        elif CHOIX_UTILISATEUR  == "5":
            afficher_vente()
        elif CHOIX_UTILISATEUR =="6":
            vente_client()
        elif CHOIX_UTILISATEUR == "7":
            rapport()
        elif CHOIX_UTILISATEUR =="8":
            chargerProduits()
            print("\n chargement de données terminer\n")
        elif CHOIX_UTILISATEUR == "9":
            print("\n À BIENTÔT...")
            sys.exit() 