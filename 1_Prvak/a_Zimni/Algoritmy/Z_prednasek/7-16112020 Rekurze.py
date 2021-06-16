"""
Abstraktní datové typu
    zásobník, fronta (cyklická, ...)
    zápis jako pole, lineární spojový seznam, ...

Rekurzivně můžu euklida, palindrom, Fibonachiho
"""


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def fib2(n):
    if n == 0:
        return 0
    a = 0
    b = 1
    while n > 1:
        a, b, = b, a + b
        n -= 1
    return b


print(fib2(int(input())))

"""
Můžeme odvodit z rekurze vzorec a ten použít

Můžeme vzužít rychlého umocňování matice
"""


def otoc():
    u = input()
    if u != "":
        otoc()
    print(u)
