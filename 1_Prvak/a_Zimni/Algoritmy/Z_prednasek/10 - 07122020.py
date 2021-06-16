"""
Prohledávání stavového prostoru do hloubky
    = Depth-first search = Backtracking

    Projít všechny možnosti x najít jedno řešení
    Na stejném principy je založená rekurze

    Opět rekurzivní procedura nebo zásobník

    Osm dam na šachovnici, jezdcova procházka

    Časová a paměťová složitost

    Urychlení
        Ořezávání
            Průběžně kontrolujeme stav
            Dáma -> kontrolovat kolize
        Heuristiky
            Odhad na nejlepší místo
            V případě jezdcovy procházky -> skákat prvně na místa s malým počtem pokračování

        Kombinace
            Cesta mezi dvšms městy
                Pokud už jsem urazil delší cestu než tu nejkratší -> X
                Heuristika třeba jet na východ


    Algoritmus minimaxu
        Hra s úplnou informací
        Najít nejlepší tah

        Strom hry
            ...

Prohledávání do šířky

"""

