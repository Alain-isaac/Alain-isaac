def verification(nompro,prix,quantite):

    if nompro == "" or quantite == "" or prix == "":
        print("toute les cases sont obligatoires veuillez les remplires")
        return 0 
    try: 
        nompro = int(nompro)
    except:
       
        try: 
            quantite = int(quantite)
            prix = float(prix)
        except: 
            print("saisissez les entiers pour la case (quantité et prix) ")
            return 0
        else:
            if prix <= 0 or quantite <= 0 :
                print("veuillez saisir un nombre supérieur à 0 pour (la quantité et le prix)")
                return 0 
    else :
        print("le nom du produit doit être une chaîne de caractères")
        return 0
    return 1
            
    