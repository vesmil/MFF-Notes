# Programování - recap před zkouškou

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

Počet písniček celkem <= 10 000 \
Počet dní = 92 \
Počet zpěváků <= 100 \
Počet měst <= 20 \
Na jednom koncerte <= 100 pesničiek \

### Moje řešení

1. Floyd-Warshall na cesty mezi všemi městy
2. Hešovací tabulka s klíčem (zpěvák, název) a hodnotou odpovídající její délkce
3. Předchozí krok využiji na vyrobení slovníku koncertů s jejich celkovými časy
4. Core problém

*Note 1: Nebudeme používat stringy, ale čísla (názvy měst, kapel, ...)*

*Note 2: Můžu paralelně provést v jednom vláknu Floyda a v druhém časy skladeb a koncertů*

#### Core problém

Prvně si to představím jako orientovaný graf, kde jsou vrcholy koncerty, \
uspořádám si to do pomyslných sloupců odpovídajících dnům a \
z každého koncertu vede hrana do všech koncertů další den.

To vede na dynamické programování - buď rekurze nebo tabulka

Pak si uvědomím, že BÚNO můžu brát jen nejdelší koncerty v městě

Rekuzi přeskočím, protože není tak hard si to představit a rovnou vytvořím 3D pole, kde jsou řádky města, sloupce dny a do hloubky počet kilometrů.
Jedna buňka je pak reprezentace toho, že jsem v danou chvíli na koncertu byl a je v ní maximální počet minut na tyhle souřadnice.

Pak jsem tam hodil úvahu na téma, jestli se vyplatí pro všechny z 2000 možných množství kilometrů vlastní buňka (a tedy nevzít třeba spoják místo pole), protože ze začátku to bude dost prázdné. A navíc když vezmu setřízenou strukturu jako AVL strom, tak můžu odřezávat slepé větve (zbývá míň kilometrů a mám menší množství minut) v rozumném čase. Conlusion byl, že to AVLkem asymptoticky spomalím log počet kilometrů, ale že IRL by se to někdy mohlo hodit.

*Stačílo jen zmínit, že neznám úplně praktickou použitelnost, protože jsem AVL ještě nikdy neimpletoval a měl jsem to jako otázku v druhé části xdddd*

To 3D pole pak procházím po sloupcích, kde pro každou buňku projdu obsahy všech buněk v předchozím slupci (dni) a pokud je to možné, tak od ní odečtu vzdálenost a přičtu čas

Nakonec z posledního dne vypíšu max čas

To, že to doběhne je triviální a snadno se vypočítá složitost a ukáže parciální správnost.
