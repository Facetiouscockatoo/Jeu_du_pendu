
from fonctions import *

def pendu_console():
    mot_a_trouver = choix_du_mot()
    premiere_lettre = mot_a_trouver[0]
    liste_temporaire = []
    for i in range(len(mot_a_trouver)):
        if mot_a_trouver[i] == premiere_lettre:
            liste_temporaire.append(premiere_lettre)
        else:
            liste_temporaire.append("_")
    liste_temporaire.pop()
    print(liste_temporaire)
    n = 8
    mot_trouve = False
    while n > 0 and (not mot_trouve):
        proposition = input("Tentez quelque chose ! ")
        if len(proposition) > 1:
            if mot_complet(proposition):
                mot_trouve = True
        else:
            try lettre(proposition,liste_temporaire,mot_a_trouver)
            with 
            if not lettre(proposition,liste_temporaire,mot_a_trouver):
                n-=1
            else:
                if liste_temporaire == mot_a_trouver:
                    mot_trouve = True
        
        print(liste_temporaire)
    
    return mot_trouve
                 

pendu_console()