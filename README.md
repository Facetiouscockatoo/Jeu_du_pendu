# Jeu_du_pendu
Changements effectués et erreurs réparées:
    
    random(0, len()) -> random(0, len()-1) En effet la dernière valeur n'est pas exclue !

    création d'une liste à partir de mot_a_trouver : On regardais si liste_temporaire (str list) était égale à mot_a_trouver (str).
    Comme je l'avais dit, string et string list se comportent de la même façon mais ne sont pas égaux ! ( je devrais m'écouter parfois... )

    Changement dans choix_du_mot() pour ne pas à avoir de .pop dans le jeu :
    ( mot_a_trouver = mot_a_trouver[:-1] -> enlève le dernier terme de mot_a_trouver )
    ( à noter que c'est pour ça qu'il y a une dernière ligne vide dans dictionnaire : elle correspond au \n de infiniment )

    Changement au niveau de lettre() :
    L'erreur que j'implémentais si on donnait une lettre déjà présente faisait un 'break' du programme ( c'est le principe d'une erreur ( type ValueError), j'aurais dû le voir venir)
    J'ai donc changé pour renvoyer un entier k: il vaut 0 si la lettre est présente, puis elle vaut par défaut 1 avant d'entrer dans la boucle for ( donc elle reste à 1 en cas de mauvaise lettre )

    Changement dans mot_complet():
    Pour éviter le problème de typage (Je sais pas pourquoi il voyait choix_du_mot() comme une fonction ), j'ai donc mis mot_a_trouver dans les entrées
    (Ah non j'avais juste écris mot_a_trouver = choix_du_mot et pas choix_du_mot(), mais je garde les changements puisque ça marche )

    Changement au niveau du jeu:
    J'ai mis tf = lettre pour ne pas effectuer lettre dans chaque 'if' ( puisque maintenant il y en a 2) 

IMPORTANT ! 
Si ton logiciel de programmation Python n'est PAS en FRANCAIS ( ou dans une langue prenant en compte les accents ) ( le mien est en anglais )
Les mots à ACCENTS NE FONCTIONNENT PAS ( les accents sont remplaçés par 'Ã''@') ( "génération" par exemple ).