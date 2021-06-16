"""
Merge sort
    Dvě setříděná pole můžeme efektivně sloučit

"""

spatny = [6, 5, 4, 3, 2, 1]
dobry = [1, 2, 3, 4, 5, 8, 7, 6]
random = [8, 9, 7, 2, 1, 6]

aa = [1, 4, 5, 7]
bb = [2, 3, 6, 8]


def merge(a, temp, zacatek, stred, konec):
    i, j, k = zacatek, stred + 1, zacatek

    while i <= stred and j <= konec:
        if a[i] < a[j]:
            temp[k] = a[i]
            i += 1
        else:
            temp[k] = a[j]
            j += 1
        k += 1

    # na konec připojí prvky z levého čí pravého běhu
    while i <= stred:
        temp[k] = a[i]
        i += 1
        k += 1

    while j <= konec:
        temp[k] = a[j]
        j += 1
        k += 1

    a[zacatek:konec + 1] = temp[zacatek:konec + 1]


def mergesort(a):
    n = len(a)
    temp = [None] * n

    beh = 1
    while beh < n:
        for zacatek in range(0, n - beh, 2 * beh):
            stred = zacatek + beh - 1
            konec = min(stred + beh, n - 1)
            merge(a, temp, zacatek, stred, konec)
        beh *= 2

    return a


print(mergesort(random))

""" 
Vnější třídění
    Data co se nevejdou do RAM
    Kritérium:
        minimalizovat I/O operace
        
Řešení slévání běhů
    féze slévání a rodělení
        Vylepšení
            Sloučit je
            Přetřídit počátek v RAM
            Slévání k>2 běhů

Dolní odhad třídění

Rozhodovací strom
....


CountingSort
"""
