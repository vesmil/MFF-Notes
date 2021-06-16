""""
Grafy
    Reprezentace
        Matice sousednosti
            Vhodná pro gtafy s malým počtem prvků a málo hranami
        Seznam nálsedníků
            pole N seznamů
                v Puthonu, jinak problém s alokací
            matice N x N-1
                neušetřím prostor, ale ušteřím rychlost hledání
            matice N x R
                když z každého vede max R cest
            celkem máme M hran
                seznam ve dvou jednorozměrných polích
                jedno následníky a jedno indexování
        Seznam hran
            pole délky M se všemi hranami
            nebo spojový sezna,
        Matice incidence
            nebudeme s ní pracovat
        Dynamická reprezentace

    Základní grafové porblémy
         Je graf souvislý?
         Komponenty souvislosti
         Obsahuje nějaký cyklus?
            <=> je graf nebo les
        Určit libovolnou kostru
        Určit zda je bipartivní
            Prohledávání do hloubky a do šířky

        Nejkratší cesta určit délku a najít
            Prohledávání do šířky, můžou být i orientované

        Prohledávání do hloubky
            změna od stromů - musíme kontrolovat průchody

            Průcchod rekurze
                navstiven = False * n

                def Pruchod(v):
                    navstiven[v] = True
                    zpracuj_vrchol(v)
                    for v3echny hrany (v, u):
                        if not navstiven[u]
                            Pruchod(u)

            Průchod zásobníkem
                navstiven = [False] * n
                navstiven[s] = True
                zasob = [s]

                while len(zasob)>0:
                v = zasob.pop()
                pro všechny hrany(v,u):
                    if not navstiven[u]:
                        navstive[u] = True
                        zasob.append(u)

            Složitos O(N+M)

        Prohledávání do šířky
            opět pole navstiven
            stejně jako do hloubku ale s frontou

            navstiven = [False] * n
            navstiven[s] = True
            fronta = [s]

            while len(zasob)>0:
                v = fronta.pop(é)
                pro všechny hrany(v,u):
                    if not navstiven[u]:
                        navstive[u] = True
                        zasob.append(u)

            umíme tu frontu udělat lépe... tohle totiž složitosti neodpovídá

    And finnaly
    Řešení problémů
        1. Souvislost
                průchod s počítadlem vrcholů
                pokud má počítadlo hodnotu N ✓
        2a. Komponenta
                průchod a výstup pole navštíven bool
        2b. Všechny komponenty
                opakovaně 2a s polem navšítven intů
            Stejná časová složitost jako průchod (když hledáme od místa, kde jsem skončil)
        3. Existence cyklu
                průchod, ale dávám pozor, jestli byl vrchol navstiven
        4. Nalezení kostry
                analogicky jako 3, pokud nebyl navštiven -> přidám do kostry
        5. Určit bipartivitu
                průchod a vrcholy střídavě značíme 1 a -1 a dáváme pozor na sousedy

        6. Nejkraší vzdálenost
            průchod do šírky
                nenavštívené vrcholy -1, výchozí vrchol 0 a sousedé +1
                    "algoritmus vlny"
                opět O(N+M)
        7. Nejkratší cesta
            k 6. přibyde zpětný chod

"""