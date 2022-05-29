# Požadavky ke zkoušce z ADS2

Seznam všech definic, algoritmů, vět a důležitých příkladů z přednášky, které požaduji u zkoušky. K algoritmu vždy patří rozbor korektnosti a časové a prostorové složitosti. K větám patří důkaz.

## Vyhledávání v textu

> Průvodce 303 - 315

**Terminologie okolo řetězců (podslova, prefixy, suffixy)**

Značení $\Sigma, \alpha, \iota$ ... prefixy, sufixy, ...

**Knuth-Morris-Pratt**

Abychom při vyhledávání v textu nepostupovali hrubou silou, tak si vytvoříme vyhledávací automat - pole zpětných hran, dopředné hrany

Invariant: Jaký nejdelší prefix jehly je sufix sena
Složitost: $\Theta(S)$ - složit jednoho kroku podle počtu dopředných hran a zpětných hran maximálně jako dopředných
Konstrukce automatu v $\Theta(J)$ tak, že automat spustím na řetězec bez prvního písmena

**Aho-Corasicková**

Ve složitosti je potřeba ošetřit zvláštní vstup a tedy  $\Theta(S + \text{ počet výskytů} + \text{ součet jehel})$

Automat bude trie ve které budou zkratkové hrany
Konstrukce po hladinách a přidávání konce slov nebo zpětných hran

**Rabin-Karp (okénkové hešování)**

Vytvořím si hešování, které můžu rychle měnit s posunem doprava

$H(x_0, \cdots, x_{j-1}) = (x_0 r^{j-1} + x_1 r^{j-2} + \cdots + x_{j-1}r^0) \text{ mod } N$ 

Pak mi stačí přenásobit poslední hešh $r$ a odečíst $x_0 r^j$ a přičíst další znak a tedy $x_j$

**Počet kolizí u okénkového hešování**

Pro ideální hešovací funkci je $Pr[\text{falešný výskyt}] =\frac{1}{N}$ a tedy průměrný čas pro falešné je $O(\frac{S \cdot J}{N})$ a to ostatní je v $O(S)$ a $O(J\cdot V)$ -  takže (nic moc pro hodně opravdových výskytů)

Vlastnosti polynomů - vytýkání kořenů, omezení počtu kořenů, polynomy stejné pokud stejné ve více než stupeň bodech 

Naše hešovací funkce má z vlastností pravděpodobnost falešného výskytu $\frac{J}{N}$ a tedy nám stačí volit $N$ jako $J^2$

---

## Toky v sítích

> Průvodce 319 - 342

**Síť, tok, přebytek, velikost toku**

Orientovaný (BÚNO symetrický)  graf, zdroj, stok, funkce, která přiřazuje kapacity, přítok, odtok

Tok je funkce pro kterou přiděluje čísla omezená kapacitou a drží Kirchhoffův zákon

**Rezerva hrany, nasycená hrana** - $r(uv) := c(uv) - f(uv) + f(vy)$, nasycená má kladnou rezervu

**Ford-Fulkerson**

Myšlenka postupného vylepšování toku nejmenší rezervou na cestě
Musíme přidat odečítání v protisměru, i tak se ale zastaví jen pro racionální (zachová celočíselnost toku)

Edmond-Karp nám říká, že když budeme používat nejkratší nenasycenou cestu, tak $O(nm)$ iterací a $O(m)$ jedna iterace

**Řez, kapacita řezu, velikost toku na řezu, minimální řez a maximální tok**

Elementární řez je obvs - průnik skalárního součinu a hran mezi komponenty, zdroj v jedné...

Delta na řezu ($f^\delta (A,B) = f(A,B) - f(B,A)$) je velikost toku - ze součtu přebytků vrcholů
Velikost toku může být maximálně tak velká jako velikost řezu - a když rovnost, tak je maximální tok - přispíváním

Tím ukážu i stav po konci F.F. - vezmu si množinu vrcholů pro které existuje cesta ze zdroje

**Největší párování v bipartitním grafu** - ez... jedna iterace $O(m)$ a počet iterací $O(n)$ (každá zlepší aspoň o jedna)

**Čistý tok, blokující tok, vrstevnatá síť** - Usnadní nám Dinice

Čistý tok (průtok) - $f^*(uv) = f(uv) - f(vu)$
Blokující tok - na každé cestě ze zdroje je alespoň jedna nasycená hrana
Vrstevnatá síť - Všechny její vrcholy leží na nejkratších cestách

**Dinicův algoritmus (zlepšující toky)**

Sestrojíme síť rezerv bez nulových rezerv, vyčistíme ji, pokud neexistuje cesta, tak konec, jinak zlepšíme náš tok pomocí nějakého blokujícího

Čištění sítě - BFS bez hran do navštívených a mazání slepých uliček přes frontu
Blokující tok najdu tak, že budu zaplňovat a mazat hrany a průběžně čistit slepé uličky

Korektnost opět podobná F.F. - když neexistuje nenasycená cesta ze zdroje

Složitost - Hledání blokujícího toku je $O(nm)$, čistění a všechno ostatní je $O(m)$
Délka nejkratší cesty vždy roste, protože hrany po směru mažeme a proti směru prodlužují, a z toho celkem $O(n ^2m)$

**Goldbergův algoritmus (s výběrem nejvyššího vrcholu)**

Pošleme vlnu (tok, který může mít libovolný nezáporný přebytek ve vrcholech) a potom budeme zpátky převádět přebytky

Indukcí získáme základ ($f$ je pořád vlna, $h$ neklesá, $h(z)$ a $h(s)$... , $f^\Delta(v) \geq 0$) a invariant o spádu (kladná rezerva implikuje spád max. jedna)
Lemma o korektnosti pak, že je to tok (jinak by se nezastavil) a je maximální (sporem - existovala by nenasycená cesta poruší lemma o spádu)

Pro $u$ s přebytkem $\exists$ nenasycená cesta do $z$ - přes množinu nenasycených cest z $u$ do které spadá $z$ kvůli součtu přebytků (přispívání hran).
Max výška je $2n$ (z cesty do zdroje), z toho získáme, že maximálně $2n^2$ kroků

Převedení je nasycené pokud vyplýtváme rezervu - těch může nastat $nm$. Pro počet nenasycených použiji potenciál - součet výšek kladných přebytků. Zvednutí vrcholu zvýší o 1 ($2n^2$), nasycené nejvýše o $2n$ ($2n^2m$), nenasyceně sníží alespoň o 1. Celkem dostanu $O(n^2m)$ 

Implementace pomocí seznamu všech vrcholů s kladným přebytkem, seznam využitelných hran pro každý vrchol.
Výběr vrcholu i převedení přebytku $O(1)$, zvednutí vrcholu $O(n)$. Celkem $O(n^2m)$, protože $2n^2\cdot n + nm \cdot 1 + n^2m \cdot 1$

S největším přebytkem to bude $O(n^3)$ pomocí potenciálu - nejvyšší hladina s přebytkem
Dá nám $O(n^2)$ snížení a zvýšení a na fázi $n$ nenasycených převedení, protože v každém vrcholu max jednou

---

## Algebraické algoritmy

> Průvodce 391 - 406

**Reprezentace polynomu grafem**

Graf je reprezentován více než stupeň hodnotami - to nám umožní efektivnější násobení polynomů. Vezmeme dva polynomy, doplníme nulami, dosadíme hodnoty, vynásobíme vypočítané funkční hodnoty a převedeme zpátky - převod je ale obecně pomalý, naštěstí my to obecně nemusíme.

Budeme chtít rozděl a panuj. Dosazované hodnoty budou v půlkách pouze s jiným znaménkem a když rozdělím polynom na sudé a liché exponenty, tak bude stačit rekurzivně vyhodnotit jen polovinu bodů a druhá snadno - z toho $O(n \log n)$. Jenomže se znaménka rekurzí rozbijí.

**Primitivní n-tá odmocnina z jedničky**

 $e^{\frac{2k\pi\cdot i}{n}}$ je primitivní odmocnina jedničky a  $e^{-\frac{2k\pi\cdot i}{n}}$ komplexní sdružení je také primitivní

Pozorování: $\omega^0,\cdots, \omega^{n-1}$ jsou různá a důkaz přes podíl stejných, pro sudé $n$ je prostřední prvek $-1$

**Rychlá Fourierova transformace, její inverze a násobení polynomů**

Když polynom rekurzivně vyhodnotíme v $\omega^0,\cdots, \omega^{n-1}$. Uděláme to tak, že získáme vyhodnocení s $\omega^2$ v polovočních polynomech jenom se sudými a pak jenom s lichými koeficienty. Ty vyhodnocení  spojíme tak, že pro $j<n/2$ bude  $y_j = s_j + \omega^j \cdot l_j$ a  $y_{j + n/2} = s_j - \omega^j \cdot l_j$.

Vyhodnocené polynomy pak mezi sebou snadno vynásobíme v $O(n)$. Pak to ale budeme muset převést zpět na koeficienty pomocí inverze.

Fourierova transformace je zobrazení $y_j = \sum_{k=0}^{n-1}x_k\cdot \omega^{jk}$, v našem případě zobrazujeme vektoru koeficientů na jeho graf v bodech $\omega$. A protože je to lineární zobrazení, tak je nějaká matice $\Omega$ a její inverze $\Omega^{-1}$. Elementárními úpravami zkusíme, že $\Omega \cdot \overline\Omega = n \cdot E$

$\Omega_{jk} = \omega^{jk}$  a $\Omega^{-1} = \frac{1}{n} \overline{\omega^{jk}}$ a můžeme na výpočet opět použít rychlou Fourieurku neboť se to bude lišit jenom o faktor

---

## Paralelní algoritmy

> Průvodce 349 - 360

**Hradlová síť**

Konečná abeceda a acyklický graf, kde vrcholy jsou vstupy, výstupy, hradla s omezenou aritou...

Počítám po taktech, již spočítaná hradla se nezmění (indukce)
Časová složitost je hloubka sítě (počet taktů) a prostor je počet hradel

Příklad s různou složitostí vícenásobného OR

**Sčítání přirozených čísel hradlovou sítí**

Školním způsobem dostaneme lineární složitost, brzdí nás přenosy z nižších řádů

Rozebereme jednobitové bloky a libovolně velké bloky, jak se chovají - pak to převedeme do binárky
Pak budu spojovat bloky po dvou a až dostanu vše, tak je zase začnu zahušťovat

**Komparátorová síť**

Komparátor prohazuje hodnoty - v průvodci ukázka bublinkového třídění

**Bitonické třídění komparátorovou sítí**

Čistě bitonická posloupnost a bitonická posloupnost (dá se rozdělit na roustoucí a klesající posloupnost)

*Separátor* - rozdělí bitonickou posloupnost na dvě bitonické posloupnosti, kde všechny v jedné jsou větší
*Bitonická třídička* - setřídí bitonickou posloupnost (snadno štěpením na poloviny se složitostmi $O(\log n)$)
*Slévačka* - dvě setříděné posloupnosti spojí do jedné setříděné (jednu obrátím a dá do třídičky)

Celkem hloubka $\Theta(\log^2 n)$ a $\Theta(n \log^2 n)$ komparátorů

Jak separátor separuje? Komparujeme dva prvky posunuté o polovinu
Rozdělíme si posloupnost na horu a údolí - $k$ bude předěl a podle předělu se bude prohazovat...

---

## Geometrické algoritmy

> Průvodce 369 - 385

**Konvexní obal**

Nějaký obecná poloha - budeme zleva zametat rovinu a odebírat z obalu body, které poruší konvexnost
Pro lepší popis si rozdělíme obal na horní a dolní obálku

Algoritmus zapíšeme tak, že body setřídíme podle $x$, první vložíme do $D$ i $H$ a pak budeme body přidávat do obou obálek, přičemž budu kontrolovat poslední trojici bodů a to jak zatáčí - vyhazování

A pokud budu mít body nad sebou, tak můžu trošičku pootočit a to odpovídá lexikografickému třídění

Brzdí nás akorát třídění bodů, protože zbytek je lineární (můžu odebrat jen body, kterém jsem přidal)
Jak ale zjišťovat, jak trojice zatáčí - přes determinanty, ten nám se souřadnicemi vrchol určí obsah rovnoběžníku a to i záporně podle orientace úhlu

**Průsečíky úseček**

Mohlo by to být až kvadratické kvůli případu mřížky, to ale běžně nenastává a proto budeme zase zametat
Budu se snažit aby všechny průsečíky nad přímkou už byly nahlášeny, to vede k nějaké diskrétní simulaci

Budeme mít události - začátky události, konce úseček a průsečíky (ty musím plánovat dynamicky)
Všimnu si, že před tím než nastane průsečík, tak se úsečky stanou sousední - naplánuji si průsečík (jsem ochoten rušit)

Algoritmus si tedy bude pamatovat průřez a kalendář událostí a dokud nebude kalendář prázdný, tak se zachovám podle typu události - smažu, přidám do průřezu nebo nahlásím průsečík a z toho změním průřez a přeplánuji průsečíky

Kalendář i průřez budou BVS - operace $O(\log n)$ a z toho složitost $(2n + p)$ událostí a každá v $O(\log n)$

**Voroného diagram**

Systém oblastí (množin) odkud je nejblíže k nějakému bodu - ty oblasti jsou konvexní mnohoúhelníky (s pomocí os)
Počet hranic těch oblastí je lineární - uděláme duálem rovinný graf z oblastí a pak $e \leq 3v-6$ a $v + f = e + 2$

**Lokalizace bodu v mnohoúhelníkové síti**

Začnu s tím, že budu zametat a podle událostí zjistím kam to spadá - $O(n \log n)$
Pak to zlepším, že si rovinu rozkrájím na pásy a pro každý si uložím kopii průřezu - dotaz v $O(\log n)$, ale výroba $O(n^2)$

**Semipersistentní binární vyhledávací strom**

Pro předchozí téma mi ale stačí si pamatovat změny - *sempersistentní* vyhledávací strom
Zakázáno modifikovat původní vrcholy a proto vkládání vytvoří kopii cesty až do kořenu - čas i paměť operací $O(\log n)$

Tím pádem to zredukuji z $O(n^2)$ na $O(n \log n)$

---

## Převody problémů

> Průvodce 431 - 454

**Rozhodovací problém** - Funkce z $\{0,1\}^*$ do $\{0,1\}$ a tedy na vstup odpoví ANO/NE

**Bipartitní párování jako rozhodovací problém** - Má $G$ párování o alespoň $k$ hranách?

Provedeme kódování precizně - $\fbox{ N }\ \fbox{ K }\ \fbox{ Matice sousednosti }$
Musíme ještě specifikovat jak $N$ a $K$ jsou velké - to zapíšu v jedničkové soustavě před to a ukončím to nulou

Také si musíme dodefinovat, že na nesplňující kódování budeme odpovídat nulou

**Převod mezi problémy**

Problémy lze převést pokud existuje nějaká v polynomiálním čase spočitatelná funkce (převod či redukce), která mi přeloží vstup pro první algoritmus na vstup pro druhý algoritmus a odpovědi jsou pro každý vstup ekvivalentní

Pokud $L\rightarrow M$ a $M$ je polynomiálně řešitelné, pak $M$ je polynomiálně řešitelné  - $O\left(b^k\right) = O\left(a^l + {a^{lk}}\right)$...

**Vlastnosti převoditelnosti** - reflexivní (převod identita), tranzitivní (skládání převodů), ne-antisymetrické a ne-lineární

**Problémy:**

* **Klika** - úplný podgraf na $k$ vrcholech
* **Nezávislá množina** - nezávislá množina na $k$ vrcholech
* **SAT, 3-SAT, 3,3-SAT** - splnitelnost CNF formule / s klauzulemi max. délky 3 / každá proměnná max. 3x
* **3D-párování** - tři množina a zajímá nás, jestli existuje způsob, jak vytvořit perfektní podmnožinu trojic

**Převod klika ↔ nezávislá množina** - triviálně přes doplněk grafu

**Převod SAT → 3-SAT → 3,3-SAT**

Z 3-SAT na SAT akorát zkontrolujeme vstup a pak identita
Obráceně budeme rozštípávat klauzule na dvě kratší - do jedné dám prvovýrok a do druhé opačný

V polynomiálním čase proto, že po $(k-3)$ krocích jedna klauzule (shora to odhadneme $n^3$)

Musím ukázat, že jeden krok zachová splnitelnost - dvě implikace a to tak, že pokud uštípnutá je nesplnitelná, tak novou v té uštípnuté dám na $1$... a obrácená implikace stačí zapomenout nové

Z 3-SAT na 3,3 pak budu dělat nahrazením novými proměnnými a pak vytvořím cyklickou implikaci 
3,3-SAT se snadno vylepší na to, že literál není 3x pozitivně ani 3x negativně - bude se to hodit pro 3D-pár.

**Převod 3-SAT → nezávislá množina**

Udělám si z klauzulí trojúhelníky, spojím negace a pak budu hledat NzMno velikosti počtu klauzulí

**Převod nezávislá množina → SAT**

Vyrobím si proměnné podle toho, jestli vrcholy patří do NzMno a zavedu klauzule, že nepřidám vrcholy se sousední hranou. Pak ale musím zařídit, že vyberu alespoň $k$ vrcholů - budu mít klauzule na jejich počítání

**Převod 3,3-SAT → 3D-párování**

Musím mít nějaký *gadget* pro proměnou (2 kluci, 2 holky, 4 zvířátka) a pro klauzuli (kluk, holka a 3 zvířátka)
Navíc si budeme muset ale pořídit kluky a holky, které ubytují zbylá zvířátka ($2 \cdot \#\text{prom} - \# \text{klauzulí}$)

Proč? Nechť je formule splnitelná, podle něj vyrobím gadgety a ukáži párování a pak obráceně....

## NP-úplnost

**Třída P** - třída všech problémů řešitelných v polynomiálním čase ($P(|x|)$ počet kroků)
**Třída NP** - třída problému takových, že mají polynomiální verifikátor (ten dostane polynomiální certifikát)

**NP-těžké **- dá se na něj převést každý problém z NP a **NP-úplný** - pokud navíc leží v NP

**Pokud K∈P a K je NP-úplný, pak P = NP** - Nechť $L \in $ NP, pak $L \rightarrow K$ a proto $L \in$ P
**Pokud A→B a B∈P, pak A∈P** - už jsme dělali... je potřeba jen promyslet délku vstupu do $B$
**Pokud A→B, A je NP-úplný a B∈NP, pak B je NP-úplný** - prvně všechny NP problémy převedu na A...

**Cookova věta: SAT je NP-úplný (náznak)**

Pro každý problém z P zle algoritmem vyrobit v polynomiálním čase hradlovou síť s $n$ vstupy a $1$ výstupem
To naznačíme z počítačů (booleovské obvody měnící se v čase). Stačí nám tedy $T$ kopií sítě velikosti $T$...

Usnadníme si definici NP tak, že certifikát bude mít pevnou velikost v závislosti na vstupu

Ukážeme, že obvodový SAT je NP-úplný (v NP leží očividně)
Budeme mít NP problém $L$, verifikátor $V$ a polynom $g$ pro důkaz. Potom můžu vygenerovat polynomiálně velký obvod pro $V$. Tomu obvodu zafixuji vstup původní vstup a hledám splňující certifikát.

**Převod obvodového SATu na SAT**

Podle výstupů hradel vyrobím proměnné a klauzule např. ${x\rightarrow \fbox{NOT} \rightarrow z}$ bude $(x \Rightarrow \neg z) \wedge (\neg x \Rightarrow z)$ 

**Klasické NP-úplné problémy**

* SAT. 3-SAT, ...
* *Nezávislá množina, Klika, Barvení grafu, Hamilton, 3D párování*
* *Součet podmnožiny, Batoh, Dva loupežníci. $Ax=1$*

## Jak zvládnout těžký problém

Malý vstup, speciální případy, aproximace, heuristika (genetické algoritmy), ...

**Nezávislá množina ve stromu**

Alespoň jedna nezávislá množina ve stromu obsahuje list
Nechť $M$ je nějaká nezávislá množina, pokud v ní $l$ je, tak hotovo a jinak ho budu přidávat...

Z toho iterativně přidám list a odeberu jeho souseda

**Barvení intervalového grafu**

Příklad s přednášky - intervaly na přímce
Setřídím a pak timeline zametám bodem (přidám do posluchárny nebo založím novou) - bez třídění $O(n)$

Funkčnost triviální, optimální z několika překrývajících se přednášek (kliky)

**Pseudopolynomiální algoritmus pro problém batohu**

Pro malá čísla použijeme dynamické programování - podproblém bude prvních $k$ předmětů
Zadefinuji $A_K(c)$ jako minimální hmotonost, která má cenu $c$ (pokud není, tak $\infty$)

Budu si vyplňovat tabulku s řádky jako $k$ a sloupce budou $c$ tak, jestli obsahuje $k$-tý předmět a tedy $O(Cn)$

**Aproximační algoritmus**

Algoritmus, který nám dá řešení jenom $\alpha$-krát horší než je optimum (rozdíl pro maximalizační a min...)

**2-aproximace obchodního cestujícího v metrickém prostoru**

Hledáme co nejkratší hamiltonovskou kružnici v ohodnoceném úplném neorientovaném grafu

Najdeme minimální kostru a tu obejdeme
Proč je to optimální? Protože $\text{min. kostra} < \text{náš algoritmus} < 2 \cdot \text{kostra}$

**Neaproximovatelnost obchodního cestujícího bez trojúhelníkové nerovnosti**

Kdyby existoval, pak P=NP
Aproximaci bych totiž mohl použít pro nalezení hamiltonovské kružnice, tak že bych graf ve kterém ji hledám doplnil pomocí dlouhých hran

**FPTAS pro problém batohu**

Zmenšíme a zaokrouhlíme ceny (nakvantujeme) a pak použijeme náš pseudopolynomiální

Chyba jedné ceny je $\frac{C_{max}}{M}$ a celé množiny je $n$-krát větší - budeme se snažit dosáhnout $\epsilon$ tak, že $M = \lceil n / \epsilon \rceil$
Abychom dosáhli přesnosti $\epsilon$ ještě musíme zahodit předměty, které se nevejdou do batohu

Zvládneme $O(n^3/\epsilon)$

**Polynomiální aproximační schéma (PTAS)** - libovolná $\epsilon$-aproximace se spočte v $O(\text{poly}(n))$, kde v poly je $\epsilon$

**Plně polynomiální aproximační schéma (FPTAS)** - libovolná $\epsilon$-aproximace se spočte v $O(\text{poly}(n\cdot \epsilon))$

