
from fonctions import choix_du_mot
from fonctions import lettre
from fonctions import mot_complet

def pendu_console():
    mot_a_trouver = choix_du_mot()
    premiere_lettre = mot_a_trouver[0]
    liste_temporaire = []
    for i in range(len(mot_a_trouver)):
        if mot_a_trouver[i] == premiere_lettre:
            liste_temporaire.append(premiere_lettre)
        else:
            liste_temporaire.append("_")
    
    print(liste_temporaire)
    print(mot_a_trouver)
    n = 8
    mot_trouve = False
    while n > 0 and (not mot_trouve):
        proposition = input("Tentez quelque chose ! ")
        if len(proposition) > 1:
            if mot_complet(proposition):
                mot_trouve = True
                return mot_trouve
        else:
            
            
            if lettre(proposition,liste_temporaire,mot_a_trouver) == 1:
                n-=1
            if lettre(proposition,liste_temporaire,mot_a_trouver) == 0:
                pass
            else:
                if liste_temporaire == mot_a_trouver:
                    mot_trouve = True
                    return mot_trouve
        
        print(liste_temporaire,n)
    
    return mot_trouve
                 

pendu_console()