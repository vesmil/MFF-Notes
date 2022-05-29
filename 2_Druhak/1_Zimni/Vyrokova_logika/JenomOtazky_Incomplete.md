## Otázka #1:

>  Algoritmy pro 2-SAT a Horn-SAT (důkaz korektnosti).

### 2-CNF

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

---

### Horn-SAT

#### Algoritmus řešení Horn-SAT - jednotková propagace

1. Obsahuje-li dvojici jednotkových klauzulí $l$ a $\overline{l}$, není splnitelný
2. Obsahuje-li jednotkovou klauzuli, nastav ji na jedna a odstraň všechny klauzule s $l$ a $\overline{l}$ ze všech klauzulí
3. Neobsahuje-li, je splnitelný ohodnocením 0 všech zbývajících

*Pozorování*: Splnitelnost se jednotkovou propagací (ten druhý krok) zachovává

*Důkaz*: první dva kroky obvs, třetí krok díky Hornově tvaru neboť každá zbývající klauzule obsahuje negativní literál

---

## Otázka #2:

>  Tablo metoda ve VL: syst. tablo (dokončenost, kon. důkazu), korektnost, úplnost.

### Dokončenost

Pro každou teorii $T$ a položku $R$ je systematické tablo $\tau$ dokončené

*Důkaz:* Nechť $\tau = \cup \tau_n$ je systematické tablo z $T$ s $R$ v kořeni, pak

* Je-li větev bezesporná, pak je i její prefix v $\tau_n$ bezesporný a je-li položka $P$ neredukovaná, je neredukovaná i na jejím prefixu
* Do úrovně každé položky P je konečně položek a tedy kdyby $P$ byla neredukovaná na nějaké bezesporné větvi v $\tau$, v nějakém kroku by na ní přišla řada 
* Navíc každá $n$-tý axiom bude nejpozději v $\tau_n+1$ na každé bezesporné větvi
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

**Shodování:** $v$ je model teorie $T$, který se shoduje s položkou v kořeni. Pak v tablu existuje větev shodující s $v$

*Důkaz:* Indukcí podle konstrukce table - posloupnost $V_0, V_1, \cdots$ , t,ž, $V_n$ se shoduje $v$ a $V_n$ je obsažena ve $V_{n+1}$

### Korektnost

Je-li $\varphi$ dokazatelná z $T$, je $\varphi$ pravdivá v $T$ ($T \vdash \varphi \Rightarrow T \models \varphi$)

*Důkaz:* Sporem - budeme předpokládat, že tablo dokazatelná $\varphi$ není pravdivá v $T$

---

**Protipříklad:** Bezesporná větev v dokončeném tablu poskytuje protipříklad přes obvs. ohodnocení $v$ z tabla

*Důkaz:* Indukcí dle struktury formule v položce na $V$

 * Je-li $T(p)$ na $V$, kde $p$ je prvovýrok - $\overline{v}(p) = 1$, je-li $Fp$ $\overline{v}(p) = 0$ dle definice
 * Je-li $T(\varphi \wedge \psi)$ na $V$ je $T\varphi$ a $T\psi$ neboť $\tau$ je dokončené, a ostatní spojky obdobně

### Úplnost

Je-li formule pravdivá, je i dokazatelná - $T \models \varphi \Rightarrow T \vdash \varphi$

*Důkaz:* Ukážeme, že tablo s $F\varphi$ je sporné, kdyby ne, máme nějakou bezespornou větev a dle předchozího tvrzení získáme ohodnocení prvovýroků shodující se s $v$ t.ž. $\overline{v}(\varphi) = 0$, protože $v$ je dokončená a splňuje všechny axiomy je modelem teorie - spor s tím, že $\varphi$ platí v každém modelu

---

## Otázka #3:

> Věta o kompaktnosti VL a její důsledky.

Teorie má model, když každá její konečná část má model

*Důkaz:*

$\Rightarrow$ je zřejmá

$\Leftarrow$ Pokud $T$ nemá model, je z ní dokaztelný $\bot$ nějakým systematickým tablem, to je ale konečné ... viz. výše

---

Spočetně nekonečný graf je $k$-obarvitelný právě když každý jeho konečný podgraf je $k$-obarvitelný

$(\Rightarrow)$ je zřejmá

$(\Leftarrow)$ Nechť každý podgraf je $k$-obarvitelný, vezměme prvovýroky $\{p_{u,i} \ | \ u \in V, 1 \leq i \leq k\}$ a $T$ s axiomy:

* $p_{u,1} \vee \cdots \vee p_{u,k}$  -  pro všechna $u \in V$
* $\neg(p_{u,i} \wedge p_{u,j})$  -  pro všechna $u\in V$, $1\leq i \leq j \leq k$
* $\neg(p_{u,i} \wedge p_{v,i})$  -  pro všechna ${u,v}\in E$, $1\leq i \leq k$

Nebo-li vrcholu musí mít alespoň nějakou barvu, nemůže mít dvě barvy najednou a dva sousední vrcholy nemají...

$G$ je tedy $k$-obarvitelný, když $T$ má model. Díky kompaktnosti stačí dokázat, že každá konečná $T' \subseteq T$ má model
Nechť $G'$ je podgraf na vrcholech t.ž. $p_{u,i}$ se vyskytuje v $T'$. $G'$ je dle předpokladu $k$-obarvitelný a tedy $T'$ má model

---

## Otázka #4:

>  Rezoluce ve VL: korektnost, úplnost. LI-rezoluce (úplnost pro Horn. formule).

### Korektnost

Prvně korektnost rezolučního pravidla

Je-li $S$ rezolucí zamítnutelná, je nesplnitelná

*Důkaz:* Nechť $S\vdash_R \square$, kdyby nějaké $\mathcal{V} \models S$ a tedy by $\mathcal{V}$ splňovalo každou klauzuli a tedy $\mathcal{V} \models \square$ a to není možné

---

### Úplnost rezoluce

Je-li konečná $S$ nesplnitelná, je rezolucí zamítnutelná a tedy $S\vdash_R \square$

*Důkaz:* Indukcí dle počtu proměnných

* Nemá-li nesplnitelná $S$ žádnou proměnou je dokazatelná
* Nechť $l$ je literál v $S$. A tedy $S^l$ a $S^\overline{l}$ jsou nesplnitelné. (dosazení konstanty za $l$)
* Jelikož mají $S^l$ a $S^\overline{l}$ mají méně proměnných, tak dle i. p. z nich existují stromy pro odvození $\square$
* Je-li každý list jedno z těch stromů z $S$, tak ten strom je rezolučním a odvodíme $\square$
* Pokud ne, tak doplníme literál $\overline{l}$ do každého listu jenž není z $S$ a získáme rezoluční strom $\{\overline{l}\}$ a obdobně i opačný
* Rezolucí kořenů  $\{\overline{l}\}$ a  $\{l\}$ získáme $\square$

---

**Lineární rezoluce:** konečná posloupnost $(C_n, B_n)$ t. ž. $B_i \in S$ nebo $B_i = C_j$ pro $j<i$ a $C_{i+1}$ je rezolventa $C_i, B_i$ 

### LI-rezoluce (linear input)

Je lineární rezoluce ve které je každá boční klauzule ze vstupní formule $S$

#### Úplnost LI

Je-li Hornova $T$ splnitelná a $T \cup \{G\}$ nesplnitelná pro cíl $G$, lze odvodit $\square$ z $T\cup\{G\}$ LI-rez. začínaje $G$

*Důkaz:* Díky kompaktnosti $T$ konečná a budeme opět postupovat dle počtu proměnných velice podobně jako v předchozím důkazu.

Začneme s tím, že existuje nějaký fakt a ten můžeme z dokazované teorie vyredukovat a pak to nakonec zase doplnit

---

## Otázka #5

> Sémantika PL: věta o konstantách, vlastnosti otevřených teorií, věta o dedukci.

### Věta o konstantách

Formule $\varphi$ s volnými proměnnými a $T$ jazyka $L$. Rozšíření $L'$ obsahuje $c_1, \cdots, c_n$ a $T'$. Pak

$$T \models \varphi \Leftrightarrow T' \models \varphi (x_1/c_1, \cdots, x_n/c_n)$$

*Důkaz:* 

($\Rightarrow$)  Mám model $\mathcal{A}'$ a nechť $\mathcal{A}$ je jeho redukt. Jelikož $A \models \varphi[e]$ pro každé $e$, tak $\mathcal{A} \models \varphi [e(x_1/c_1^{A'}, \cdots, x_n/c_n^{A'})]$ ...

($\Leftarrow$)  Mám model $\mathcal{A}$ a jeho expanzi $\mathcal{A}'$, pak $\mathcal{A}' \models \varphi [e(x_1/c_1^{A'}, \cdots, x_n/c_n^{A'})]$ ...

---

**Otevřené teorie** jsou ty jejichž všechny axiomy jsou otevřené

Otevřená formule platí v podstruktuře stejně

Podstruktura modelu otevřené teorie je opět model té teorie

Pokud otevřená neplatí, lze to doložit na konkrétních případech - redukce, Herbrandův model, ...

---

**Věta o dedukci** říká, že pokud formule platí ve sjednocení teorie a formule, pak první formule tu druhou v teorii implikuje

*Důkaz:* transformací příslušných tabel

---

## Otázka #6

> Tablo metoda v PL: syst. tablo (dokon. a kon. důkazu), význam axiomů rovnosti. 

Přidáme od VL atomické tabla pro kvantifikátory a rozšíříme jazyk

### Systematické tablo

Za $\tau_0$ atomické tablo a v případě $(*)$ vzít term $t_1$. Následně nejlevější vrchol v co nejmenší úrovni daného tabla obsahující výskyt $P$, který není redukovaný a ten podle jeho tvaru připojím atomické tablo na každou bezespornou větev za $P$ a přidám na konec $T\varphi_n$ na větve, které ji neobsahují

**Dokončenost** - Pro každou teorii a položku je systematické tablo dokončené.

*Důkaz:* Do úrovně $v$ je konečně mnoho výskytů všech položek. Kdyby výskyt $P$ byl neredukovaný, byl by vybrán v nějakém kroku a každá formule z teorie bude někdy na každé bezesporné větvi.

---

**Konečnost** - Je-li systematické tablo důkazem, je konečné.

*Důkaz:* Kdyby ne, tak dle Königa by obsahovalo nekonečnou větev, která je bezesporná.

---

$T^*$ je rozšířená o axiomy rovnosti (jejich generální uzávěry), aby rovnost byla identita, musíme model faktorizovat

Ty jsou $x = x$, $x_1 = y_1, \cdots \rightarrow f(x_1, \cdots) = f(y_1, \cdots)$, $x_1 = y_1, \cdots \rightarrow R(x_1, \cdots) \rightarrow R(y_1, \cdots)$

---

## Otázka #7:

> Tablo metoda v PL: korektnost, kanonický model (s rovností), úplnost. 

### Korektnost

Struktura se shoduje s položkou pokud $P$ je $T\varphi$ a $\mathcal{A} \models \varphi$

Nechť $\mathcal{A}$ je model teorie $T$, který se shoduje s kořenem tabla. Pak v tablu dokážeme najít větev, která se shoduje s modelem $\mathcal{A}$ až na to, že můžeme mít nové symboly a proto ukážeme, že strukturu $\mathcal{A}$ můžeme vyexpandovat do $L_c$.

*Důkaz:* Stačí nám to expandovat jenom o symboly na větvi. To uděláme indukcí podle konstrukce tabla

Nalezneme větev $V_n$ a expanzi $\mathcal{A_n}$

* Vznikne-li bez prodloužení $V_n$, tak jen opíšeme.
* Vznikne-li připojením $T\varphi$ k $V_n$, nechť $V_{n+1}$ je tato větev a $\mathcal{A}_{n+1} = \mathcal{A}_n$ 
* Jinak vznikne prodloužením o atomické tablo a z IP se $\mathcal{A}_n$ shoduje s $P$
  1. Je to jen spojka $V_n$ jen opíšeme.
  2. Pro $T (\forall x)$, $F(\exists x)$ je $\mathcal{A}_{n+1}$ libovolná expanze o konstanty z $t$
  3. Pro $T (\exists x)$, ... pak pro nějaké $a$ platí $\mathcal{A}_n \models \varphi(x)[e(x/a)]$. Z toho je $\mathcal{A}_{n+1}$ rozšíření o $c^A = a$.
* Základní krok je z analýzy atomických tabel

Pro každou teorii a sentenci, je-li $\varphi$ tablo dokazatelná, je pravdivá

*Důkaz:* Nechť je tablo dokazatelná a není pravdivá. Pak existuje model ve kterém neplatí, ten lze expandovat do $L_c$ tak, že se shoduje s nějakou větví. To ale není možné, protože pak by platilo $T\varphi$ a $F\varphi$ a tedy všechny jsou sporné

### Kanonický model

$R(s...) \Leftrightarrow TR(s...)$ je položka na $V$

---

## Otázka #8:

> Löwenheim-Skolemova věta. Věta o kompaktnosti PL a její důsledky.

Každá bezesporná $T$ jazyka bez rovnosti má spočetně nekonečný model

*Důkaz:* Systematické tablo s $F\bot$ v kořeni, to je dokončené a obsahuje bezespornou větev - redukt modelu...

**Kompaktnost** je podobná jako u VL

---

## Otázka #9:

>  Extenze o definice, Skolemova veta, Herbrandova věta.

Pozor na substituovatelnost při dosazování

Extenze, konzervativní, existuje nahraditelná z původního jazyka

---

Každá teorie má otevřenou konzervativní extenzi $T^*$

*Důkaz:* Nahradíme každý axiom prenexním tvarem a ten zase za Skolemovu variantu. Redukt každého modelu je i modelem $T$, tak je to extenze a jelikož každý model lze vyexpandovat, tak konzervativní. Otevřená jádra tvoří $T^*$ 

---

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

---

## Otázka #10:

> Rezoluce v PL: korektnost, úplnost, lifting lemma, LI-rezoluce. 

#### Korektnost

*Rezolučního pravidla:* Tedy $\mathcal{A} \models C_1 \wedge \mathcal{A} \models C_2 \Rightarrow \mathcal{A} \models C$

*Důkaz:* Jelikož jsou $C_1, C_2$ otevřené, tak platí i po aplikaci $\sigma$ na $\mathcal{A}$. Platí-li $\{ A_1, \cdots \}\sigma[e]$, pak musí platit $C_2\sigma[e]$ neboť ta má tu část, která platí v negaci a tedy i $\mathcal{A} \models C[e]$, podobně pokud $\{ A_1, \cdots \}$ neplatí.

Je-li formule rezolucí zamítnutelná, je nesplnitelná

*Důkaz:* Nechť je $\square$ dokazatelný, pak z korektnosti rezolučního pravidla ve struktuře platí $\square$ a to je spor 

---

**Lifting lemma** - *rezoluční důkaz lze z VL zdvihnout do PL*

Získáme-li rezolventu základních instancí klauzulí po $\tau_1$ a $\tau_2$ je to i rezolventa původních klauzulí po aplikování $\tau_1 \tau_2$
Původní klauzule nemůžou obsahovat stejnou proměnnou

*Důkaz:* Předpokládejme rezolventu základních instancí $C^*$ přes literál $P(t_1, \cdots, t_k)$ a tedy po substituci $\tau_1$ dostaneme $\{ P(t_1), \cdots \}$ z $\{ A_1 , \cdots \}$ a po $\tau_2$ to samé v negaci z $\{ \neg B_1, \cdots \}$. A je-li $\sigma$ $\text{mgu}$ (nejobecnější ...) pro množinu $\{A_1, \cdots, B_1, \cdots\}$, pak sjednocení ... je rezolventa. Navíc $\tau_1 \tau_2 = \sigma(\tau_1 \tau_2)$ a tedy $C\tau_1 \tau_2 = \cdots = C^*$

Je-li formule nesplnitelná, je z ní dokazatelný $\square$

*Důkaz:* Je-li nesplnitelné je nesplnitelná i množina základních instancí. Můžeme zamítnout a pak $\square$ zdvihnout 

---

## Otázka #11:

> Elementární ekvivalence, důsledky L.-S. vety. Izomorfismus a sémantika.



---

## Otázka #12:

> Invariance definovatelných množin na automorfismy. 



---

## Otázka #13:

> $\omega$-kategoričnost, podmínky pro konečnou a otevřenou axiomatizovatelnost