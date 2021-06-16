# Programování - recap před zkouškou

Idc na co se vlastě budou ptát, jen jsem projel prezentace a vypsal pár věcí sem

V druhým souboru jsou pak příklady

EDIT: na zkoušce se prý ptají hlavně na dynamické programování, AVL stromy a virtuální metody

Takže se asi vyplatí si hodit ADSko před Programkem

Jinak není špatné se podívat na nějaké příklady na [forum](http://forum.matfyz.info/viewtopic.php?f=247&t=11818) \
A já napsal svoje zadání na konec tohohle souboru

## Notes ze zimního

Všechno je objekt, lze třeba i vracet funkce a nebo je přepsat

Co všechno je mutable? A že třeba tuple a string nejsou.

Začátek interface, abstract, duck typing

Staticmethod a classmethod, i proměná může patřit třídě

Polymorfismus - schopnost volat metody objektů odvozených z jiných tříd

V Pythonu jsou všechny funkce/metody virtuální

Strom hry, minimax, negamax, heuristika

…

## Notes z letího

Some basic stuff

### 2. Přednáška

`public`, `private`, `protected` - kdokoliv/jen stejná třída/i dědic třída

`static` - přísluší třídě a ne objektu

Objekty mají atributy a třídy proměnné

### 3. Přednáška

modifikátory \
&nbsp; `ref` - předání proměnné refernecí \
&nbsp; `out` - neinicializovaná proměná, která se přepíše

konstruktor - implicitní, přetíženost, `:base{}` a `:this{}`

`virtual` - musí být přepsaná `override`

Tabulka virtuálních metod (VMT) - tabulka příslučící celé třídě a každý objekt má odkaz na tu svou

Alternativa je metody schovávat pomocí `new`, idc co je lepš \
s `new` se to dá asi předefinovat ůplně a `override` přepíše jen implementaci

### 4. Přednáška

`abstract` - znamená nekompletní implementaci a automaticky je virtuální

`interface` - obsahuje pouze deklaraci metody, kterou pak třída musí mít

Rozdíl v těch dvou, aspoň jak to chápu já, je, že abstract je core identita dědící třídy a interface tomu pak dává jen určité bonuové vlastnosti. Navíc abstract může mít statické členy, konstruktor, definici metod, konstanty a nemusí být ani plně implementovaná...

`sealed` - z metody nelze dědit

V usingu můžeme vytvářet aliasy

### 5. a 6. Předáška - Diskrétní simulace

Programování řízené událostmi - nějaká smyčka, která kontroluje události\
Používá se hlavně v GUI

### 7. Předáška - Grafika

DirectX, OpenGL, Graphics

`System.Drawing` - pen, color, bitmapa, brush

### 8. Přednáška - Generika

`System.Collections`

Generika - `List<int>` …

`try`, `catch`, `finally` a `throw`

UML a Data Flow diagram

### 9. Přednáška - Basically ADS

Dynamické programování - Editační vzdálenost, … viz. ADS

Snad jediné matice byly new:

* na vynásobení a×b a b×c potřebujeme a·b·c
* uděláme si tabulku P, kde P_{k,i} reprezentuje počet pro součin k matic počínaje i-tou
* a pak ji od k=0 vytváříme 

### 10. Předáška - Basically ADS 2

* Grafy, definice, nejkratší cesta, kostra, …
* Quickselect, quicksort
* …

### 11. Přednáška

`delegate`  - předávání funkce jako parametr \
dokonce ji ani nemusíme pojmenovávat

#### Vlákna

To jsou zase systémy

Producent-konzument, paralelizace

Třída Thread, které v parametru dáme delegát - spustíme metoudou `Start`

### 12. Přednáška

Příklad zkoušky

Hygiena programování

Specifika jiných jazyků 

### 13. Přednáška - Xamarin a testování

`Assert`, nový podprojekt UnitTesting

### 14. Přednáška - Genetické algoritmy

Snadná aproximace

&nbsp;

---

&nbsp;

# Co si vytáhnul já

### Zadání

Během prázdnin chcete navštívit koncerty tak, aby jste měli naposloucháno co nejvíce minut hudby. \
Koncerty jsou v určitýčh městech a mezi všemi městy vede celočíselně dlouhá cesta (nemusí ale být přímá) \
Můžete najezdit celkem 2000km a každý den stihnete nejvýše jeden koncert. Ovšem žádná dvě města nejsou tak daleko, aby jste koncert další den nestihli.

### Vstup - soubor se značkami na začátku řádku
```
M...dvojice měst a jejich vzdálenost
P...název skladby, zpěvák, délka
K...koncert - den, město a zpěvák
	p...název skladby na koncertě (pod každým K je více)
```

### Výstup

Maximální délka hudby

### Omezení

Počet písniček celkem <= 10 000
Počet dní = 92
Počet zpěváků <= 100
Počet měst <= 20
Na jednom koncerte <= 100 pesničiek

### Řešení

*BTW Nebudeme používat stringy, ale čísla (názvy měst, kapel, ...)*

1. Floyd-Warshall na cesty mezi všemi cesty
2. Hešovací tabulka s klíčem zpěvák a název a hodnotou její čas
3. Slovník koncertů s hodnotami jejich celková doba
4. Core problém

#### Core problém

Prvně si to představím jako orientovaný graf, kde jsou pomyslné sloupce dny a vrcholy koncerty. \
To vede na dynamické programování - buď rekurze nebo tabulka

Pak si uvědomím, že BÚNO můžu brát jen nejdelší koncerty v městě

Rekuzi přeskočím, protože to není tak hard si to představit a rovnou vytvořím skoro 3D pole, kde jsou řádky města, sloupce dny a do hloubky počet kilometrů \
Uvnitř je pak reprezentace toho, že jsem v danou chvíli na koncertu byl a maximální počet minut na tyhle souřadnice \
To, že je skoro 3D souvisí s mojí polemikou na téma, jestli se vyplatí pro všechny z 2000 možných množství kilometrů vlastní buňka, protože ze začátku to bude prázdné \
Navíc když vezmu setřízenou strukturu jako AVL strom, tak můžu odřezávat slepé větve (zbývá míň kilometrů a mám menší množství minut) \
*Stačílo jen zmínit, že neznám konstanty, protože jsem AVL ještě nikdy neimpletoval a měl jsem to jako otázku v druhé části xdddd* \
To 3D pole pak procházím po sloupcích, kde pro každou buňku projdu obsahy všech buněk v předchozím slupci a pokud možno, tak k nim přičtu pohodu a odečtu vzdálenost \
Nakonec z posledního dne vypíšu max čas
