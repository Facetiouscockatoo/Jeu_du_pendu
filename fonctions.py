#header 
"""
Propriétaires: JEUNET Florian, VILLEMINOT Benoit
Reste à faire: tout
Fonctions nécesaires au déroulement d'un jeu du pendu  
"""
import random

mots_possibles = open("dictionnaire",'r').readlines()

def choix_du_mot():
    i = random.randint(0,len(mots_possibles))

    mot_a_trouver=mots_possibles[i]
    return mot_a_trouver

def mot_complet(mot):
    mot_a_trouver = choix_du_mot
    if len(mot) != len(mot_a_trouver) or mot != mot_a_trouver:
        return False
    else:
        return True
    
def lettre(caractere,liste_temporaire,mot_a_trouver):
    if caractere in liste_temporaire:
        raise ValueError("Lettre déjà là")
    k=0
    for i in range(len(mot_a_trouver)):
        if caractere == mot_a_trouver[i]:
            liste_temporaire[i] = caractere
            k+=1
    if k == 0:
        return False
    else: 
        return True



