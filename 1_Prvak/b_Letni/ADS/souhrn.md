Je tady hromada typos, ale idk jestli se mi to reálně chce opravovat

# Úvod 
> 1. Přednáška 4.3.2021

**Příklad na začátek**: Najděte nejdelší rostoucí podposloupnost 

To ale přeskočím, protože se ještě k tomu vrátíme detailněji na konci

# RAM (Random Access Machine)

Nadefinujeme si nějaký abstraktní stroj (výpočetní model)

Ty stroje jsou stejně silné… vysvětlení někdy jindy (hádám, že je tím myšleno Turing complete)

Zpátky k RAMu:

* počítá s celými čísly
* nekonečná paměť indexovaná čísly (reálně ale bude konečná, protože bude počítat konečně dlouho)
* instrukce
	* přiřazení
	* aritmetika (+, -, *, /, mod a bitové AND, OR, XOR, RSHIFT a LSHIFT)
* operandy
	* literál (např: 42)
	* buňka paměti (např [42]) (konvence $A := [-1]$…)
	* nepřímá adresace (např [[42]])

Výpočet: v paměti dostaneme vstup, provádíme instrukce, v paměti odevzdáme výstup

> 2. Přednáška 11.3.2021

Cena Instrukce?

1. Jednotková velikost
	* pozor na velká čísla (vede to k paradoxům) a například umím dělat součet $n$ čísel konstantně
2. Jednotková, ale omezíme  čísla šířkou slova $W$ (bitů)
	* Potřebujeme $W \geq \log n$ kvůli čtení vstupu a tedy všechna čísla jsou menší než $2^{c\cdot \log n}$
	* Omezili jsme tedy polynomem nejen velikost čísel, ale i adresovatelný prostor
3. Logaritmická cena instrukce - cena je počet bitů se kterými pracujeme
	* Je to hodně nepohodlné
4. Relativní logaritmická
	* $\lceil \frac{\text{počet bitů čísel}}{\log n} \rceil$
	* kombinuje výhody předchozích (neomezený prostor a pohodlí)

## Čas a prostor výpočtu

#### Definice Pro program o vstupu $x$ je

**Čas běhu:**  $t(x) :=$ součet cen provedených instrukcí

**Prostor běhu:** $s(x) :=$ max. použitá adresa - min. použitá adresa (obvykle počítáme i vstup)

Zavádí se pak i nekonstantní cena buněk

Mohou ale být i nekonečné, ale nebudeme se jim zabývat

**Časová složitost:** $T(n) :=$ max{$t(x)$ | $x$ je vstup velikosti $n$}

> Co to je ale vstup velikosti $n$? Je to např. počet čísel, bitů, znaků řetězce, vrcholů a hran…

**Prostorová složitost:** Analogicky maximální z prostoru běhů pro všechny vstupy velikost $n$

### Příklad algoritmu

**Bublinkové třídění:**

```
ZNOVU:
P ← 0    # indikátor toho, zda se něco přesunulo
I ← 1   

DALSI:   # zkouším vyměnit dva prvky vedle sebe
J ← I + 1
if  $[I] ≤ [J] then goto OK
T ← [I]
[I] ← [J]
[J] ← T
P ← 1
  
OK:
I ← I + 1
if I < [0] then goto DALSI   # v nule mám celkovou délku, takže tohle je for cyklus
if P=1 then goto ZNOVU       # tohle je zase vnější for cyklus

halt
```

**Analýza**

Vnitřní je 4-8 instrukcí a proběhne až $n - 1$krát

V tom vnějším jsou navíc 3 instrukce, takže má $4n-1$ až $8n-5$ instrukcí a proběhne $1$ až $n$ cyklů

Z toho je časová složitost mezi $4n$ a $8n^2 - 5n + 1$ (Toho se ale reálně nedá dosáhnout)

Nejhorší případ ale určitě bude v rozmezí

$$ 4n^2 - n + 1\leq T(n) \leq 8n^2 - 5n + 1 $$

A asymptoticky je to $\Theta(n^2)$

**Proč asymptotika**

* Je to snazší
* Konstanty jsou strojově závislé
* Pro velké vstupy stejně rozhoduje hlavně právě asymptotika

> Typicky vezmeme asymptoticky nejrychlejší algoritmus a pak ladíme konstanty

---

# Grafové algoritmy

> Již bychom měli znát BFS a DFS

**Standardní notace** je graf $G = (V,E)$, kde $V$ jsou vrcholy a $E$ hrany a jejich počty: $n := |V|$, $m := |E|$

Také budeme typicky implicitně uvažovat orientované grafy

## Reprezentace grafu
1. Matice sousednosti $n \times n$
2. Seznamu sousedů (seznam vrcholů a v každém nějaký list)
 
# DFS - mosty, cykly, souvislost

Zavedeme si DFS trochu jinak než známe (budeme používat stavy otevřený, zavřený a nenalezen)

DFSv2(v):

1. $stav(v) \gets$ otevřený
2. Pro hrany $vw$:
3. &nbsp; Pokud $stav(w) =$ nenalezen:
4. &nbsp; &nbsp; DSFv2(w)
5. &nbsp; $stav(w) \gets$ zavřený

Navíc si ještě přidám hodinky (zavedu si dvě pole $in(v)$ a $out(v)$ - inicializovaná nulami)\
Implementace je mimochodem velmi jednoduchá, protože stačí po 1.kroku zvětšit $T$ a uložit ho do $in$ (to stejné pak pro po 5. pro $out$)

Lemma: DFS se zastaví v čase $O(n+m)$

*Dva způsoby důkazu:*

1. $O(n + \sum_{v \in V} \deg^{out}(v)) = O(n+m)$ (vrchol otevřen max. 1 a DFS max. 1 na $v$)
2. Pozorování, že na všechny hrany sáhnu jen jednou a jednu hranu dám konstantně

Lemma: Po DFS je $\forall v$ $stav(v)$ nenalezený a nebo zavřený a zavřený znamená, že $v$ je dosažitelný z $v_0$

*Důkaz*:

$\implies$ indukcí podle běhu algoritmu (pokud vrchol zavřeme, tak je dosažitelný, protože jsme ho předtím otevřeli a tedy existuje hrana)

$\impliedby$ důkaz sporem - kdyby existoval, dosažitelný vrchol, který nebyl nalezen, tak zvolíme nejbližší takový vrchol z $v_0$. Potom můžeme zvolit předposlední vrchol z nejkratší cesty mezi těmi dvěma vrcholy a tím dostaneme spor.

> 3. Přednáška 18.3.2021

Na procházení se můžeme dívat jako na uzávorkování (otevření a zavření jsou krajní)

Zároveň se dá i představit takzvaný DFS strom (strom ve kterém jsou jen hrany, které byly v DFS) a podle toho můžeme hrany i klasifikovat.
x

<!-- **TODO… třeba** obrázek DFS stromu -->

Můžeme totiž rozdělit hrany k vrcholům ve kterých už jsem byl na **zpětné**, **dopředné** a **příčné** podle toho, zda je vrchol předkem, potomkem a nebo ani jedno z toho již navštíveného vrcholu

To, že to jsou jediné možnosti dokážu pomocí již zmíněného uzávorkování

Když je $xy \in E$, tak uzávorkování může být:

1. $(_x \cdots (_y \cdots )_y \cdots )_x$ -- buď stromová nebo dopředná (záleží kde mezi závorkami jsem)
2. $(_y \cdots (_x \cdots )_x \cdots )_y$ -- zpětná hrana
3. $(_y \cdots )_y \cdots (_x \cdots )_x$ -- příčná hrana
4. !$\sout{(_x \cdots )_x \cdots (_y \cdots )_y}$ -- nemůže nastat

Jak to je v neorientovaných grafech? Podle toho kdy hranu objevím

| poprvé |podruhé |
--- | ---
| stromová | zpětná |
| zpětná | dopředná |

Klasifikovat hranu zvládneme konstantně - protože stačí znát vzájemnou polohu závorek a to je v $in$ a $out$

Věta: DFS v čase $\Theta(n+m)$ a prostoru $\Theta(n+m)$ najde dosažitelné vrcholy a klasifikuje hrany

## Mosty

### V neorientovaných grafech

Hrana je most, když jejím odebráním má graf více komponent

Lemma: Hrana není most $\iff$ leží na nějaké kružnici

Je to skoro až pozorování teda \
Kdykoliv mám hranu na kružnici, tak rozpojením se nic nestane, protože to můžu obejít \
A naopak když to pak zůstane stále souvislé, tak pořád existuje cesta a přidáním vznikne kružnice

Pozorování: Zpětná leží na kružnici $\implies$ nikdy není most, protože kružnice \
Musíme vyšetřovat jenom stromové (příčné v neorientovaných neexistují)

Platí $uv$ leží na kružnici $\iff$ $\exists xy \in E$ zpětná t.ž. $x$ je potomkem $v$ a $y$ je předkem $v$

V podstatě tedy pak pro každou hranu zkoumáme, jestli je pod ní nějaký vrchol, ze kterého vede hrana nad tu hranu

To, že je něco předek se testuje snadno porovnáním obou $in$, protože cestou dolů rostou \
Využití toho je ale pomalé, protože musíme pro každou hranu projít podstrom pod ní

Definujeme tedy $low(v) := \min \{ in(y) | xy$ je zpětná hrana & $x$ je neostře pod $v \}$ \
Neboli jak vysoko dosáhnu z pod $v$ zpětnou hranou

Z toho je naše původní podmínka pro zpětnou hranu ekvivalentní tomu, že $low(v) < in(v)$

Jak spočítat $low(v)$? - vezmu minimum z $low$ synů a zároveň zpětných hran z $v$ a to trvá $O(\deg(v))$

Asymptoticky to tedy nezpomalím

Dokázali jsme větu: Alg. nalezne všechny mosty v čase a prostoru $\Theta(n+m)$

## Acyklické Oritentované Grafy (DAG)

Některé problémy se na DAGu řeší lépe

#### 1. Je graf DAG?

Lemma: $\exists$ dosažitelný cyklus $\iff$ DFS najde zpětnou hranu

$\implies$ je celkem triviální, protože každý cyklus musí mít zpětnou (příčná nic neznamená)

$\impliedby$ nechť existuje cyklus, pak zvolíme vrchol $v$ z toho cyklu s min. out a jeho následníka na cykly vrchol $w$ - na hraně $vw$ tedy roste $out$ a $out$ a je to tedy zpětná hrana

Dosažitelnost vyřešíme opakováním z neobjevených vrcholů a nebo přidám zdroj \
To budu dále nazývat jako opakované DFS

#### 2. Topologické uspořádání

To znamená najít uspořádání těch vrcholů tak, že hrany vedou jen zleva doprava

Nebo-li lineární uspořádání $\preceq$ na $V(G)$, kde $\forall xy \in E(G) : x \preceq y$ \
Resp. pohled jako na očíslování vrcholů…

Pozorování: kružnice nemá TU (a dokážeme, že je to jediné co může bránit)

Věta: $G$ má topologické uspořádání $\iff$ $G$ je DAG

Df. $v \in V$ je zdroj $\equiv \deg^{in}(v)=0$ a symetricky stoky s $deg^{out}$

Lemma: každý DAG má zdroj i stok (jdu proti hranám a nikdy nevstoupím do stejného vrcholu)

Takže nám jako důkaz stačí odtrhávat zdroje (A jde to v $O(n+m)$)

Věta: Pořadí v němž DFS opouští vrcholy je opačné topologickému

#### 3. Topologická indukce

Příklad: zvolíme si $u$ a chceme $c(v) :=$ # cest z $u$ do $v$

Nechť $v_1, \cdots, v_n$ je top. pořadí a tedy $u =$ nějaké $v_i$

* Pro $j<i : v_j = 0$ - jsou před vrcholem, takže do nich nemůže vést cesta
* $v_i = 1$
* pro $j > i$ induktivně

Dá se všimnout, že: \
$$ c(v_j) = \sum_{p:pv_j \in E} c(p) $$

Protože to počítáme induktivně tak to, co potřebujeme už máme a čas je tedy $\Theta(n+m)$

#### 4. Plánování

Máme nějaký graf činností závislostí mezi činnostmi pak topologické uspořádání je možný způsob, jak tyto činnosti provést ve správném pořadí

#### 5. Silná souvislost

Definuje se pomocí relace dosažitelnosti

$u$ je v relaci s $v$, pokud existuje sled z $u$ do $v$

Zavedu si ještě jednu relaci mezi $u$ a $v$ a ta nastane, pokud sled existuje oboustranně

Pozorování: druhá zmíněná relace je ekvivalence a třídám této ekvivalence se říká komponenty silné souvislosti

Graf je silně souvislý pokud je tato komponenta pouze jedna

Nadefinujeme si ještě graf komponent $C(G)$ nebo-li kondenzaci, který má za vrcholy komponenty grafu $G$ a hrany jsou mezi vrcholy pokud se z jedné komponenty lze dostat do druhé

Lemma: $C(G)$ je DAG

*Důkaz*: kdyby existoval cyklus, tak existuje cyklus v původním grafu a ty vrcholy jsou ve stejné komponentě

> 4. Přednáška 25.3.2021

Graf komponent $C(G)$

1. je DAG
2. $\exists$ alespoň jedna stoková a jedna zdrojová komponenta
3. Je-li $C$ stoková a $v \in C$, pak DFS($v$) navštíví právě $C$
4. Pokud spustíme opakované DFS, pak vrchol s max. outem leží ve zdrojové
5. Zavedeme transpozici grafu, neboli opačý graf $G^T := (V(G), \{ vu\ |\ uv \in E(G)\}$ \
   $G$ je DAG $\iff$ $G^T$ je DAG \
   Mají stejné ekvivalentní třídy a zdroj se prohodí se stokem, takže jsou izomorfní
6. Najdeme $v$ ve zdrojové komponentě v $G^T$ 
7. Odebereme stokovou komponentu a opakujeme $\rightarrow$ korektní, ale pomalé
8. Procházíme vrcholy v pořadí klesajících outů v $G^T$, pokud ještě nemají přiřazenou komponentu, tak spouštím DFS v $G$ a označuji komponenty

To poslední odpovídá tomu, že odeberu stokovou komponentu a najdu další a stojí to na následujícím lemma:

Pokud $C_1, C_2$ jsou komponenty t.ž. $C_1C_2 \in E(C(G))$, pak $\max out(u) > \max out(v)$ pro $u\in C_1$, $v \in C_2$

Jinými slovy, že pokud je z $C_1$ do $C_2$ hrana, tak $C_1$ v DFS opustím později než $C_2$

*Důkaz:* Rozbor případů

1. DFS vstoupí do $C_1$ před $C_2$ - z $C_1$ vstoupím do $C_2$ a kompletně ji projde
2. Dřív vstoupím do $C_2$ - kompletně projdu $C_2$ před tím než se dotknu $C_1$

Aplikujeme to na neDAG

#### Algoritmus

1. Sestrojíme $G^T$
2. $Z \gets$ prázdný zásobník
3. Opakované DFS v $G^T$ a při opuštění vrcholu přidáme do $Z$
4. $\forall v$ komp($v$) $\gets \emptyset$
5. Postupně odebíráme vrcholy ze $Z$
6. &nbsp; Pokud komp($v$) $= \emptyset$
7. &nbsp; &nbsp; Spustíme DFS v $G$ z vrcholu $v$ \
   &nbsp; &nbsp; Chodíme do vrcholů s komp $= \emptyset$ a nastavíme je na $V$

Algoritmus najde komponenty silné souvislosti v čase a prostoru $\Theta(n+m)$

# Nejkratší cesty

Nadefinujeme si orientovaný graf $G=(V,E)$ s délkami hran $l: E \mapsto \mathbb{R}_0^+$ \
&nbsp; (l je prostě zobrazení, které hranám přiřadí *pro začátek* nezápornou hodnotu)

Délka cesty z $u$ do $v$ ($uv$-cesty $P$) je prostě jen součet hran na té cestě $l(P) := \sum_{e\in P} l(e)$

Vzdálenost je nejkratší cesta $d(u,v) := \text{min} \{\ l(P) \ | \ P \text{ je } uv\text{ cesta } \}$

Lemma: Pokud $S$ je $uv$-sled pak $\exists P \ uv\text{-cesta}$ t.ž. $l(P) \leq l(S)$i \
*Důkaz*: můžu vystřihávat cykly

Z toho lze vidět, že sledy vzdálenost neovlivní a tedy  $d(u,v) := \min \{\ l(P) \ | \ P \text{ je } uv\text{ sled } \}$

Další pozorování je, že platí trojúhelníková nerovnost $\forall u, v, w: d(u,v) \leq d(u,w) + d(w,v)$ \
Opět se v podstatě ukáže z předchozího lemma

Záporné hrany to ale celé rozbijí

Nejkratší sled neexistuje a nejkratší cesta je těžká

Opatrný kompromis: zakážeme záporné cykly

#### Případ, kdy mají všechny hrany jednotkovou délku

Dá se přes BFS ve kterém "vrstvy" odpovídají vzdálenostem v lineárním čase - vytvoří se strom nejkratších cest

Cestu samotnou si pak můžu poznamenávat do vrcholů a nebo udělat zpětný chod

Definice: Strom nejkratších cest

* strom na (dosažitelných částí) $V$
* podgraf $G$
* orientovaný od kořene, kterým je vrchol ve kterém začínáme $(u)$
* cesta ve stromu do jakéhokoliv vrcholu z $u$ je jednou z nejkratších cest v $G$

Je to tedy kompaktní reprezentace nejkratších cest z $u$ kamkoliv

Lemma: Strom cesty existuje i v ohodnocených grafech 

*Důkaz*: \
&nbsp; Postupně budujeme a při přidávání nového vrcholu existuje nějaký poslední vrchol ve stromu \
&nbsp;  To funguje především proto, že prefix nejkratší cesty je opět nejkratší cesta

#### Délky hran jsou přirozená čísla

Dá se líně rozdělit hrany na jednotkové, ale to je hodně pomalé

Ale my si zavedeme "budíky" pro vrcholy, které uchovávají, kdy se poprvé dostaneme do vrcholu \
Spíme než nás budík probudí a přenastavím okolní budíky

Je to v podstatě diskrétní simulace jako na programování a také základ Dijkstrova algoritmu

> 5. Přednáška 1.4.2021

## Dijkstra

Z předchozí úvahy můžeme napsat algoritmus

1. $\forall v \ h(v) \gets + \infty, s(v) \ gets \ neviděný$
2. $h(u) \gets 0, s(u)\gets$ otevřený &nbsp; &nbsp;&nbsp; # počáteční vrchol
3. Dokud existují otevřené vrcholy:
4. &nbsp; $v \gets$ otevřeý s $min. h(v)$ &nbsp; &nbsp; &nbsp; &nbsp; # vzít si s nejmenším časem (budíkem)
5. &nbsp; Pro všechny hrany $vw$: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # okolní se pokusím zlepšit
6. &nbsp; &nbsp; Pokud $h(v) + l(v,w) < h(w)$
7. &nbsp; &nbsp; &nbsp; $h(w)\gets h(v) + l(v,w)$
8. &nbsp; &nbsp; &nbsp; $s(w) \gets$ otevřený
9. &nbsp; $s(v) \gets$ zavřený

Na základě naší předchozí úvahy víme, že to funguje alespoň pro přirozená čísla

Časová složitost - projdu všechny vrcholy max. jednou a pro něj všechny hrany - to je $O(n^2)$ plus hledání min.

Takový odhad se nám ale až tolik nehodí, protože v řídkých grafech se hodí znát i odhad k počtu hran \
Navíc si můžeme všimnout, že hledáme minimum zbytečně, protože se toho nemohlo moc změnit

Potřebuji tedy datovou strukturu s ExtractMin, Insert a Decrease

A dá se všimnout, že provedeme\
$O(n\cdot T_{Insert} + n\cdot T\cdot T_{ExtMin} + m\cdot T_{Decrease})$

#### V poli

ExtractMin je v poli lineární (ostatní konst.), dosazením dostaneme $O(n^2)$, takže se nám to potvrdilo

#### V haldě (binární)

> Definici haldy už známe… btw v haldě se vyplatí číslovat od jedničky, kvůli synům

Insert je $O(\log n)$, minimum najdeme v kořeni a smažeme ho v $O(\log n)$ no a decrease $O(\log n)$, protože bude probublávat nahoru\
Ale je tam háček, že si musíme pamatovat, kde se vrchol v haldě nachází

Dosazením podobně dostaneme $O((n + m)\log n)$ a je to tedy mezi $n \log n$ a $n^2 \log n$

**Finoacciho halda** je $O(n \log n + m)$

#### Zpátky ke korektnostii

Vezmeme to obklikou a budeme se dívat na něco obecnějšího

### Relaxační algoritmus

Ty jsou založené na tom, že:

1. Všechny vrcholy mají nějaké zpočátku vysoké ohodnocení (kromě počátku)
2. Snažím se vylepšit hodnocení okolních vrcholů - relaxace
3. Mám stavy, abych se nazacyklil (otevřený - od předchozí relaxace se $h(v)$ změnilo)


A jejich průběh bude:

1. $\forall v$ $h(v) \gets \infty$, $s(v) \gets$ neviděný
   $h(u) \gets 0$,$s(u) \gets otevřený$
2. Dokud $\exists v$ otevřený:
3. &nbsp; Relaxuj $v$ 

>  Dijkstra ve druhém kroku otvírá vrchol s min. $h(v)$, dá se to ale i jinak

#### Co platí i pro záporné hrany (bez záporných cyklů)

Invariant O: $\forall v \ h(v)$ nikdy neroste a pokud je $h(v)$ konečné, tak je rovno délce nějakého $uv$-sledu

*Dúkaz* indukcí (podle běhu algoritmu):\
První část je zřejmá z toho, že algoritmus jenom snižuje\
Druhá část se dokáže tím, že začneme v nule a při relaxaci vždy přičteme délku hrany

Lemma D (dosažitelnost): Pokud se algoritmus zastaví, pak pro každý $v \in V$ platí:

* $v$ je dosažitelný z $u$
* $v$ je zavřený
* $h(v)$ je konečné

> Viz. korektnost DFS/BFS

Lemma V (vzdálenost): Pokud se alg. zastaví, pak $\forall v \in V : h(v) = d(u,v)$

*Důkaz*: Pokud není dosažitelný, tak $h(v)$ je nekonečno a to je ta vzdálenost, jinak je vše konečné \
&nbsp; Díky inv. O. je $h(v) \geq d(u,v)$, my ale musíme ukázat, že ostře větší nenastane \
&nbsp; Vyberu tedy vrchol $v$, pro který je to ostře větší, t.ž. $uv$-cesta má nejméně hran (co do $l$) a vezmu nějakého předchůdce pro kterého to sedí a z něj jsme se museli pokoušet snížit ohodnocení dalšího vrcholu (chtělo by to asi detailněji - otevřít, zavřít, relaxovat, …)

##### Co platí konkrétně pro Dijsktru (graf bez záporných hran)
&nbsp; 
Invariant M (Monotonie): Kdykoliv je $o$ otevřený vrchol a $z$ zavřený, tak $h(z) \leq h(o)$ a $h(z)$ se už nezmění \
*Důkaz*: klasicky indukcí podle výpočtu \
&nbsp; a) zpočátku (vakuově pravdivé)\
&nbsp; b) při relaxaci - z IP platí $h(z) \leq h(v) \leq h(o)$ a rozborem pokusů změnit zavřené, otevřené i neviděné vrcholy invariant bude platit (buď se vrcholy nezmění a nebo budou $\geq v$

Věta: Dijkstrův algoritmus zavírá vrcholy v pořadí vzdálenosti od $u$, každý dosažitelný právě jendou a $h(v)$ v okamžiku uzavření je rovno $d(u,v)$

Dostaneme kombinací předchozích

## Bellman-Ford

Další způsob jak udělat relaxaci je mít otevřené vrcholy má ve frontě (a tedy zavírat nejstarší z otevřených)

V čase $O(n \cdot m)$

Funguje i na záporné hrany bez záporných cyklů

Definujeme si fázi výpočtu jako $F_0 :=$ otevření $u$ a $F_i :=$ zavření otevřených v $F_{i-1}$ a otevření jejich následníků

Díky tomu můžeme uvažovat následující invariant:

&nbsp; Na konci fáze $F_i$ $\forall v \in V \leq$ délka nejkratšího $uv$-sledu o max. $i$ hranách (to může být i $\infty$)

Z toho plyne, že po nejvýše $n-1$ fází platí $h(v) \leq d(u,v)$ a $n$-tá fáze to zavře

*Důkaz invariantu*: Indukcí podle $i$ \
&nbsp; a) $i = 0$ triviálně \
&nbsp; b) Na konci $(i+1)$-té fáze - pokud $S$ má méně než $i$ hran, tak to platilo z IP, zajímavé je tedy $S$ má právě $i$ hran, v takovém případě, ale platilo, že do předchozího vrcholu vede nejkratší sled a my jenom přidáme délku hrany a vrchol zavřeme nejpozději v $i+1$ fázi

> 6. Přednáška 8.4.2021

# Minimální kostry

Je dán souvislý neorientovaný graf s $\mathbb{R}$ váhami hran (*BÚNO* unikátními) a chceme najít kostru $T$ t.ž. $w(T)$ je min. 

$w(T) := \sum_{e\in T} w(e)$ - váha kostry je prostě součet vah hran

## Jarníkův algoritmus

Je to hladový algoritmus

Pěstujeme si strom $T$ tak, že opakujeme jeden krok

* Vybereme si nejlehčí z hran mezi $T$ a zbytkem a přidáme ji

Lemmátko: Po $n$ krocích se Jarník zastaví a dám nám kostru \
*Důkazík*: Přidávám jen listy, takže pořád strom a kdyby nějaký vrchol chyběl, tak tu hranu musí přidat

Definice: Množina $R \subseteq E$ je elementární řez $\equiv \exists A \subseteq V, B=V \backslash A, A,B \neq 0$ t.ž. $R = E(A,B)$ \
Jinými slovy je to množina hran vedoucí mezi $A,B$, kde $A,B$ vznikne rozdělením grafu na neprázdné části

Řezové lemma: nechť

* $G$ je graf s unikátními vahamami
* $R$ elementární řez v $G$,
* $e$ nejlehčí hrana v $R$,
* $T$ nějaká min. kostra v $G$

Pak $e \in T$ (nejlehčí hrana každého elementárního řezu leží v kostře)

*Důkaz*: \
&nbsp; Nechť $T$ je kostra $e\notin T$ (a dokážeme, že ta kostra není minimální) \
&nbsp; $R = E(A,B)$ pro $A,B$ a $e = \{ a,b \}$ pro nějaké $a\in A$ a $b\in B$ \
&nbsp; $\exists C$ cesta v $T$ mezi $a, b$ \
&nbsp; $\exists f \in C \cap R$ (nějaká další hrana mezi $a,b$ v řezu) \
&nbsp; $T - f$ má 2 komponenty v jedné je $a$ a v druhé $b$
&nbsp; $Ť = $T - f + e$ a to je také kostra  \
&nbsp; $w(Ť) < w(T)$, protože $e$ byla v řezu nejlehčí

Z toho plyne

1. JA najde min. kostru (hrany mezi $T$ a zbytkem je elementární řez)
2. existuje jediná min. kostra (k tomu jsou potřeba unikátní váhy)
3. min. kostra je jednoznačně určena pořadím hran podle vah (z toho je např. nepotřebujeme sčítat)

Časová složitost: $O(n\cdot m)$ \
Pro každý vrchol vybíráme asymptoticky až všechny hrany

#### Odbočka k neukinátním vahám

I tak by Jarník našel minimální kostru 

V takovém případě lze doporovnat stejné váhy a vyrobit lin. uspořádání, které využijeme ke kostře viz. 3.

### Verze podle Dijkstry

Pro sousedy vrcholů v $T$ si pamatuji nejlehčí hranu do $T$

Najdu vrchol s nejlehčí hranou, přidám ji přepočítám vrcholy, které mohla změnit \
Mohla změnit hrany mezi nově přidaným vrcholem a již dřívějšími sousedy

Opět mám stavy vrcholů (otevřený - sousedé $T$, zavřený - už v $T$, neviděný)

$n \times$ Insert \
$n \times$ ExtractMin \
$m \times Decrease$

V závislosti na implementaci se dostanu na $O(n^2)$ nebo $O((n+m)\log n$ 

## Borůvkův algoritmus

Místo stromku si pěstujeme les a v každém kroku přidáme min. hranu ze všech stromků

Složitost $\Theta(m \cdot \log n)$, protože mám $\leq \log n$ fází a každá je $O(m)$

*Důkaz* počtu fází a zastavení:

* Na konci $k$-té fáze mají všechny stromky $2^k$ vrcholů a indukcí
	* Pro $k = 0$ platí $1= 2^0$
	* $k+1$ fáze \
	  srůst alespoň 2 původních stromků a to znamená, že má alespoň $2^{k+1}$

Lemma: Výstup je min. kostra \
&nbsp; *Důkaz*: Každá přidaná hrana je nejlehčí v elementárním řezu mezi stromkem a zbytkem

Je ale výborný pro paralelizaci a jsou na něm postavené další algoritmy

## Kruskalův algoritmus

Setřídíme hrany od nejlehčí k nejtěžší

Postupně přidáváme do podgrafu podle toho, jestli vznikne cyklus

Lemma: Alg. najde min. kostru
 
*Důkaz*:

* očividně se zastaví, protože každou hranu vezme jednou
* podgraf je vždy les (nemohl vzniknout cyklus)
* na konci strom
* je min. díky řez. lemmatu (řez mezi jedním stromkem a zbytkem grafu a opravdu nejlehčí)

Se složitostí je to komplikovanější, protože pro efektivní postup si zavedeme Union-Find
 
$m \times$ Find \
$n \times$ Union

Musíme ale i třídit a to je $O(m \log n)$

Spoiler z Union-Findu: \
&nbsp; V poli je to $O(m \log n + n^2)$\
&nbsp; Se lepší implementací DFU to zvládneme $O(m \log n)$

## Union-Find (DFU)

Udržujeme komponenty souvislosti

Operace Find (jsou $u,v$ ve stejné komponentě) a Union (přidat $uv$)

**Pole** \
Find v $O(1)$ a Union v $O(n)$ a Kruskal pak $O(m \log n + n^2)$ 

**Keříky** \
strom orientovaný ke kořeni (každý vrchol si pamatuje otce) a jeho vrcholy reprezentují komponentu

Find se dělá tak, že z $u$ i $v$ jdu do jejich kořene a pak porovnám kořeny a je to $O(\text{hlouka keříku})$ \
Union se dělá opět nalezením kořenů a potom se spojí, opět v $O(\text{hloubka keříku})$
 
Takhle to ale může degenerovat 

Vylepšení: Udržuji si v kořenech hloubky keříků a vždy připojuji ty menší pod větší

Lemma: Keřík hloubky $h$ má alespoň $2^h$ vrcholů \
*Důkaz* indukcí podobně jak u borůvky: spojím dva $2^h$ na jeden $2^{h+1}$

Důsledek: \
&nbsp; Union a Find trvají $O(\log n)$ \
&nbsp; Kruskal trvá $O(m \log n + m \log n + n \log n) = O(m \log n)$

Co se umí? 
> Nebude se zkoušet, ale je to cool

* $O(m)$ pro rovinné grafy
* $O(m)$ pro alespoň trochu husté - to znamená, že už pro $m \geq n \cdot \log \log \log n)$
* $O(m)$ pro celočíselné váhy
* $O(m)$ průměrně
* $O(m)$ pro seřazené hrany
* $O(m \cdot log^* n)$ obecně, kde $log^*$ je inverzní k $2^{{2^2}^{\cdots}}$, kde 2 je $k$ 
* $O(m \cdot \alpha(n))$ obecně, kde $\alpha$ je Achermannova funkce (ta roste ještě pomaleji)

> 7. Přednáška 15.4.2021

# Datové struktury 

Způsob ukládání dat

Nějaký blackbox s rozhraním a implementací

### Rozhraní

* fronta, zásobník, posloupnost
* prioritní fronta (halda)
* množina (konečná podmnožina univerza), která má Find($x$), Inset($x$) a Delete($x$)
* slovník (částečně zobrazení, kde z klíčů máme hodnotu)
* uspořádaná množina (nebo slovník) umí i Min, Max, Pred($x$) a Succ($x$)

Statické x dynamické podle toho, jestli data můžeme průběžně přidávat

### Implementace

* pole
* spojový seznam
* binární halda
* binární vyhledávací strom
* …

### Operace v množině podle implementace

Struktura | Find | Insert | Delete
--- | --- | --- | --- 
Pole | $\Theta(n)$ | $\Theta(1)$/$\Theta(n)$* | $\Theta(n)$ 
Seznam | $\Theta(n)$ | $\Theta(1)$/$\Theta(n)$* | $\Theta(n)$ 
Vyhledávací strom | $\Theta(\log n)$ | $\Theta(\log n)$ | $\Theta(\log n)$
Hešovací tabulky - průměrně | $\Theta(1)$ | $\Theta(1)$ | $\Theta(1)$ 

\*) záleží, jestli musím kontrolovat, zda už tam je

## Binání strom

Má nějaký kořen a pak respektive levý a pravý podstrom

### Značení

vrchol $v$

* levý a pravý syn $l(v)$ a &r(v)$
* levý a pravý podstrom $L(v)$ a $R(v)$
* všechny potomky $T(v)$
* $h(v) :=$  maximální počet hran mezi $v$ a listem 
* $n :=$ celkový počet vrcholů

Pokud chybí syn, tak $l(v)$ nebo $r(v) = \emptyset$ \
a dodefinujeme $T(\emptyset) = \emptyset$ a $h(\emptyset) = -1$

### Binární vyhledávací strom

Vrcholy obsahují klíče $k(v) \in \mathcal{U}$ (musí být z univerza a různé)

A navíc platí, že $\forall v : \forall l \in L(v): k(l) < k(v)\ \wedge \forall r \in R(v) k(r)>k(v)$ a z toho právě plyne, že klíče různé

### Operace

**Show (enumerate)** -- $\Theta(n)$\
&nbsp; Rekurzivně se volám na oba podstromy a vypíšu je

**Find** -- $\Theta(\text{hloubka stromu})$\
&nbsp; Podle toho, co hledám, tak jdu do $l(v)$ a nebo $r(v)$…

**Insert** -- $\Theta(\text{hloubka stromu})$\
&nbsp; Začnu hledat a buď najdu nebo najdu prázdné místo a přidám ho

**Delete** -- $\Theta(\text{hloubka stromu})$\
&nbsp; Buď je to list, má jednoho syna a nebo 2 syny \
&nbsp; Když jeden, tak přepojím a když dva, tak najdu např. min. z pravého podstromu (btw může mít pravého syna)

Chceme tedy relativně mělké stromy \
Můžeme totiž dostat takzvaně degenerovaný strom nebo-li liánu s lineární hloubkou

### Dokonale vyvážený BVS

Rozdíl mezi počty prvků levého a pravého podstromu je vždy nejvýše jedna

Dokážeme to algoritmem, který takový strom vyrobí

Vezmu setříděnou posloupnost, prostřední prvek je kořen a rekurzivně se zavoláme na l. a p.polovinu (podstromy) \
Ten je mimochodem $\Theta(n)$, alespoň když si ve funkci budeme předávat akorát indexy

Pozorování: Hloubka d.v. BVS $\leq \log_2 n$, protože na nejdelší cestě se při kroku dolů velikost $T(v)$ zmenší alespoň dvakrát (takže po $\log n$ dojdou vrcholy) a s rozdílem 1 nás zachrání to, že do $T(v)$ se počítá i $v$

Má to ale nevýhodu, že je dokonalá vyváženost těžká udržovat, a v algoritmizaci celkem výjimečně to jde i dokázat

Věta: V každé implementaci operací Insert, Delete, v d.v. BVS má alespoň 1 z operací složitost $\Omega(n)$  pro nekonečně mnoho hodnot $n$ (šlo by to pro všechna $n$, ale to je složitější)

*Důkaz*: \
&nbsp; Zvolíme $n=2^k - 1$ a pro ten je tvar stromu určen jednoznačně\
&nbsp; Já provedu Inser($n+1$) a Delte(1) \
&nbsp; To je opět určeno jednoznačně, ale všechny vrcholy jsou posunuté a tedy $\Omega(n)$ vrcholů změnilo, zda jsou listy \
&nbsp; V každém z nich změna min. 1 ukazatele $\rightarrow \Omega(n)$ změn ukazatelů\
&nbsp; Pak ještě provedeme Insetr($n+2$) a Delte(2) a budeme to dál opakovat, aby se to nemohlo amortizovat \
&nbsp; Čas na dvojici je $\Omega(n)$ a tedy alespoň jedna operace to mít musí taky

### AVL strom

Definice strom je hloubkově vyvážený $\equiv$ rozdíl výšek levého a pravého podstromu je vždy nejvýše jedna

Díky dodefinování hloubky prázdného podstromu to funguje \
např. pokud má vrchol jednoho syna, tak to musí být list

Dokonale je i hloubkově, ale obráceně to být nemusí

Věta: Hloubka AVL stromu je $\Theta(\log n)$

*Důkaz*:
 
&nbsp; **Horní odhad hloubky** \
&nbsp; &nbsp; Budeme počítat $A_n :=$ min. #vrcholů AVL stromu hloubky $h$ (nejprázdnější strom) \
&nbsp; &nbsp; Můžeme si všimnout, že to je $A_h = 1 + A_{h-1} + A_{h-2}$ (vrcholu plus dva podstromy rozdílné výšky) \
&nbsp; &nbsp; Můžeme použít Fibonacciho, ale to my ještě nevíme, takže indukce, že $A_h \geq 2^{h/2}$

* Pro $h=0$: $A_0 = 1 \geq 2^0$ \
Pro $h=1$: $A_1 = 2 \geq 2^{\frac{1}{2}} \approx 1.414$ 
* Pro $h\geq 2$: $A_h \geq A_{h-1} + A_{h-2} = 2^{\frac{h}{2}}(\frac{\sqrt{2}}{2} + \frac{1}{2} \geq 2^{h/2})$ a to v závorce je větší než 1, takže to vychází

&nbsp; &nbsp; $\implies \exists c>1: A_h \geq c^h$ a v našem případě $c=\sqrt{2}$ \
&nbsp; &nbsp; A z toho už musí platit, že strom na $n$ vrcholech má hloubku $\leq \log_c n$, protože jinak by $A_h \geq c^{\geq \log_c n} > n$ \
&nbsp; &nbsp; A $\log_c n \in O(\log n)$

&nbsp; **Dolní odhad hloubky**\
&nbsp; &nbsp; Analogicky si zavedeme $B_n :=$ max. # vrcholů na stromu hloubky $h$ \
&nbsp; &nbsp; $B_h = 2^{h+1}-1$ pro úplný strom \
&nbsp; &nbsp; $h\geq \log_2 n + 1 \implies$ hloubka $\in \Omega(\log n)$

> 8. Přednáška 22.4.2021

> Btw je to skoro celý jen rozbor případů

#### Vyvažování AVL stromů

<!-- TODO as usual -->

Hodí se vidět [tabuli z hodiny](https://kam.mff.cuni.cz/~mares/video/ls2021/ads1/08-avl.pdf)

Po Insert a Delete se bude strom opravovat

V každém vrcholu si budeme udržovat $\delta(v) = h(r(v)) - h(l(v))$ neboli znaménko vrcholu

* pravý je hlubší $\delta(v) = 1$ značíme $+$ 
* $-1$ značíme $-$
* $0$ značíme $0$

##### Rotace

Prostě prohodíme dva vrcholy mezi sebou a jejich podstromy, tak aby to sedělo

<!-- TODO: udělat svoje obrázky, každopádně v HTML komentu nějaký jsou -->

<!-- <center><img src="https://ksp.mff.cuni.cz/kucharky/vyhledavaci-stromy/vyhledavaci_stromy_04.png"></center> -->

##### Dvojitá rotace

Prostě akorát provedeme dvakrát, chtělo by to ale obrázek 

<!-- <center><img src="https://ksp.mff.cuni.cz/kucharky/vyhledavaci-stromy/vyhledavaci_stromy_05.png"></center> -->

#### Vyvažování Insert
Obecně do vrcholu přijde zdola signál, že podstrom se prohloubil

Jestli zprava nebo zleva je symetrické, takže budeme rozebírat třeba jenom zleva

1. Pokud byl pravý hlubší ($+$), tak se to srovná na $0$ a hloubka se nezmění
2. Pokud přišla informace do $0$, tak se dostaneme na $-$ a posíláme informaci dál
3. V případě, že byl vrchol $-$, tak se dostaneme na $-2$ a musíme zasáhnout
	* Byl $-$ zrotujeme syna a vrchol do kterého informace přišla a celková hloubka stejná
	* Byl $0$ nenastane, protože se z nuly nešíří signál… skoro (kromě začátku insertu)
	* Byl $+$ provedeme dvojitou rotaci a vyneseme do kořene pravý podstrom levého syna a hloubka stejná

**Jak se to tedy chová celkově?**

* buď oprava znaménka a pak možná pokračovat
* nebo nějaká rotace a skončíme

#### Vyvažování Delete

Převedeme na smazání buď listu nebo vrcholu s 1 synem a v obou případech klesne hloubka o 1

Oebceně tedy do vrcholu přijde signál, že hloubka podstromu klesla o jedna (opět BÚNO zleva)

1. Přijde do $-$, znaménko jde na nulu a hloubka klesla
3. Přijde do $0$, znaménko jde na $+$ a končíme
3. Přijde do $+$ musíme opět opravit a zase rozdělujeme znaménka synů
	* $+$ opět opravíme rotací a dál posíláme signál, že se to snížilo
	* $0$ zrotujeme, dáme to na $-$ a nic neposíláme
	* $-$ dvojitá rotace, znaménko na 0 a posílám dál

 Jak se to tedy chová celkově? 

* buď změna znaménka nebo nějaká rotace
* možná pokračujeme 

#### Závěr

Insert, Delete i Find v AVL stromu mají časovou složitost $\Theta(\log n)$

### Odbočka - externí vrcholy

Pokud vrcholu chybí nějaký ze synů, tak ho nahradíme externími vrcholu (NULL)

Zjednoduší to formalismus a má to nějaké výhody i v praxi

* Ext. vrcholy odpovídají intervalům mezi klíči
* Každý interní vrchol má právě dva syny
* Listy jsou externí vrcholy

## Vícecestný vyhledávací strom

* zakořeněný strom
* má interní a externí vrcholy
* synové vrcholu mají pořadí
* v inter. vrcholech jsou sestupně seřazené klíče a na kraje dáme $\pm \infty$
* \#synů je #klíčů $+ 1$

Budu vyžadovat aby externí vrcholy byly na stejné hladině \
Sice je to podstatně striktnější než jsme doteď měli, ale těch více klíčů to opraví

### $(a,b)$ strom

Vícecestný vyhledávací strom s parametry $a,b$, kde platí, že $a\geq 2$ a $b\geq 2a-1$

1. Všechny ext. vrcholy jsou stejně hluboko
2. Int. vrcholy mají $a$ až $b$ synů (a tedy $a-1$ a $b-1$ klíčů) \
   Máme ale ještě výjimku pro kořen, ten jen $1$ až $b$

> 9. Přednáška 29.4.2021

Lemma: $(a,b)$-strom s $n$ klíči má hloubku $\Theta(\log n)$

*Důkaz*: 

**Horní mez** \
&nbsp; $m_h :=$ min. #klíčů ve stromu hloubky $h$ \
&nbsp; Každý vrchol má min. možný # synů a tedy i klíčů \
&nbsp; Kořen má $2$ syny a $1$ klíč, vnitřní mají $a$ sunů a $a-1$ klíčů \
&nbsp; Obecně tedy dostaneme počet vrcholů na hladinách: $1, 2a^0, 2a, 2a^2, 2a^3, ...$ \
&nbsp; Potřebujeme to sečíst, to je ale součet geometrické řady \
&nbsp; Sečte se to tedy na $2a^{h-1}-1 \leftarrow$ roste exponenciálně \
&nbsp; Když počet prvků roste exponenciálně, tak hloubka roste logaritmicky

**Dolní mez** \
&nbsp; Dělá se to obdobně, takže zde jenom naznačení \
&nbsp; $M_h :=$ max. #klíčů ve stromě hloubky $h$ \
&nbsp; ... opět zde bude nějaká geometrická řada\
&nbsp; $M_h \sim b^h \implies$ min. hloubka roste logaritmicky

#### Náročnost operací

**Find**: $O(1)$ na hladinu $\implies \Theta(\log n)$ celkem

**Insert**: \
&nbsp; nemůžu prostě přidat vrchol do listu, ale musím přidat klíč do vrcholu \
&nbsp; může ale nastat přetečení (a tedy měl předtím $b-1$ klíčů) \
&nbsp; To udělám tak, že prostřední klíč zatřídím do otce a na otce připojím dvě poloviny \
&nbsp; To může zkaskádovat až do kořene, ale nakonec prostě rozštěpím kořen (založím nový)

&nbsp; Potenciální problém je s tím, že když vrchol rozpůlíme, tak by mohl mít málo klíčů \
&nbsp; Tedy $\frac{b-1}{2} < a-1$, to nám ale definice zakázala 

**Delete**: \
&nbsp; Převedeme to na Delete z nejnižší vnitřní hladiny \
&nbsp; Nahradíme ho minimem z podstromu, ale může nastat podtečení \
&nbsp; Můžeme to řešit tak, že to slepíme se sourozencem, ale ten by dost často přetekl \
&nbsp; Takže si budeme půjčovat od bratra (levý a pravý jsou symetrický), BÚNO levého \
&nbsp; Rozlišíme dva případy

1. Bratr má $> a-1$ klíčů
	* Budu si půjčovat z bratra
	* Musím to udělat tak, že přesunu maximum z levého do otce a klíč z otce do vrcholu
2. Bratr má právě $a-1$ klíčů
	* Budeme se spojovat s bratrem
	* Přidám k dvěma vrcholům klíč z otce a spojíme to do jednoho (takže $2a-2$) ✓
	* Podtékání může opět pokračovat až do kořene a v takovém případě kořen smažeme

Časová složitost: $O(1)$ na hladinu, $\Theta(\log n)$ hladin, takže celkem $\Theta(\log n)$
 
#### Volba $a,b$

S rostoucím $b$ se to zpomaluje a typicky chceme buď $2a-1$ nebo $2a$

Nechceme ani velké $a$

Optimální jsou $(2,3)$ nebo $(2,4)$… or are they? &nbsp; ♬ *Moon men stars playing* ♬

Na reálných počítačích se na disku spíše používá $(256,512)$-strom kvůli blokům disku a přístupu do paměti

A na keši jsou bloky po 64B, takže si vyberu (4,8) strom

#### Na okraj

* varianta, která má data jen v listech (a v ostatních klíče)
* občas se jim také říká B-stromy

### Červeno-černý strom

#### Překlad (2,4)-stromu na BVS

Můžu mít $2$-vrchol, $3$-vrchol a $4$-vrchol <!-- , které vypadají TODO: obrázek -->

Definice: Left-Leaning Red-Black Tree (LLRB) je BVS s ext. vrcholy a hranami obarvenými <span style="color:#FF6666">červeně</span> a <span style="color:#707070">černě</span> t.ž.

1. Nejsou 2<span style="color:#FF6666">R</span> těsně za sebou
2. Když z vrcholu dolů vede jen 1<span style="color:#FF6666">R</span> hrana, potom vede doleva
3. Hrany do listů jsou jen <span style="color:#707070">B</span>
4. Na $\forall$ cestách kořen-list je stejný #<span style="color:#707070">B</span> hran

Lemma: $\exists$ bijekce mezi (2,4)-stromy a LLRB stromy \
Plyne to z axiomů - pokryje to všechny možné počty synů, listy jsou na stejně hladině, …

Jak vypadají operace?

&nbsp; **Rotace červené hrany** \
&nbsp; &nbsp; Zachová černé axiomy (3.-4.), ale může to rozbít červené (1.-2.) \
&nbsp; &nbsp; &nbsp; Protože nic nedělá s černými hranami, ale může vyrobit třeba $4$-vrchol

&nbsp; **Přebarvení $4$-vrcholu** \
&nbsp; &nbsp; Opět zachová černé axiomy, ale může to rozbít červené  \
&nbsp; &nbsp; &nbsp; Černé hrany do listů zůstanou, ale jedna se ubere a pak přidá, ale opět může vzniknout např. $5$-vrchol

&nbsp; **Insert**: \
&nbsp; &nbsp; Směrem dolů přebarvujeme $4$-vrcholy (vzniká červená spoušť) \
&nbsp; &nbsp; Nahradíme externí vrchol za vnitřní a to připojíme červenou hranou (opět červené problémy) \
&nbsp; &nbsp; Směrem nahoru R opravujeme -- rotujeme right-leaning nebo červené za sebou \
&nbsp; &nbsp; Opět to trvá $\Theta(\log n)$ a mimochodem hodí se ty barvy pamatovat třeba v listech

> 10. Přednáška 6.5.2021

### Trie

Reprezentace množiny řetězců nad abecedou $\Sigma$ (např. $\{0,1\},\{0,\cdots,9\}$, …)

Pokud bychom v tom chtěli hledat přes BVS, tak $\Theta(\log n \cdot \text{délka řetězce})$ (protože porovnáváme celou délku)

Podíváme se ale na něco, co má lepší vlastnosti

Písmenkový strom (trie - ze slov tree a retrieval) je zakořeněný vyhledávací strom s vrcholy, jejichž synové můžou být až všechny prvky abecedy

Hladiny odpovídají pořadí písmen ve slovech

Vrcholy odpovídají prefixům slov v množině

Protože ale i prefixy můžou být slova, tak nemůžeme spoléhat na to, že slova jsou jen v listech, ale musíme si ve vrcholech pamatovat, zda se jedná o slovo

&nbsp; Member($y$) -- $\Theta(|y|)$

&nbsp; Insert($y$) -- $\Theta(|y|)$ -- buď slovo označím a nebo přidávám vrcholy

&nbsp; Delte($y$) -- $\Theta(|y|)$ -- pokud nemá syny, tak postupně maže hrany nahoru

&nbsp; paměť je $\Theta(\sum_i |x_i|)$ -- suma délek řetězců

Co když je abeceda velká? Lineárně s počtem znaků se zvětší paměť a zpomalí Delete s Insertem

Když pole nahradíme vyhl. stromem, tak dostaneme paměť $\Theta(|x_i|)$ a všechny operace $\Theta ( |y| \cdot \log | \Epsilon | )$

Číslicový strom - radix trie \
základ $z$ a $n$ čísel z rozsahu $\{ 0, \cdots , L-1 \}$ \
$n$ číslic $\sim \log_z L \rightarrow$ čas na operaci $\Theta(\log_z L)$

Vyhledávací strom vs číslicový strom \
To se špatně porovnává, protože závisí na počtu čísel vs rozsahu čísel \
Ale je to hodně podobné, pokud jsou čísla různá, tak $L\geq n$

# Hešování

Myšlenka je taková, že každý prvek z univerza $\mathcal{U}$ se snažíme pomocí hešovací funkcí zařadit do jedné z $m$ přihrádek

Může ale nastat kolize a proto máme v přihrádce seznam

Například můžu roky zahešovat podle toho jakým číslem končí

Je představa, že máme rovnoměrné rozložení $n$ prvků do přihrádek \
typicky $\frac{n}{m}$ prvků v přihrádce a to můžeme dostat na konstantu

Find, Insert a Delete tedy v čase $O(1)$

## Volba hešovací funkce

Ideální neexistuje, ale zde je pár praktických

* Lineární kongruence \
 $x\mapsto ax \mod m$, kde $m$ je prvočíslo a $a$ je nesoudělné s $m$ (typicky $a \approx 0.618m$)

* Multiply-shift -- pro $\mathcal{U}=[2^W]$ ($W$ bitů), $m = 2^k$\
$x\mapsto (ax \mod 2^W) >> W-k$

* Skalární součin \
 $x_0, \cdots, x_{d-1} \mapsto (\sum_i a_i x_i) \mod m$ &nbsp; &nbsp; &nbsp; (parametry $A_0, \cdots, a_{d-1}$)

* Polynom \
$x_0, \cdots, x_{d-1} \mapsto (\sum_i a^i x_i) \mod m$ &nbsp; &nbsp; &nbsp; (nemusím si pak pamatovat tolik různých parametrů)

* Toleranční hešování \
Rozdělím číslo na části, každou částí indexuju tabulku a to, co z nich dostanu, přiXORuju

## Nafukovací hešovací tabulka

Na začátku si udělám nějakou tabulku, sleduji faktor naplnění ($\alpha := \frac{n}{m}$) a vzroste-li $\alpha$ příliš, tak přehešujeme (kompletně vybudujeme novou strukturu s více přihrádkami)

Můžeme si všimnou, že nemůžeme přidat konstantní počet přihrádek, ale potřebujeme je znásobit

Přehešovat z $2^i$ do $2^{i+1}$ trvá $\Theta(n + 2^{i+1})$, ale $2^i$ je $\Theta(n)$

Například \
&nbsp; Zjednodušeně budeme uvažovat konstantu jako 1 a tedy $\alpha \leq 1$ \
&nbsp; Počty přihrádek jsou postupně $1,2,4,8, \cdots$ \
&nbsp; V každém intervalu přibude $2^{i-1} prvků, ale tolik jsme těch prvků museli přidat \
&nbsp; Časová složitost je tedy konstantní amortizovaně

## C-univerzální systém

Hešování je nebezpečné pokud vstup není náhodný, ale úmyslně špatný

Budeme tedy chtít volit hešovací funkcí náhodně z nějaké množiny funkcí… neboli systému \
A funkce v něm ještě nějak parametrizujeme (například máme funkci $f_a(x) = (ax) \mod m$ a $a$ je parametr

Definice: Systém funkcí $\mathcal{H}$ z $\mathcal{U}$ do $[m]$ (přihrádky) je potom $c$-univerzální pro $c > 0$ $\equiv$ \
Když si vyberu nějaké prvky $x,y$ z $\mathcal{U}$, tak pravděpodobnost, že zkolidují je malá, formálně \
$\forall x,y \in \mathcal{U}, x\neq y: Pr_{h\in\mathcal{H}}[h(x)=h(y)] \leq \frac{c}{m}$

Příklad systému - skalární součin nad tělesem $\mathbb{Z}_p$ \
Univerzum jsou uspořádané $d$-tice toho tělesa a parametr patří do toho univerza\ 
$\mathcal{U}=\mathbb{Z}^d_p$, $a\in \mathbb{Z}^d_p$, přihrádky: $\mathbb{Z}_p$

Věta: Tento systém je $1$-univerzální

*Důkaz*: pro $x \neq y$

$$ Pr_{h\in \mathcal{H}} [h(x) = h(y)] = Pr_a [ax = ay] $$

$$ \sum_{i=1}^d a_i (x_i - y_i) = 0 $$

BÚNO předpokládejme, že se liší v první souřadnici ($x_1 \neq y_1$)

Nechť zafiuxji $a_2, \cdots, a_d$

$$ a_1(x_1 - y_1) +  \sum_{i=2}^d a_i (x_i - y_i) = 0 $$

Lineární rovnice s právě jedním řešením (a $a_1$ můžu zvolit podle přihrádek)

$$ Pr[a_1 \text{ je řešení}] = \frac{1}{p} $$ 


> 11. Přednáška 13.5.2021

Víme, že $\exists 1$-univerzální systém

Lemma: Nechť $\mathcal{H}$ je $c$-univerzální systém fcí z $\mathcal{U}$ do $[m]$, $x_1, \cdots, x_n \in \mathcal{U}$ navzájem různé a $y \in \mathcal{U}$. Potom

$$\mathbb{E}_{h\in \mathcal{H}} [\# i:h(x_i)=h(y) \leq c \cdot \frac{n}{m} + 1]$$

V podstatě to říká, že obsazení přihrádky kam padlo $y$ je ve střední hodnotě celkem malé podle obsazenosti

*Důkaz*: \
&nbsp; Předpokládejme, že $\forall y\neq x$ (případ $y=x$ zařídí $+1$ na konci \
&nbsp; Zavedeme indikátory $I_1, \cdots, I_n$ a $I_i$ je 1, pokud se prvek $i$ zahešoval do stejné přihrádky jako $y$\
&nbsp; Obsazení přihrádky kam padlo $y$ je potom součet všech indikátorů \
&nbsp; Použijeme linearitu střední hodnoty a tedy, že střední hodnota součtu je součet středních hodnot \
&nbsp; Střední hodnota indikátoru je pravděpodobnost, že $x_i$ se zahešovalo stejně jako $y$ a to je menší nebo rovno $\frac{c}{m}$ \
&nbsp; A na závěr ty střední hodnoty sečteme na $\frac{cn}{m}+1$ a máme hotovo

Důsledek: $\mathbb{E}$ časové složitosti operací Find, Insert, Delete je $O(\frac{n}{m})$, což je díky přehešování konstantní

## Otevřená adresace

V každém prvku může být jenom jeden prvek a když je při hešování plná, tak zkusíme jinou

Definice: Každému $x \in \mathcal{U}$ přiřadíme vyhledávací posloupnost $h(x,0), h(x,1), \cdots, h(x, m-1)$ \
Dá se představit, že to hešovací funkce se dvěma parametry \
A také musí platit, že je to permutace na $[m]$ - nechceme, aby se to nezahešovalo, když bude pole plné

Operace:

&nbsp; Insert($x$) -- prostě opakujeme hešování dokud nenajdeme prázdnou přihrádku

&nbsp; Find($x$) -- zastaví se o prázdnou přehrádku

&nbsp; Delete($x$) -- nemůžeme jenom mazat, ale můžeme třeba přidávat pomníčky o které se find nezastaví \
&nbsp; &nbsp; Časem to stejně budeme potřebovat přehešovat

Příklady:

* lineární přidávání $h(x,i) = (f(x) + i)\mod m$, kde $f(x)$ je nějaká hešovací funkce
	* na přednášce byl příklad, že může snadno degenerovat a vznikat ostrůvky

* dvojité hešování -- $h(x,i) = (f(x) + i \cdot g(x)) \mod m$

Věta: Pokud vyhl. posloupnosti jsou nezávislé plně náhodné permutace, pak:

$$\mathbb{E}\ [\ \# \text{ přihrádek navštívených při neúspěšném Findu }] \leq \frac{1}{1-\alpha}$$

Důkaz: \
&nbsp; Nechť $y\in \mathcal{U}$ hledáme $h_1, \cdots, h_m$ je jeho vyhled. posl. \
&nbsp; $P_i := \text{Pr}[\text{projdeme alespoň }i \text{ přihrádek}]$ \
&nbsp; $P_1 = 1$ -- alespoň jednu přihrádku projdu vždycky \
&nbsp; $P_2 = \frac{n}{m} = \alpha$ -- pravděpodobnost, že první byla obsazená \
&nbsp; $P_i = \frac{n}{m} \cdot	\frac{n - 1}{m - 1} \cdots \frac{n-i+1}{m-i+1}$ a jednotlivé zlomky jsou menší rovno $\frac{n}{m}$ a to celé je tedy $\leq \alpha^{i-1}$ \

$$\mathbb{E}[\# \text{ navštívených přihrádek}] = \sum_{i\geq 1} i \cdot Pr[\text{navštíveno právě } i] $$

&nbsp; To je nějaká lineární kombinace $P_i$, takže my zkusíme zjistit kolikrát se $P_j$ započítalo

&nbsp; Ale $Pr[\text{navštíveno právě } i]$ je $P_i - P_{i+1}$

$$ \sum_{j\geq 1} P_j (j-(j-1)) \leq \sum_{j \geq 1} \alpha^{j-1} = \sum_{j \geq 0} \alpha^j = \frac{1}{1-\alpha}  $$

Dvojité hešování mimochodem $O\left(\frac{3}{1-\alpha}\right)$ a lineární přidávání $O\left(\frac{2}{(1-\alpha)^2}\right)$ 

# Rozděl a panuj (Divide et impera)

## Mergesort (třídění sléváním)

Rekurzivně se voláme na dvě poloviny a až je dostaneme, tak je slijeme -- zastavíme se o blok velikosti jedna

…však už to známe, takže pseudokód ani psát nebudu

### Anlýza složitosti

BÚNO $n=2^k$… prostě si to jen zjednodušíme

Mám nějaký rekurzivní vzorec $T(n)=2T(\frac{n}{2}) + n$ a $T(1)=1$

Paměť $M(n) = M(\frac{n}{2}) + n$ a to je očividně $\Theta(n)$, protože $M(n) = n + \frac{n}{2} + \frac{n}{4} + \cdots$

Jak ale řešit časovou složitost?

* Rozepsáním

$$ T(n) = 2T \left(\frac{n}{2}\right) + n $$

$$ T(n) = 4T\left(\frac{n}{4}\right) + 2n $$

$$ \vdots $$

$$ T(n) = 2^i \cdot T\left(\frac{n}{2^i}\right) + i\cdot n $$

&nbsp; $T(1)$ dostaneme pro $\frac{n}{2^i}$ a tedy $i = \log n$

$$ T(n) = 2^{\log_2 n} \cdot T(1) + \log_2 n \cdot n $$

$$ T(n) = n + \log n \cdot n $$

&nbsp; A tedy $\Theta(n \log n)$

	Logaritmy bez základu jsou v algoritmizaci brány většinou jako dvojkové (kvůli bitům)

* Strom rekurze

&nbsp; Alternativní způsob jak to řešit

&nbsp; Nakreslíme si strom a budeme počítat kolik má hladin, problémů na hladinu, jak je problém v hladině velký a tedy i čas na jednu hladinu

&nbsp; V našem případě bychom dostali $\log_2 n$ vysoký strom, jehož problémy na hladinu se vždy zdvojnásobí, ale velikost je poloviční \
&nbsp; Jedna hladina má tedy pořád velikost $n$ a to jenom vynásobíme počtem hladin

> 12. Přednáška 20.5.2021

## Násobení n-ciferných čísel

Klasické násobení, tak jsme se ho učili je $O(n^2)$

Nápad rozdělit to na půl a zavolat se rekurzivně

Chceme $X \cdot Y$ a máme

&nbsp; $X = A \cdot 10^{10/2} + B$ \
&nbsp; $Y = C \cdot 10^{10/2} + D$

BÚNO mocniny dvojky - dá se doplnit nulami

$X \cdot Y = AC \cdot 10^n + (AD + BC) \cdot 10^{n/2} + BD$

To nám ale moc nepomůže, protože pak máme $\log hloubku$, $4^i$ problémů na hladinu o velikosti $\frac{n}{2^i}$ \
…takže už jen v poslední hladině máme $n^2$ 

Dá se ale všimnou triku, že vypočítám jen $AC$, $BD$, $(A+B)(C+D)$, protože

$$ (A+B)(C+D) = AC + AD + BC + BD $$

$$ \cdots - AC - BD = AD + BC$$

Stačí tedy $3$ násobení (rekurzivní volání) $\frac{n}{2}$ ciferných čísel

Strom rekurze s $\log_2 n$ hloubkou, $3^i$ p. na hladinu o velikosti $\frac{n}{2^i}$

$$ T(n) = \sum_{i=0}^{\log_2 n} 3^i \cdot \frac{n}{2^i} = n \sum_{i=0}^{\log_2 n} \left( \frac{3}{2} \right)^i $$

$$ \frac{q^{k+1}-1}{q-1} = \Theta(q^k) = \Theta\left(\left(\frac{3}{2}\right)^{\log_2 n}\right) $$

$$ T(n)=\Theta(n^{1.59}) $$

Implementace: 

* Pro dost malý vstup zastavíme rekurzi a dopočítáme to hrubou silou
* Vyšší základ soustavy… třeba $2^{32}$

Umí se $O^{1+\epsilon}$ pro libovolně malé $\epsilon$, $O(n \log n)$ a $O(n)$

## Rekurze obecně (Master theorem)

Také nazýváno jako Kuchařková věta 

$$ T(n) = a \cdot T(\frac{n}{b}) + \Theta(n^c),\ \ \ \ \ \ T(1) = 1$$

Na $i$-té hladině je $a^i$ podproblémů

Hloubka je $\log_b n$

Čas na podproblém je $\left(\frac{n}{b^i}\right)^c \rightarrow$ čas na hladinu $a^i \cdot \left(\frac{n}{b^i}\right)^c$

Zavedeme si $\frac{a}{b^c} = q$

$$ T(n)=\sum_{i=0}^{\log_b n} a^i \cdot \left(\frac{n}{b^i}\right)^c = n^c \sum_{i=0}^{\log_b n} q^i $$

Rozbor případů podle velikosti $q$

1. $q=1$

$$ T(n) = n^c \cdot (\log_b n + 1) \cdot 1 = \Theta(n^c \cdot \log n)$$

2. $q < 1$

$$ \sum_{i=0}^{\log_b n} q^i \leq \sum_{i\geq=0}^{\log_b n} q^i = \frac{1}{1-q} = \Theta(1) $$

$$ T(n) = \Theta\left(n^c\right) $$

3. $q > 1$

$$ \sum_{i=0}^{\log_b n} q^i = \frac{q^{\log_b n + 1}-1}{q-1} \approx q^{\log_b n} = \left(\frac{a}{b^c}\right)^{\log_b n} = \frac{n^{log_b a}}{n^c} $$

To ještě vynásobíme vynechaným $n^c$

$$ T(n) = \Theta(n^{\log_b a}) $$

K důkazu zbývají případy, kdy $n$ není mocnina $b$ \
To ale udělám jednoduše tak, že vezmu nejbližší vyšší a nižší mocninu $b$ k $n$ a $n$ mezi ně sevřu \
Ty mocniny se ale asymptoticky neliší

## Násobení čtevrcových matic (Strasseův algoritmus)

BÚNO $n=2^k$

Rozdělím si matice na čtyři bloky

$$ \begin{pmatrix} A & C \\ B & D \end{pmatrix} \cdot  \begin{pmatrix} P & Q \\ R & D \end{pmatrix} =  \begin{pmatrix} I & J \\ K & L \end{pmatrix} $$

$I = AP + BR$, … podobně pro ostatní a tedy 8 součinů matic řádu $\frac{n}{2}$

$T(n) = 8T\left(\frac{n}{2} + \Theta(n^2)\right)$ a z kuchařky to je $\Theta(n^{\log_2 8})$

Chytřejším násobením se ale dostaneme na $\Theta(n^{\log_2 7})$

## Selekce - $k$-tého nejmenšího prvku z $x_1, \cdots, x_n$

### QuickSelect

### Postup:

1. vybereme pivota
2. rozdělíme mi vstup na L, S, P částí podle provnání s pivotem
3. rekurze do správné částí…

Nemám ale pod kontrolu to, jak velké ty části jsou -- jak dobrého pivota vyberu

1. V nejlepším případě $p =$ medián \
&nbsp; $T(n) = T\left(\frac{n}{2}\right) + \Theta (n)\ \ \ \rightarrow \ \ \ T(n) = \Theta(n)$

2. V nejhorším případě oddělám jen jeden prvek  \
&nbsp; $T(n) = n + (n-1) + (n-2) + \cdots + 1 = \Theta(n^2)$

3. Nám ale stačí jakýsi skoro medián \
&nbsp; Když budu v prostředních dvou čtvrtinách, tak vždy jednu krajní čtvrtinu odstraní \
&nbsp; $T(n) = T\left(\frac{3}{4}n\right) + \Theta(n) = n + \frac{3}{4}n + \left(\frac{3}{4}\right)^2 n + \cdots = \Theta(n)$

4. Randomizované hledání skoromediánu \
&nbsp; &nbsp; &nbsp; 1. vyberu $p$ náhodně \
&nbsp; &nbsp; &nbsp; 2. spočítám kolik je menších a větších než $p$ \
&nbsp; &nbsp; &nbsp; 3. pokud to není skoromedián, tak znovu

&nbsp; Věta: v takovém případě je $\mathbb{E}[\text{čas. složitosti}] = \Theta(n)$ \
&nbsp; &nbsp; K tomu nám stačí aby $\mathbb{E}[\# \text{ pokusů}] = \Theta(1)$

&nbsp; &nbsp; Můžeme si všimnout, že pravděpodobnost toho, že pokus uspěje je $\geq \frac{1}{2}$

&nbsp; &nbsp; Lemma (o džbánu): pokud pokusu uspěje s pravděpodobností $p$ pak $\mathbb{E}[\# \text{ pokusů do 1. úspěchu}] = \frac{1}{p}$ \
&nbsp; &nbsp; A z toho plyne, že $\mathbb{E}[\# \text{ pokusů}] \leq 2$

Ještě dokážeme lemma o džbánu 

$$\mathbb{E} = \sum_n n \cdot Pr[\# \text{ pokusů} = n] = \sum_n n \cdot (1-p)^{n-1} \cdot p$$

Pravděpodobnost, že je $n$ pokusů je to samé jako, že $1-p$ pokusů neuspělo a poslední uspěl

Dá se všimnout, že

$$\mathbb{E} = 1 + (1-p)\mathbb{E} $$

$$ \mathbb{E} = \frac{1}{p} $$

5. Volíme pivota náhodně \
&nbsp; Rozdělíme běh na fáze, kde fáze končí výběrem skoromediánu

&nbsp; Můžeme si všimnou, že $Pr[\text{fáze skončí}] \geq \frac{1}{2} \implies \mathbb{E}[\text{pokusů na fázi}] \leq 2$

&nbsp; Další pozorování je, že fáze zmenší $n$ aspoň $\frac{3}{4} \times$
&nbsp; Střední hodnota času na fázi je tedy lineární a když to sečteme přes všechny fáze, tak

$$ \Theta\left(n + \frac{3}{4}n + \left(\frac{3}{4}\right)^2 n + \cdots \right) = \Theta(n) $$

> 13. Přednáška 27.5.2021

## $k$-tý nejmenší prvek, randomizace

### Select $(x_1, \cdots, x_n; k)$

1. Rozdělíme $x_1,\cdots, x_n$ na pětice $P_1, \cdots, P_t$ $\ (t=\lceil \frac{n}{5}  \rceil)$
2. Najdeme mediány všech pětic
3. $p$ = select na mediány pětic
4. dá se to jako pivot v již zmíněném algoritmu

#### Věta - to má složitost $\Theta(n)$

***Důkaz***

Z obrázku nerovností vím, že zahodím vždy alespoň $3/10$ prvků

$$ T(n) = T(n/5) + T(7/10 n) + \Theta(n) $$ 

$$ T(1) = 1 $$

Uhodnu, že $T(n) = c \cdot n$ a pak:

$$ cn = 1/5 cn + 7/10 cn + n $$

$$ c = 10 $$

# QuickSort

Historicky první algoritmus, který $n \log n$ dal alespoň průměrně

## Pseudokód (vstup je $x_1, \cdots, x_n$)

1. Pokud $n\leq 1$ vrátím vstup &nbsp; # okrajová podmínka
2. Zvolím pivot $p$
3. Vezmu vstup a rozdělím si ho podle p na L, S, P části
4. Rekurzivní volání do L a P
5. Slepím to za sebe

### Složitost
- pokud $p$ bude medián

$$ T(n) = 2T(n/2) + O(n) $$

$$ T(n) = \Theta(n \log n) $$

- pokud $p$ bude min/max

$$ T(n) = T(n-1) + T(0) + n $$
$$ T(n) = \Theta (n^2) $$

#### Věta - náhodná volba pivota má časovou složitost $\Theta (n \log n)$

##### 1. *Důkaz*

&nbsp; Budeme počítat počet porovnání pro každý prvek \
&nbsp; Porovnání účtujeme prvku, který nebyl pivotem \
&nbsp; Dostaneme z toho nějakou náhodnou veličinu $P_i$ a jejich suma bude pak celkový počet porovnání \
&nbsp; Střední hodnota počtu porovnání je suma středních hodnot porovnání pro jeden prvek

&nbsp; Mimochodem počet porovnání bude lineární k celkové složitosti

&nbsp; Sledujeme velikost podproblému ve kterém je $x_i$

* V případě pseudomediánu se za $O(\log n)$ fází dostaneme na konstantu, protože se fáze zmenší max. na $3/4$
* Střední hodnota počtu kroků pro jeden prvek na fázi je konstantní ($\leq 2$)

&nbsp; Z toho $O (n \log n)$

##### 2. *Důkaz* - trochu rigoróznější

&nbsp; Nechť $y_1, \cdots, y_n$ je setříděné pořadí prvků \
&nbsp; Zavedu indikátory $C_{ij}$ podle toho, pokud jsme porovnali $y_i$ a $y_j$ \
&nbsp; &nbsp; To se stane nejvýše jednou, protože jeden je pivot a ten pak nepokračuje \
&nbsp; Celkový počet porovnání je součet indikátorů

&nbsp; Střední hodnota počtu porovnání je suma středních hodnot indikátorů \
&nbsp; Střední hodnota E[C_{ij}] je pravděpodobnost, že $y_i$ a $y_j$ bylo porovnáno \
&nbsp; Co se ale k tomu muselo stát?

* Právě je $y_i$ nebo $y_j$ pivot
* Žádný z $y_i$ a $y_j$ ještě pivot nebyl (takže $y_i$ nebo $y_j$ se z prvků $y_i, \cdots, y_j$ stalo jako první)
* Ta pravděpodobnost je $\frac{2}{j - i + 1}$
 
&nbsp; Takže střední hodnota počtu porovnání je:

$$ \sum_{1 \leq i < j \leq n}\frac{2}{j - i + 1} = \sum_{1 \leq d \leq n} \frac{2}{d} \cdot (n - d + 1) \leq 2n \sum_{1 \leq i < j \leq n} \frac{1}{d} $$

To je $n$-té harmonické číslo a to roste logaritmicky

** Lemma: $\ln n \leq H_n \ln n + 1$, kde $H_n = \sum_{1 \leq i \leq n} 1/i$ **

*Důkaz:*

&nbsp; Dá se to představit na grafu paraboly body, které prochází čísly z harmonické sumy \
&nbsp; Nadefinuji si $I_n$ jako plochu pod tou křivkou a přes integrál to je $\ln n$ \
&nbsp; Ta suma je potom obsah "schodiště", kde u každého bodu přidáme úsečku doleva \
&nbsp; To schodiště je menší než, když tu křivku zintegrujeme \
&nbsp; Zároveň když nakreslím u schodiště úsečku doprava (přičtu 1), tak je to větší

---

# Dynamické programování (memoizace)

## Klasický příklad s rekurzivním Fibnoaccim

&nbsp; &nbsp; &nbsp; $F(n) = 1\text{ pokud } n \leq 1 \text{ jinak } F(n) = F(n-1) + F(n-2)$

To je bez kešování pomalé, dá se to představit jako binární strom s hledaným číslem v kořenu a my projdeme celý strom místo cesty z levého listu

- Výsledná hodnota je totiž prostě suma hodnot v listech (a to jsou nejvýše jedničky)

Už ale víme, že $F_n \geq 2^{n/2}$ a to znamená, že náš algoritmus je exponenciální

Takže **si  budu pamatovat předchozí výsledky**

Před zanořením se podíváme, jestli je v poli definované a pokud ho už budeme počítat, tak to ho zapíšeme do pole

Každou hodnotu tedy počítáme jenom jednou a to v konstantním čase

Celkem to tedy trvá $O(n)$

Jiná možnost vyplňovat cyklem v poli $P[0], \cdots ,P[n]$

## Základní principy DP

1. Začneme s exponenciálním algoritmem
2. Všimneme si, že často počítáme to samé
3. Zavedeme si proto paměť na známé výsledky
4. Rekurzi nahradíme vyplňování keše ve správném pořadí

## Hledání nejdelší rostoucí podposloupnosti v $x_1, \cdots, x_n$

BÚNO si přidám $x_0=0$ a $x_{n+1}=\infty$

NRP($i$) je délka NRP vybrané z $x_i$ ... $x_{n+1}$ začínající $x_i$

1. $d \gets 1$
2. Pro $j=i+1, \cdots,  n+1$:
3. &nbsp; Pokud $x_i < x_j$
4. &nbsp; &nbsp; $d = \text{max}\left(\text{NRP}(j) + 1, d\right)$
5. Vrátíme $d$

To má zjevně exponenciální složitost (v případě rostoucí posloupnosti vyzkouším všechny podposloupnosti $2^n$)

Volání se ale opakují, takže přidáme keš

Funkce se pak zavolá $O(n)$-krát a pokaždé počítá v $O(n)$, takže je to $O(n^2)$

Abychom se nemuseli rekurzit, tak to uděláme ve správném pořadí zprava doleva

**NRP(n)**

1. $P[n+1] = 1$
2. Pro $i = n, \cdots, 0$
3. &nbsp; $d = 1$
4. &nbsp; Pro $j = i+1, \cdots, n + 1$
5. &nbsp; &nbsp; Pokud $x_i < x_j$
6. &nbsp; &nbsp; &nbsp; $d =$ max$\left(P[j]+1,d\right)$
7. &nbsp;  $P[i] = d$ 
8. Vrátíme $P[0]$

I když teda to pořád není optimální a například vhodnou datovou strukturou jde v $O(n \log n)$

Alternativně sestrojíme graf ve kterém vrcholy budou prvky posloupnosti a hrany povedou mezi vrcholy pro které platí, že vrchol směrem doprava je větší

Potom hledáme nejdelší cestu v DAGu

Má triviální topologické pořadí a cestu najdeme indukcí v $O(n^2)$

#### Bonus - Kouzelené řešení z první přednášky

Postupně přidáváme $x_1$, $x_2$, ...

Udržujeme si $m_i$ := min. koncový prvek RPP délky $i$

Platí

* $m = min (x_1, \cdots, x_m)$
* $m_0 = -\infty$
* $m_i \leq m_{i+1}$

Z toho je posloupnost s $m$ neklesající

Co když přidáme prvek $x_k$? (Jaké RPP vznikly?)

Za každou RPP nějaké délky $i$, která končí menším prvkem než jsme přidali přidáme ten prvek -> RPP délky $i + 1$ končící tím prvkem

V $log n$ najdeme binárně rozhraní mezi čísly menšími a většími než $x_k$ v posloupnost $m$

Celkem $O(n \log n)$

> 14. Přednáška 3.6.2021

## Editační vzdálenost

Editační operace jsou v podstatě překlepy (změna, vložení a smazání znaku)

Editační vzdálenost je min. délka posloupnosti editačních operací, které z prvního řetězce udělají druhý

* Někdy také Levenštejnova vzdálenost
* Je to metrika
* Značí se $L(\alpha, \beta)$ pro řetězce $\alpha,\beta$

Pozorování: operace jsou BÚNO prováděné z leva do prava v $\Alpha$

**Jak vlastně vypadá první operace?**

Představíme si $\alpha$ jako $a_1, \cdots, a_n$ a  $\beta$ jako $b_1, \cdots, b_n$

Možnosti jsou potom:

1. Smazat $a_1$ $\mapsto L(a_2 \cdots a_n, b_1 \cdots b_n)$
2. Změnit $a_1$ na $b_1$ $\mapsto L(a_2 \cdots a_n, b_2 \cdots b_n)$
3. Vložit $b_1$ před $a_1$ $\mapsto L(a_1 \cdots a_n, b_2 \cdots b_n)$
4. Ponechat $a_1$ i $b_1$ $\mapsto L(a_2 \cdots a_n, b_2 \cdots b_n)$

Počítáme pak, že zkusíme 1. - 4. a pak vyberme mininum

Zavedeme si Edit$(i,j)$ s cílem spočítat  $L(a_1 \cdots a_n, b_1 \cdots b_n)$
 
Edit(i,j)
1. Pokud $i>n$: Vrátíme $m-j+1$ # to co zbylo z $\beta$ \
   Pokud $j>m$: Vrátíme $n-i+1$
2. $l_v \gets 1 + Edit(i, j + 1)$ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # vložit
3. $l_s \gets 1 + Edit(i + 1, j)$ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # smazat
4. $l_z \gets 1 + Edit(i + 1, j + 1)$ &nbsp; &nbsp; # změnit
5. Pokud $\Alpha \neq \Beta_j$ : $l_z \gets l_z + 1$
6. Vrátím min$(l_v, l_s, l_z)$

Pozorování - je to dost pomalé (např. pro "aaaaa" a "aaaaa") zbytečně zkouším kroky

Druhé pozorování je, že $i$ a $j$ leží někde v řetězci (mezi $1$ a $n+1$, resp. $1$ a $m+1$) \
Už kešeování by nás tedy dostalo na $\Theta(n \cdot m)$ různých volání

### Nerekurzivní verze

Představa s tabulkou, kterou vyplňujeme z pravého dolního rohu

1. Pro $j = 1 \cdots m + 1$: $T[n+1, j] \gets m-j+1$ \
   Pro $i = 1 \cdots n$: $T[i, m+1] \gets n-i+1$
2. Pro $i=n \cdots 1$:
3. &nbsp; Pro $j = m \cdots 1 $:
4. &nbsp; &nbsp; $\delta \gets$ 0 nebo 1 podle toho, jestli $a_i = b_j$
5. &nbsp; &nbsp; $T[i,j] = min(1 + T[i+1, j], 1 + T[i, j + 1], \delta + [i+1, j+1])$

Takže to máme časově v $\Theta(n \cdot m)$ a prostorově $\Theta(n \cdot m)$\
(bez pamatování posloupnosti to jde i $\Theta(n+m)$

### Grafový pohled

Na $y$ ose je pozice v $\Alpha$ a na $x$ ose je pozice v $\Beta$

Z každého vrcholu pak máme tři cesty podle editačních operací

Cesta z $(1,1)$ do $(n,m)$ je posloupnost editačních operací, které z $\Alpha$ udělá $\Beta$

Plán tedy je vytvořit graf a spočítat nejkratší cestu

Graf vytvoříme v $\Theta(n \cdot m)$ (protože je to počet vrcholů)

Je to DAG, takže ho můžeme zpracovat v topologickém pořadí a tedy nejkratší cesta $\Theta(n \cdot m)$

On je to ale vlastně úplně stejný algoritmus, jako ten předtím

## Optimalizace vyhledávacích stromů

**Příklad**:

* na 1 se ptáme 10x
* na 2 se ptáme 1x
* na 3 se ptáme 5x

Ten strom může vypadat 5 způsoby

Levá liána, … , dokonale vyvážený, … , pravá liána

Když budeme počítat kolikrát se podíváme na všechny vrcholy, tak to vyjde 37, 28, 31, 23, 27

<!-- TODO *Třeba pak udělám obrázek* -->

Problém tedy je: máme klíče $x_1 < \cdots < x_n$ a váhy  $w_1 \cdots w_n \in \mathbb{N}$

Pro BVS T na  $x_1 \cdots x_n$ definujeme hloubku $h_1 \cdots h_n$ jako $h_i :=$ počet vrcholů na cestě od kořene do $x_i$

Cena stromu $C(T) := \sum_i h_i \cdot w_i$

A chceme najít $T$ s minimálním $C(T)$

*Pozorování* Co kdyby v kořenu opt. stromu bylo $x_i$?

$$ OPT(x_1 \cdots x_n) = OPT(x_1 \cdots x_{i - 1}) + OPT(x_{i + 1} \cdots x_n) + \sum_{j=1}^n w_j $$

(odebrali jsme hranu od kořene a tak to tou sumou kompenzujeme)

My ale kořen neznáme a proto zkusíme všechny vrcholy jako kořeny

Zavedeme si funkci, která si spočítá optimální cenu BVS pro klíče od $x_l$ do $x_p$

OptBVS(l.p)

1. Pokud $l>p$: vrátíme 0
2. Vrátíme $\min(C_l \cdots C_p) + \sum_{i=l}^p w_i$, \
   kde $C_i := OptBVS(l, i-1) + OptBVS(i+1,p)$

Klasický proces… je to pomalé a $l, p$ jsou někdy mezi $1$ a $n+1$, takže je jen $O(n^2)$ podproblémů

Kešováním tedy dostaneme $O(n^2)$ podproblémů, každý v čase $O(n)\rightarrow$ jsme na $O(n^3)$

A při nahrazování cyklem jdu od nejkratších intervalů k nejdelším

1. Pro $l = 1 \cdots n$: $T[l, l-1]\gets 0$
2. Pro $d = 1 \cdots n$: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; # d je délka intervalu
3. &nbsp; Pro $l = 1 \cdots n - d + 1$: &nbsp; &nbsp; # $l$ je levý okraj
4. &nbsp; &nbsp; p \gets l + d - 1 &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; # pravý okraj
5. &nbsp; &nbsp; $T[l,p] \gets \min(C_l \cdots C_p) + \sum_{i=l}^p w_i$,  \
   &nbsp; &nbsp; kde $C_i := T[l, i-1] + T[i+1, p]$
6. Vrátíme $T[1,n]$

Čas $O(n^3)$ a prostor $O(n^2)$

Pokud chceme jak ten strom vypadá, tak si v 5. zapamatujeme optimální kořen (pro které $C_i$ bylo minimum) \
&nbsp; kořen opt. stromu pro daný inteval

Z toho už dáme rekurzivní budování jako u dokonale vyváženého stromu (místo prostředku vezmeme zapamatované kořeny)

Umí se to ale udělat i v $O(n^2)$ - hodí se na to nerovnost, že Kořen$[l, p-1] \leq$ Kořen$[l,p] \leq$ Kořen $[l-1,p]$

## Dynamické programování obecně

Pěkný abstraktní pohled, že mám systém podproblémů (tzv. stavy DP) a ty mezi sebou mají nějaké závislosti, které tvoří DAG

Princip DP je projít stavy v topologickém pořadí

## Vzdálenost mezi všemi dvojcemi bodů v ohodnoceném orientovaném grafu (Floydův-Warshallův algoritmus)

Orientovaných graf bez záporných cyklů s vrcholy $1 \cdots n$ a matici délek hran (buď délka, nekonečno nebo $0$)

Chceme matici vzdáleností ($D_{ij}=$ vzdálenost z $i$ do $j$)

Umíme už spustit $n$ Dijkstru (to je $n^3$) a nebo $n$ Bellman-Ford$, to je ale v hustém grafu $n^4$

Floyd-Warshall je sice taky kubický, ale zato je triviální

Df: $D_{ij}^k :=$ délka nejkratšího sledu z $i$ do $j$, jehož vnitřní vrcholy leží v ${1 \cdots k}$

$D^0$ je matice délek hran a $D^n$ je $D$

Výpočet $D^k$ z $D^{k-1}$

$D_{ij}^k$ je buď $D_{ij}^{k-1}$ a k nepoužito nebo $D_{ik}^{k-1} + D_{kj}^{k-1}$ a k použito BÚNO 1x

Opět si vybereme tu lepší variantu (a tedy minimum) - to zvládneme konstantně

Celou matici tedy spočítám v $\Theta(n^2)$ a jdu z $D^0$ do $D^k$, takže dohromady $\Theta(n^3)$

**Nevýhoda** má to i kubickou paměť, to je ale zbytečné, protože si vždy stačí pamatovat jen dvě matice

A ještě lepší je přepisování na místě (musíme ale ukázat, že $D_{ik}^{k-1} + D_{kj}^{k-1}$ zůstalo stejné)

1. Pro $k = 1 \cdots n$:
2. &nbsp; Pro $i = 1 \cdots n$:
3. &nbsp; &nbsp; Pro $j = 1 \cdots n$:
4. &nbsp; &nbsp; &nbsp; $D_{ij} = min(D_{ij}, D_{ik} + D_{kj})$

&nbsp;

---

&nbsp;

# Zkoušky

Z fora jsou zadání na zkouškách:

1. AVL-stromy -- Definice, důkaz logaritmické hloubky, postup Insertu nebo Deletu
2. Most v neorientovaném grafu -- Jak jej najít
3. $S=\{3^i \cdot 5^j \cdot 5^k \ |\ i,j,k \in \mathbb{N}\}$
Najít prvních n nejmenších prvků množiny S + složitosti, důkaz správnosti
4. Je zadán strom, najděte v něm jako podgraf největší housenku. (Nejvíce vrcholů) \
Housenka je to když máme cestu a v jakýkoliv vrcholech přidáme jakýkoliv počet listů + složitosti, důkaz správnosti

---

1. Násobení $n$-ciferných čísel rychleji než $n^2$
2. Minimální kostra + důkaz
3. Vymyslet algoritmus na mazání vrcholů v grafu, který zachovává souvislost (když algoritmu dáme souvislý graf a budeme mazat podle toho, co nám řekne, tak v každém kroku bude graf souvislý)
4. Okénkový medián $k$ prvků v nekonečné posloupnosti

---

1. Hledání topologického uspořádání
2. Násobení $n$-ciferných…
3. Okénkový…
4. Algoritmus na rozklad grafu na cesty délky 2 

---

1. (a,b) strom
2. Hledání minimální kostry
3. Slovní žebřík - slovník $n$ slov délky až $i$. najděte nejdelší posloupnost slov, které se jedno z druhého tvoří odebráním jednoho libovolného písmene, např Glass -> Glas -> Gas -> as
4. Knihovna - v knihovně je $n$ knih, z nichž $k$ je setřízeno špatně - dotřiďte knihovnu \
5. **Bonus:** V daném stromě zrušte co nejméně hran tak, aby vznikla alespoň jedna komponenta souvislosti obsahující právě $k$ vrcholů

---

1. Jarník a řezové lemma
2. Třídění $n$ čísel z množiny $\{ 1 \cdots n^4 \}$
3. Směnárna s $n$ měnami podle matice kurzů $K$ ($K_{i,j} :=$ kolik dostaneme $j$ za $i$) Lze na směňování vydělat? 
4. Jak setřídit posloupnost, víme-li, že každý prvek se nachází ve vzdálenosti nejvýše $k$ od správné polohy? 
5.  Bonus:  Najít dvě funkce $f,g$, tak aby neplatilo $f=O(g)$ ani $g=O(f)$

