import random


def afficher_damier_ascii(état):
    """Afficher le damier

    Votre affichage doit être identique à
    celui illustré. Notez aussi que votre fonction sera testée
    avec plusieurs états de jeu différents.

    Args:
        état (dict): Dictionnaire représentant l'état du jeu.

    Examples:
        >>> état = [
                {
                    "nom": "jowic42",
                    "pions": [0, 2, 6, 9, 12]
                },
                {
                    "nom": "robot",
                    "pions": [0, 9, 2, 6, 12]
                }
            ]
        >>> afficher_damier_ascii(état)
            Légende:
              □ = jowic42
              ■ = robot

                   . | . : | : : | : : | : . | .
                     █   . | .   |   . | .   ●
              ...    ●     |     |     |     █      .
            1 ──□□ ○─┼─────┼─────┼─────┼─────┼───────
              ...    |     |     |     |     |      .
              .      |     |     |     |     |    ...
            2 ───────┼────□□ ○───█─────┼─────┼───────
              .      |     |     ●     |     |    ...
              ..     |     ●     |     |     |     ..
            3 ───────┼─────█─────┼─────┼─────┼─○ □□──
              ..     |     |     |     |     |     ..
              .      |     |     |     |     |    ...
            4 ───────┼─────┼───○ □□────┼─────┼───────
              .      |     |     |     |     |    ...
              ...    |     |     |     |     |      .
            5 ──○ □□─┼─────┼─────┼─────┼─────┼───────
              ...    |     |     |     ●     |      .
                   . | .   |     |     █   . | .
                   : | : . | . : | : . | . : | :
    """

    grille = [
    ['  ', ' '*5, '. | . : ', '| : : ', '| : : ', '| : . ', '| .     '],
    ['  ', ' '*7, '|', '   . ', '|', ' .   ', '|', '   . ', '|', ' .   ', '|',' '*7],
    ['  ', '...    ', '|', '     ' , '|', '     ', '|', '     ', '|', '     ', '|','      .'],
    ['1 ──', '─'*5, '┼', '─'*5, '┼', '─'*5, '┼', '─'*5, '┼', '─'*5, '┼', '─'*5, '─'*2],
    ['  ', '...    ', '|', '     ' , '|', '     ', '|', '     ', '|', '     ', '|','      .'],
    ['  ', '.      ', '|', '     ' , '|', '     ', '|', '     ', '|', '     ', '|','    ...'],
    ['2 ──', '─'*5, '┼', '─'*5, '┼', '─'*5, '┼', '─'*5, '┼', '─'*5, '┼', '─'*5, '─'*2],
    ['  ', '.      ', '|', '     ' , '|', '     ', '|', '     ', '|', '     ', '|','    ...'],
    ['  ', '..     ', '|', '     ' , '|', '     ', '|', '     ', '|', '     ', '|','     ..'],
    ['3 ──', '─'*5, '┼', '─'*5, '┼', '─'*5,'┼', '─'*5, '┼', '─'*5, '┼', '─'*5, '─'*2],
    ['  ', '..     ', '|', '     ' , '|', '     ', '|', '     ', '|', '     ', '|','     ..'],
    ['  ', '.      ', '|', '     ' , '|', '     ', '|', '     ', '|', '     ', '|','    ...'],
    ['4 ──', '─'*5, '┼', '─'*5, '┼','─'*5,'┼','─'*5,'┼','─'*5,'┼', '─'*5, '─'*2],
    ['  ', '.      ', '|', '     ' , '|', '     ', '|', '     ', '|', '     ', '|','    ...'],
    ['  ', '...    ', '|', '     ' , '|', '     ', '|', '     ', '|', '     ', '|','      .'],
    ['5 ──'  ,'─'*5, '┼', '─'*5, '┼','─'*5,'┼','─'*5,'┼','─'*5,'┼', '─'*5, '─'*2],
    ['  ', '...    ', '|', '     ' , '|', '     ', '|', '     ', '|', '     ', '|','      .'],
    ['  ', ' '*5, '. ','|',' .   ', '|', '     ', '|', '     ', '|', '   . ', '|', ' .     '],
    ['  ', ' '*5, ': | : . ', '| . : ', '| : . ', '| . : ', '| :     ']
    ]

    pion1aller = '□□ ○─'
    pion1retour = '─○ □□'
    pion1fin = '○ □□─'

    sc = '□'

    fst_aller = '────□'
    th_aller =' ○───'

    fst_retour = '───○ '
    th_retour = '□────'

    v_croix = '█'
    v_rond =  '●'

    numero_pion = 0
    for i in état[0]['pions']:
        numero_pion += 1
        if i == 0:
            grille[numero_pion*3][1] = pion1aller
        elif i == 6:
            grille[numero_pion*3][11] = pion1retour
        elif i == 12:
            grille[numero_pion*3][1] = pion1fin
        elif i < 6:                                           # aller
            grille[numero_pion*3][2*i-1] = fst_aller
            grille[numero_pion*3][2*i] = sc
            grille[numero_pion*3][2*i+1] = th_aller
        elif i < 12:                                        # retour
            grille[numero_pion*3][-2*i+23] = fst_retour
            grille[numero_pion*3][-2*i+24] = sc
            grille[numero_pion*3][-2*i+25] = th_retour

    numero_pion = 0
    for i in état[1]['pions']:
        numero_pion += 1
        if i == 0:
            grille[1][numero_pion*2] = v_croix
            grille[2][numero_pion*2] = v_rond
        elif i == 6:
            grille[17][numero_pion*2+1] = v_croix
            grille[16][numero_pion*2] = v_rond
        elif i == 12:
            grille[1][numero_pion*2] = v_rond
            grille[2][numero_pion*2] = v_croix
        elif i < 6:                                            # aller
            grille[3*i][numero_pion*2] = v_croix
            grille[3*i+1][numero_pion*2] = v_rond
        elif i < 12:                                           # retour
            grille[-3*i+36][numero_pion*2] = v_croix
            grille[-3*i+35][numero_pion*2] = v_rond

    print('Légende:\n  □ = ', état[0]['nom'], '\n  ■ = ',état[1]['nom'] , '\n')
    for line in range(19):
        print(*grille[line], sep = '')


def verif_damier_ascii():
    état = [
    {
        "nom": "jowic42",
        "pions": []
    },
    {
        "nom": "robot",
        "pions": []
    }
    ]

    liste = []
    for i in range(10):
        liste.append(random.randint(0,12))
    
    état[0]['pions'] = liste[0:5]
    état[1]['pions']= liste[5:10]

    ligne_courante = 1
    compteurH = 10
    compteur = 0
    for H in état[0]['pions']:
        compteurV = 10
        for i in range(1, 6):
            if (état[1]['pions'][i-1] == ligne_courante or état[1]['pions'][i-1] == ligne_courante+compteurH):
                if H == i or (H-compteurV) == i:
                    compteur += 1
                    print('couple', compteur)
                    print("i = ", i)
                    print('ligne_courante=', ligne_courante)
                    print('compteurH = ', compteurH)
                    print('compteurV = ', compteurV)
                    print('H = ', H)
                    print('V = ', état[1]['pions'][i-1])
                    print('-------------------------')
            compteurV -= 2
        ligne_courante += 1
        compteurH -= 2
    print(état[0]['pions'])
    print(état[1]['pions'])

    afficher_damier_ascii(état)
    print(compteur)

#verif_damier_ascii()

def sum_square(n):
    i = 1
    while True:
        for j in range(i+1):
            if i**2+j**2 == n:
                return print(i, j)
        i += 1
sum_square(169)
