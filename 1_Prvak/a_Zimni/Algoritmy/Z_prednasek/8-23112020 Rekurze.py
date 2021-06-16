k = 3
n = 5


def cislo(c):
    """ všechny k-tice v soustavě o základu n"""
    for i in range(n):
        c.append(i)
        if len(c) < k:
            cislo(c)
        else:
            print(c)
        c.pop()


# cislo([])

"""
Kdyby to nebyl Python, tak musíme prvně alokovat pole a pak si předávat argument index pole

A zároveň lze napsat elegantněji... ale miň efektivně
"""

arr1 = [0] * k


def cislo1(p):
    """ všechny k-tice v soustavě o základu n"""
    if p == k:
        print(arr1)
    else:
        for i in range(n):
            arr1[p] = i
            cislo1(p + 1)


# cislo1(0)

"""
Variace bez opakování lze udělat s ifem předchozích hodnot 

Zajímavější jsou ale kombinace bez opakování
"""

arr2 = [0] * (k + 1)


def kombinace(p):
    """ všechny k-prvkove kombinace z n prvku"""
    if p > k:
        print(arr2[1:])
    else:
        for i in range(arr2[p - 1] + 1, n - (k - p) + 1):  # proc ten konec range, vzdyt to je nula???
            arr2[p] = i
            kombinace(p + 1)


# kombinace(1)

""" 
Doplnění znamének 

n čísel a my máme doplnit + nebo -
"""

# num = [int(_) for _ in input.split()]
# ...
# to nebudu psát voe

"""
Rozklad čísla
    budem dělat pouze klesající aby se to neopakovalo
"""

m = 7
a = [m + 1] * (m + 1)


def rozklad(z, p):
    """
    z - kolik zbývá
    p - kolikátý vytváříme
    """
    if z == 0:
        print(a[1:p])
    else:
        for i in range(1, min(z, a[p - 1] + 1)):
            a[p] = i
            rozklad(z - i, p + 1)


# rozklad(m, 1)

""" Binární strom rekuzrivně

průchod PREORDER, INORDER, POSTORDER
"""


class Vrchol:

    def __init__(self, x=None):
        self.info = x
        self.levy = None
        self.pravy = None
        # self.rodic = None


def preorder(self):
    print(self.info)
    if self.levy is not None:
        self.levy.preorder()
    if self.pravy is not None:
        self.pravy.preorder()


" Lze to zapsat i zásobníkem"
# TODO podivat se na video se zasobnikem (1:05?)

"""
Obecný strom s max počtem dětí a nebo seznamem

Kanonická reprezentace
    Ukazuje na bratra a na syna
    Špatné na průchod
    
Písmenkový strom (trie)
"""
