import time


def vprime(n):
    for x in range(2, n-1):
        if n % x == 0:
            return False
    return True

def liste_prime(z):
    liste = []
    for i in range(2, z):
        if vprime(i):
            liste.append(i)
    return print(liste)

r = 100000
debut = time.perf_counter()
liste_prime(r)
fin = time.perf_counter()
print(f"La liste des nombres premiers parmis les {r} premiers nombres a été trouvé en {fin - debut} secondes.")