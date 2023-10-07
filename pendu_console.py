
from fonctions import choix_du_mot
from fonctions import lettre
from fonctions import mot_complet

def pendu_console():
    mot_a_trouver = choix_du_mot()
    
    mot_a_trouver_liste=[mot_a_trouver[i] for i in range(len(mot_a_trouver))]
    
    premiere_lettre = mot_a_trouver[0]
    liste_temporaire = []
    for i in range(len(mot_a_trouver)):
        if mot_a_trouver[i] == premiere_lettre:
            liste_temporaire.append(premiere_lettre)
        else:
            liste_temporaire.append("_")
    
    n=8
    mot_trouve = False
    print(liste_temporaire,n)
    while n > 0 and (not mot_trouve):
        proposition = input("Tentez quelque chose ! ")
        if len(proposition) > 1:
            if mot_complet(proposition,mot_a_trouver):
                mot_trouve = True
                return mot_trouve
            else:
                n-=1
        else:
            
            tf=lettre(proposition,liste_temporaire,mot_a_trouver)
            if tf == 1:
                n-=1
            if tf == 0:
                pass
            else:
                if liste_temporaire == mot_a_trouver_liste:
                    mot_trouve = True
                    return mot_trouve
        
        print(liste_temporaire,n)
    
    return mot_trouve

