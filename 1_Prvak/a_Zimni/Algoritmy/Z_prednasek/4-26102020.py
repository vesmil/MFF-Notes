spatny = [6, 5, 4, 3, 2, 1]
dobry = [1, 2, 3, 4, 5, 8, 7, 6]
random = [8, 9, 7, 2, 1, 6]


def BubbleSort0(a):
    n = len(a)

    for i in range(1, n):
        for j in range(n - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
        print(a)
    return a


# Asymptoticka slozitost (Thetea) je n^2 nebo take n(n-1)(n-2)...
# Pokud v urcitem rozmezi nevymenim zadne prvky, tak uz jsou vsechny serazene

def BubbleSort1(a):
    n = len(a)

    while n > 1:
        vymena = 0
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                vymena = j + 1
        n = vymena
        print(a)
    return a


# BubbleSort0(dobry)
# BubbleSort0(dobry)

"""
Bubble sort je ale useless

Selection sort
1. Najdi nejmensi a vymen s prvkem 0
2. Druhy nejmensi na pozici 1

Po provedeni i teho cyklu je na i i-ty nejmensi
"""


def SelectionSort(a):
    n = len(a)
    for i in range(n - 1):
        minIndex = i  # docasne minimum
        for j in range(i + 1, n):
            if a[minIndex] > a[j]:
                minIndex = j
        a[i], a[minIndex] = a[minIndex], a[i]  # vymena minima po cyklu s i-tym prvkem
        print(a)

    return a


# SelectionSort(random)

""""
Slozitost:
    pocet porovnani stejny jako u bubble (n^2)
    Vymen je n-1
    
Dalsi je Insertion Sort
    Inspirace trideni karet
    (Vezmem novou kartu a projdem ty co mame zprava do leva)
"""


def InsertionSort(a):
    for i in range(1, len(a)):
        x, j = a[i], i  # Vlozeni do setrideneho 0...i
        while j > 0 and a[j - 1] > x:
            a[j] = a[j - 1]
            j -= 1
        a[j] = x

        print(a)
    return a


# InsertionSort(random)

"""
Invariant: po i tem kroku jsou pozice 0 az i setridena

Opet theta n^2

Lepsi nez Bubblesort

Srovnani se Selection sort - v nem musime projit zbyvaji pro nalezeni minima
V Inserion muze stacit jedine -> Vyhodne pro castecne setridene vstupy
    (Prumerne polovina porovnani nez selection sort)
    
____________________________________________________________________________

Lepsi nez kvadraticke trideni - HeapSort
    Haldove trideni
        Cas O(n log n)
    
    Datova struktura binarni halda
        Operace:  Pridej a odeber min
        
        Odbocka: Graf ma vrcholy a hrany
            Spojeni dvou vrcholu je cesta
            -> Cyklus
            Souvisly graj pokud mezi kazdou dvojici je cesta
            Vzdalenost je nejkratsi cesta
            
            Strom je souvisly a acyklicky
                Ma koren a listy
                Rodic ma deti
                    Pokud jsou deti usporadane ->  Usporadany strom
                Binarni strom - Usporadany koronovy strom, kde kazdy strom ma dve deti
                I-ta hladina
                
            Binarni halda je binarni strom, který
                kazda hladine od provni do predposledni je zaplnena
                Posledni hladina se zaplnuje zleva
                
            Pro kazdy vrchol plati, ze je hodnota je vetsi nez jeho deti
                - min halda
            
    Mame hladu vyska h a n vrcholu
        Pak plati na i-te hladine je 2^i vrcholu
        Na posledni hladine je aspon jeden vrchol
        Tedy n>= suma... -> 2^h   tedy h<= log (o zakladu 2) n
        
    Haldu lze ulozit do pole po hladinach
        Rodic a[i] ma deti a[2*i+1] a a[2*i+2]
        
        0  1  2  3  4  5  6  7  8  9
        5  7  6  9  8  15 11 16 14 10
        
                    5
              7          6
          9       8   15   11
        16 14   10
        
        
    Operace pridej
    Nakonec prvek odebrem
    Probublani
    Je-li poruseno haldove usporadani - vymena rodice s mensim z deti
    
    
    Vstup: pole a
    1. Z prvku vybuduju haldu
        trivialni halda obsahujici jen prvni prvek
        postupne budu pridavat pomoci pridej
        
    2. Budeme odebirat minimum
    
    Problem: trideni na miste

____________________________________________________________________________

Merge sort - n log n

"""

# random = [8, 9, 7, 2, 1, 6]
# ranodmhalda = [1,2,4,7,6,8,9]

halda = []
temp = []


def Pridej(b):
    global halda
    halda.append(b)
    n = len(halda) - 1

    while halda[n] < halda[(n - 1) // 2] and n != 0:
        halda[n], halda[(n - 1) // 2] = halda[(n - 1) // 2], halda[n]
        n = (n - 1) // 2


def OdeberMin(a):
    global halda
    global temp
    temp.append(a[0])

    halda[0] = halda[len(halda) - 1]
    halda = halda[:-1]

    n = 0


# probublani

def Vybuduj(a):
    for i in range(len(a)):
        Pridej(a[i])


def HeapSort(a):
    Vybuduj(a)
    for i in range(len(halda)):
        OdeberMin(halda)


HeapSort(random)
