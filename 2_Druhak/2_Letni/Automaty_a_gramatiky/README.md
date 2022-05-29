# Automaty a gramatiky

> 1. Přednáška

## Úvod

### Historie...

### Dělení

|                      Automat                      |            Gramatika             |
| :-----------------------------------------------: | :------------------------------: |
| Turingovy stroje (nedeterministické, vícepáskové) |              Typ 0               |
|             Lineárně omezené automaty             | Kontextové a monotónní gramatiky |
|               Zásobníkově automaty                |     Bezkontextové gramatiky      |
|     Konečné automaty (DFA, NFA, $\lambda$NFA)     |       Regulární gramatiky        |



### Praktické využití, příklady, ...

### Deterministický konečný automat (DFA)

Je konečná pětice $A = (Q, \Sigma, \delta, q_0, F)$ 

* Konečná množiny stavů $Q$
* Konečná neprázdná množina vstupních symbolů (abecedy) $\Sigma$
* Přechodová funkce $\delta$
  * Zobrazení $Q\times \Sigma \rightarrow Q$, reprezentované hranami grafu (nebo tabulkou)
* Počáteční stavu $q_0 \in Q$ (vede do něj šipka ’odnikud’)
* Neprázdné množiny koncových (přijímajících) stavů (final states) $F \subseteq Q$, označených dvojitým kruhem či šipkou ’ven’.

### Pojmy

**Slovo** $s$ - konečná posloupnost symbolů ze $\Sigma$ (může být i prázdné $\epsilon$ nebo $\lambda$)
**Množina všech slov** $\Sigma^*$ (neprázdných $\Sigma^+$)
**Jazyk** $L$ - množina slov v abecedě

**Operace se slovy** - zřetězení $uv$, mocnina $u^n$, délka $|u|$, počet výskytů $|u|_s$

**Rozšířená přechodová funkce** $\delta^*$ - definujeme induktivně jako $\delta^*(q, \lambda) = q$ a $\delta^*(q,wx) = \delta^*(\delta^*(q,w),x)$ (takže logicky)

**Jazyk rozpoznávaný konečným automatem** - je $L(A) = \set{w\ | \ w \in ... \and \delta*(q_0, w) \in F}$ 
Slovo je **přijímáno**...
Jazyk je **rozpoznatelný**...

**Třida** jazyků rozpoznatelných konečnými automaty značíme $\mathcal{F}$

**Pumping lemma** - pro každý regulární jazyk existuje $n$ t. ž. slovo $w$ delší než $n$ můžeme rozdělit na tři částí $xyz$ t. ž.

* $y \neq \lambda$
* $|xy| \leq n$
* $\forall k: xy^k z \in L$

$n$ se volí jako počet stavů automatu

*Důkaz:* Mám regulární jazyk a tedy existuje DFA s $n$ stavy a $L=L(A)$... prostě se nějaký stav zopakuje, tak tu smyčku exploitnu

**Důsledek:** Jazyk slov se stejným počtem jedniček jako nul není regulární

*Důkaz důsledku:* Předpokládejme, že je regulární, vezmu $n$, rozdělím $w = 0^n 1^n$ na $xyz$ a protože $|xy| \leq n$	

**Druhý důsledek:** Jazyk slov $1^p$, kde $p$ je prvočíslo není regulární

...

> 2. Přednáška

### Kongruence

### Myhill-Nedorova věta

### Automatový homomorfismus

### Ekvivalence

### Minimalizace DFA

> 3. Přednáška

### Nedeterministické konečné automaty

### Rozšířená přechodová funkce

### Převod NFA na DFA

### Konečné automaty s lambda přechody

### Množinové operace nad jazyky

> 4. Přednáška

> 5. Přednáška

> 6. Přednáška

### Palindromy

Z pumping lemma nejsou regulární

## Formální (generativní) grmatika

terminály, neterminály, počátek, pravidla

...
