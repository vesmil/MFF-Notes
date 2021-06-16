"""
Nejlepší třídení
    Heapsort a nebo
    Python má Timsort
        Slévání
        (Lokalita přístupu, cache paměť procesoru)

Třídění II
    V lineárním čase - počítáním
"""
pet = [1, 1, 1, 2, 3, 4, 5]


def countingsort(a, k):
    c = [0] * (k + 1)

    for x in a:
        c[x] += 1
    i = 0
    for x in range(k + 1):
        for cetnost in range(c[x]):
            a[i] = x
            i += 1

    return a


print(countingsort(pet, 5))

""""
Přihrádkové třídení 
    Založeno na počítání

Podivat se znovu na video na Moodle
"""
stud = [1, 1, 1, 2, 3, 4, 5]


def prihrsort(a, k, klic):
    c = [0] * (k + 1)
    for x in a:  # cetnost
        c[klic(x)] += 1
    suma = 0
    for i in range(k + 1):  # kumolovana cetnost
        c[i], suma = suma, c[i] + suma

    b = [None] * len(a)  # vystup
    for x in a:
        b[c[klic(x)]] = x
        c[klic(x)] += 1

    return b


""""
Radixove trideni

List

Binární halda
"""
