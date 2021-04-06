```py
def verifier_saut(état, joueur, pion):
    #le pion equivaut à la ligne courante
    position = état[joueur][pion]

    if ((joueur == 1 and (pion == 1 or pion == 5) and position < 6) or 
        (joueur == 1 and (pion == 2 or pion == 4) and position >= 6) or 
        (joueur == 2 and (pion == 1 or pion == 5) and position >= 6) or 
        (joueur == 2 and (pion == 2 or pion == 4) and position < 6)):
        saut = 3
    elif ((joueur == 2 and (pion == 1 or pion == 5) and position < 6) or 
        (joueur == 2 and (pion == 2 or pion == 4) and position >= 6) or 
        (joueur == 1 and (pion == 1 or pion == 5) and position >= 6) or 
        (joueur == 1 and (pion == 2 or pion == 4) and position < 6)):
        saut = 1
    elif ((joueur == 1 and pion == 3) or
        (joueur == 2 and pion == 3)):
        saut = 2
    
    post_position = position + saut
    if position > 6 and post_position > 12:
        post_position = 12
    elif position < 6 and post_position > 6:
        post_position = 6
    
    if position < 6:
        for i in range(position, post_position):
            pass
    if position >= 6:
        for i in range(position, post_position):
            pass
```