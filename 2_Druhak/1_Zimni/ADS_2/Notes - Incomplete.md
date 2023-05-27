# Vyhledávání v textu

## Notace

$\Sigma$ - abeceda (konečná - bude se uvažovat rozumně velká)
$\Sigma^\star$ - množina všech řetězců
$\alpha,\beta, \cdots$ - řetězce
$x, y, \cdots$ - znakyl
$|a|$ - délka řetězce
$\epsilon$ - prázndný řetězec
$\alpha \beta$ - konkatenace
$a[i]$ - $i$-tý znak
$a[i:j]$ - podřetězec jak v Pythonu (dolní index inkluzivní, horní exkluzivní)
&nbsp; s prázdným jedním je to prefix nebo sufix

Každý podřetězec je prefix sufixu

## Problém

Máme vstup seno $\sigma$ ($S := |\sigma|$) a jehlu $\iota$, $J := |\iota|$
A chceme množinu všech indexů na kterých začíná jehla

## Řešení

### Naivní přístup

Zkusit v každém místě sena, jeslti je tam jehla $\Theta(S \cdot J)$
Pokud začneme porovnávat tam, kde jsme skončili, tak sice $\Theta(S)$, ale nebude to fungovat

### Inkrementální algoritmus

Přepočítáváme vnitřní stav algoritmu - jak dlouhý kus jehly jsme už viděli, formálně: 

$$\text{stav } \alpha := \text{nejdelší prefix jehly, který je sufixem sena}$$

Nový stav bude buď $\epsilon$ nebo $\alpha'x$ - $a'$ je sufix $\sigma$ a prefix $\iota$m takže $\alpha'$ je sufix $\alpha$

Můžeme mít předvýpočet Zpětná funkce $z$ a defubiváné:

$$z(\alpha) := \text{nejdelší } \alpha' \text{ vlastní sufix } \alpha \text{, který je prefixem } \iota$$

Budeme ale pracovat se stavem jako s číslem

Dostaneme algoritmus **KMP**

Zformujeme ho pomocí vyhledávacího automatu

> Na tabuli obrázek grafu s dopřednými a zpětnými hranami mezi stavy a přechodu mezi nimi pomocí písmen

Pomocná funkce pro jeden krok automatu:

---

**Krok($i,x$):**

1. &nbsp; Dokud $\iota[i] \neq x$:
2. &nbsp; &nbsp; Je-li $i=0$: vrátíme $0$
3. &nbsp; &nbsp; $i \gets Z[i]$
4. &nbsp; Vrátíme $i + 1$

---

**Hledej($\sigma$):**
1. &nbsp; $i \gets 0$
2. &nbsp; Pro $j = 0, \cdots, S - 1$:
3. &nbsp; &nbsp; $J \gets \text{Krok}(i, \sigma[j])$
4. &nbsp; &nbsp; Pokud $i = J$: ohlasíme výskyt na $j - |\iota| +1$

---

> Musíme na konec sena přidat nepoužitý znak

#### Kolik kroků to je?

*Lemma*: Hledej($\sigma$) má složitost $\Theta(S)$

*Důkaz*:
Máme $S$ kroků, ale teď nás zajímá jeden krok - skok po hraně

Počet dopředných hran je nejvýše S
zpětných hran skočíme maximálně tolikrát, kolik máme počet dopředných hran

Musíme ale prvně sestrojit automat

*Pozorování*:
pokud $\alpha$ je stav a spustíme automat na vstup $\alpha[1:]$, pak skončíme ve stavu $z(\alpha)$

Pak vytváříme automat pomocí volání na základě přehozího pozorvání -- bootsraping \
(můžeme to udělat, protože vždy už ty zpětné, které pak budeme potřeovat existují)

---

**Konstrukce automatu:**
1. &nbsp; $Z[0] \gets 0, Z[1] \gets 0$
2. &nbsp; $i \gets 0$
3. &nbsp; Pro $j  = 2, \cdots, J$:
4. &nbsp; &nbsp; $i \gets$ krok($i, \iota[j-1]$)
5. &nbsp; &nbsp; $Z[j] \gets i$

---

*Věta:* KMP najde všechny výskyty v čase $\Theta(S+J)$

#### Více jehel

Musíme si ve složitosti ošetřit zvláštní výstup $\Theta(S + \sigma J_i + \text{ počet výskytů})$

Musíme KMP zobecnit
Automat pak bude trie -- povede více dopředných hran 
Trochu upravíme Hledej -- přidáním nekončí a proto:
Zavedeme si zkratkové hrany - nejbližší koncový stav po zpětbých hranách

#### Reprezentace automatu

* stavy očíslovat od nuly
* Slovo($i$) $:=$ která jehla končí ve stavu $i$
* Zpět($i$) $:=$ kam vede zpětná hrana
* Zkratka($i$) $:=$ kam vede zkratková hrana
* Dopředu ($i,x$) $:=$ dopředná hrana pro písmeno $x$

> všechny můžou být i $\emptyset$

---

**Krok($i,x$):**

1. &nbsp; Dokud Dopředu$(s,x) \neq \emptyset$:
2. &nbsp; &nbsp; Je-li $s=$ kořen: vrátíme $0$
3. &nbsp; &nbsp; $s \gets$ Zpět($s$)
4. &nbsp; Vrátíme Dopředu $x$

---

**Hledej($\sigma$):**

1. &nbsp; $s \gets 0$
2. &nbsp; Pro $i = 0, \cdots, s - 1$:
3. &nbsp; &nbsp; $d \gets \text{Krok}(s, \sigma[i])$
3. &nbsp; &nbsp; $t \gets s$
4. &nbsp; &nbsp; Dokud $t \neq \emptyset$: 
5. &nbsp; &nbsp; &nbsp; Je-li Slovo($t$) $\neq \emptyset$
6. &nbsp; &nbsp; &nbsp; &nbsp; ohlasíme výskyt
7. &nbsp; &nbsp; &nbsp; $t \gets$ Zkratka($t$)

---

**Lemma**: Hledej beží v čase $O(S +$ #výskytů$)$

**Důkaz**: 
Opět počet kroků zpět je menší než počet dopředu a to je menší než S
Pokud jde po zkrace, tak to "naúčtujeme" počtu výskutů

Co s konstrukcí?
Nemůžeme použít to co z KMP, protože by zpětné mohli vést do nenavštívených -- musíme stavět po vrstvách

---

**Konstrukce automatu($\iota_1, \cdots, \iota_n$):**
1. &nbsp; Vybudovat trii pro $\iota_1, \cdots, \iota_n$ -- dopředné hraby a kořen $r$
2. &nbsp; Zpět($r$)$\gets \emptyset$, Zkratka($r$) $\gets \emptyset$
3. &nbsp; Pro $s$ syny kořene: Zpět($s$) = 0, Zkratka $\gets \emptyset$
4. &nbsp; $F :=$ fronta se syny kořene
5. &nbsp; Dokud $F \neq \emptyset$
6. &nbsp; &nbsp; $v \gets$ Dequeue($F$)
7. &nbsp; &nbsp; Pro $s$ syny $v$:
8. &nbsp; &nbsp; &nbsp; Zpět($s$) $\gets$ Krok(Zpět($v$, písmeno na hraně $vs$))
9. &nbsp; &nbsp; &nbsp; Přidáme $s$ do $F$
10. &nbsp; &nbsp; &nbsp; Pokud Slovo(Zpět($v$)) $\neq \emptyset$:
11. &nbsp; &nbsp; &nbsp; &nbsp; Zkratka($s$) $\gets$ Zpět($v$)
12. &nbsp; &nbsp; &nbsp; Jinak: Zkratka($s$) $\gets$ Zkratka(Zpět($v$))

---

**Lemma:** Konstrukce běží v čase $O(\sum \iota)$

**Důkaz:** Vybudování a prohledávání do šířky je lineární s délkami jehel. Přidávání zpětnách je lineární (už z minula)

### Rabinův-Karpův algoritmus

Založím to na hešovacím algoritmu

Spočítám si heš jehly a pak pojedu okénkem a kontrolovat hesh okénka

> Normálně bychom ten heš museli přepočítat, ale my si vytvoříme šikovnou hešovací funkci

$h(x_0, \cdots, x_{j-1}) = (x_0 r^{j-1} + x_1 r^{j-2} + \cdots + x_{j-1}r^0) mod H$

Posunuté je to pak $h(x_1, \cdots, x_{j}) = (x_1 r^{j-1} + x_1 r^{j-2} + \cdots + x_{j}r^0) mod H$

Takže mi vlastně stačí přenásobit poslední hešh $r$ a odečíst $x_0 r^j + x_j$

---

**Rabinův-Karpův algoritmus:**

1. &nbsp; Zvolíme náhodné $r$ a  vypočítáme $r^j$
2. &nbsp; $c\gets h(\iota), a\gets h(\sigma[:j])$
3. &nbsp; Pro $i = 1, \cdots, S-J:$
4. &nbsp; Pokud $a=c$ & $\sigma[i:i+J]=\iota$: výskyt
5. &nbsp; $a \gets (a\cdot r - \sigma[i]\cdot r^j + \sigma[i+J]) mod H$

---

#### Složitost

* Režie a počítání hešů $O(S)$
* Skutečné výskyty $O(J \cdot V)$ ($V$ je počet výskytů)
* Falešné výskyty 
    * pro ideální hešovací funkci je Pr[falešný výskyt] $=\frac{1}{H}$
    * a tedy průměrný čas je $O(\frac{S \cdot J}{H})$
    

Naše funkce ale ideální není... i když není až tak daleko

**Lemmata o polynomech:**

Pokud $x_1, \cdots, x_k$ jsou všechny kořeny polynomu P, pak: $P(x) = (x-x_1) \cdot (x-x_2) \cdots (x-x_k) \cdot Q$ a $Q$ je polynom bez kořenů

To má důsledek, že nenulový polynom stupně $d$ má max $d$ kořenů

Nechť $P, Q$ jsou polynomy stupně $< n$ a $x_1 , \cdots, x_n$ navzájem různá čísla t.ž. $\forall i: P(x_i) = Q(x_i)$. Potom $P=Q$

**Důkaz:**
$R:=P-Q$ je polynom stupně $<n$ t.ž.$\forall i: R(x_i) = 0$

To můžeme využít k tomu, že pravděpodobnost, že je falešné pozitivum je $\leq \frac{J}{H}$

> 18.10.2021

# Toky v sítích

Síť se skládá z:

* Orientovaného grafu $G(V,E)$
* $z,s \in V$ -- zdroj a stok
* funkce $c: E \mapsto \mathbb{R}_0^+$ -- kapacity hran


Definice:

* $f^+(v) := \sum_{UV\in E}f(uv)$ -- přítok
* $f^-(v) := \sum_{VU\in E}f(uv)$ -- odtok
* $f^\delta(v) := f^+(v) - f^-(v)$
* $|f| := f^\delta(s)$ -- velikost toku


Tok je $f: E\mapsto \mathbb{R}_0^+$ t.ž.

1. $\forall e \mapsto E: f(e) \leq c(e)$
2. $\forall v \in V, v \neq s : f^\delta = 0$ - Kirhoffuův zákon


Pozorování:

$f^\delta(s) = -f^\delta(z)$


Důkaz:

$0 = \sum_v f^\delta(v) = f^\delta(s) + f^\delta(z)$


Jak hledat maximální tok:

Nápad na zlepšovací algoritmus -- ten je ale špatně

## Fordův-Fulkersonův algoritmus

Občas můžeme tok zlepšovat i v protisměru

Definujeme rezervu hrany -- o kolik víc můžu po té hraně poslat (po směru a protisměru)

$f(uv) := c(uv) - f(uv) + f(vu)$

Z grafu uděláme BÚNO symetrický (obrácené hrany budou mít nulovou kapacitu)

**Fordův-Fulkersonův algoritmus:**
1. &nbsp; $f \gets 0$
2. &nbsp; Dokud $\exists P$ nenasycená cesta $z\mapsto s$:
3. &nbsp; &nbsp; $\epsilon \gets min_{e \in P} r(e)$
4. &nbsp; &nbsp; Pro všechny $uv \in P:$
5. &nbsp; &nbsp; &nbsp; $\delta min(\epsilon, f(vu))$
6. &nbsp; &nbsp; &nbsp; $f(vu) \gets \delta$
7. &nbsp; &nbsp; &nbsp; $f(uv) \gets f(uv) + \epsilon - \delta$

**Konečnost:**

* Pro celá čísla se vždy zastaví
* Pro racionální se také vždy zastaví
* Obecně ne

**Věta (Edmond a Karp):**

Pro nejkratší nenasycenou cestu je #iterací $O(nm)$

Z toho F.F běží v $O(nm^2)$

Zavedu si řez -- hrany mezi dvěma částmi grafu, přičemž v jednom je zdroj a v druhém stok, formálně:

Pro $A,B \subseteq V: E (A,B) := \{ ab \in E\ |\ a \in A \wedge b \in B \} = E \cap (A \times B)$

**Elementární řez** $:= E(A,B)$ pro jakékoliv $A,B \subseteq V, A \cup B = V, A \cap B = \emptyset, z \in A, s \in B$

$f(A,B) := \sum_{e\in E(A,B)} f(e)$ ... $c(A,B) = $ kapacita řezu

$f^\delta(A,B) = f(A,B) - f(B,A)$

$f^\delta(A,B)$ je vždy velikost toku


Důkaz:

$f^(A,B) = \sum_{v \in B} = f^\delta(s) = |f|$


Lemma:

$ \forall f$ tok, $\forall E(A,B$ řez: $|f| \leq c(A,B)$

$f^\delta (A,B) = f(A,B) - f(B,A) \leq c(A,B) - 0$

Pokud $f$ je rovnost $f$ je maximální, $E(A,B)$ je minimální


Situace po zastavení FF:

$A := v\ | \exist\text{ cesta z } z \text{ do } s \text{ po hranách s }r > 0 \}$

* na každé hraně musí být $f=c$ -- sporem, protože pak existuje nenasycená cesta do bodu vedle řezu...
* z druhé strany je tok nulový

A tedy podle předchozího lemma máme maximální tok


### Problém největšího párování v bipartitním grafu

Párování v grafu $(V,E)$ je $F\subseteq E$ t.ž. $\forall e, f \in F: e \cap f \neq \emptyset$

Úloha největší párování

Vyrobíme si z grafu síť, přidám zdroj a stok k levé a pravé paritě a všem hranám dám kapacitu jedna a najdeme celočíselný tok

Párování pak bude odpovídat hranám původního grafu s $f=1$

Bijekce mezi toky a párováními, která zachovává velikost


Věta: Pokud $\forall e \in E: f(e) \in {0,1}$ pak F.F v $O(nm)$

Důkaz podle toho kolik se přidá v iteraci a kolik stojí jedna iterace

Čas $O(n'm') = O((n+2)(n+m)) = O(nm)$

> Umí se $O(\sqrt{n} m)$, ale to si nebudeme ukazovat


Definice: čístý tok $f^\star$ k toku $f$:

$f^\star (uv) := f(uv) - f(vu)$


Vlastnosti:

1. $f^\star (uv) := - f^\star (vu)$
2. $f^\star (uv) \leq c(uv)$ ...analogicky obráceným směrem
3. $\forall v$ t.ž. $f^\delta(v) = 0$ pro $f^\delta(v):= \sum_{uv \in E} f^\star (uv)$

Lemma:

$\forall$ funkci $g: E \mapsto \mathbb{R}$ splňující předchozí vlastnosti $\exists f$ tok $: g = f^\star$

D§kaz:

* BÚNO $g(uv) \geq 0$
* f(uv) := g(uv)$ a $f(vu) := 0$ a to funguje

$r(uv) = c(uv) - f^\star (uv)$

## Dinicův algoritmus

> 25.10.2021

Zavedeme si síť rezerv a pomocí toku v ní budeme zlepšovat ten původní

**Lemma** o zlepšování:

Nechť $f$ je tok v síti $S$ a $g$ je tok v síti rezerv $R(S,f)$. Pak $\exists$ tok v S t.ž. $|f'| = |f| + |g|$.

Jde sestrojit v čase $O(m)$

*Důkaz:*

> Připomenutí $f^\star(uv) = f(uv) - f(vu)$

$f'^\star = f^\star + g^\star$

Pak se to ukáže zdefinice

Hvězdičkově se s tím dobře pracuje

> Dinicův algoritmus je o hledání kompromisu mezi přidáváním triviálního toku a přidáním maximálního toku

Definice:

Tok $g$ je **blokující** $\equiv \forall P$ cesta ze $z$ do $s$ $\exists e \in P: g(e) = c(e)$

Nelze ho zlepšit po směru

Pročištěná síť - každá hrana a vrchol leží na cestě do stoku

**Dinicův algoritmus:**
1. &nbsp; $f \gets 0$
2. &nbsp; Opakujeme:
3. &nbsp; &nbsp; $R \gets $ sít rezerv a vymaže nulové
4. &nbsp; &nbsp; Pročitstíme $R$
5. &nbsp; &nbsp; $l \gets$ délka nejkratší cesty v $P$, pokud $\infty$ skončíme
6. &nbsp; &nbsp; $g \gets$ blokující tok v $R$
4. &nbsp; &nbsp; Zlepšíme $f$ pomocí $g$

**Lemma:**

Když se zastavíme, tak máme maximální tok

**Čištění sítě:**
1. &nbsp; BFS $\rightarrow$ rozdělení do vrstev
2. &nbsp; Smažeme vrstvy za spotřebičeme
3. &nbsp; Smažeme zpětné hrany nebo hray uvnitř vrstvy
4. &nbsp; $F$ fronta $\gets \{ \ v \ |\ deg^{out} v = 0 \ and \ v \neq s \ \}$
4. &nbsp; Dokud $F \neq null$:
5. &nbsp; &nbsp; Vezmeme $v$ z $F$
6. &nbsp; &nbsp; Smažeme $v$ a hrany do něj
7. &nbsp; &nbsp; Klesne-li nějaký $deg^{out}$ na 0, přidáme ho do $F$


**Hledání blokujícího toku ve vrstevnaté síti:**

1. &nbsp; $g \gets 0$
2. &nbsp; Dokud $\exists P$ cesta ze $z$ do $s$:
3. &nbsp; &nbsp; $\epsilon \gets$ min $c(e) - g(e)$
4. &nbsp; &nbsp; $\forall e \in P$ g(e) \gets g(e) + \epsilon$
5. &nbsp; &nbsp; Kdykoliv je $g(e) = c(e)$ smažeme hranu
6. Dočistím síť

Jak složitá je jedna fáze algoritmu?

Sestrojení sítě rezerv, smazání nulové rezervy, nalezení nejkratší cesty a číštění sítě je $O(m)$

Hledání blokujícího toku - ve whilu je to bez čištění $O(n)$
to čištění je $O(m)$ celkem

Hledání blokujícího toku je tedy $O(nm)$

Jedna fáze je tedy $O(nm)$

Kolik ale může být fází?

Vychází z toho, že $l$ nikdy neklesá a naopak se vždy zvedá o 1 - počet fází je tedy nejvýše $n$

Celkově tedy trvá $O(n^{2}m)$

Musíme ještě dokázat to neklesání

[...](https://kam.mff.cuni.cz/~mares/video/zs2122/ads2/04-dinic.mp4)


## Goldbergův algoritmus

Vlna v síti - porušuje Kirhofa, tak že stačí aby přebytek vrcholu byl nezáporný

Operace převádění přebytku

Myšlenka zavedeme výšky a pak převádíme přebytky pouze dolů

Algoritmus se bude dívat, jestli se může zbavit přebytku a buď se ho zbaví a nebo se zvýší

> 11.2021

**Goldbergův algoritmus:**
1. &nbsp; $\forall v : h(v) \gets 0$; $h(z) \gets n$
2. &nbsp; $\forall e : f(e) \gets 0$; $\forall zv \in E : f(zv) \gets c(zv)$
3. &nbsp; Dokud $\exists u \neq z,s: f^\Delta(u) > 0$
4: &nbsp; &nbsp; Pokud $\exists uv \in E$: $f(uv) > 0, h(u) > h(v):
5. &nbsp; &nbsp; &nbsp; Převedeme po $uv$
6. &nbsp; &nbsp; Jinak:
7. &nbsp; &nbsp; &nbsp; $h(u) \gets h(u) + 1$

**Invariant A:**

* $f$ je vlna
* $\forall v : h(v)$ neklesá
* $h(z) = n, h(s) = 0$
* $\forall v \neq z: f^\Delta(v) \geq 0$

Důkaz vcelku triviální

**Invariant S:**

Spád $r$ je prostě jen rozdíl výšek přilehlých vrcholů

Pokud $r(uv) > 0$ pak $h(u) - h(v) \leq 1$

**Lemma k:**

Když se algoritmus zastaví $f$ je maximální tok

*  Je to tok

Rozdíl mezi vlnou a tokem jsou Kirchhoffovy zákony je v přebytkách \
Když se ale algo zastaví, tak jsou přebytky jen ve zdroji a stoku

* není-li $f$ maximální, existuje nenasycená cesta $z \rightarrow s$

Cesta překonává spád $n$, má maximálně $n-1$ a tím pádem $\exists$ hrana se spádem $> 1$ a to je spor

> Těžší je ale dokázat konečnost

**Invariant C:**

Pokud $f^\Delta(u)>0$ pro $u\neq z,s$: pak $\exists$ nenasycená cesta z $u$ do $z$

**Invariant V:**

$\forall v : h(v) \leq 2n$

**Lemma Z:**

Počet zvednutí je nejvýše $2n^2$

**Důkaz Inv. C:**

$f^\Delta(u)>0$

$A:= \{ v \ | \ \exists \text{ nenasycená cesta z } u \text{ do } v \}$

Nyní ukáži, že v $A$ je i zdroj

$$\sum_{v \in A} f^\Delta(v) \leq 0$$

Aspoň jeden vrchol má tedy záporný přebytek... no a to může mít jen zdroj

Teď tedy ke konečnosti

Převedení po hraně $uv$ je buď nasycené a nebo nenasycené a to podle toho, jestli rezerva klesne na $0$ nebo přebytek klesne na $0$ (může se stát obojí a pak je to nasycené)

A teď to spočítám

**Lemma S:**

Celkový počet nasycených převedení $\leq nm$

Uvažme jednu hranu a po té se to stane nejvýše $n$-krát

To vidíme z toho, že aby se převedlo víckrát po sobě, tak se $u$ alespoň dvakrát zvedne \
No a to z Invariantu $v$ nastane nejvýše $n$-krát

Co ale nenasycená převedení?

**Lemma N:**

\# nenasycených převedení $O(n^2m)$

Potenciálový argument

$$\Phi := \sum_{v \neq z,s : f^\Delta(v)>0} h(v)$$

* $\Phi \geq 0$
* $\Phi_{start} = 0$
* zvednutí zvýšší potenciál o 1 - celkově potenciál naroste o $2n^2$
* syté převedení zvedne potenciál nejvýše o $2n$ a tedy celkem $2n^2m$
* nenasycené převedení potenciál snižuje - rozborem případů je delta menší nebo rovno $-1$

Takže protože je potenciál vždy nezáporný, operace které známe zvyšují potenciál jenom trochu a z toho víme kolik může být operací, který potenciál snižují

### Implementace

$S :=$ seznam $v \neq z,s: f^\Delta(u)>0$

Pro každý vrchol $\forall H(v) :=$ seznam hran s kladnými rezervami a spádem alespoň 1 \
To si můžu pěkně udržovat až na zvednutí, to je $O(n)$

* Výběr je $O(1)$
* Převedení je $O(1)$
* Zvednutí je $O(n)$

Z toho je to celkově $O(n^2m)$

[...](https://kam.mff.cuni.cz/~mares/video/zs2122/ads2/05-goldberg.mp4)

Příště si ukážeme, že se to dá na $O(n^3)$

> 08.11.2021

**Lemma:**

Goldbergův algoritmus je s výběrem nejvyššího vrcholu $O(n^3)$ nenasycených převedení

*Důkaz:*

Opět potenciálem, $H$ nejvyšší výška vrcholu s přebytkem

To se v průběhu buď zvýšší nebo sníží o 1

A zvednout $H$ můžu jen $O(n^2)$ krát, tedy i snížit (a pak mám jednu poslední fázi)

Celkový počet změn je tedy $O(n^2)$ a tedy i celkový počet fází

A počet nenasycených převedení během jedné fáze je nejvýše $n$

Dokonce se dá dokázat, že #NP je $O(n^2\sqrt{m})$



> # Odsud je to pořádně už jen v souhrnu

# Algebraické algoritmy

## Rychlá Fourierova transformace

### Úvodní povídání o polynomech

$P(x) := \sum_{j=0}^{n-1} p_j \cdot  x^j$

$n$ - velikost polynomu

normalizace: $p_{n-1}$ je nenulový a stupeň $deg(p) := max \ j: p_j \neq 0$

Nulový polynomy má $deg$ $-1%

#### Násobení polynomů

$$P(x) \cdot Q(x) = (\sum p_j \cdot x^j) (\sum q_k \cdot x^k) =$$

$$=\sum p_j q_k x^j x^k = \sum^{m+n-2}_{t=0}\left(\sum_{j=0}^t p_j q_{t-j}\right) x^t$$

Stupeň $P \cdot Q$ je součet stupňů $P$ a $Q$

Násobení má složitost $O(n^2)$

> koeficienty se dají představit jako překroucený skalární součin - konvoluce

Rovnost polynomů? 

* $\equiv$ identická - stejné koeficienty po normalizaci
* reálné funkce $\forall x : P(x) = Q(x)$

**Lemma:**

Nechť $P,Q$ jsou polynomy stupně max $d$ a $x_0, \cdots, x_1$ navzájem různá čísla. Potom

$\forall j: P(x_j) = Q(x_j) \implies P \equiv Q$

**Lemma:**

Nechť $P$ je polynom stupně $d \geq 0$

Potom existuje nejvýše $d$ čísel $a$ t.ž. $P(a) = 0$

$R(x_j) = P(x_j) - Q(x_j) = 0 \implies R \equiv 0 \implies P \equiv 0$

---

$P$ je polynom velikosti $n$

Pevně zvolíme $x_0, \cdots, x_{n-1}$

$(p_0, \cdots, p_{n-1}) \rightarrow (p(x_0), \cdots, p(x_{n-1}))$

> tzv. z koeficientů udělám graf

Teď už se nám začíná rýsovat plán

1. Doplníme $P,Q$ $n/2$ koeficienty
2. Zvolíme $x_0, \cdots, x_{n-1}$
3. Sestrojíme grafy
4. Po složkách vynásobíme grafy
5. Najdeme koeficienty $R$

Ale 3. a 5. je v $O(n^2)$

Takže já si 3. udělám tak, že si $x$ vyberu šikovně

A chceme použít rozděl a panuj

BÚNO $n=2^k$

Požadavek na párování $x$ : $x_j = -x_{n/2 + j}$

$P(x) = p_0 \cdot x^0 + p_2 \cdot x^2 + \cdots p_{n-2} x^{n-2} + p_1 \cdot x^1 + p_3 \cdot x^3 + \cdots p_{n-1} x^{n-1}$

A to můžu vyjádřit jako $S(x^2) + x \cdot L(x^2)$

$P(-x_j) = S(x_j^2) - x_j L(x_j^2)$

A tedy jsme převedli vyhodnocení $P$ velikosti $n$ v $n$ bodech na vyhodnocení $L,S$ v $\frac{n}{2}$ bodech

$T(n) = 2T(\frac{n}{2}) + \Theta(n)$

$T(n) = \Theta(n \cdot \log n)$

Ale tenhle algoritmus nám rozbíjí párování \
To ale zachráníme komplexními čísly

> Odbočka ke komplexním číslům

$e^{\frac{2k\pi\cdot i}{n}}$ odpovídá bodu na jednotkové kružnici v komplexní rovině

Číslo $\omega$ je primitivní $n$-tá odmocnina jestliže $\omega^0 = 1$ a na $1$ až na $n-1$ jsou různé od $1$

Pozorování: $e^{\frac{2k\pi\cdot i}{n}}$ je primitivní, $e^{-\frac{2k\pi\cdot i}{n}}$ (komplexní sdružení) také

1. $\omega^0, \cdots, \omega^{n-1}$ jsou různé
Kdyby opakování nastalo, tak se podívám na podíl a to mi říká, že tam byla už jednička

2. Pokud $n$ je sudé, pak $\omega^{\frac{n}{2}} = -1$
To platí z toho, že odmocnina z $1$ je buď $1$ nebo -1...

### Záchrana algoritmu

Volíme $x = (\omega^0, ..., \omega^{n-1})$

Ty $x$ tvoří páry, protože $\omega^{\frac{n}{2}+j} = \omega^{\frac{n}{2}} \cdot \omega^{j} = - \omega^j$

Navíc dostaneme mocněním na druhou posloupnost stejného typu

**FFT:**

Vstup je $n=2^k$ (velikost vstupu), $\omega = \sqrt[n]{1}$, vektor funkčních hodnot $(p_0, \cdots, p_{n-1})$ \
Výstip je $(y_0, \cdots, y_{n-1})$  t.ž. $y_j = P(\omega^j)$

1. Pokud $n=1$, vrátíme $y_0 = p_0$ 
2. Dvě rekurzivní volání \
$(s_0, \cdots, s_{\frac{n}{2}-1}) \gets FFT(\frac{n}{2}, \omega^2, (p_0, p_2, \cdots, p_{n-2}))$ \
$(l_0, \cdots, l_{\frac{n}{2}-1}) \gets FFT(\frac{n}{2}, \omega^2, (p_1, p_3, \cdots, p_{n-1}))$
3. Pro $j = 0, \cdots, \frac{n}{2} - 1$
4. &nbsp; $y_j \gets s_j + \omega^j + l_j$ a $y_{\frac{n}{2} + j} \gets s_j - \omega^j + l_j$

> Strana 399 v průvodci

**DFT** je lineární zobrazení

Definované jako sumou...

Dá se to tedy zapsat jako násobení maticí

Hledáme inverzi

Co když $\omega$ vynásobíme $\overline{\omega}$... podíváme se na $jk$ pozici a tam je $\omega^{t\cdot(j-k)}$ a pak to sečtu jako geometrikou řadu

Ta matice tedy bude vypdat tak, že má na diagonále $n$ a všude jinde $0$

**Důsledky:**

* $\omega^{-1} = \frac{1}{n} \cdot \overline{\omega}$

* To snadno spočítáme přes FFT a nakonec vydělíme $n$

Z toho máme násobení polynomů v $\Theta(n \log n)$

Dá se z toho udělat algoritmus na násobení čísel

# Hradlové sítě

# Geometrické algoritmy

Úvodní úloha: 

### Ohraničit jabloně co nejkratším plotem

Pozorování

* může mít jenom konvexní úhly, protože jinak by to šlo zkrátit z trojúhelníkové nerovnosti 
* je to $n$-úhelník, protože zaoblená hrana to jen prodlouží

Nápad se skenováním (posouváním přímky) zleva doprava a přepočítáváním nových úseček

Zatím budu předpokládat, že žádné dva body nejsou nad sebou

Algoritmus bude rozlišovat dolní a horní obálku

1. Setřídíme body podle x-ové souřadnice, označíme je b1, . . . , bn. 
2. Vložíme do horní a dolní obálky bod b1: H ← D ← (b1). 
3. Pro každý další bod b = b2, . . . , bn: 
4. Přepočítáme horní obálku: 
5. Dokud |H| ≥ 2, H = (. . . , hk−1, hk) a úhel hk−1hkb je orientovaný doleva: 
6. Odebereme poslední bod hk z obálky H. 
7. Přidáme bod b na konec obálky H. 
8. Symetricky přepočteme dolní obálku (s orientací doprava). 
9. Výsledný obal je tvořen body v obálkách H a D.

Jak následně rozhodovat o orientaci úhlů (napravo a nalevo) - podívám se ba determinant roznásobení vektorů úseček

### Najít souřadnice všech průsečíků úseček

To může trvat až kvadraticky, protože průsečíků může být kvadraticky mnoho

Normálně se to dá tedy hledat tak, že budu hledat průsečík každé dvojice

Ale většinou máme menší počet a proto najdeme lepší způsob

Opět použijeme zametání roviny a budeme plánovat události podle sousednosti přímek

Algoritmus si bude pamatovat vstup, průřez - to jsou úsečky proťaté zametací přímkou a kalendář událostí

1. Inicializujeme průřez P na ∅.
2. Do kalendáře K vložíme začátky a konce všech úseček.
3. Dokud K není prázdný:
4.  Odebereme nejvyšší událost. 
5.  Pokud je to začátek úsečky: zatřídíme novou úsečku do P.
6.  Pokud je to konec úsečky: odebereme úsečku z P. 
7.  Pokud je to průsečík: nahlásíme ho a prohodíme úsečky v P.
8.  Přepočítáme naplánované průsečíkové události v okolí změny v P (nejvýše dvě odebereme a dvě nové přidáme).

Jak to naimplementovat? 

Kalendář událostí je BVS
Průřez bude taky BVS s úsečky jako klíči

Složitost $O((n+p) \cdot \log n)$

### Voroného diagram

Motivace s poštami

Voroného diagram pro množinu bodů neboli míst x1, . . . , xn ∈ R2 je systém oblastí B1, . . . , Bn ⊆ R2 , kde Bi obsahuje ty body roviny, jejichž vzdálenost od xi je menší nebo rovna vzdálenostem od všech ostatních xj

Nejbližší bod v rovině 
Dokážeme převádět na lokalizaci bodu v síti mnohoúhelníků

Voroného diagram má lineární kombinatorickou složitost. Tím myslíme, že diagram pro $n$ míst obsahuje $O(n)$ vrcholů, hran i stěn.

Rovinný graf má $e\leq 3v - 6$ ...

Zametání pro lokalizaci

Pamatování pásů

Stačí nám změny - perzistentní datová struktura

Semi-perzistentní vyhledávací strom

$O(n)$ událostí $\rightarrow O(n)$ operací $\rightarrow O(n \log n)$ prostoru i času

* Build $O(n \log n)$
* Prostor $O(n \log n)$
* Dotaz $O(\log n)$

# NP úplnost

## Co je efektivní a co ne?

## Rozhodovací problém

Rozhodovací problém (zkráceně problém) je funkce z množiny ${0, 1}^∗$ všech řetězců nad binární abecedou do množiny ${0, 1}$.

### Bipartitní párování

432 průvodce

## Převádění problémů

### Pohled jako na relaci

### Příklady převodů

#### Klika v grafu a Nezávislá množina

Klika - Hledáme v grafu podgraf, který je úplný graf na $k$ vrcholech

Nezávislá - Množina vrcholů mezi kterými není hrana

To se na sebe převede triviálně doplňkem

#### Problém SAT
