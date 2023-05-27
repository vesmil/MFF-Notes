# Výroková logika

_Poznámky založené na [nové přednášce](https://jbulin.github.io/teaching/fall/nail062/)._

## Pojmy

[TOC]

### Model ve výrokové logice, pravdivostní funkce výroku.

> **Jazyk** - množina prvovýroků $\mathbb{P}$, logické spojky ($\vee,\wedge,\neg,$ ...) a závorky
> 
> **Výrokové formule** (výroky) a jejich hodnoty - induktivně def. (prvek, negace, ...)
> 
> **Teorie** - množina výroků (axiomů) v $\mathbb{P}$ neboli podmnožina $VF_\mathbb{P}$
> 
> **Booleovská funkce** - $\left\lbrace0,1\right\rbrace^n \rightarrow \left\lbrace0,1\right\rbrace$

**Pravdivostní funkce** výroku $\varphi$ v konečném jazyce je $f_{\varphi,\mathbb{P}}: \left\lbrace0,1\right\rbrace^{|\mathbb{P}|} \rightarrow \left\lbrace0,1\right\rbrace$:

* Je-li $\varphi$ $i$-tý prvek, pak $f_{\varphi,\mathbb{P}}(x_0, \ldots, x_{n-1}) = x_i$

* Je-li $\varphi = \neg \varphi'$ pak $f_{\varphi,\mathbb{P}}(x_0, \ldots, x_{n-1}) = f_{\neg}\left(f_{\varphi',\mathbb{P}}\left(x_0, \ldots, x_{n-1}\right)\right)$

* Je-li $\varphi = \varphi_1 \ \square \ \varphi_2$ pak $f_{\varphi,\mathbb{P}}(x_0, \ldots, x_{n-1}) = \ldots$

Závisí tedy pouze na proměnných z $\text{Var}(\varphi) \subseteq \mathbb{P}$

**Model** je libovolné ohodnocení prvovýroků $v: \mathbb{P} \rightarrow \left\lbrace0,1\right\rbrace$, třída všech modelů $M_\mathbb{P}$ ...

Říkáme, že $v$ je modelem teorie $T$ pokud každý axiom ve $v$ platí neboli $v \models T$

### Sémantické pojmy (pravdivost, lživost, nezávislost, splnitelnost) v logice, vzhledem k teorii.

> Platnost v modelu znamená, že $f_{\varphi,\mathbb{P}}(v) = 1$

* **Pravdivý** - Platí ve všech modelech (značí se $\models \varphi$)

* **Lživý** - Neplatí v žádném modelu ($\not\models \varphi$)

* **Nezávislý** - Není pravdivý ani lživý nebo-li $\emptyset \subsetneq M_\mathbb{P}(\varphi) \subsetneq M_\mathbb{P}$

* **Splnitelný** - $M_\mathbb{P}(\varphi) \neq \emptyset$

**Vzhledem** k teorii - omezíme se pouze na modely teorie - $M_\mathbb{P}(T, \varphi)$

Predikátová logika viz [Pravdivost ve struktuře](### Pravdivostní hodnota formule ve struktuře při ohodnocení, platnost formule ve struktuře.).

### Ekvivalence výroku resp. výrokových teorií, $T$-ekvivalence.

Výroky jsou ekvivalentní pokud mají stejné modely $\varphi \sim \psi \Leftrightarrow M_\mathbb{P}(\varphi) = M_\mathbb{P}(\psi)$

Teorie jsou ekvivalentní pokud jsou navzájem extenzí - stejné modely a jazyk

Opět $T$-ekvivalenci získáme jako omezení na modely teorie...

### Sémantické pojmy o teorii (sporná, bezesporná, kompletní, splnitelná).

* **Sporná** - nemá ani jeden model, platní v ní všechny výroky

* **Bezesporná** (splnitelná) - má alespoň jeden model, není sporná

* **Kompletní** - právě jeden model, každý výrok je v ní buď lživý nebo sporný

### Extenze teorie (jednoduchá, konzervativní), odpovídající sémantická kritéria.

> **Množina všech důsledků** $Csq(T)$ jsou ty výroky z $VF_\mathbb{P}$, které platí v teorii $T$

Teorie $T$ v jazyce $\mathbb{P}$ je extenzí $T'$ v $\mathbb{P'}$ pokud platí

* $\text{Csq}(T) \subseteq \text{Csq}(T')$ nebo-li $M_{\mathbb{P}'}(T') \subseteq M_{\mathbb{P}'}(T)$

* $\mathbb{P} \subseteq \mathbb{P}'$ 

Jinými slovy restrikce libovolného modelu $T'$ musí být modelem $T$

**Jednoduchá** - nezmění jazyk, $\mathbb{P} = \mathbb{P}'$ 

**Konzervativní** - nepřidá důsledky
Tedy každý model $T$ lze nějak expandovat do $\mathbb{P}'$ (nebo-li každý z $T$ lze získat restrikcí)

### Tablo z teorie, tablo důkaz.

**Tablo z teorie** $T$ je označkovaný binární strom který lze zkonstruovat konečnou posloupností následujících pravidel

1. Jednoprvkový strom je položka ($T \varphi$ nebo $F \varphi$)

2. Pokud je na větvi $V$ položka $P$, tak na konec $V$ můžeme připojit její atomické tablo

3. Na konec libovolné větve lze také připojit $T \alpha$ pro libovolný axiom z $T$

Tablo položky $P$ znamená tablo s $P$ v kořeni

**Tablo důkaz** $\varphi$ z $T$ je sporné tablo z teorie $T$ s $F \varphi$ v kořeni (znač. $T \vdash \varphi$) a tablo zamítnutí je sporné tablo s $T \varphi$ v kořeni

Tablo je sporné pokud každá jeho větev je sporná - obsahuje $T \varphi$ a $F \varphi$

Větev je dokončená pokud je sporná nebo pokud je každá položka na něm redukovaná a zároveň obsahuje každý axiom $T$

Položka $p$ je redukovaná pokud je kořen atomického tabla na $V$ nebo je prvovýrok

### Kanonický model.

Máme-li dokončené bezesporné tablo, pak kanonickým modelem rozumíme ohodnocení $v$ takové, že $v(\varphi) = 1$ právě když $T \varphi \in V$

Pro bezespornou dokončenou větev se shoduje s $V$ - ukáže se indukcí

V predikátové logice viz. [Korektnost tablo metody](### Věta o korektnosti tablo metody v predikátové logice.)

### Kongruence struktury, faktorstruktura, axiomy rovnosti.

**Kongruence struktury** je ekvivalence, která splňuje všechny kongruence

* Pro funkce - pro všechna $x_i \sim y_i$ platí $f(x_1, \cdots, x_n) \sim f(y_1, \cdots, y_n)$

* Pro relace - pro ... platí $R(x_!,\cdots, x_n) \Leftrightarrow R(y_1, \cdots, y_n)$

**Faktorstruktura** je pak struktura s univerzem všech rozkladových tříd podle $\sim$
Její funkce jsou následně definované pomocí reprezentantů

$$
f^{\mathcal{A}/\sim}([x_1]_\sim, \ldots) = [f^\mathcal{A}(x_1, \ldots)]_\sim
$$

**Axiomy rovnosti** - podobně, $x=x$, relace... a funkce:

$$
x_1 = y_1 \ldots \Rightarrow f(x_1, \ldots, x_n) = f(y_1, \ldots, y_n)
$$

### CNF a DNF, Hornův tvar. Množinová reprezentace CNF formule, splňující ohodnocení.

> **Literál** - prvovýrok nebo jeho negace
> 
> **Elementární konjunkce** - konjunkce literálů
> 
> **Klauzule** - disjunkce literálů

**DNF** - disjunkce elementárních konjunkcí

**CNF** - konjunkce klauzulí

**Hornův tvar** - má-li každá klauzule v CNF nejvýše jeden pozitivní literál
Fakt - jeden pozitivní, pravidlo - alespoň jeden pozitivní a cíl - jenom negativní

**Množinová reprezentace** znamená, že klauzule budeme zapisovat jako množiny

**Splňující ohodnocení** nebo-li model - pokud obsahuje nějaký literál z každé formule

### Rezoluční pravidlo, unifikace, nejobecnější unifikace.

Mějme klauzule $C_1$ a $C_2$ a literál $\mathcal{l}, \overline{\mathcal{l}}$ potom rezolventa těchto klauzulí je klauzule

$$
C = \left\lbrace C_1 \backslash \left\lbrace\mathcal{l} \right\rbrace \cup C_2 \backslash \left\lbrace\overline{\mathcal{l}} \right\rbrace \right\rbrace
$$

Substituce $\sigma = \left\lbrace x_1/t_1, \ldots \right\rbrace$. kde $x$ není rovno $t$ (*základní* má konstantní termy, *přejmenování* je pro $t$ různé proměnné)

Skládání substitucí je množina 

$$
\sigma_{\tau} = \left\lbrace {x_i}/{t_i \tau} \bigg| x_i \in X, x_i \neq t_i \tau \right\rbrace \cup 
\left\lbrace {y_j}/{s_j} \bigg| y_j \in Y \setminus X \right\rbrace
$$

**Unifikace** pro množinu $S = \left\lbrace E_1, \ldots, E_n\right\rbrace$ je substituce $\sigma$ t.ž. $E_1\sigma = \ldots = E_n \sigma$

Nejobecnější je potom když pro každou unifikaci $\tau$ existuje $\lambda$ t.ž. $\tau = \sigma \lambda$

### Rezoluční důkaz a zamítnutí, rezoluční strom.

Rezoluční důkaz je konečná posloupnost klauzulí t.ž. $C_i$ je rezolventou $C_j, C_k$

Pokud lze dokázat $\square$ z $\varphi$, tak je rezolucí zamítnutelná

Rezoluční strom je ... pro který platí následující pravidla

- kořen C, listy jsou klauzule z $S$ a v každém vnitřním rezolventa synů

### Lineární rezoluce, lineární důkaz, LI-rezoluce, LI-důkaz.

Lineární rezoluce je posloupnost $(C_1, B_1), \ldots, C$, kde ...

LI-rezoluce pak omezí $B_!$ čistě na vstup, je to úplné pro Hornovy formule

### Signatura a jazyk predikátové logiky, struktura daného jazyka.

Dvojice $\langle \mathcal{R,F} \rangle$ disjunktních množiny symbolů (relační a funkční včetně konstantních) spolu s aritami a bez symbolu "$=$"

Struktura je potom trojice $\mathcal{A} = \langle \mathcal{A, R^A, F^A} \rangle$, kde $\mathcal{A}$ je neprázdná množina (nazýváme univerzum či doména), $\mathcal{R^A}$ je interpretace relačního symbolu a ...

Jazyk - signatura, rovnost, spočetně mnoho proměnných, rel. funkc. a konst. symboly, kvantifikátory a logické spojky

### Atomická formule, formule, sentence, otevřená formule.

> **Term** je každá proměnná a konstantní symbol z $L$, a zároveň $f(t_1,\cdots,t_n)$

Atomická formule je nápis $R(t_1, \ldots, t_n)$, kde $R$ je $n$-ární relační symbol

Formule je pak vytvořena pomocí logických spojek, kvantifikátorů, ...

**Uzavřená formule (sentence)** neobsahuje volné proměnné

**Otevřená formule** neobsahuje kvantifikátory

Výskyt je vázaný je-li součástí podstromu... jinak je volný

### Instance formule, substituovatelnost, varianta formule.

Term $t$ je substituovatelný za proměnnou $x$ ve .. pokud po nahrazení všech výskytů $x$ za $t$ nevzinkne žádný vázaný výskyt proměnné z $t$

Formule vzniklá substitucí se nazývá instance $\varphi(x/t)$

Varianta pak je nahrazení $(Qx)\varphi$ za $(Qy)\varphi(x/y)$ v případě, že $y$ nemá volný vyskyt ve $\varphi$ a zároveň je substituovatelné za $x$

### Pravdivostní hodnota formule ve struktuře při ohodnocení, platnost formule ve struktuře.

* **Model jazyka** je libovolná struktura (soubor všech je pak třída)

* **Ohodnocení** je fce. která převede proměnné na členy struktury

* **Hodnota termu** při ohodnocení $t^\mathcal{A}[e]$ je dána induktivně (proměnná, konst, fce)

Formule v jazyce, ohodnocení - $PH^{\mathcal{A}}(\varphi)[e]$ je definována induktivně  
Atomická formule je $1$ pokud $(t_1^\mathcal{A}[e], \cdots) \in R^\mathcal{A}$, negace, operátory, ...

Platnost ve struktuře při ohodnocení znamená, že $PH^{\mathcal{A}}(\varphi)[e] = 1$ nebo-li $\mathcal{A} \models \varphi(e)$

Pokud platí platí při každém ohodnocení, říkáme, že je pravdivá

### Kompletní teorie v predikátové logice, elementární ekvivalence.

Teorie je kompletní, je-li bezesporná a každá sentence je v ní buď lživá nebo pravdivá

Neplatí, že by měla jediný model - těch má nekonečně - až na elementární ekvivalenci 

Struktury jsou elementárně ekvivalentní ($\equiv$) pokud v nich platí téže sentence

### Podstruktura, generovaná podstruktura, expanze a redukt struktury.

Podstruktura ... jestliže $\emptyset \neq B \subseteq A$, z $R^\mathcal{B} = R^\mathcal{A} \cap B^{Ar(R)}$ a funkce podobně...

Mnžoina je univerzium podstruktury právě když, že je uzavřená na funkce včetně konstantních (také restrikce)

Platí věta podobná kompaktnosti...

Nejmenší podmnožina $\mathcal{B}$, která obsahuje $X$ a je uzavřená je univerzem generované podstruktury

**Expanze a redukt** pak pro $L \subseteq L'$ na stejné doméně znamená, že interpretace funkčních i relačních symbolů společných pro $L$ i $L'$ musí být stejná.

### Definovatelnost ve struktuře.

Formuli s jednou volnou proměnnou můžeme chápat jako množinu prvků, které mají určitou vlastnost, dvě pak jako relaci. Obecně potom množina definovaná formulí je:

$$
\varphi^{\mathcal{A}}\left(x_1, \ldots, x_n\right)=\left\{\left(a_1, \ldots, a_n\right) \in A^n \mid \mathcal{A} \models \varphi\left[e\left(x_1 / a_1, \ldots, x_n / a_n\right)\right]\right\}
$$

Zkráceně totéž zapíšeme také jako $\varphi^{\mathcal{A}}(\bar{x})=\left\{\bar{a} \in A^n \mid \mathcal{A} \models \varphi[e(\bar{x} / \bar{a})]\right\}$.

Pro formule $\varphi(\bar{x}, \bar{y})$, kde $|\bar{x}|=n$ a $|\bar{y}|=k$, strukturu $\mathcal{A}$ v témž jazyce, a $k$-tici prvků $\bar{b} \in A^k$. Množina definovaná formulí $\varphi(\bar{x}, \bar{y})$ s parametry $\bar{b}$ ve struktuře $\mathcal{A}$, je:

$$
\varphi^{\mathcal{A}, \bar{b}}(\bar{x}, \bar{y})=\left\{\bar{a} \in A^n \mid \mathcal{A} \models \varphi[e(\bar{x} / \bar{a}, \bar{y} / \bar{b})]\right\}
$$

### Extenze o definice.

* Relační symboly - ..
* Funkční symboly - ...
* Konstantní symboly - ...

Viz. [vlastnosti](### Vlastnosti extenze o definice.)

### Prenexní normální forma, Skolemova varianta.

Prenexní norma má kvantifikátory na začátku

Skolemizace je převod otevřené formule na uzavřenou

### Izomorfismus struktur, izomorfní spektrum, ω-kategorická teorie.

...

### Axiomatizovatelnost, konečná axiomatizovatelnost, otevřená axiomatizovatelnost.

Teorie je axiomatizovatelná pokud...

### Rekurzivní axiomatizace, rekurzivní axiomatizovatelnost, rekurzivně spočetná kompletace.

Pokud existuje algoritmus, který doběhne a rozhodne zda $\varphi \in T$

Pokud nějaká množina kompletních extenzí je rekurzivně spočetná...

### Rozhodnutelná a částečně rozhodnutelná teorie.

Rozhodnutelná pokud doběhne algoritmus na $T \models \varphi$

Částečně rozhodnutelná - algoritmus nemusí doběhnout na $T \not\models \varphi$

---

## Lehké otázky

### Množinu modelů nad konečným jazykem lze axiomatizovat výrokem v CNF, výrokem v DNF.

Množina spojek je univerzální pokud výrokem z nich lze reprezentovat každou booleovskou funkci. To je ekvivalentní k tomu, že pro každou množinu $M \in M_\mathbb{P}$ musí existovat $\varphi$ t.ž. $M_\mathbb{P}(\varphi) = M$ (to plyne z $M = f^{-1}[1]$ a pak $f_{\varphi,\mathbb{P} = f} \Leftrightarrow \ldots$)

Pokud by $M$ obsahovala jeden model, mohli bychom ho vytvořit $\varphi_v = \bigwedge_{p \in \mathbb{P}} p^{v(p)}$

Následně, pokud by modelů bylo více

$$
\varphi_M = \bigvee_{v \in M} \bigwedge_{p \in \mathbb{P}} p^{v(p)}
$$

...long story short pro libovolnou množinu modelů $K$ máme

$$
M_{\mathbb{P}}\left(\bigvee_{\nu \in K} \bigwedge_{p \in \mathbb{P}} p^{\nu(p)}\right)=K=M_{\mathbb{P}}\left(\bigwedge_{\nu \in \bar{K}} \bigvee_{p \in \mathbb{P}} p^{1-{\nu(p)}}\right)
$$

První plyne z pozorování výše, druhé pak z duality... či separátní pozorování

Alternativně lze použít převod úpravami, který se dokáže indukcí

### Algebra výroků bezesporné teorie nad konečným jazykem je izomorfní potenční algebře.

Nechť ... na faktorizaci $VF_{\mathbb{P}}/\sim_T$ lze zadefinovat operace podle reprezentantů...

$$
AV^{\mathbb{P}}(T) = \langle V F_{\mathbb{P}} / \sim_T , \neg, \wedge, \vee, \bot, \top \rangle
$$

Kde operace jsou definovány jako $[\varphi]_{\sim_T} \land [\psi]_{\sim_T} = [\varphi \land \psi]_{\sim_T}$ ...

Potom je funkce $h([\varphi]_{\sim_T}) = M(T, \varphi)$, která výroku přiřazuje modely korektně definovaná prostá funkce $h: VF_{\mathbb{P}}/\sim_T \rightarrow \mathcal{P}(M(T))$ 

Navíc je pro konečné $M(T)$ na (surjektivní)

Následně platí

$$
...
$$

$$
h(\neg[\varphi]_{\sim_T}) = M(T) \setminus M(T, \varphi) \\ \ \\
h([\varphi]_{\sim_T} \land [\psi]_{\sim_T}) = M(T, \varphi) \cap M(T, \psi) \\ \ \\ 
h([\varphi]_{\sim_T} \lor [\psi]_{\sim_T}) = M(T, \varphi) \cup M(T, \psi) \\ \ \\
h([\bot]_{\sim_T}) = \emptyset, \quad h([\top]_{\sim_T}) = M(T)
$$

### 2-SAT, Algoritmus implikačního grafu, jeho korektnost.

Výrok je 2-CNF pokud každá jeho klauzule má nejvýše 2 literály

Implikační graf $\varphi$ v 2-CNF je graf dle následujících pravidel

* Vrcholy jsou $p$ a $\neg p$ pro každý ...

* Klauzuli $l_1 \vee l_2$ reprezentujeme dvojicí hran $\overline{l_1} \rightarrow l_2$ a $\overline{l_2} \rightarrow l_1$

* Klauzuli $l_1$ ...

Ohodnocení z něj získáme tak, že provedeme kontrakci hran silně souvislých komponent - graf $G^*_\varphi$ - ve kterém dle topologického uspořádání budeme nastavovat komponenty na $0$ a v opačné na $1$

$\varphi$ je splnitelný právě když žádná komponenta silné souvislosti neobsahuje dvojici opačných literálů

*Důkaz:*  víme, že prvovýroky v komponentě musí být ohodnocena stejně, protože jinak by existovala implikace... a tedy nemůže obsahovat dvojici opačných

Naopak ukážeme, že z $G^*_\varphi$ získáme model, pokud by naše ohodnocení neplatilo znamenalo by to, že neplatí nějaká klauzule. Oboje musí platit, protože pořadí...

### Horn-SAT, Algoritmus jednotkové propagace, jeho korektnost.

Výrok je hornovský pokud každá jeho klauzule má nejvýše jeden pozitivní literál

Algoritmus pro polynomiální...

1. Pokud obsahuje dovjici opačných - není řešitelný

2. Pokud obsahuje jednotkovou - ohodnoť na 1

3. Pokud neobsahuje jednotkovou - ohodnoť vše na $0$

Výrok získaný jednotkovou propagací je splnitelný právě když původní je splnitelný

Algoritmus je korektní, protože ze 3. kroku získáme validní ohodnocení díky hornově tvaru neboť každá klauzule obsahuje negativní literál

### Algoritmus DPLL pro řešení SAT.

Definujeme čistý výskyt - pokud klauzule obsahují $l$ a ne $\overline{l}$ 

Algoritmus je obdobný s tou výjimkou, že po odstranění jednotkových, odstraňujeme čisté výskyty, až nám dojdou i ty tak rekurzí rozvětvíme, v nejhorším případě je tedy exponenciální

Navíc je tam podmínka, že pokud obsahuje prázdnou klauzuli, tak není splnitelný

Opět 

### Věta o konstantách.

Mějme formuli $\varphi$, potom nahrazení volných proměnných za konstantní symboly má stejnou splnitelnost

TODO pomocí expanzí a reduktů...

### Vlastnosti extenze o definice.

Str. 90

Konzervativní extenze...

### Vztah definovatelných množin a automorfismů.

### Tablo metoda v jazyce s rovností.

**V predikátové logice** - nutné nadefinovat položky typu "svědek" a "všichni", ty lze použít při vytváření atomických tabel (c_i \in C a libovolný L_C term)

Je potřeba změnit i definici redukovanosti - i-tý výskyt položky typu všichni je redukovaný pokud je na V také (i+1)-výskyt a na V se vyskytuje T(x/t_i) resp. ...

**Jazyku s rovností** - nutnost rozšířit o generální uzávěry axiomů rovnosti

...

### Věta o kompaktnosti a její aplikace.

Teorie $T$ má model právě, když každá její konečná část má model

$\Rightarrow$ Triviálně vezmeme model $T$

$\Leftarrow$ Sporem, pokud teorie nemá model, pak je z ní dokaztelný $\bot$ a to konečným table. V tom se ale vyskytuje pouze konečně mnoho axiomů z $T$

Aplikace - bipartitní podgrafy $\mathbb{P} = V(G)$ a $T = \{  \}$

### Věta o korektnosti rezoluce ve výrokové logice.

### Věta o korektnosti rezoluce v predikátové logice.

Postup:

- Nejdříve musíme redukovat otázku na splnitelnost otevřené teorie
  
  - Prenexní tvar (převede kvantifikátory na začátek)
  
  - Generální uzávěr (odstraní volné)
  
  - Skolemova varianta (odstraní existenční kvantifikátor novou funkcí)
  
  - Odstranění kvantifikátorů

- Takto vytvořená teorie (otevřená konzervativní extenze) je ekvisplnitelná

- Grounding -

### Souvislost stromu dosazení a splnitelnosti CNF formule.

### Unifikační algoritmus (korektnost stačí vyslovit).

### Nestandardní model přirozených čísel.

Nechť $\underline{\mathbb{N}}=\left\langle \mathbb{N}, S, +, \cdot, 0, \leq \right\rangle$ a $Th(\underline{\mathbb{N}})$ je množina všech pravdivých sentencí...
Dále definujeme $n$-tý numerál jako $S(\ldots S(0)\ldots)$ do této teorie přidáme novou sentenci.

Vezmeme konstantí symboi $c$ a vyjádříme, že je ostře větší než každý $n$-tý numerál

Zjevně každá konečná část teorie má model - a tedy i celá teorie.

### Kompletní jednoduché extenze DeLO*.

Str. 135

Teorie hustého lineárního uspořádání...

### Existence spočetného algebraicky uzavřeného tělesa.

Str. 137

### Tělesa charakteristiky 0 nejsou konečně axiomatizovatelná.

Str. 142

### Kritérium otevřené axiomatizovatelnosti.

### Rekurzivně axiomatizovaná teorie je částečně rozhodnutelná, kompletní je rozhodnutelná.

### Teorie konečné struktury v konečném jazyce s rovností je rozhodnutelná.

### Gödelovy věty o neúplnosti a jejich důsledky (bez důkazů).

---

## Těžké otázky

### Věta o korektnosti tablo metody ve výrokové logice.

Shodovat s položkou znamená, že $P = T \varphi$ a $v \models \varphi$ nebo ...

Shoduje-li se model s položkou v kořeni, potom se shoduje s některou větví

- Indukcí podle konstrukce tabla najdeme prvky větve

- Pokud jsme neprodloužili větev, pokud jsme přidali axiom a pokud jsme přidali atomické tablo pro položku $P$, tak lze nalézt...

Je-li formule tablo dokazatelná z $T$, pak je v $T$ pravdivá

Dokážeme sporem, nechť $\varphi$ je tablo dokazatelná, ale existuje model $v$ ve kterém naplatí. Na základě předchozí věty, jelikož se položka shoduje s $v$, existuje větev, která se shoduje s $v$. To ale není možné neboť každá větev je sporná.

### Věta o korektnosti tablo metody v predikátové logice.

Nejdříve nadefinujeme kanonický model.

> L_C je rozšíření jazyka L o spočetně mnoho konstantních symbolů

**V predikátové logice** - je to L_C struktura $\mathcal{A}=\left\langle A, \mathcal{F^A \cup C^A, R^A} \right\rangle$ definována:

- Doména $A$ je množina všech konst, termů

- Pro každý n-ární relační symbol $("s_1", \ldots, "s_n") \in \mathcal{R^A}$ pokud $\text{T}R(\ldots) \in V$

- Pro ... funkční symbol $f("s_1", \ldots, "s_n") = "f(s_1, \ldots, s_n)"$

Pro jazyk s rovností dále musíme definovat relaci $=^B$ podle $\text{T}s_1 = s_2$ a kanonický model pak definujeme jako faktorstrukturu

### Věta o úplnosti tablo metody ve výrokové logice.

Str. 53

Každé dokončené tablo s $F\varphi$ je sporné...

### Věta o úplnosti tablo metody v predikátové logice.

Str. 105

### Věta o konečnosti sporu, důsledky o konečnosti a systematicnosti důkazů.

### Věta o úplnosti rezoluce ve výrokové logice.

Str. 62

Využijeme kompaktnost

### Věta o úplnosti LI-rezoluce pro výrokové Hornovy formule.

Str. 63 a 131

### Věta o úplnosti rezoluce v predikátové logice (Lifting lemma stačí vyslovit)

Str. 129

### Skolemova věta.

Každá teorie má otevřenou konzervativní extenzi

...

### Herbrandova věta.

Str. 121

$L$-struktura je Herbarndův jazyk jestliže $A$ je množina všech konstantních $L$-termů

### Löwenheim-Skolemova věta včetně varianty s rovností, jejich důsledky.

Str. 110 a 136

### Vztah izomorfismu a elementární ekvivalence.

Str. 138

### ω-kategorické kritérium kompletnosti.

Str. 140

### Neaxiomatizovatelnost konečných modelů.

Str. 141

### Věta o konečné axiomatizovatelnosti.

Str. 142

### Rekurzivně axiomatizovaná teorie s rekurzivně spočetnou kompletací je rozhodnutelná.

Str. 147

### Nerozhodnutelnost predikátové logiky.

Str. 149
