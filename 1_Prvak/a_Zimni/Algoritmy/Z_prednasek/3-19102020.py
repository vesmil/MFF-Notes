###region Euklid
"""
Největší společný dělitel
    Brute force
    Prvočíselný rozklad
    Euklidův algoritmus
		Modulo místo odečítání
        Počet iterací je log2 x + log2 y + 1
"""


def euklid(x, y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x


def euklid1(x, y):
    while y > 0:
        x, y = y, x % y
    return x


# print(euklid1(int(input("1:")), int(input("2:"))))

###endregion

###region Horner

def horner(a, x):
    h = 0
    for i in range(len(a)):
        h = h * x + a[i]
    return h


# print(horner([5,0,10,1],2))

###endregion

###region Převod z binární soustav
""" 
Hornerovo schéma s jiným x a str vstupem
"""

cislice = "01"


def bin2int(bin):
    n = 0

    for i in range(len(bin)):
        n = n * 2 + cislice.index(bin[i])
    return n


# print(bin2int("10100"))

###endregion

###region Převody do binární soustav
""" 
Inverzní algoritmus
Potřebuji ho nakonec otočit
"""


def int2bin(n):
    bin = []

    while n > 0:
        bin.append(cislice[n % 2])
        n //= 2

    return "".join(reversed(bin))


# print(int2bin(16))

###endregion

# region Rychlé umocňování
"""
X^13
X^13 = X^8 . X^4 + x
Prevod do binarky
"""


def mocnina(x, n):
    mocnina = 1

    while n > 0:
        if n & 1 == 1:  # na posledním bytu je 1 (to samé co modulu 2)
            mocnina *= x
        x, n = x * x, n >> 1  # bitový posun o jednu do prava, na první místo jde 0
    return mocnina


# print(mocnina(2,10))


def mocnina2(x, n):
    mocnina = 1

    while n > 0:
        if n % 2 == 1:
            mocnina *= x
        x, n = x * x, n // 2
    return mocnina

# print(mocnina2(2,10))

# endregion
