# Automaty a gramatiky

[TOC]



> 1. Přednáška

## Úvod

...

## Chomeského hierarchie

### Chomského hierarchie

| Typ  | Gramatiky                             | Automat             | Pravidla                                        | Příklad                         |
| ---- | ------------------------------------- | ------------------- | ----------------------------------------------- | ------------------------------- |
| 0    | Rekurzivně spočetné - $\mathcal{L}_0$ | Turingův stroj      | $\gamma\rightarrow \alpha$                      | ...                             |
| 1    | Kontextové (mono) - $\mathcal{L}_1$   | Ohraničený Turingův | $\alpha A\beta \rightarrow \alpha \gamma \beta$ | $L=\{a^{n}b^{n}c^{n} | n > 0\}$ |
| 2    | Bezkontextové  - $\mathcal{L}_2$      | Zásobníkový automat | $A \rightarrow \alpha$                          | $L=\{a^{n}b^{n}| n > 0\}$       |
| 3    | Regulární - $\mathcal{L}_3$           | Konečný automat     | $A \rightarrow a$, $A \rightarrow aB$           | $L=\{a^{n}|n \geq 0\}$          |

kde:

- $a$ je terminál
- $A,B$ jsou neterminály
- $\alpha, \beta, \gamma$ jsou posloupnosti terminálů nebo/a neterminálů, přičemž $\gamma$ nemůže být prázdná

Detaily později

## Deterministický konečný automat (DFA)

...je uspořádaná pětice $A = (Q, \Sigma, \delta, q_0, F)$ 

* Konečná množina stavů $Q$
* Konečná neprázdná množina vstupních symbolů (abecedy) $\Sigma$
* Přechodová funkce $\delta$ (zobrazení $Q\times \Sigma \rightarrow Q$, reprezentované hranami grafu nebo tabulkou)
* Počáteční stav $q_0 \in Q$
* Neprázdná množina koncových stavů $F \subseteq Q$

### Úvodní Pojmy

**Slovo** $s$ - konečná posloupnost symbolů ze $\Sigma$ (může být i prázdné $\epsilon$ nebo $\lambda$)
**Množina všech slov** $\Sigma^*$ (neprázdných $\Sigma^+$)
**Jazyk** $L$ - množina slov v abecedě

**Operace se slovy** - zřetězení $uv$, mocnina $u^n$, délka $|u|$, počet výskytů $|u|_s$

**Rozšířená přechodová funkce** $\delta^*$ - def. induktivně jako $\delta^*(q, \lambda) = q$ a $\delta^*(q,wx) = \delta^*(\delta^*(q,w),x)$

**Jazyk rozpoznávaný konečným automatem** - je $L(A) = \set{w\ | \ w \in ... \and \delta*(q_0, w) \in F}$ 

**Stav je dosažitelný** pokud $\exists w : \delta(q_0, u_0) = u$...

Slovo je **přijímáno**...
Jazyk je **rozpoznatelný**...

**Třidu** jazyků rozpoznatelných konečnými automaty značíme $\mathcal{F}$

### Pumping lemma

Pro každý regulární jazyk existuje $n$ t.ž. slovo $w$ delší než $n$ (počet stavů automatu) můžeme rozdělit na tři částí $xyz$ t. ž.

* $y \neq \lambda$
* $|xy| \leq n$
* $\forall k: xy^k z \in L$

*Důkaz:* Regulární jazyk a tedy existuje DFA s $n$ stavy a $L=L(A)$... nějaký stav se zopakuje a tu smyčku exploitnu

**Důsledek:** Jazyk slov se stejným počtem jedniček jako nul není regulární

*Důkaz:* Předpokládejme, že je regulární, vezmu $n$, rozdělím $w = 0^n 1^n$ na $xyz$ a protože $|xy| \leq n$	

**Druhý důsledek:** Jazyk slov $1^p$, kde $p$ je prvočíslo ($\geq n+2$) není regulární...

> 2. Přednáška

### Součin automatů...

### Kongruence

Relace $\sim$ když mám dvě slova ve stejné třídě a přidáním $w \in \Sigma^*$ dostanu slova opět ze společné třidy

*Konečného indexu* znamená, že rozklad na třídy ekvivalence má konečný počet tříd

### Myhill-Nedorova věta

V regulárním jazyce existuje pravá kongruence tak, že $L$ je sjednocení tříd rozkladu

*Z automatu kongruence:* podle stavů je dělení (kongruence je rozšířená přechodová funkce)
*Z kongruence automat:* podle dělení jsou stavy...

**Pumpovatelný neregulární jazyk**  - např. $L = \{ u \ | u = a^+ b^i c^i\ \vee u = b^i c^i \}$...

**Nekonečnost regulárního jazyka** - nekonečný jazyk je ekvivalentní s existencí slova délky mezi $n$ a $2n$...

### Automatový homomorfismus

Automat přijímací jazyk není jednoznačný...

Zavedeme homomorfismus -	$h(q_0) = q'_0$,	$h(\delta_1(q,w)) = \delta_2(h(q, w)),$		$q \in F_1 \Leftrightarrow h(q) \in F_2$

### Ekvivalence

Automaty jsou **ekvivalentní **rozpoznávají-li stejný jazyk
Existuje-li homomorfismus, pak jsou ekvivalentní - *důkaz* triviálně postupně aplikovat pravidla homomorfismu na $w \in F_1$

### Minimalizace DFA

Stavy $q,p$ jsou ekvivalentní pokud $\forall w : q^*(p,w) \in F \Leftrightarrow q^*(q,w) \in F$, jinak jsou rozlišitelné

**Algoritmus na hledaní rozlišitelných** - přijímací a nepřijímací jsou rozlišitelné, následně induktivní postup

...

Automatu je **redukovaný** pokud nemá nedosažitelné stavy a žádné dva nejsou ekvivalentní (**redukt...**)

Redukované ekvivalentní automaty jsou ismorfní

#### Vladanův algoritmus na redukci

Tabulka - všechny stavy na řádky, na sloupce $n$-tá ekvivalence a po ní vždy všechny vstupní znaky

Ekvivalence podle délky rozlišitelnosti suffixů
Nultá ekvivalence - ekvivalentní jsou si konečné stavy
$n$-tá ekvivalence - po přidání všech písmen dostanu ekvivalentní stavy

Jednoprvkové třídy zjemňovat nemusíme...

> 3. Přednáška

## Nedeterministické konečné automaty

Stále jen regulární jazyky, akorát nám usnadní návrh

Ve více stavech je paralelně... nebo-li přechodová funkce vrací podmnožinu stavů

**Rozšířená přechodová funkce** - Induktivně definované sjednocení

Pro příjem zavádíme, že průnik výsledku rozšířené přechodové funkce a přijímacích stavů je neprázndný

### Převod NFA na DFA (podmnožinová konstrukce)



### Konečné automaty s lambda přechody

Dovolíme přechody bez přečtení symbolu...



### Množinové operace nad jazyky

> 4. Přednáška

> 5. Přednáška

> 6. Přednáška

### Palindromy

Z pumping lemma nejsou regulární

## Formální (generativní) grmatika

terminály, neterminály, počátek, pravidla

...
