import random

while True:
    nom_fichier = "eddy.txt" 
    liste_mots = [] 

    with open(nom_fichier, "r") as fichier:
        

        for ligne in fichier:
            mots_ligne = ligne.split() 
            for mot in mots_ligne:
                liste_mots.append(mot) 

    mots = liste_mots
    mot =random.choice(mots)

    rhyme_pretto = input("tu veux un eddy cool? o/n    :")
    if rhyme_pretto == "o":
        print("eddy de " + mot)

    else : 
        print ("eddy pas marrant")

