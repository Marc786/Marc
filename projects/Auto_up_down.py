import random



def guess():
    tranche = int(input("Sur quel tranche de nombre voulez vous jouer (nombre positif) ?"))
    if tranche < 0:
        raise ValueError
    rnb = random.randint(0,tranche)
    check = True
    while check:
        guess = int(input("Choisissez un nombre au hazard :"))
        if guess == rnb:
            check = False
            print("gg")
        elif guess > rnb:
            print("Trop Haut!")
        elif guess < rnb:
            print("Trop Bas!")

def guess_auto_random():
    tranche = int(input("Sur quel tranche de nombre voulez vous jouer (nombre positif) ?"))
    if tranche < 0:
        raise ValueError("La tranche doit etre superieur a 0")
    nombre = int(input("Quel est le nombre que le bot doit trouver ?"))
    if nombre > tranche:
        raise ValueError("Le nombre doit etre plus petit ou egal a la tranche")
    check = True
    coups = 0
    while check:
        coups += 1
        guess = random.randint(0, tranche)
        if guess == nombre:
            check = False
    print(f'Le bot a trouve en {coups} coups.')

def guess_auto_algo():
    tranche = int(input("Sur quel tranche de nombre voulez vous jouer (nombre positif) ?"))
    check1 = True
    while check1:    
        try:
            if tranche < 0:
                raise ValueError("La tranche doit etre superieur a 0, réessayer.")
            check1 = False
        except ValueError as identifier:
            print(identifier)
            tranche = int(input("Sur quel tranche de nombre voulez vous jouer (nombre positif) ?"))
    nombre = int(input("Quel est le nombre que le bot doit trouver ?"))
    check2 = True
    while check2:
        try:
            if nombre > tranche:
                raise ValueError(f"Le nombre doit etre plus petit ou egal a la tranche que vous avez choisie ({tranche}), réessayez.")
            check2 = False
        except ValueError as identifier:
            print(identifier)
            nombre = int(input("Quel est le nombre que le bot doit trouver ?"))
    checkwin = True
    coups = 0
    low_guess = 0
    high_guess = tranche
    guess = random.randint(0, tranche)
    #guess = tranche/2
    while checkwin:
        coups += 1
        if guess == nombre:
            checkwin = False
        elif guess > nombre:
            high_guess = guess
            guess = guess - (guess-low_guess)//2
            print(guess)
        elif guess < nombre:
            low_guess = guess
            guess = guess + (high_guess-guess)//2
            print(guess)
    print(f'Le bot a trouve en {coups} coups.')

guess_auto_algo()
