> Gregorovy [prezentace](https://kti.mff.cuni.cz/~gregor/logika/) jsou better, tohle je jen výtah

# 1. Přednáška - Úvod

*K čemu to je, historie, doporučená literatura, ...*

**Členění logiky**

* Výroková logika - logické spojky
  	1. řádu - proměnné pro individua, funkční a relační symboly, kvantifikátory
  	2. řádu - proměnné pro množiny individuí (i relace a funkce)
  	3. řádu - proměnné pro množiny množin ...

**Syntax a sémantika...**

**Korektnost a úplnost dokazovacího systému...**

**Paradoxy...**

**Dodatková prezentace o množinách, relacích, stromech, atd.**

# 2. Přednáška - Jazyk

Množina $\mathbb{P}$ je množina výrokových proměnných (prvovýroků) - např. $\{p_0, \cdots, q_0, \cdots \}$

**Jazyk výrokové logiky** nad $\mathbb{P}$ obsahuje proměnné z $\mathbb{P}$ (mimologické symboly), logické spojky a závorky

 Zavedeme také konstantní symboly $\top$ a $\bot$ - definice ...

## Výrokové formule

V. f. (výroky) nad $\mathbb{P}$ jsou dány induktivně:

* Každý prvovýrok (z $\mathbb{P}$) je formule
* Dvě formule dají pomocí logických spojek opět formuli - výčet
* Každá formule vznikne konečnou kombinací prvních dvou pravidel

**Pojmy**: Podformule, množina všech formulí - $VF_\mathbb{P}$, množina všech proměnných ve formuli - $var(\varphi)$

**Konvence zápisu (závorkování)** - Prvně se provede $\neg$. pak  $\vee,\ \wedge$ a nakonec $\rightarrow,\ \leftrightarrow$

**Vytvořující strom výroku** - ...

**Dvouhodnotová logika, pravdivostní tabulky, booleovská funkce** - ...

## Hodnota výroku

Hodnota $\overline{v} ( \varphi )$ při ohodnocení $v$ je dána induktivně podle tabulek...

Výrok $\varphi$ na $\mathbb{P}$ může být 

* Splněn při ohodnocení $v$, pokud $\overline{v}(\varphi )=1$, značíme $v \models \varphi$
* Pravdivý - značíme $\models \varphi$
* Lživý (sporný) - ...

* Nezávislý - ...
* Splnitelný - ...

* Logicky ekvivalentní jinému výroku - ...

## Model jazyka

*Předchozí definice lze převést na terminologii modelů*

**Model jazyka** $\mathbb{P}$ je ohodnocení $v: \mathbb{P} \rightarrow \{ 0,1 \}$

**Třída všech modelů** $M(\mathbb{P})$

Pokud v modelu $v$ platí, pak $v$ je model výroku, $M^\mathbb{P}(\varphi)$ je třída všech modelů výroků

Pravdivý platí v každém modelu, lživý nemá model, ...

### Univerzálnost spojek

Můžeme zavést spojku pro libovolnou Booleovu funkci např. $\uparrow, \downarrow$ (NAND a NOR)

Univerzální množina zvládne reprezentovat každou Booleovskou funkci např. $\{ \neg, \wedge, \vee\}$ nebo $\{\neg, \rightarrow\}$

## CNF a DNF

**Literál** je prvovýrok nebo jeho negace ($p^0$ je $\neg p$, $p^1$ je $p$ a $\overline{l}$ je opačný k literálu $l$)

**Klauzule** je disjunkce literálů - prázdná je $\bot$
**Elementární konjunkce** je konjunkce literálů  - prázdná je $\top$

**CNF** je konjunkce klauzulí
**DNF** je disjunkce elementárních konjunkcí

### Převod tabulkou

DNF - když je to výrok v tabulce pravdivé, tak mu bude odpovídat konjunkce odpovídajících prvovýroků
CNF - když je to výrok v tabulce lživé, tak mu bude odpovídat jedna klauzule negací prvovýroků

Funguje to vždycky, protože hodnota výroku závisí pouze na ohodnocení jeho proměnných

### Převod úpravami

Nahrazujeme podvýroky podle tabulky -  důkaz pravdivosti i proveditelnosti je podle struktury formule

1. Převod implikace a ekvivalence
2. Negace konjunkce, disjunkce, dvojitá
3. Můžeme prohazovat a vytýkat

## Problém splnitelnosti

**SAT** - je daná výroková formule splnitelná?

**2-CNF** - výrok je $k$*-CNF* má-li každá jeho klauzule nejvýše $k$ literálů
**2-SAT** - je *2-CNF* výrok řešitelný?

**3-SAT** je NP-úplný problém

> **Zkouška #1:** - Algoritmy pro 2-SAT a Horn-SAT (důkaz korektnosti). 

### Linearita 2-SAT

Rozklad orientovaného grafu na komponenty silné souvislosti lze v $O(|V| + |E|)$

**Implikační graf** výroku v *2-CNF*

* vrcholy jsou proměnné nebo jejich negace
* $l_1 \vee l_2$ reprezentujeme $\overline{l_1} \rightarrow l_2,\ \overline{l_2} \rightarrow l_1 $
* $l_1$ pomocí  $\overline{l_1} \rightarrow l_1$

Výrok je splnitelný, práv;ě když žádná silně souvislá komponenta neobsahuje dvojice opačných literálů

*Důkaz:*

$(\Rightarrow$) :  každé splňující ohodnocení ohodnotí všechny literály ze stejně komponenty stejně

$(\Leftarrow)$ nalezneme ohodnocení:

* Označme $G^*_\varphi$ graf vzniklý kontrakcí komponent, ten je acyklický
* Má topologické uspořádání - $p < q$ pro každou hranu $pq$
* V rostoucím pořadí podle $<$ budeme nastavovat neohodnocené literály na $0$ a v opačné na $1$
* Toto ohodnocení je splňující, protože, kdyby ne, tak spor
  * Musí totiž existovat hrany $p\rightarrow q$ a $\overline{q} \rightarrow \overline{q}$ s $v(p)=1$ a $v(q)=0$
  * Ale spor se zadáním, protože $p<q$ a $\overline{q} < \overline{p}$

### Horn-SAT

**Jednotková klauzule** - ...
**Hornova klauzule** - nejvýše jeden pozitivní literál
**Hornův výrok** - konjunkce Hornových klauzulí
**Horn-SAT** - problém splnitelnosti...

#### Algoritmus řešení Horn-SAT - jednotková propagace

1. Obsahuje-li dvojici jednotkových klauzulí $l$ a $\overline{l}$, není splnitelný
2. Obsahuje-li jednotkovou klauzuli, nastav ji na jedna a odstraň všechny klauzule s $l$ a $\overline{l}$ ze všech klauzulí
3. Neobsahuje-li, je splnitelný ohodnocením 0 všech zbývajících

*Pozorování*: Splnitelnost se jednotkovou propagací (ten druhý krok) zachovává

*Důkaz*: první dva kroky obvs, třetí krok díky Hornově tvaru neboť každá zbývající klauzule obsahuje negativní literál

> **Pozn:** Vhodnou reprezentací to jde lineárně

# 3. Přednáška - Teorie a tablo

* Teorie nad jazykem $\mathbb{P}$ je množina $T$ výroků z $VF_{\mathbb{P}}$
* Model teorie $T$ nad $\mathbb{P}$ je ohodnocení $v \in M(\mathbb{P})$ ve kterém všechny axiomy platí - znač. $v \models T$
* Třída modelů $M^\mathbb{P}(T)$ jsou všechny modely z $M(\mathbb{P})$ ve kterých jsou axiomy pravdivé
* Konečnou teorii lze nahradit konjunkcí jejich axiomů

**Sémantika vzhledem k teorii** $T$ nad $\mathbb{P}$ : 
Výrok $\varphi$ nad $\mathbb{P}$ je pravdivý v $T$, pokud platí v každém modelu teorie - $T \models \varphi$, obdobně lživý, nezávislý, splnitelný, ...
Ekvivalentní v $T$ pokud mají stejné modely

Jsou-li všechny axiomy tautologie, všechny pojmy vzhledem k $T$ se shodují s původními

**Důsledek** teorie $\theta^\mathbb{P}(T)$ je množina všech výroků pravidvých v $T$ nebo-li $\{ \varphi \in VF_\mathbb{P} \ | \ T \models \varphi \}$

Pro každé $T, T', \varphi, \varphi_1, \cdots$ nad $\mathbb{P}$ platí:

* $T \subseteq \theta^\mathbb{P}(T)$ - teorie je podmnožina důsledků
* $\theta^\mathbb{P}(\theta^\mathbb{P}(T)) = \theta^\mathbb{P}(T)$ - důsledek důsledku je původní důsledek
* $T\subseteq T' \Rightarrow \theta^\mathbb{P}(T) \subseteq \theta^\mathbb{P}(T')$ - přidáváním axiomů do teorie můžu jenom rozšířit co je pravdivé 
* $\varphi \in \theta(\{ \varphi_1, \cdots \}) \Leftrightarrow \models (\varphi_1 \wedge \cdots) \rightarrow \varphi$ - ...

*Důkazy z definic, protože* $T\models \varphi \Leftrightarrow M(T) \subseteq M(\varphi)$

## Vlastnosti teorie

* Sporná  - jestliže v ní platí $\bot$ ( x bezesporná)
* Kompletní - nemá nezávislé výroky
* Extenze, jestliže její prvovýroky a důsledky jsou nadmnožina té původní
  * Jednoduchá je pokud má stejné prvovýroky
  * Konzervativní pokud důsledky původní jsou průnik důsledků té nové a všech výroků z původních provýroků
* Ekvivalentní pokud jsou si navzájem extenzí

**Pozorování:**

 * Bezesporná $\Leftrightarrow$ má model, kompletní $\Leftrightarrow$ má jediný model
 * $T$ je extenze $T'$, když $M^\mathbb{P}(T) \subseteq M^\mathbb{P}(T')$ a jsou ekvivalentní, když mají stejné modely

## Algebra výroků

Pro bezespornou $T$  nad $\mathbb{P}$ lze zadefinovat logické operace na množině $VF_\mathbb{P}$ pomocí reprezentantů, např.

$$[\varphi]_{\sim_T}\ \wedge [\psi]_{\sim_T} = [\varphi \wedge \psi]_{\sim_T}$$

($[\varphi]_{\sim_T}$ je třída ekvivalence)

Pak $AV^\mathbb{P}(T) = \langle VF_\mathbb{P} / \sim_T, \neg, \vee, \wedge, \top, \bot \rangle$ je algebra výroků

Je jedno jakého reprezentanta si zvolíme, protože $\varphi \sim_T \psi$, tak nám vydělí stejnou podmnožinu
A tedy $h([\varphi]_{\sim_T}) = M(T,\varphi)$ je korektní funkce z $VF_\mathbb{P}$ do potenční množiny modelů $T$

Navíc platí - konjunkce odpovídá průniku, disjunkce sjednocení, negace rozdílu, zobrazení $\bot$ na prázdnou množinu

Je to prostá funkce, nemusí být ale na (na je ale v případě, že množina modelů je konečná)

Booleova algebra je izomorfní s touto tzv. potenční algebrou $P(M(T))$

Umožní nám to **analýzu teorií** nad konečně provýroky ($|\mathbb{P}| = n$)

* Neekvivalentních výroků nad $\mathbb{P}$ je $2^{2^{n}}$ (možných podmnožin modelů s tímto výrokem)
*  Pravdivých $2^{2^n-m}$

---

**Dokazovací systémy**

*Snažíme se důkaz formalizovat jako syntaktickou proceduru*

* Důkaz je konečný objekt, který může vycházet z axiomů dané teorie
* $T \vdash \varphi$ značí dokazatelnost z teorie

Formální dokazovací systém má být korektní a nejlépe i úplný

Příklady dokazovacích systémů (kalkulů) jsou: tablo metody, Hilbertovské kalkuly, přirozená dedukce, ...

## Tablo metoda

Jazyk pevný a spočetný, $\mathbb{P}$ spočetná a pak každá teorie nad $\mathbb{P}$ je spočetná

*Tablo metoda binární strom sloužící k vyhledávání protipříkladu, pokud každá větev tabla selže - protipříklad  nebyl nalezen, máme konečné tablo a je dokázáno. Pokud protipříklad ale existuje může dokončené tablo být nekonečné*

**Atomické tabla** nám dávají předpis pro konečné tablo - buď ony a nebo jejich připojování na konec větev

### Tablo důkaz

$P$ je položka na větvi $V$ tabla $\tau$

* $P$ je redukovaná pokud je na $V$ kořen atomického
* $V$ je sporná obsahuje-li $T\varphi$ a $F\varphi$
* $V$ je dokončená je-li každá její položka redukovaná

Tablo důkaz se dělá s negací dokazované formule v kořeni

Do důkazu lze přidat axiom připojením na konec větve  

# 4. Přednáška - Tablo, Hilbertovský kalkul, ...

## Systematické tablo

> **Zkouška #2:** Tablo metoda ve VL: syst. tablo (dokončenost, kon. důkazu), korektnost, úplnost.

Vždy redukujeme nejlevější položku v nejnižší úrovni tabla a atomické tablo za to přidáme na konec (případně přidáme ještě  $n$-tý axiom)

### Dokončenost

Pro každou teorii $T$ a položku $R$ je systematické tablo $\tau$ dokončené

*Důkaz:* Nechť $\tau = \cup \tau_n$ je systematické tablo z $T$ s $R$ v kořeni, pak

* Je-li větev bezesporná, pak je i její prefix v $\tau_n$ bezesporný
* Je-li položka $P$ neredukovaná, je neredukovaná i na jejím prefixu
* Do úrovně každé položky P je konečně položek
* Kdyby $P$ byla neredukovaná na nějaké bezesporné větvi v $\tau$, v nějakém kroku by na ní přišla řada 
* Každá $n$-tý axiom bude nejpozději v $\tau_n+1$ na každé bezesporné větvi
* Tedy systematické tablo $\tau$ obsahuje pouze dokončené větve   $\square$

---

**Königovo lemma:** Z kombagry - nekonečný konečně větvící se strom má nekonečnou větev

### Konečnost

Je-li $\tau$ sporné tablo, je $\tau_n$ sporné konečné tablo

*Důkaz:* 

* Nechť $S$ je sporná množina vrcholů, kdyby byla nekonečná, tak existuje nekonečná větev a $\tau$ není sporné
* Jelikož je $S$ končené, všechny vrcholy leží do úrovně nějaké $m$, a tedy $m+1$ má nad sebou vždy spor
* Zvolme $n$ tak, že se $\tau_n$ shoduje s $\tau$ do $m+1$   $\square$

Z toho plyne, že je-li systematické tablo důkazem, tak je konečné (prodlužují se jenom bezesporné)

---

> To, že se položka $P$ shoduje s ohodnocením $v$ znamenám, že $P$ je $T\varphi$ a $\overline{v} = 1$  nebo obráceně (respektive se na to dá dívat tak, že ta položka při tom ohodnocení platí)

**Shodování:** $v$ je model teorie $T$, který se shoduje s položkou v kořeni. Pak v tablu existuje větev shodující s $v$

*Důkaz:* Indukcí podle konstrukce table - posloupnost $V_0, V_1, \cdots$ , t,ž, $V_n$ se shoduje $v$ a $V_n$ je obsažena ve $V_{n+1}$

* Základ indukce ověříme z atomických table
* Pokud větev při konstrukci tabla nezmění, tak prostě jen $V_{n+1} = V_n$ 
* Pokud připojíme $T\varphi$ pro $\varphi \in T$, tak protože $v$ je model $\varphi$, tak se $V_{n+1}$ shoduje s $v$
* Jinak připojujeme atomické tablo nějaké položky $P$. Protože se $P$ shoduje a tvrzení platí pro atomická tabla   $\square$

### Korektnost

Je-li $\varphi$ dokazatelná z $T$, je $\varphi$ pravdivá v $T$ ($T \vdash \varphi \Rightarrow T \models \varphi$)

*Důkaz:* Sporem - budeme předpokládat, že tablo dokazatelná $\varphi$ není pravdivá v $T$

Protože se ale $F\varphi$ shoduje s $v$, existuje větev shodující se s $v$, to ale není možné, protože každá větev je sporná   $\square$

---

**Protipříklad:** Bezesporná větev v dokončeném tablu poskytuje protipříklad přes obvs. ohodnocení $v$ z tabla

*Důkaz:* Indukcí dle struktury formule v položce na $V$

 * Je-li $T(p)$ na $V$, kde $p$ je prvovýrok - $\overline{v}(p) = 1$, je-li $Fp$ $\overline{v}(p) = 0$ dle definice
 * Je-li $T(\varphi \wedge \psi)$ na $V$ je $T\varphi$ a $T\psi$ neboť $\tau$ je dokončené, a ostatní spojky obdobně

### Úplnost

Je-li formule pravdivá, je i dokazatelná - $T \models \varphi \Rightarrow T \vdash \varphi$

*Důkaz:* Ukážeme, že tablo s $F\varphi$ je sporné, kdyby ne, máme nějakou bezespornou větev a dle předchozího tvrzení získáme ohodnocení prvovýroků shodující se s $v$ t.ž. $\overline{v}(\varphi) = 0$, protože $v$ je dokončená a splňuje všechny axiomy je modelem teorie - spor s tím, že $\varphi$ platí v každém modelu

### Vlastnosti teorií přes důkazy

Je-li $\varphi$ dokazatelná z $T$ je to věta teorie $T$. Množina vět $T$ je $\text{Thm}^{\mathbb{P}}(T)$

Teorie je sporná, jestliže v ní lze dokázat spor. Kompletní, jestliže není sporná a každou formuli lze dokázat nebo zamítnout. Extenze nějaké teorie, jestliže jsou její věty a prvovýroky nadmnožina, ...

#### Důsledky

* $\varphi$ je v $T$ dokazatelné, když tam platí
* Množina vět je stejná jako množina důsledků
* $T$ je sporná, když nemá model - není splnitelná
* $T$ je kompletní, když má právě jeden model - je sémanticky kompletní
* $T,\varphi \vdash \psi \Leftrightarrow T \vdash \varphi \rightarrow \psi$  (Věta o dedukci)

> **Zkouška #3:** Věta o kompaktnosti VL a její důsledky.

## Kompaktnost

Teorie má model, když každá její konečná část má model

*Důkaz:*

$\Rightarrow$ je zřejmá	

$\Leftarrow$ č.1. : Pokud $T$ nemá model, je z ní dokaztelný $\bot$ nějakým systematickým tablem, to je ale konečné ...

$\Leftarrow$ č.2. : Uvážíme strom na konečných binárních posloupnostech $\sigma$ uspořádaných prodloužením, které do $S$ patří právě když existuje ohodnocení $v$ prodlužující $\sigma$ .... idc

### Aplikace kompaktnosti

Spočetně nekonečný graf je $k$-obarvitelný právě když každý jeho konečný podgraf je $k$-obarvitelný

$(\Rightarrow)$ je zřejmá

$(\Leftarrow)$ Nechť každý podgraf je $k$-obarvitelný, vezměme prvovýroky $\{p_{u,i} \ | \ u \in V, 1 \leq i \leq k\}$ a $T$ s axiomy:

* $p_{u,1} \vee \cdots \vee p_{u,k}$  -  pro všechna $u \in V$
* $\neg(p_{u,i} \wedge p_{u,j})$  -  pro všechna $u\in V$, $1\leq i \leq j \leq k$
* $\neg(p_{u,i} \wedge p_{v,i})$  -  pro všechna ${u,v}\in E$, $1\leq i \leq k$

Nebo-li vrcholu musí mít alespoň nějakou barvu, nemůže mít dvě barvy najednou a dva sousední vrcholy nemají...

$G$ je tedy $k$-obarvitelný, když $T$ má model. Díky kompaktnosti stačí dokázat, že každá konečná $T' \subseteq T$ má model
Nechť $G'$ je podgraf na vrcholech t.ž. $p_{u,i}$ se vyskytuje v $T'$. $G'$ je dle předpokladu $k$-obarvitelný a tedy $T'$ má model

#  5. Přednáška - Rezoluce

> **Zkouška #4:** Rezoluce ve VL: korektnost, úplnost. LI-rezoluce (úplnost pro Horn. formule).

## Rezoluční metoda

*Základ pro řešiče, předpokládaná formule v CNF, množinová reprezentace formulí, zamítací procedura, ...*

**Množinová reprezentace formulí v CNF:**
Literál, klauzule, prázdná klauzule $\square$ (nesplněná), formule $S$ (prázdná $\emptyset$ je splněná), (částečné) ohodnocení $\mathcal{V}$

**Rezoluční pravidlo:** Z dvou klauzulí, které obsahují opačné literály, lze odvodit další klauzuli (rezolventu)

**Rezoluční důkaz** je konečná posloupnost klauzulí a rezolvent $C_0, \cdot, C_n = C$

klauzule může být rezolucí dokazatelná ($S\vdash_R C$) nebo zamítnutelná ($S\vdash_R \square$) -  zamítnutí je důkaz $\square$ z S

### Korektnost

Je-li $S$ rezolucí zamítnutelná, je nesplnitelná

*Důkaz:* Nechť $S\vdash_R \square$, kdyby nějaké $\mathcal{V} \models S$ a tedy by $\mathcal{V}$ splňovalo každou klauzuli a tedy $\mathcal{V} \models \square$ a to není možné

**Rezoluční strom** je konečný binární strom s kauzelemi v listech, kořenem $C$ a rezolventy ve vnitřních vrcholech

**Rezoluční uzávěr** $\mathcal{R}(S)$ je nejmenší množina - $\forall C\in S: C\in \mathcal{R}(S)$ a rezolventy dvou klauzulí v $R(S)$ jsou v $R(S)$

## Redukce dosazením:

$S^l = \{ C \backslash l \notin C \in S \}$ - to je jako bychom dosadili $\top$ a $\bot$ za literály a $l$ a $\overline{l}$

$S$ je splnitelná právě když $S^l$ nebo $S^\overline{l}$ je splnitelná

*Důkaz:*

$(\Rightarrow)$ Nějaké splňující ohodnocení $\mathcal{V}$, které búno neobsahuje $\overline{l}$, pak $V \models S^l$ neboť $\mathcal{V}\backslash\{l,\overline{l}\} \models C$ a tedy $\mathcal{V}\backslash\{\overline{l}\} \models C$

$(\Leftarrow)$ Naopak předpokládejme $\mathcal{V}\models S^l$, jelikož se $l$ ani $\overline{l}$ nevyskytuje v $S^l$. Pak $V' \models S$ neboť $C$ obsahující $l$...

**Strom dosazení:** Postupnou redukci dosazování můžeme reprezentovat stromem

$S$ není splnitelná právě když každá větev obsahuje $\square$ - pokud je nesplnitelná, tak to jde do konečně krocích

### Úplnost rezoluce

Je-li konečná $S$ nesplnitelná, je rezolucí zamítnutelná - $S\vdash_R \square$

*Důkaz:* Indukcí dle počtu proměnných

* Nemá-li nesplnitelná $S$ žádnou proměnou je dokazatelná    
* Nechť $l$ je literál v $S$. A tedy $S^l$ a $S^\overline{l}$ jsou nesplnitelné.
* Jelikož mají $S^l$ a $S^\overline{l}$ mají méně proměnných, tak dle i. p. z nich existují stromy pro odvození $\square$
* Je-li každý list jedno z těch stromů z $S$, tak ten strom je rezolučním a odvodíme $\square$
* Pokud ne, tak doplníme literál $\overline{l}$ do každého listu jenž není z $S$ a získáme rezoluční strom $\{\overline{l}\}$
  * Obdobně i opačný
* Rezolucí kořenů  $\{\overline{l}\}$ a  $\{l\}$ získáme $\square$

Důsledek toho je i pro nekonečně spočetné $S$

### Lineární rezoluce

*Omezení rezoluční metody*

**Lineární důkaz:** konečná posloupnost $(C_n, B_n)$ t. ž. $B_i \in S$ nebo $B_i = C_j$ pro $j<i$ a $C_{i+1}$ je rezolventa $C_i, B_i$ 

$C_0$ je počáteční, $C_i$ je centrální a $B_i$ je boční klazule

$C$ je lineárně dokazatelná značíme $S \vdash_L C$, zamítnutí je důkaz $\square$

Každý lineární důkaz lze transformovat na rezoluční důkaz a tedy je-li $S$ lineárně zamítnutelná, tak je nesplnitelná

*Pro Hornovy formule se dá dál omezit*

Fakt - $\{p\}$ pro $p^1$, pravidlo - právě jeden pozitivní a alespoň jeden negativní, cíl - neprázdná bez pozitivního

Nesplnitelná Hornova formule obsahuje fakt i cíl - bez faktu/cíle nastavím všechny proměnné na $0$ nebo $1$

### LI-rezoluce (linear input)

Je lineární rezoluce ve které je každá boční klauzule ze vstupní formule $S$

#### Úplnost LI

Je-li Hornova $T$ splnitelná a $T \cup \{G\}$ nesplnitelná pro cíl $G$, lze odvodit $\square$ z $T\cup\{G\}$ LI-rez. začínaje $G$

*Důkaz:* Díky kompaktnosti $T$ konečná a budeme opět postupovat dle počtu proměnných

* $T$ obsahuje fakt pro nějakou $p$
* $T' = (T \cup \{G\})^p$ je nesplnitelná dle lemmatu, $G^p = G \backslash \{ \overline{p} \}$
* Je-li $G^p = \square$ ...
* Jinak dle i. p. lze $\square$ odvodit z $T'$ začínající $G^p$
* Doplněním $\overline{p}$ do všech listů jež nejsou v $T \cup \{ G \}$
* ...

# 6. Přednáška - Predikátová logika, instance a varianty

## Predikátová logika

*Tvrzení o individuích, jejich vlastnostech a vztazích*

**Jazyk 1. řádu** obsahuje proměnné, funkční a konst symboly, relační symboly, kvantifikátory, logické spojky, závorky

**Signatura jazyka** je dvojice relačních a funkčních symbolů s danými aritami (žádný z nich není rovnost)

**Jazyk** je dán signaturou a uvedením, jestli obsahuje rovnost, např jazyk s rovností $\langle +, -, 0\rangle$ je jazyk teorie grup

**Termy **- Induktivním předpisem z proměnných nebo konstant s postupným přidáváním do funkcí

Konstantní term je bez proměnných
Množina všech termů $\text{Term}_L$
Podterm, vytvořující strom, infix - ...

**Atomické formule** - $n$-ární relace termů, množin všech je $\text{AFm}_L$

**Formule** jazyka $L$ - induktivním předpisem z atomických formulí pomocí bool funkcí a existenčních kvantifikátorů

Množina formulí $\text{Fm}_L$, podformule

**Výskyt proměnné** - Vázaný výskyt je-li proměnná v kvantifikátoru, jinak volný - volná a vázaná proměnná

**Otevřené formule** - otevřená bez kvantifikátoru (množina $\text{OFm}_L$), **Uzavřená** (stenence) - bez volných

## Substituce

Když dosadíme term za proměnnou, chceme aby formule říkala o termu to samé, co předtím...

Term je substituovatelný pokud po nahrazení volných výskytů nevznikne žádný vázaný

Substitucí vzniká instance - $\varphi(x/t)$

Pomocí substituce můžeme vytvořit ekvivalentní formule - přejmenování

## Struktury

Jazyk $L = \langle \mathcal{R}, \mathcal{F} \rangle$ a neprázdná množina $A$

**Realizace relačního symbolu** $R\in \mathcal{R}$ je libovolná relace $R^A \subseteq A^{ar(R)}$ (relace správné arity), rovnost je $id_A$
**Realizace funkčního symbolu** $f\in \mathcal{F}$ je libovolná funkce $f^A : A^{ar(f)} \rightarrow A$ - libovolná funkce správné arity

Struktura je trojice $\mathcal{A} = \langle A, \mathcal{R}^A, \mathcal{F}^A \rangle$ - (množina a soubory realizací)

### Hodnota ternu

Ohodnocení je funkce $e: \text{Var} \rightarrow A$

Hodnota $t^\mathcal{A}[e]$ je dána induktivně tak, že každá $x \in Var$ má ohodnocení $e$ a funkce dostane ohodnocení
Konstanta je $c^\mathcal{A}[e] =c^\mathcal{A}$ a nezávisí na ohodnocení

### Hodnota formule

Hodnota $H^\mathcal{A}_{at}(\varphi)[e]$ formule $\varphi$ ve struktuře $\mathcal{A}$ -  spočítají se hodnoty termů a podívá se, jestli ta $n$-tice je v $R^\mathcal{A}$

Sentence má všechny termy konstantní a její hodnota nezávisí na ohodnocení $e$
Hodnota $\varphi$ závisí pouze na ohodnocení volných proměnných

Výpis hodnot neatomických formulí pro Booleovské funkce (kvantifikátory se přeloží na $min$ a $max$)

**Platnost při ohodnocení** - pokud  $H^\mathcal{A}(\varphi)[e] = 1$, pak formule při ohodnocení $e$ platí ($\mathcal{A} \models \varphi[e]$, resp. $\mathcal{A} \not\models \varphi[e]$)

*Pozorování:* 

$t$ je subsituovatelný za $x$ do $\varphi$, pak platí $\mathcal{A} \models \varphi(x/t)[e] \Leftrightarrow \mathcal{A} \models \varphi[e(x/a)]$ 
$\psi$ je varianta $\varphi$, pak platí $\mathcal{A} \models \varphi[e] \Leftrightarrow \mathcal{A} \models \psi[e]$

**Platnost ve struktuře:** pravdivá a lživá pro každé ohodnocení

* $\mathcal{A} \models \varphi \Rightarrow \mathcal{A} \not\models \neg \varphi$ (pro sentenci i obráceně)
* $\mathcal{A} \models \varphi \wedge \psi \Leftrightarrow \mathcal{A} \models \varphi[$ a $\mathcal{A} \models \psi$
* $\mathcal{A} \models \varphi \wedge \psi \Leftarrow \mathcal{A} \models \varphi[$ nebo $\mathcal{A} \models \psi$ (pokud je jedna z nich sentence, tak i obráceně)
* $\mathcal{A} \models \varphi \Leftrightarrow \mathcal{A} \models(\forall x)\varphi$

**Platnost v teorii**

* Teorie je množina formulí jazyka $L$, její model je struktura, že $A \models T$ (každé $\varphi \in T$)
* Třída modelů, pravidovst, lživost, nezávislost, ...
* Prázdná teorie má model stejný jako model jazyka a teorii vynecháváme ($\models \varphi$)

# 7. Přednáška - Vlastnosti teorií, podstruktury, ...

> **Zkouška #5**: Sémantika PL: věta o konstantách, vlastnosti otevřených teorií, věta o dedukci.

### Nesplnitelnost a pravdivost

*Lze převést na problém existence modelu*

Negace sentence nemá v teorii model $\Leftrightarrow$ výrok je v teorii pravdivý

*Důkaz:* triviálně přes to, že ne $\neg \varphi$ neplatí v žádném modelu

**Základní algebraické teorie** - teorie grup, komutativních grup, okruhů, těles

**Vlastnosti teorií** once again - sporná, kompletní (sentence jsou buď pravdivé nebo lživé), extenze, ...

$T$ je bezesporná když má model, kompletní, když má elementární ekvivalenci a jeden model, ...

Elementárně ekvivalentní jsou, když v nich platí stejné formule (například porovnávání v $\mathbb{Q}$ a $\mathbb{R}$)

### Podstruktura (indukovaná)

Nechť $\mathcal{A} = \langle A, \mathcal{R}^A, \mathcal{F}^A \rangle$ a $\mathcal{B} = \langle B, \mathcal{R}^B, \mathcal{F}^B \rangle$

$B \subseteq A$         $\forall R \in \mathcal{R} : R^B = R^A \cap B^{ar(R)}$         $\forall f \in \mathcal{F}: f^B = f^A \cap (B^{ar(f)} \times B)$

Poslední nám říká, že se ve funkci omezíme (parcializujeme) na potřebnou doménu

Podmnožina je doménou nějaké podstruktury v případě, že je uzavřená na všechny funkce a relace

**Platnost v podstruktuře** - Pro každou otevřenou formuli platí, že $\mathcal{B}\models \varphi[e] \Leftrightarrow \mathcal{A} \models \varphi [e]$

*Důkaz:* Pro atomickou z definice, dále indukci dle struktury formule.

Otevřená formule (bez kvantifikátoru) platí ve struktuře právě když platí v každé podstruktuře

Každá podstruktura otevřené teorie (všechny její axiomy otevřené) je jejím model

**Generovaná podstruktura** $\mathcal{A}\langle X \rangle$ - hledáme nejmenší možnou podstrukturu, která obsahuje danou podmnožinu

Odebráním realizací chybějících symbolů z jazyka získáme redukt, obráceně expanze

### Věta o konstantách

Formule $\varphi$ s volnými proměnnými a $T$ jazyka $L$. Rozšíření $L'$ obsahuje $c_1, \cdots, c_n$ a $T'$. Pak

$$T \models \varphi \Leftrightarrow T' \models \varphi (x_1/c_1, \cdots, x_n/c_n)$$

*Důkaz:* 

($\Rightarrow$)  Mám model $\mathcal{A}'$ a nechť $\mathcal{A}$ je jeho redukt. Jelikož $A \models \varphi[e]$ pro každé $e$, tak $\mathcal{A} \models \varphi [e(x_1/c_1^{A'}, \cdots, x_n/c_n^{A'})]$ ...

($\Leftarrow$)  Mám model $\mathcal{A}$ a jeho expanzi $\mathcal{A}'$, pak $\mathcal{A}' \models \varphi [e(x_1/c_1^{A'}, \cdots, x_n/c_n^{A'})]$ ...

### Definovatelné množiny

Množina definovaná formulí $\varphi(x_1, \cdots, x_n)$ ve struktuře $\mathcal{A}$ je množina $n$-tic z $A$ (vektorů) $\overline{x}$, které platí v $\mathcal{A}$
Množina definovaná formulí s parametry $\varphi^{A,\overline{b}}(\overline{x},\overline{y})$ ... (příklad s formulí sousednosti a parametry graf a jeden vrchol)

Definovatelné množiny $\text{Df}^n(\mathcal{A},\mathcal{B})$

Příklad s dotazy do databáze a teorie Booleových algeber...

> **Zkouška #6:** Tablo metoda v PL: syst. tablo (dokon. a kon. důkazu), význam axiomů rovnosti. 

## Tablo metoda v predikátové logice

### Rozdíly

* V položkách budou vždy sentence (když nejsou, tak je můžeme nahradit generálním uzávěrem)
* Přidáme atomické tabla pro kvantifikátory - za ty budeme substituovat konstantní termy
* Jazyk rozšíříme o konstantní symboly ($L_c$)

**Předpoklady** -  Dokazujeme sentenci z teorie v uzavřeném tvaru ve spočetném jazyku $L$ (zajistí spočetnou teorii)

*Zatím budeme předpokládat jazyk bez rovností*

# 8. Přednáška - Tablo metoda v PL, kanonický model

## Tablo

Binární značkovaný strom s předpisem, že každé atomické tablo je konečné tablo a na konec větví můžeme připojovat atomické tabla pro položky nebo axiomy (musíme zmínit použití libovolné/určité konstanty)

Většina stejné jako pro VL - sporné, bezesporné, důkaz, dokazatelná sentence, zamítnutí, ...

### Dokončenost

*Dokončená bezesporná větev by měla poskytovat protipříklad*

Výskyt položky $P$ ve $v$ je $i$-tý pokud má $i-1$ předků a je redukovaný na $V$ skrze $v$ 

* Pokud není ve tvaru $T\forall$ ani $F\exists$ a $P$ je kořen atomického tabla (jako předtím)
* Pokud toho tvaru je, má $(i+1)$-ní výskyt na $V$ a na $V$ je $T\varphi(x/t_i)$ resp. $F...$, kde $t_i$ je $i$-tý konstantní term

Chceme totiž mít na dokončených bezesporných větvích zaručeno, že to může pokračovat dál (objeví se všechny $t$)

Větev je dokončená je-li sporná nebo každý výskyt je redukovaný a $V$ obsahuje $T\varphi$ pro všechny $\varphi \in T$

### Systematické tablo - konstrukce

Na začátku máme položku v kořeni a teorii. Následně algoritmus o 4 krocích

Za $\tau_0$ atomické tablo a v případě $(*)$ vzít term $t_1$. Následně nejlevější vrchol v co nejmenší úrovni daného tabla obsahující výskyt $P$, který není redukovaný a ten podle jeho tvaru připojím atomické tablo na každou bezespornou větev za $P$ a přidám na konec $T\varphi_n$ na větve, které ji neobsahují

*Prostě přidávat $\forall x$ pořád dokola*

**Dokončenost** - Pro každou teorii a položku je systematické tablo dokončené.

*Důkaz:* Do úrovně $v$ je konečně mnoho výskytů všech položek. Kdyby výskyt $P$ byl neredukovaný, byl by vybrán v nějakém kroku a každá formule z teorie bude někdy na každé bezesporné větvi.

Je-li systematické tablo důkazem, je konečné.

*Důkaz:* Kdyby ne, tak dle Königa by obsahovalo nekonečnou větev, která je bezesporná.

### Tablo v jazyce rovností

Přidají se axiomy rovnosti (více druhů - jedna položka, po složkách rovny implikují rovnost funkcí nebo relací)

**Kongruence a faktorstruktura**

Ekvivalence je kongruence pro $f$, pokud nezáleží kterého reprezentanta z ekvivalence si vyberu, obdobně relace

Mám kongruenci pro všechny funkce, pak dává smysl strukturu faktorizovat
Faktorstruktura je s truktura s doménou tříd ekvivalence a funkce definované podle reprezentantů

Například kongruence $\text{mod }p$ a faktorstruktura $\mathbb{Z}_p$

> **Zkouška #7:** Tablo metoda v PL: korektnost, kanonický model (s rovností), úplnost. 

### Korektnost tablo metody

*Bude zákldat na tom, že žádný příklad se nepřeskočí*

Struktura se shoduje s položkou pokud $P$ je $T\varphi$ a $\mathcal{A} \models \varphi$

Nechť $\mathcal{A}$ je model teorie $T$, který se shoduje s kořenem tabla. Pak v tablu dokážeme najít větev, která se shoduje s modelem $\mathcal{A}$ až na to, že můžeme mít nové symboly a proto ukážeme, že strukturu $\mathcal{A}$ můžeme vyexpandovat do $L_c$.

*Důkaz:* Stačí nám to expandovat jenom o symboly na větvi. To uděláme indukcí podle konstrukce tabla

Nalezneme větev $V_n$ a expanzi $\mathcal{A_n}$

* Vznikne-li bez prodloužení $V_n$, tak jen opíšeme.
* Vznikne-li připojením $T\varphi$ k $V_n$, nechť $V_{n+1}$ je tato větev a $\mathcal{A}_{n+1} = \mathcal{A}_n$ 
* Jinak vznikne prodloužením o atomické tablo a z IP se $\mathcal{A}_n$ shoduje s $P$
  1. Je to jen spojka$V_n$, tak jen opíšeme.
  2. Pro $T (\forall x)$, $F(\exists x)$ je $\mathcal{A}_{n+1}$ libovolná e1xpanze o konstanty z $t$
  3. Pro $T (\exists x)$, ... pak pro nějaké $a$ platí $\mathcal{A}_n \models \varphi(x)[e(x/a)]$. Z toho je $\mathcal{A}_{n+1}$ rozšíření o $c^A = a$.
* Základní krok je y analýzy atomických tabel

Pro každou teorii a sentenci, je-li $\varphi$ tablo dokazatelná, je pravdivá

*Důkaz:* Nechť je tablo dokazatelná a není pravdivá. Pak existuje model ve kterém neplatí, ten lze expandovat do $L_c$ tak, že se shoduje s nějakou větví. To ale není možné, protože pak by platilo $T\varphi$ a $F\varphi$ a tedy všechny jsou sporné

### Kanonický model

*Z bezesporné větve vyrobíme model, který se shoduje s $V$*

Tablo z $T$ jazyka $L = \langle\mathcal{F},\mathcal{R}\rangle$m pak kanonický model z větve $V$ je $L_c$ struktura $\mathcal{A} = \langle A, \mathcal{F}^A, \mathcal{R}^a \rangle$, kde platí 

* A jsou všechny konstantní termy z $L_c$
* $f^a(s...) = f(s...)$ pro každý $f\in F \cup (L_c/L)$
* $R(s...) \Leftrightarrow TR(s...)$ je položka na $V$

####  Kanonický model s rovností

$T^*$ je rozšířená o axiomy rovnosti, aby rovnost byla identita, musíme model faktorizovat

Musí se na $V$ objevit $T(s_1 = s_2)$ pro relaci $=^A$, ta je potom ekvivalence a navíc kongruence pro $\mathcal{F}, \mathcal{R}$

#  9. Přednáška - Úplnost, LS věta, prenexní

### Úplnost

Kanonický model z bezesporné dokončené větve se shoduje s $V$

*Důkaz:* Indukcí dle struktury sentence v položce na $V$

* Atomická $\varphi$, pokud  je $T\varphi$ na $V$, tak z konstrukce $A \models \varphi$, jinak $F\varphi$ a bezesporná větev...
* $\varphi \wedge \psi$, tak $T\varphi$ a $T\psi$ na $V$, protože je to dokončená větev a tedy $A\models \varphi$ a $A \models \psi$
* Obdobně pro všechny ostatní spojky
* Pro $T\forall$ a $F\exists$ je pro každé $t$ na větvi a tedy $A \models (\forall x)\varphi(x)$, obdobně $T\exists$ a $F\forall$ jsou na $V$ pro nějaké $c$

Pro každou teorii a sentenci, je-li sentence pravdivá, tak je tablo dokazatelná.

*Důkaz:* Nechť $\varphi$ je pravdivá v $T$, ukážeme, že libovolné tablo s $F\varphi$ v kořeni je sporné

* Kdyby ne, tak je tam nějaká bezesporná větev a dle předchozího lemmatu existuje struktura shodující s tou větví a v ní $\mathcal{A} \models \neg \varphi$. V reduktu té struktury $\mathcal{A}' \models \neg \varphi$ a protože je dokončená tak obsahuje $T$ všechny axiomy - spor

### Vlastnosti teorií

Množina vět (dokaztelných sentencí) $\text{Thm}^L(T) = \{\varphi \in \text{Fm}_L \ | \ T \vdash \varphi \}$

Sporná, kompletní, extenze, ekvivalentní, ... prostě se to klasicky shoduje

> **Zkouška #8:** Löwenheim-Skolemova věta. Věta o kompaktnosti PL a její důsledky.

## Löwenheim-Skolemova věta

Každá bezesporná $T$ jazyka bez rovnosti má spočetně	 nekonečný model

*Důkaz:* Systematické tablo s $F\bot$ v kořeni, to je dokončené a obsahuje bezespornou větev - redukt modelu...

S rovností se musí model zfaktorizovat a může být konečný

Teorie má model, právě když každá její konečná část má model.

*Důkaz:* $(\Rightarrow)$ zřejmá a $(\Leftarrow)$ pokud $T$ nemá model, platí v ní $\bot$ a to jde dokázat konečným tablem 

**Nestandardní model přirozených čísel**

Máme standardní model přirozených čísel a množinu všech pravdivých sentencí v ní $\text{Th}(\underline{\mathbb{N}})$, $n$-tý numerál je term $\underline{n} = S(\cdots S(0)\cdots)$ a zavedeme teorii $T = \text{Th}(\underline{\mathbb{N}}) \cup {n \leq c \ | \ n \in \mathbb{N}}$, kde $c$ je nový konstantní symbol

Její každá konečná část má model a tedy $T$ má model - nestandardní model přirozených čísel 
Platí v něm to samé, ale obsahuje prvek větší než všechny numerály

> **Zkouška #9:** Extenze o definice, Skolemova veta, Herbrandova věta.

## Rozšiřování teorii

Nechť $T$ jazyka $L$, $T'$ jazyka $L'$ a $L \subseteq L'$

 * $T'$ je extenze právě když redukt každého modelu na jazyk $L$ je modelem $T$
 * Je konzervativní pokud lze každý model z $T$ expandovat do $L'$

*Důkaz:* 

* Je-li to extenze pak libovolný axiom z $T$ platí i v $T'$ a ten lze pak zredukovat a platí a naopak...
* Jeli $T' \models \varphi$ pak v nějaké jeho expanzi je splněno a tedy je splněno i v redukované

### Extenze o definovaný relační symbol

$T$ rozšíříme na $T'$ přidáním axiomu $R(x_1,\cdots, x_n) \leftrightarrow \psi(x_1, \cdots, x_n)$

*Např. zadefinujeme relaci porovnání jako formuli, že můžeme k prvnímu číslo něco přičíst a rovná se to*

Každý model $T$ lze jednoznačně expandovat na $T'$ a tedy $T'$ je konzervativní extenze

Každou formuli v rozšířeném jazyku dokážu přeložit do původního jazyka prostě tak, že relaci budu nahrazovat axiomem, který jsme využili - ten ale musím upravit na nějakou variantu tak abych zaručil substituovatelnost

### Extenze o definovaný funkční symbol

Extenze je $T$ vzniklá přidáním axiomu  $f(x_1,\cdots, x_n) = y \leftrightarrow \psi(x_1, \cdots, x_n, y)$
Pro $\psi$ musí ale platit nějaké podmínky - existence a $y$ a jeho jednoznačnost 

*Např binární mínus zavedeme pomocí binárního plus a unárního mínus*

Každý model lze jednoznačně expandovat a pro každou formuli existuje způsob jak ji přeložit zpátky existencí $z$... **TODO**

**Extenze o definice** - postupnou extenzí o definici relačního či funkčního symbolu a opět každý model lze jednoznačně expandovat, extenze je konzervativní a mžeme přejít zpátky na ekvivalentní

## Ekvisplnitelnost

*Redukování splnitelnosti na otevřené teorie*

 $T$ a $T'$ jsou ekvisplnitelné, pokud $T$ má model $\Leftrightarrow$ $T'$ má model

**Prenexní tvar: ** Kvantifikátory na začátku a až za němi výrok a jsou-li všechny $\forall$ je to **univerzální** formule

K teorii zvládneme nalézt ekvisplnitelnou tak, že axiomy převedeme do prenexního tvaru a pomocí Skolemovy varianty je převedeme na univerzální formule - jejich jádra jsou hledaná teorie (Skolemem ztratíme ekvivalenci)

### Vytýkání kvantifikátorů

* Negace, AND a OR můžeme vytknout beze změny (musíme si dát jen pozor na volnou $x$ v druhé formuli)
* U implikace se kvantifikátor v předpokladu po vytknutí změní, v druhém případě zůstane stejný

### Převod na prenexní tvar

Musíme v první řadě zmínit, že nahrazením podformule nějakou ekvivalentní je nová formule ekvivalentní původní

*Důkaz:* indukcí dle struktury formule

Ke každé formuli existuje ekvivalentní formule v prenexním normálním tvaru

*Důkaz:* Indukcí podle struktury vytýkáním kvantifikátorů, nahradíme podformule za jejich varianty

# 10. Přednáška - Skolemizace, Hebrandova věta, ...

### Skolemova varianta 

Odstraněním $\exists y_i$ z formule a jejím nahrazením za $f_i(x_1, \cdots, x_n)$ pro $i \leq n$

#### Vlastnosti

Nechť sentence $\varphi$ je skolemanizací upravena na $\varphi'$. Redukt zpátky je modelem $\varphi$ a obráceně každý model formule lze expandovat na model $\mathcal{A}'$ formule $\varphi'$ (ne nutně jednoznačně)

*Důkaz:* Redukt zpátky se ukáže nastavením ohodnocení $y$ na hodnoty nové funkce stejném ohodnocení a extenze novou funkcí, která nám z několika $x$ dá vhodnou hodnotu $y$

Z toho plyne, že Skolemova varianta je ekvisplnitelná

### Skolemova věta

Každá teorie má otevřenou konzervativní extenzi $T^*$

*Důkaz:* Nahradíme každý axiom prenexním tvarem a ten zase za Skolemovu variantu. Redukt každého modelu je i modelem $T$, tak je to extenze a jelikož každý model lze vyexpandovat, tak konzervativní. Otevřená jádra tvoří $T^*$ 

### Redukce nesplnitelnosti na VL

Je-li otevřená teorie nesplnitelná, lze to doložit - zde to uděláme konjunkcí konečně axiomů v konstantních termech

Substitucí konstantních termů získáme ground (základní) instanci a u té se to určí snadno

### Herbrandův model

*Minimální model, kterým to půjde splnit a můžeme ho využít pro ostatní*

Univerzum budou všechny konstantní termy (potřebujeme tedy alespoň jeden konstantní symbol v jazyce)

Předpis pro funkce zůstává stejný a relac	e nejsou předepsané

Herbrandův model teorie $T$ je Herbrandova struktura jež splňuje $T$

### Herbrandova věta

Otevřená teorie v jazyce bez rovnosti a alespoň jedním konstantním symbolem má Herbrandův model a nebo existuje konečně mnoho základních instancí axiomů jejichž konjunkce je nesplnitelná.

*Důkaz:* Vezmeme $T'$ ze všech základních instancí axiomů a tablo metodou budeme chtít $F\bot$.
Kanonický model z bezesporné větve je Herbrandovým modelem a jinak je sporné.

S rovností přidáme axiomy rovnosti a zfaktorizujeme ho.

#### Důsledky

$(\exists x_1)\cdots(\exists x_n) \varphi \Leftrightarrow \exists$ konstatní termy t. ž.$\varphi(x_1/t_{11}, \cdots, x_n/t_{1n}) \vee \cdots \or \varphi(x_1/t_{m1}, \cdots, x_n/t_{mn})$ je tautologie

*Důkaz:* $(\exists x_1)\cdots(\exists x_n) \varphi \Leftrightarrow (\forall x \cdots) \neg \varphi$ je nesplnitelná... 

Otevřená teorie má model právě když teorie všech základních instancí má model

*Důkaz:* Má-li $T$ model, tak v něm platí každá instance axiomů z $T'$... jinak existuje konečná nesplnitelná konjunkce

> **Zkouška #10:** Rezoluce v PL: korektnost, úplnost, lifting lemma, LI-rezoluce. 

## Rezoluce v  PL

Literál je atomická formule nebo její negace, klauzule, formule v množinové reprezentaci, ...

Rozdíl je, že rezoluční pravidlo nám umožní rezolvovat přes unifikovatelné literály

Přejmenováním v rámci klauzule dostaneme ekvisplnitelnou formuli, protože nahradíme generálním uzávěrem...

### Přímá redukce do VL

Značně neefektivně můžeme převést formuli na množinu všech základních instancí klauzulí a zavedením prvovýroků

### Substituce

Efektivněji můžeme hledat substituci $\sigma = \{x_1/t_1, \cdots \}$ pro dvě klauzule, tak abych u jedné dostal opačné literály

>  **Pozn:** Chceme dostávat co nejobecnější substituce

Několik druhů substituce - základní (všechny termy konstantní), přejmenování proměnných

Substituci lze aplikovat na výrazy (literál nebo term)

#### Skládání substitucí

Substituce je současná a neřetězí se, ale můžeme zadefinovat $E(\sigma\tau) = (E\sigma)\tau$ ...

>  **Pozn:** Není komutativní, ale je asociativní

### Unifikace

Musíme umět najít substituci, která pro množinu výrazů, která z nich udělá jediný literál

Nejobecnější unifikace je taková, že z ní každá další jde vytvořit další substitucí

#### Algoritmus

V množině výrazů se snažím napravit nejlevější pozici na které se liší
To můžu pokud tam je nějaká proměnná $x$ a term neobsahující $x$

*Korektnost algoritmu:* 

* V každém kroku eliminuje jednu proměnou, tak někdy skončí
  * Skončí-li neúspěchem - nelze unifikovat jednu pozici a tedy to nejde celé
  * Skončí-li úspěchem - tak tu unifikaci máme evidentně
  * Proč je ale nejobecnější?
    * Předpokládejme, že $\tau$ je unifikace, budeme postupovat indukcí podle skládání substitucí
    * Pro $i=0$ triviálně, Nechť $\sigma_{i+1} = x/t$ a stačí nám ukázat, že pro každou proměnnou $v$ je $v\sigma_{i+1}\tau = v\tau$
      * Pro $v \neq x$ se nic nezmění a tedy $v = x$. Zavedeme $v\sigma_{i+1} = x \sigma_{i+1} = t$ a jelikož $\tau$ je unifikace $S_i$ a $x$  i term $t$ jdou v rozdílu na pozici $i$, musí $\tau$ unifikovat $x$ a $t$ a tedy $t\tau = x\tau$

# 11. Přednáška - Rezoluce v PL

### Rezoluční pravidlo

Nechť dvě klauzule neobsahují stejnou proměnou a jsou ve tvaru $C_1 = C_1' \cup \{ A_1, \cdots \}$ a $C_2 = C_2' \cup \{ \neg B_1, \cdots \}$ a $S = \{A_1, \cdots, B_1, \cdots\}$ lze unifikovat pomocí $\sigma$ pak $C_1'\sigma \cup C_2'\sigma$ je rezolventa těch dvou klauzulí

### Rezoluční důkaz

Obdobně jako ve VL, ale máme povoleno přejmenování...

> **Pozn:** občas je potřeba zamítnou víc najednou

#### Korektnost

*Rezolučního pravidla:* Tedy $\mathcal{A} \models C_1 \wedge \mathcal{A} \models C_2 \Rightarrow \mathcal{A} \models C$

*Důkaz:* Jelikož jsou $C_1, C_2$ otevřené, tak platí i po aplikaci $\sigma$ na $\mathcal{A}$. Platí-li $\{ A_1, \cdots \}\sigma[e]$, pak musí platit $C_2\sigma[e]$ neboť ta má tu část, která platí v negaci a tedy i $\mathcal{A} \models C[e]$, podobně pokud $\{ A_1, \cdots \}$ neplatí.

Je-li formule rezolucí zamítnutelná, je nesplnitelná

*Důkaz:* Nechť je $\square$ dokazatelný, pak z korektnosti rezolučního pravidla ve struktuře platí $\square$ a to je spor 

#### Úplnost

**Lifting lemma** - *rezoluční důkaz lze z VL zdvihnout do PL*

Získáme-li rezolventu základních instancí klauzulí po $\tau_1$ a $\tau_2$ je to i rezolventa původních klauzulí po aplikování $\tau_1 \tau_2$
Původní klauzule nemůžou obsahovat stejnou proměnnou

*Důkaz:* Předpokládejme rezolventu základních instancí $C^*$ přes literál $P(t_1, \cdots, t_k)$ a tedy po substituci $\tau_1$ dostaneme $\{ P(t_1), \cdots \}$ z $\{ A_1 , \cdots \}$ a po $\tau_2$ to samé v negaci z $\{ \neg B_1, \cdots \}$. A je-li $\sigma$ $\text{mgu}$ (nejobecnější ...) pro množinu $\{A_1, \cdots, B_1, \cdots\}$, pak sjednocení ... je rezolventa. Navíc $\tau_1 \tau_2 = \sigma(\tau_1 \tau_2)$ a tedy $C\tau_1 \tau_2 = \cdots = C^*$

Nechť $S'$ je množina všech základních instancí pro $S$. Je-li $C'$ rezolucí dokazatelná z $S'$, tak ji můžeme zdvihnout.

*Důkaz:* Indukcí dle délky rezolučního odvození

Je-li formule nesplnitelná, je z ní dokazatelný $\square$

*Důkaz:* Je-li nesplnitelné je nesplnitelná i množina základních instancí. Můžeme zamítnout a pak $\square$ zdvihnout 

### Lineární rezoluce

> **Pozn.** opět nějaké omezení bez ztráty úplnosti

Obdobně jako předtím se vždy rezolvuje pomocí bočních klauzulí

$S$ je lineárně zamítnutelná $\Leftrightarrow$ $S$ je nesplnitelná

*Důkaz:* $(\Rightarrow)$ Můžeme přetransformovat na rezoluční důkaz a $(\Leftarrow)$ Plyne z úplnosti na VL

#### LI-rezoluce

Opět lineární vstupní rezoluce, která je kompletní jen pro Hornovy klauzule

Je-li Hornova $T$ splnitelná a pro cíl $G$ je $T \cup \{ G \}$ nesplnitelná, tak lze začínaje v $G$ odvodit $\square$

*Důkaz:* Z důkazu ve VL, Herbranda a lifting lemmatu

> **Zkouška #11:** Elementární ekvivalence, důsledky L.-S. vety. Izomorfismus a sémantika.

## Teorie struktury

Množina sentencí platných v struktuře $Th(\mathcal{A})$

Je kompletní (buď je v ní sentence pravdivá neb lživá) a je bezesporná (má model)

Je to jednoduchá extenze původní teorie kterou modelovalo $\mathcal{A}$
Pokud začínáme s kompletní teorií, tak jsou si ekvivalentní t.j. $\theta(T) = Th(\mathcal{A})$

### Elementární ekvivalence

Struktury jsou el. ekvivalentní pokud v nich platí stejné formule

Struktury $\mathcal{A}$ a $\mathcal{B}$ jsou elementárně ekvivalentní $(\equiv)$ pokud $\text{Th}(\mathcal{A}) = \text{Th}(\mathcal{B})$

**Jednoduché kompletní extenze** u $DeLO^*$ - teorie hustého lineárního uspořádání
Do té můžeme přidat různé varianty toho, že největší a nejmenší prvek existují a bude kompletní

### Důsledky Löwenheim-Skolemovy věty

*Teorie má model, který je spočetně nekonečný (s rovností spočetný)*

Ke každé struktuře $\mathcal{A}$ jazyka bez rovnosti existuje spočetně nekonečná ekvivalentní struktura

*Důkaz:* Teorie $\text{Th}(\mathcal{A})$ je bezesporná a má spočetně nekonečný model. Protože je kompletní tak...

Ke každé nekonečné struktuře s rovností to samé

### Spočetné algebraicky uzavřené těleso

*Algebraicky uzavřené znamená, že každý polynom má kořen*

Existuje spočetné algebraicky uzavřené těleso

*Důkaz:* Existuje spočetná struktura ekvivalentní s $\mathbb{C}$

# 12. Přednáška - Izomorfismus struktur, axiomatizovatelnost

### Izomorfismus struktur

*Bijekce z domény první struktury do domény druhé struktury s převodem funkcí a relací*

**Automofismus** je izomorfismus sám se sebou

*Izomorfismus zachovává sémantiku*

Bijekce je izomorfismus, pokud $h(t^A[e]) = t^B[e \circ h]$ a $A\models \varphi[e] \Leftrightarrow B \models \varphi[e \circ h]$

*Důkaz:* $(\Rightarrow)$ Indukcí dle struktury termu resp. formule a $(\Leftarrow)$ Dosazením přepisů

Když jsou dvě struktury izomorfní, tak jsou i elementárně ekvivalentní

Pro konečné struktury v jazyce s rovností platí i obrácená implikace

*Důkaz:* 

* Jejich velikost je stejná, protože lze vyjádřit, že existuje právě $n$ prvků
* Půjdeme přes expanzi o jméno ... **TODO**

**Zkouška #12:** Invariance definovatelných množin na automorfismy. 

### Definovatelnost a automorfismy

*Množina definovatelná formulí s nějakými parametry*

Automorfismus zachová celou množinu (pak se zobrazí zase na sebe)

 *Důkaz:* rozepsáním

---

**Dál už na to kašlu**

---

**Zkouška #13:** $\omega$-kategoričnost, podmínky pro konečnou a otevřenou axiomatizovatelnost

### Kategoričnost

Izomorfní spektrum je počet navzájem neizomorfních modelů $T$ pro kardinalitu $\kappa$

Teorie je $\kappa$-kategorická pokud má až na izomorfismus právě jeden model kardinality $\kappa$

DeLO je $\omega$-kategorická

*Důkaz:* Indukcí lze nalézt prosté parciální funkce... **TODO**

#### $\omega$-kategorické kritérium

* Je-li teorie jazyka bez rovnosti $\omega$-kategorická, je kompletní
* Je-li s rovností $\omega$-kategorická a bez nekonečného modelu, je kompletní

*Důkaz:* Každý model je elementárně ekvivalentní s nějakým spočetně nekonečným - jediný

### Axiomatizovatelnost

#### Důsledek kompaktnosti

# 13. Přednáška - Rozhodnutelné teorie, ...

Otevřená axiomatizovatelnost

Rekurzivní axiomatizace

Robinsonova aritmetika

Peanova aritmetika

> Nerozhodnutelnost bude bez důkazů

Nerozhodnutelnost

Godelova věta

Self-reference
