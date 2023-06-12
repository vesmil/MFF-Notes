# Kombinatorika a grafy

[Stránka přednášky](https://kam.mff.cuni.cz/~balko/kg12122/KG1.html), [Dobré poznámky](https://slama.dev/poznamky-z-prednasky/kombinatorika-a-grafy-i/)

> 1. Přednáška

## Odhad faktoriálu

**Špatný odhad:** $n^\frac{n}{2} ≤ n! ≤ n^n$

**Dobrý odhad:** $e \cdot \left(\frac{n}{e}\right)^n \leq n! \leq e \cdot n \cdot \left(\frac{n}{e}\right)^n$

*Důkaz:*  Horní odhad indukcí $n! \leq n \cdot e \cdot (n-1) \cdot \left(\frac{n-1}{e}\right)^{n-1} = n \cdot e \cdot \left(\frac{n}{e}\right)^{n} \cdot e \cdot \left(\frac{n-1}{e}\right)^{n}$ a dolní z $n(n-1)!\geq n \cdot e \cdot \left(\frac{n}{e}\right)^n $
Pro horní stačí když $e \cdot \left(\frac{n-1}{e}\right)^{n} \leq 1$ a to pomocí $1 + x \leq e^x$  (dvakrát zderivujeme a v $0$ je minimum) a dolní $e \cdot \left(\frac{n-1}{n}\right)^{n-1} \geq 1 $

**Stirlingův vzorec:** $n! \sim \sqrt{2\pi n} \cdot \left(\frac{n}{e}\right)^n$

## Odhad kombinačních čísel

**Špatný odhad #1:**  $(\frac{n}{k})^k \leq \binom{n}{k} \leq n^k$
**Špatný odhad #2:**  $(\frac{2^n}{n+1})^k \leq \binom{n}{k} \leq 2^n$

**Dobrý odhad:** $\frac{2^{2m}}{2\sqrt{m}} \leq \binom{2m}{m} \leq \frac{2^{2m}}{\sqrt{2m}}$

*Důkaz:* $P=\frac{1 \cdot 3 \cdots (2m - 1)}{2 \cdot 4 \cdot (2m)} \cdot \frac{2 \cdot 4 \cdot (2m)}{2 \cdot 4 \cdot (2m)} = \frac{(2m)!}{2^{2m}(m!)^2} = \frac{\binom{2m}{m}}{2^{2m}}$ a chceme $\frac{1}{2\sqrt{m}}\leq P \leq \frac{1}{\sqrt{2m}}$. 

$\left( 1 - \frac{1}{2^2} \right)\left( 1 - \frac{1}{4^2} \right)\cdots \left( 1 - \frac{1}{(2m)^2} \right) = \left(\frac{1 \cdot 3}{2 \cdot 2} \right) \left(\frac{3 \cdot 5}{4 \cdot 4} \right) \cdots \left( \frac{(2m-1)(2m+1)}{(2m)^2} \right) = P^2(2m+1) \leq 1$ 

Máme tedy $P^2 < \frac{1}{2m}$ a  druhý se udělá $\left( 1 - \frac{1}{3^2} \right)\left( 1 - \frac{1}{5^2} \right)\cdots \left( 1 - \frac{1}{(2m-1)^2} \right) = \frac{1}{2 \cdot 2m \cdot P^2}$

**Stirlingův vzorec:** $\binom{2m}{m} \sim\frac{2^{2m}}{\sqrt{\pi m}}$

## Náhodné procházky

Kolikrát se vrátíme do počátku při nekonečném chození náhodně dopředu a dozadu?

Identifikátor $I_{S_2n}$, že po $2n$ krocích v počátku má pravděpodobnost $P(I) = \binom{2n}{n}/2^{2n}$
Střední hodnota návrtů do počátku je pak $\sum I_{S_{2n}}$ a tedy z odhadu $\geq \sum_{i=1}^{\infty} \frac{1}{2\sqrt{i}}$

> 2. Přednáška

## Vytvořující funkce

Mocninná řada $a(x) = a_0 + a_1 x^1 + \cdots$

$(1,1, \cdots , 0, \cdots) = 1 + x + \cdots + x^n = \frac{1-x^{n+1}}{1-x}$
$(1,1,1, \cdots) = 1 + x + \cdots  = \frac{1}{1-x}$
$(\binom{n}{0},\binom{n}{1},\binom{n}{2}, \cdots) =  (1+x)^n$

Z posloupností umíme udělat funkci a pokud členy nerostou rychle, tak to umíme i obráceně
Pokud $\forall i \exists K: |a_i|\leq K^i$, pak pro všechna $x\in (-\frac{1}{K},\frac{1}{K})$ řada konverguje absolutně a navíc vytvořující funkce na $\epsilon$ okolí $0$ určuje koeficienty $a_i$

**Operace **- Součet, násobek, posuny, derivace, integrování, konvoluce

### Fibonacci - explcitní vzorec

Zavedeme $F(x) = F_0 + F_1 x + \cdots$​ , potom $F_{n+2} = F_{n} + F_{n+1}$​  přenásobíme, sečteme, vyjádříme $F(x)$, použijeme parciální zlomky a zjistíme jaké změny jsme na funkci použili

Respektive $\sum_{n\geq0}F_ {n+2} \cdot x^n = \cdots$  a tedy $\frac{F(x) - F_0 - F_1 x}{x^2} = \cdots$
$F(x) = \frac{x}{\left(1 - \frac{1 + \sqrt5}{2}\right)\left(1 - \frac{1 - \sqrt5}{2}\right)} = \frac{\frac{1}{\sqrt5}} {\left(1 - \frac{1 + \sqrt5}{2}\right)} - \frac{\frac{1}{\sqrt5}} {\left(1 - \frac{1 - \sqrt5}{2}\right)}$ a tedy  $F_n = \frac{1}{\sqrt5} \left[ \left(\frac{1 + \sqrt5}{2}\right)^n - \left(\frac{1 - \sqrt5}{2}\right)^n \right]$

<details > 
	<summary>Rozepsané víc</summary>
$$
\sum_{n\geq0}F_ {n+2} \cdot x^n = \sum_{n\geq0} F_{n}  \cdot x^n+ \sum_{n\geq0} F_{n+1} \cdot x^n \\
\frac{F(x) - F_0 - F_1 x}{x^2} = \frac{F(x) - F_0 }{x} + F(x) \\
F(x) = \frac{x}{1 - x - x^2} = \frac{x}{\left(1 - \frac{1 + \sqrt5}{2}\right)\left(1 - \frac{1 - \sqrt5}{2}\right)}\\  
\text{Z parciálních zlmoků: }
\frac{\frac{1}{\sqrt5}} {\left(1 - \frac{1 + \sqrt5}{2}\right)} - \frac{\frac{1}{\sqrt5}} {\left(1 - \frac{1 - \sqrt5}{2}\right)} 
\\ \\ \text{Z provedených operací: }
F_n = \frac{1}{\sqrt5} \left[ \left(\frac{1 + \sqrt5}{2}\right)^n - \left(\frac{1 - \sqrt5}{2}\right)^n \right]
$$
</details>
> 3. Přednáška

### Zobecněná binomická věta

Nadefinujeme si $\binom{r}{k} = \frac{r\cdot (r-1) \cdots (r-k + 1)}{k!}$ 

Funkce $(1+x)^r$ je vytvořující funkce $(\binom{r}{0},\binom{r}{1},\cdots) $ a $\sum_{i \geq 0} \binom{r}{i}x^i$ konverguje pro $x\in(-1,1)$

*Důkaz:* Aplikujeme Taylorův rozvoj na $(1 + x)^r$ pro $x=0$ a funkce je rovna svému Taylorovému rozvoji na okolí $a$ pokud existují všechny derivace, součet řady konverguje a zbytky jdou k 0.

*Důsledek:* $\forall x \in (-1,1) \text{ platí } \frac{1}{(1-x)^n} = \sum_{i=0}^\infty \binom{n+i-1}{n-1} x^i$, protože:
$$
(1-x)^{-n} = \sum_{i\geq 0} \binom{-n}{i}(-x)^i = \sum_{i\geq 0} \frac{(-n)(-n-1)\cdots(-n-i+1)}{i!}(-1)^i x^i= \\
= \sum \frac{n(n+1)\cdots(n+i-1)}{i!}x^i = \sum \binom{n+i-1}{i}x^i =  \sum \binom{n+i-1}{n - 1}x^i
$$

### Catalanovo číslo

 $b_n:=$ # bin. stromů na $n$ vrcholech odpovídá $\boldsymbol{n}$-tému Catalanovu číslu a tedy $b_n = \frac{1}{n+1}\binom{2n}{n}$

> Catalanovo číslo je také počet triangulací, správných uzávorkování, ... 

*Důkaz:* Pro všechna* $b$ platí $b_n = b_0 \cdot b_{n-1} + b_1 b_{n-2} + \cdots + b_{n-1}b_0$, to připomíná násobení vytvořujících funkcí a tedy pravá strana je koeficient u $x^{n-1}$ v $b(x)\cdot b(x)$ a tu když posuneme doprava a přičteme jedničku získáme zase původní posloupnost - $b(x) = 1 + xb^2(x)$. 

$b(x)_{1,2} = \frac{1\pm \sqrt{1-4x}}{2x}$, ale "$+$" diverguje a pak $b(x) = \frac{1-\sum \binom{\frac{1}{2}}{k}(-4)^k x^k}{2x} = \sum_{k= 1}^\infty - \frac{1}{2} \binom{\frac{1}{2}}{k}(-4)^k x^{k-1}$

Koeficient pak $b_n =-\frac{1}{2}(-4)^{n+1} \binom{\frac{1}{2}}{n+1} = \cdots = 2^n \cdot \frac{1 \cdot 3 \cdots (2-1)}{(n-1)!} \cdot \frac{n!}{n!} = \frac{1}{n+1} \frac{2n!}{n!n!} = \frac{1}{n+1}\binom{2n}{n}$

#### Rozklad čísel na sčítance

Všechna $n$ lze rozložit na $k$ kladných uspořádaných sčítanců $\binom{n-1}{k-1}$ způsoby ($k-1$ přepážek...)
Počet uspořádaných rozkladů $n$ na kladné sčítance je roven $\sum_{k=1}^n \binom{n-1}{k - 1} = 2^{n-1}$ a funkce $\frac{1-x}{1-2x}$

Jak je to s neuspořádanými? Známe snadnou vytvořující funkci posloupnosti $p(x) = \sum p_n x^n$.
A to  je $p(x) = (1+ x + x^2 + \cdots) (1 + x^2 + x^4 + \cdots)\cdots$ 


> 4. Přednáška

## Konečné projektivní roviny

Velmi pavidelný množinový systém $(X,\mathcal{P})$ kde v $X$ jsou body (prvky) a $P$ přímky (podmnožiny)

1. $\forall P,Q: \exists! x : P \cap Q = \set{x}$ 
2. $\forall x,y: \exists! P : x,y  \in P$
3. $C \subseteq X, |C| = 4: |P \cap C| \leq 2$

Všechny přímky mají **stejný počet bodů** přes to, že pro dvě existuje bod, který na nich není (buď z obecné přímo a nebo musím $\overline{ac}$ a $\overline{bd}$), díky tomu si můžu nadefinovat $\phi: P \rightarrow Q$, tak. že vezmu $x \notin P,Q$ a $\phi(y) = \overline{xy} \cap Q$,to je prosté a tedy $|P| \leq |Q|$, analogicky $Q \rightarrow P$

**Řád roviny**  je $n:= |P| - 1$

* Každým bodem $n + 1$ přímek, protože najdeme $P: x\notin P$ a $\overline{xp_k}$ je $n+1$ přímek (všechno)
* $|X|  = n^2 + n + 1$  - začneme tradičně s $a \notin \{x_1, \cdots, x_{n+1}\} $ a $\overline{ax_i} \setminus \set{a}$ má $n$ bodů, Následně $\overline{ax_i} \cap \overline{ax_j} = \set{a}$ a protože každý $x_i$ leží na $\overline{ax_i}$, tak celkem $n(n + 1) + 1$
* $|\mathcal{P}| = n^2 + n + 1$ - z duality viz. níže

### Dualita konečných projektivních rovin

Převod z přímek na body (snadné) a z bodů na přímky (všechny přímky s $x$...) - zachovává KPR

*Důkaz:* Ověřením axiomů (spor, snadné a $\set{\overline{ab},\overline{bc},\overline{cd},\overline{ad}}$)

> Na přednášce byly zajímavosti o existenci KPR - mocniny prvočísla?

Víme alespoň, že pokud existuje algebraické těleso o $n$ prvcích, tak existuje KPR řádu $n$

> 5. Přednáška

###  Konstrukce KPR z algebraického tělesa

Vezmu to těleso $\mathbb{K}^3$, body jsou ekvivalenční třídy (přenásobení $\alpha$) - reprezentanti s poslední nenulovou složkou $1$ a tedy $(x,y,1),(x,1,0),(1,0,0)$ a tedy $n^2 + n + 1$ a na závěr vytvořím přímky $\mathcal{P}$ tak, že $P_{a.b.v} = \set{\{x,y,z\}:ax + by + ct = 0}$ jako $(x,y,t)$

*Ověříme axiomy:*

* Protože $(a_1,b_1,c_1)$ a  $(a_2,b_2,c_2)$ lineárně nezávislé, tak dim. jádra $1$ a analogicky dvojka
* $(1,0,0),(0,1,0),(0,0,1),(1,1,1)$ jsou po třech lineárně nezávislé

## Latinské čtverce

Tabulka $n\times n$, kde se čísla neopakují v řádku ani ve sloupci

**Ortogonální** pokud každou dvojici čísel najdu v těch tabulkách na nějakém indexu
Tento index je určený jednoznačně (z počtu možných dvojic)

Permutace mi LČ zachovává - BÚNO první řádek $1,2, \cdots$ a je-li $L \perp L'$, pak $\pi(L) \perp L'$

Z toho získám, že počet navzájem ortogonálních čtverců řádu $n$ je nanejvýš $n-1$
*Důkaz:* BÚNO na prvním $1, 2, ...$ a dívám se na pozici $(2,1)$ a tam $2, \cdots, n$

$\exists$ KPR řádu $n\geq 2$ $\Leftrightarrow \exists$ $n-1$ navzájem ortogonálních čtverců řádu $n$

$\Leftarrow$ mám čtverec a k jeho bodům $m_{n,n}$ si přidám body $r, s, l_{n-1}$, do $r$ spojím řádky, do $s$ spojím sloupce a do $\forall l_i$ navedu $\forall j$ políčka $i$-tého latinského čtverce, kde je $j$...
Pak ověřím axiomy - přímky a sloupce budu dělat podle dvojic druhů a $\mathcal{C} = \set{r,s,m_{1,1}, m_{2,2}}$

$\Rightarrow$ zvolíme $\set{r,s,l_1, \cdots, l_{n-1}}$ náhodně, $n$ dalších protínajících $r$ a $s$, a pak z $l_{n-1}$...

> 6. Přednáška

## Toky v sítích

 Síť, velikost toku, omezení kapacitami, Kirchoff... většina je opakování z ADS (kde je to hezčí)

Existence maximálního toku - přes FF z ADS a nebo spojitá funkce na kompaktní množině

Řezy a jejich kapacity, ... maximální tok je roven kapacitě minimálního řezu, proč až později
Elementární řez, každý řez ho obsahuje, každý v inkluzi minimální řez je elementární, tok můžeme měřit elementárním řezem - podle součtu přebytků a přispívání

*Max flow, min cut důkaz* - tok omezený kapacitou - $f(A,B) - f(B,A) \leq \cdots$, 
A kapacita odpovídá toku, protože pokud je tok maximální, tak neexistuje zlepšující cesta...

**Ford-Fulkerson** - dokud existuje zlepšující cesta...
Věta o celočíselnosti - pak je FF konečný, protože vždycky se zlepší alespoň o 1...

> 7. Přednáška

### Königova-Egarváryho

Vrcholové pokrytí... je to NP těžké, ale ne v bipartitních grafech
Tam je velikost vrcholového pokrytí rovna velikosti maximálního párování

Z algoritmu, kde přidáme jednotkové hrany ze $z$ a do $s$ a kapacity původních hran dáme na $|V|$

### Hallova věta

Systém různých reprezentantů je zobrazení $I \rightarrow X$ takové, že $\forall i < I: f(i) \in M_i$ 
Incidenční graf - bipartitní graf s $I$ a $X$ a hranami $x \in M_i$, musí obsahovat párování velikosti $I$

Hallová podmínka říká, že $\exists \text{SSR} \Leftrightarrow$ $\forall J \subseteq I : |\bigcup_{j\in J} M_j| \geq|J|$
$\Rightarrow$ triviálně z prostého zobrazení, pro SSR si zvolíme J a $|\bigcup M_j| \geq |\set{f(j)}|$
$\Leftarrow$ uděláme max. párování a definujeme $A,B$ množiny z hranami s min. řezu a potom hrany z $I \setminus A$ vedou pouze do $B$ a a tedy $\bigcup M_j \subseteq B$. řez má velikost $|A| + |B|$ a HP...
Tedy kapacita řezu je $|I|$ a velikost toku je $|I|$ a máme párování

**Důsledek:**
V každém bipartitním grafu s $\text{deg}(x) \geq deg(y)$, kde $x \in A$ a $y \in B$, existuje párování vel. $|A|$

Důkaz: $k_1 =\min deg(x)$, $k_2 = \max deg(y)$, $Z \subseteq E$ mezi $J$ a $|\bigcup M_j|$
Vím, že platí $k_1 \geq k_2$ a tedy HP platí z $|J|k_1 \leq Z \leq k_2 |\bigcup M_j|$

### Latinské obdelníky

Díky předchozímu víme, že můžeme doplňovat lat. obdélníky na čtverce, prostě tak, že pokud mám více sloupců než řádků, tak ze sloupců povedou hrany do hodnot, které můžu doplnit

> 8. Přednáška

## Míra souvislosti grafu

Hranová souvislost je minimální velikost hranového řezu (nebo 1) a vrcholová analogicky...

Platí $k_e(G) - 1 \leq k_e(G - e) \leq k_e(G)$
 $k_e(G - e) \leq k_e(G)$ platí protože $k_e(G-e) \leq |F| \setminus{\set{e}} \leq |F| = k_e(G)$, kde $F$ je hranový řez
 $k_e(G) - 1 \leq k_e(G - e)$, protože $k_e(G) \leq |F| \cup \set{e} = |F| + 1 = k_e(G-e + 1)$

S vrcholovou při odebrání $e$ obdobně $k_v(G) - 1 \leq k_v(G-e) \leq k_v(G)$
$k_v(G - e) \leq k_v(G)$, protože min. vrcholový řez v $G$ je vrcholový řez i v $G-e$...
$k_v(G)-1\leq k_v(G-e)$, přeformuluji s $H = G-e$ na $k_v(H+e) \leq k_v(H) + 1$
V $H$ existuje vrcholový řez $A$, rozborem případů a jen když $e$ mezi komponenty, pak...

 Důsledek $k_v \leq k_e$, indukcí podle hran $k_v(G)- 1 \leq k_v(G-e) \leq k_e(G-e) = k_e(G) - 1$

**Ford-Fulekrsonova věta:** $k_e(G) \geq t \Leftrightarrow \exists \text{ alespoň } t \text{ hranově disjunktních cest}$
$\Leftarrow$ sporem, takový řez by totiž nemohl přerušit všechny cesty
$\Rightarrow$ pro nalezení těchto cest sestrojím jednotkovou síť, najdu tok a oddělávám cesty

**Mengerova věta:** $k_v(G) \geq t \Leftrightarrow \exists \text{ alespoň } t \text{ vrcholově disjunktních cest}$ 
$\Leftarrow$ analogicky a $\rightarrow$ taky, akorát rozseknu každý vrchol na hranu

> 9. Přednáška

Když $|F| = 1$, tak $F$ je most a když $|A| = 1$, tak $A$ je artikulace, operace podrozdělení hrany...

$G$ je vrcholově 2-souvislý $\Leftrightarrow G \div e$ je vrcholově  2-souvislý
$\Rightarrow$ Pokud je nový vrchol artikulace, tak artikulace musel být i vrchol incidentní s $e$
$\Leftarrow$ Obměnou pokud $G$ není 2-souvislý, tak má artikulaci a podrozdělení nepomůže (nebo $\forall v$...)

$G$ je vrcholově 2-souvislý $\Leftrightarrow$ Lze ho vytvořit z $K_3$ pomocí přidávání a podrozdělení hran
$\Rightarrow$ 2-souvíslý $G$ získáme tak, že k cyklu přidáváme ucha a ukáží, že se to rovná sporem
$\Leftarrow$ Nikdy nevznikne artikulace triviálně...

## Počítání dvěma způsoby

**Cayleyho vzorec** pro počet stromů na $n$ vrcholech je $\mathcal{K}(n) = n^{n-2}$
Budeme prvně počítat počet postupů výroby kořenového stromu, formálně trojice $(T,r,č)$

1. Způsob - V každém stromě s $n$ vrcholy lze kořen zvolit $n$ způsoby a pořadí hran $(n-1)!$
2. Způsob - Postupně budu přidávat šipky do lesa s $n-k$ komponenty, $(k+1)$-ní šipka musí vést z kořene jedné do libovolného vrcholu jiné $(n-k-1)\cdot n$ a tedy $\prod_{k=0}^{n-2}(n-k-1)n$

Kombinace nám dá $n(n-1)!\mathcal{K} = (n-1)!n^{n-1}$ a tedy $\mathcal{K} = n^{n-2}$

1. Způsob - $Z = \mathcal{K}(K_n)\cdot(n-1) = n^{n-2}\cdot(n-1)$ (volba kostry a pak volba hrany pro ní)
2. Způsob - $Z = \binom{n}{2}\cdot K_e(K_n)$ (volba hrany a pak volba kostry, která ji obsahuje)

$n^{n-2}\cdot(n-1) = \binom{n}{2}\cdot K_e(K_n)$, z toho plyne, že $\mathcal{K}_e(K_n) = \frac{n^{n-2}\cdot(n-1)}{\binom{n}{2}\cdot} = 2 \cdot n^{n-3}$ a protože platí $K(G) = K(G-e)+K_e(G)$, tak $n^{n-2} = \mathcal{K}(K_n-e)+2 \cdot n^{n-3}$....

Laplacián je matice, kde  $L_{i,j}:= \begin{cases} 
\deg(v_{i}) & {\mbox{pokud}}\ i=j \\
-1 & \mbox{pokud}\ i\neq j\ {\mbox{a}}\ v_{i}\mbox{ sousedí s }v_{j}\\
0 & {\mbox{jinak}} 
\end{cases}$ 

**Kirchhoffova věta:** $\mathcal{K}(g) = \det (L(G)^{1,1})$ - determinant laplaciánu bez 1.řádku a 1.sloupce

> 10. Přednáška

Systém podmnožin je nezávislý, pokud se množiny navzájem neobsahují

**Sperner:** Každý nezávislý systém v $2^{1,\cdots, n}$ obsahuje $\leq \binom{n}{\left\lceil \frac{n}{2} \right\rceil}$ množin (těsný odhad) a tedy ekvivalentně nejdelší antiřetězec $\mathcal{M}$ v částečném uspořádání má $\binom{n}{\left\lceil \frac{n}{2} \right\rceil}$ prvků

*Důkaz:* nezávislý systém té velikosti existuje, neboť stačí si vzít podmnožiny velikosti $\left\lceil \frac{n}{2} \right\rceil$ a že tam větší není počíáním $Z=|\set{(M,R):M\in \mathcal{M}, R = \mbox{maximální řetezec obsahující } \mathcal{M}}|$

1. Způsob - $Z \leq n! \cdot 1$, protože maximálních řetězců je $n!$ a $|R\cap M| \leq 1$
2. Způsob - $M$ lze doplnit $|M|!(n-|M|)!$ způsoby na max řetězec $Z \leq \sum |M|!(n-|M|)!$

A tedy $1 \geq  \sum \frac{|M|!(n-|M|)!}{n!} =\sum\binom{n}{|M|} = \cdots$ a tedy $|\mathcal{M}| \leq \binom{n}{\left\lceil \frac{n}{2} \right\rceil}$

## Ramseyova teorie

Každý systém obsahuje homogenní podsystém dané velikosti

### Dirichletův princip

Začneme s $n$ krabicemi a $m$ objekty, pokud $n\leq m$, tak alespoň jedna krabice má v sobě dva

Obecněji budem obarvovat $r$ barvami $X$ a pokud $|X| \geq D(n_1, \cdots, n_r, r) = 1 + \sum_{i=1}^r (n_i - 1)$, tak $X$ obsahuje $n_i$ prvků $i$-té barvy, kde $D(\cdots)$ je nejmenší velikost $X$ pro kterou to platí

Na každé party s více než 6 lidmi se buď 3 znají a nebo 3 neznají (existuje $K_3$ stejné barvy) - ez

**Ramsey pro 2 barvy:** počet vrcholů pro červený $K_k$ nebo modrý $K_l$ je $R(k,l) \leq \binom{k+l-2}{k-1}$

Ukážeme indukcí podle $k+l$: začátek $k = 1$ a $l=1$ jde triviálně a ukážeme pro $k \geq 2$ a $l \geq 2$
Z IP víme, že $R(k-1,l) \leq \binom{k+l-3}{k-2}$ a že $R(k,l-1) \leq \binom{k+l-3}{k-1}$

Ukážeme, že $R(k,l) \leq R(k-1, l) + R(k,l-1)$ neboť v grafu o velikosti  součtu náhodně vybereme vrchol a buď má $R(k-1,l)$ červených a nebo $R(k,l-1)$ modrých sousedů.
BÚNO tedy červené a ty obsahují podle IP buď červeně $K_{l-1}$ a nebo modré $K_l$

Pro $K \geq 3$ platí $R(k,k) > 2^{\frac{k}{2}}$

*Důkaz:* $N < 2^{k/2}$ a náhodné 2-obarvení hran $K_N$ Každá z $\binom{n}{2}$ hran má $1/2$ pravděpodobnost... Pak vezmu jev $A_K$ pro $K\subseteq V, |K| = k$, že $K$ je jednobarevný $K_k$. $Pr[A_K] = 2^{1-\binom{k}{2}}$ a chceme ukázat, že pravděpodobnost existence jednobarevného je menší než $1$.
$$
Pr \leq \sum(A_K) = \binom{n}{k} 2^{1-\binom{k}{2}} \leq \frac{N^k}{2^{k/2+1}} \cdot 2^{- \frac{k^2}{2} +\frac{k}{2} - 1} = N^k \cdot 2^{k^2/2}
$$

> 11. Přednáška

Ramseyho číslo pro $p$-tice $R_p(n_1, \cdots, n_r)$ je minimální... pro konečné obarvení množiny $\binom{X}{p}$
Zobecníme myšlenky a budeme postupovat indukcí podle $p$ a $\sum n$

pro $p=1$ je to Dirichlet a pro $p \geq 2$ ... **TODO** to vole nechápu

Každý množina 5 bodů v obecné poloze obsahuje 4 body v konvexní - rozborem

**Erdősova–Szekeresova věta - **existuje nejmenší $ES(k)$ takové, že každá konečná množina s méně než $ES(k)$ body v obecné poloze má $k$ bodů v konvexní poloze

*Důkaz:* Přes $ES(k) \leq R_4(k,5)$ - obarvíme každou čtveřici červeně pokud je v obecné a jinak modře
Potom existuje buď množina červených čtveřic velikosti $k$ a nebo pětice bodů se všemi čtveřicemi modrými

**Nekonečná verze Ramseyho** říká, že pro $p,r \in  \N$ a $r$ obarvení $\binom{\N}{p}$ existuje nekonečná $A \subseteq \N$ t.ž. všechny její $p$-tice mají v daném obarvení stejnou barvu, opět se ukáže indukcí podle $p$

**Kőnigovo lemma** v každém nekonečném konečně větveném stromě je nekonečná větev
Indukcí, že můžu vždy udělat krok do alespoň jednoho vrcholu s nekonečno následníky

Pomocí toho se sporem dá ukázat, že nekonečná R. implikuje konečnou R. přes obarvení jako vrcholy

> 12. Přednáška

## Samoopravné kódy

Abeceda, množina slov délky $n$, Hammingova vzdálenost $d(x,y)$, ...

(Blokový) kód je $C \subseteq \Sigma^n$ (prostě slova s nějakou vlastností, které můžeme použít pro přenos)
$t$ chyb zvládneme opravit, když do vzdálenosti $t$ je od přijatého jenom jenom jeden kód

$(n,k,d)_q$ - délka $n$, velikost abecedy $q$, dimenze ($k=\log_q |C|$), (minimální) vzdálenost $d$

Lze opravit $\leq \left\lfloor \frac{d-1}{2} \right\rfloor$ chyb (triválně) a nelze opravit $\geq \left\lfloor \frac{n-1}{2} \right\rfloor$ chyb (protože $d \leq n$)

**Opakovací kód** - každý poslaný symbol $n$-krát zopakujeme $(n, 1, n)_q$

**Charakteristické vektory přímek KPR** - $(n^2 + n + 1, \log_2 (n^2+n+1),2n)$
Můžeme přidat vektor samých jedniček a nic nezměníme (případně přidat doplňky)

**Hadamardovy kódy** - založený na Hadamardových maticích $\set{1,-1}^{n\times n}$ pro které $H \cdot H^T = I_n$ 
Každé dva řádky se tedy liší na $n/2$ pozicích. Kódy si zvolím podle řádků a jejich mínus násobků.
Parametry $(n, log_2(2n), 2/n)$, Sylvestrova konstrukce...

Kódy jsou ekvivalentní pokud se liší jen v přeházení pozic

Pro jaké parametry existuje kód?
**Kombinatorická koule** se středem $x$ a poloměrem $t$ je množina slov ve vzdálenosti $t$
Je-li kód s $d = 2t + 1$ pak všechny koule jsou disjunktní - důkaz třeba sporem přes trojúhelníkovou...
Počet slov v kouli nezávisí na středu - $V = \sum_{i=0}^t \binom{n}{i}(q-1)^i$

**Hammingův odhad** - pro $(n,k,2t+1)_q$ platí $|C| \leq \frac{q^n}{v(t)}$
Protože víme, že počet slov $\times$ objem koule $=$ počet slov k dispozici

Pokud je ten odhad přesně, tak to je perfektní kód
Triviální příklad je opakovací kód s $q=2$ a lichou délkou

**Gilbertův–Varshamův** pro $(n,k,d)_q$ existuje $|C| \geq \frac{q^n}{v(d-1)}$
Když budeme z množiny slovo odebírat slova a zároveň s nimi ve vzdálenosti $(d-1)$

Lineární kód (rychlé kódování a dekódování) - použijeme konečné těleso a značíme $[n,k,d]_q$
Příklady jsou opakovací nad $\mathbb{Z}_4$, rozšířený z Fanovy a nebo Hadamardovy ze Sylvestrovy konstrukce

> 13. Přednáška

Dimenze lineárního je celé číslo, protože $|C| = q^k$, minimální vzdálenost se dá určit od $0$, a stačí nám jeho báze vel. $|k|$

**Generující matice** kódu $C$ je $M = \Sigma^{k\times n}$ a řádky tvoří bázi příslušného vektorového podprostoru

Skalární součin dvou slov je $\langle x, y \rangle = \sum x_i y_i$

Na základě něj definujeme **duální kód** s **kontrolní maticí** $M^\perp$ - to je jeho ortogonální doplněk původního kódu 
Můžou se s původním  protínat víc než v počátku, ale aspoň platí, že součet dimenzí se posčítá na dimenzi celého

Pomocí kontrolní matice se dá zapsat i původní kód, prostě jako $M^\perp \cdot x = 0$

Kódování lin. kódy - máme matici $M$ BÚNO ve standardní formě a kódové slovo dostaneme z $M^T\cdot Z$

Dekódování lin. kódy - $M^\perp$ má tvar s $-B^T$ a pak $I_{n-k}$ (má $n-k$ řádků), to určuje zobrazení $S$ (**syndrom**)
$S$ je prostý na $B(0,t)$ a tedy pro syndrom existuje i inverzní zobrazení

Hammingovy kódy budou z $I_{2^n-n-1}$ a všech nenulových vektorů z $\mathbb{F}_2^1$ různých od vektorů báze
