# Automaty a gramatiky

> 1. Cvičení

## Rychlý úvod

### Gramatiky

**Systém přepisovacích pravidel** - nalezení podslova z levé strany a náhrada pravou stranou
Rozdělení na **terminály** a **neterminály** - do jazyka patří slova pouze z terminálů

### Automaty

Negenerují jazyk, ale dokáží kontrolovat jestli slovo patří do jazyka

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

**Problém s generováním prázdného slova** - dá se obejít ze startovacího neterminálu

### Chomského normální forma

Převod na ní je ekvivalentní s tím, že jazyk je bezkontextový

* $A \rightarrow BC$
* $A\rightarrow a$
* $S \rightarrow \epsilon$

Dá se vyrobit odvozovací strom - ten se dá udělat podle určitých pravidel
Např. odvozování zleva, tomu odpovídá zásobníkový automat

Umožní nám zjistit počet odvození, to nám zajistí nějaký odhad na délku jedné větve v odvozovacím stromu a tedy opakování neterminálů...

### Pumping lemma

Je tedy zřejmé, že $\mathcal{L}_0 \subseteq \mathcal{L}_1 \subseteq \mathcal{L}_2 \subseteq \mathcal{L}_3$, ale otázka je zda to není rovnost

Dostatečně dlouhé slovo můžeme pumpovat - dá nám to příklad který není v $\mathcal{L}_3$

*Co to pumpování znamená?*  Pro $w \in L$ t. ž. $|w|\geq n$, můžeme $w$ rozdělit na $xyz$, tak aby $y \neq \lambda$, $|xy| \leq n, xy^*z \in L$

*Důkaz:* Když máme pro konečný automat slovo delší než počet stavů, tak se některý opakuje
Cestu která se opakuje můžeme opakovat pořád dokola a dostaneme slovo z jazyka

> 2. Cvičení

## Typ 1

### Konečné automaty

*Příklad s automatem pro detekcí Bára a Tera, determinizování žumpou a jeho následná redukce*

#### Algoritmus pro redukci automatu

Tabulka - všechny stavy na řádky, na sloupce ekvivalence a to co budu přidávat

Ekvivalence podle délky rozlišitelnosti suffixů
První ekvivalence - ekvivalentní jsou si konečné stavy
$n$-tá ekvivalence - přidáním písmena dostanu ekvivalentní stavy

Jednoprvkové třídy zjemňovat nemusíme

Odzadu to postavím a ověřím to dostáváním do konečného stavu

### Nerodova věta

*Příklad s redukcí nekonečného automatu, který přijímá slovo z nul jejichž počet je dělitelný 3*

Z redukce, která nám dá konečný počet stavů, získáme konečný automat

### Příklady

Máme čtyřstavový automat a vím, že $a^5 \in L$, co vím o $a_{16}$, $a_{17}$, $a_{18}$?

* Vypozoruji, že se automat zacyklí. Potom podle délek cyklu zjistím, že nic nemůžu říct o $a_{16}$ a $a_{18}$
  Naopak z toho, že rozdíl mezi $17$ a $5$ je $12$, můžu si všimnout, že $12$ je dělná $4,3,2$, takže $a_{17}$ patří

Pozorování co mi dávají automaty...

Tenisový zápas

> 3. Cvičení

### Operace s regulárními jazyky a jejich automaty

#### Základní

* Sjednocení, průnik, rozdíl - udělám součin automatů a pak zvolím koncové
* Doplněk - prohodím koncové stavy

* Zřetězení, Iterace - z koncových stavů do počátečního stavu lambda přechody...
* Obrácení - Při nedeterministickém obrátíme šipky
  * Odhad počtu stavů - exponenciální (logaritmická) změna

*Jak odstranit lambda přechody?* Máme dva způsoby...

#### Mezipříklad - přidání a odebrání písmena

$L^{a+} = \{ uav \ | \ u,v \in L \}$. kde $a \in \Sigma$... a obdobně $L^{a-}...$

To uděláme pomyslně tak, že si zavedeme booleovskou proměnou, jestli jsme už písmeno přidali/odebrali

Rozdvojíme si automat, koncové stavy budou jen v jednom a přidáme ze všech stavů přechod
Odebrání obdobně 

#### Kvocienty

Levý kvocient $M \backslash L =\{ v | uv \in L \and u \in M \}$

Představme si automat pro $L$, chceme zjistit do jakých stavů se dostaneme slovy z $M$
Běžíme paralelně v $L$ a v $M$ a když jsme v koncovém stavu, tak je prohlásím za počáteční

Pravý kvocient... trhá se z pravého konce
Udělá se přes reverz...

#### Permutatítko

Když pro $a_1 \cdots a_k \in L$ je pro libovolnou permutaci $\pi$ slovo  $a_{\pi_1} \cdots a_{\pi_k} \in L^p$

Není to regulární - příklad přes cyklické nuly a jedničky
A potom se přes $0^i1^i$ ukáže, že není regulární

#### Substituce

*Zobrazení písmena na jazyk*

Příklad konstrukce s tenisovým zápasem
Automat na výhru setu složený z automatů na výhru gemu

#### Homomorfismus

*Zobrazení písmena na slovo*

Speciální případ substituce s jedno-slovovým jazykem

#### Inverzní homomorfismus

Slovo patří do jazyka, pokud obraz slova (vyměnění slova za písmena) patřil do původního jazyka

Konstrukce je náročná popsat, ale dá se představit - pro všechny stavy se slovy převedeme zpět na písmena

### Pumping lemma

...základ již byl

#### Podtrhávací pumping lemma

Pokud podtrhneme více než $n$ písmen, tak podtržené také mohu pumpovat

Původní důkaz je v podstatě v pořádku, pouze nevím, jestli v tom opakování, je alespoň jedno podtržené písmeno
Udělám to tak, že podtrhnu stavy do kterých se dostanu podtrženým písmenem...

Na přednášce byla ukázka neregulárního jazyka pro který platí pumping lemma

#### Dlouhodobý domácí úkol

Můžeš existovat jazyk pro něj i pro jehož doplněk platí podtrhávací pumping-lemma a není regulární?
viz https://ktiml.mff.cuni.cz/~maj/reseni040504.pdf si zavedeme homomorfismus s přidáváním teček za písmena

> 4. Cvičení

#### Rotace slova

Konstrukce regulárního automatu - pro každý stav dva automaty, simulace booleanu, připojení výstupního do vstupního...

*Příklad s vícenásobnou rotací*

### Regulární výrazy

Základní výrazy - prázdno, prázdné slovo, písmeno
Operátory - zřetězení $ab$, iterace $a^*$, sjednocení $a+b$,  

Odpovídá to automatům proto, že to zvládneme udělat konstrukcí

Chceme ale i druhou stranu, hodilo by se mi umět udělat z cesty regulární výraz...

#### Kleeneho algoritmus

Upravený Floyd-Warshall...

Optimalizace - nepočáteční a nekoncové vrcholy můžu zahazovat

> 5. Cvičení

### Dvoucestné automaty

*Přechodová funkce obsahuje i posun hlavy*

Stejně silné jako bez posunu, proč? Důkaz jak jinak než konstrukcí
Představa, že pokud půjdu doprava a pak doleva, tak si to předpočítám - půjde to a je to konečné?

Vladanův důkaz...

Důkaz Marty - budu si předpočítávat v jakých stavech se můžu vrátit (ta funkce je konečná)

#### Dlouhodobý domácí úkol 2

Může automat dostat kamínek, který položí na políčko?...

Hodí se k tomu důkaz Marty, kombinace prefixu a sufixu a jedna z nich je v pohodě

### Moorův stroj

Zajímá nás práce automatu - výstupní funkce (viz. příklad s tenisem)

### Regulární gramatiky a konečné automaty

Důkaz konstrukcí...

> 6. Cvičení

## Typ 2

### Bezkontextové gramatiky

Co to je gramatika? Odvozovací pravidla...

**Separované gramatiky** - práce na neterminálech a pak překlad

#### Strom odvození

Nahrazování levého neterminálu - levá derivace (přirozené)

#### Chomského normální forma - převod

Co musím napravit?

* Více věcí na pravé straně - vyřeším sbalením do dvojníků
* Převod na lambdu - (nejde to úplně), předejdeme vytvoření lambdy (pozor na cyklus)
* Převod na neterminál - obdobně to "nahradíme" ve všech pravidlech (graf silné souvislosti komponent a topologické uspořádání)

### Pumping lemma pro bezkontextové

Tvar $u_1 u_2^n u_3 u_4^n u_5$

Přepokládám CNF a díky tomu bude odvozovací strom binární - dá mi to odhad na max. hloubku, aby se zopakoval terminál

#### Příklady

* $a^jb^kc^l$, kde $j \leq k \leq l$

To vyřeším tak, že vezmu hraniční případ $a^nb^nc^n$ a nemůžu pumpovat dolů

* $a^jb^kc^l$, kde $j \neq k \neq l$

Potřebujeme podtrhávací **pumping lemma** - zahození podstromů s nepodtrhanými...

Poznačím si kolik je $a,b,c$ dohromady v $u_2 u_4$
Pumpováním budu mít
$$
a^{j - (i - 1) \cdot p_a} \ b^{k - (i - 1) \cdot  p_b} \ c^{l + (i - 1) \cdot p_c}
$$
A teď si musím zvolit $j,k,l$ tak, že během pumpování nastane rovnost

Víme, že jedno je nula, búno $p_c$, z toho chceme $l = j - (i - 1) \cdot p_a$ a tedy $i = \frac{j-l}{p_a}+1$ a potřebujeme aby $i$ bylo celé číslo
Nenulovost $p_a$ si vynutíme podtrhávacím lemmatem a velikost určíme např. jako že $l$ bude o $2j!$ víc než $j$ a $k$ zvolíme o $j!$ větší než $j$

> 7. Cvičení

### Zásobníkové automaty

Definice, počáteční konfigurace...

#### Ekvivalence přijímání prázdným zásobníkem a koncovým stavem

Simulace pomocí koncového stavu - svůj program obalím a přidám fiktivní dno a když na něj narazím, tak jdu do koncového stavu
Simulace pomocí prázdného stavu - na koncové stavy přidám vyprazdňovač (nedeterministické), ale musí opět fiktivní dno

Deterministicky to druhé nejde - viz prázdné slovo

#### Jednostavový automat

Musím si stav pamatovat na zásobníku... to má ale problém
Pak ještě další totiž i ten stav, který je pod tím

Jak se startuje?

### Bezkontextové a zásobníkový automat

...

#### Příklad s pumping lemma

Jazyk se slovy ve formátu $AHOJ = joha$ je v pořádku
Naopak $AHOJ = ahoj$ selže, protože mám podmínku, že pumpovaná část musí být dostatečně malá a já můžu zařídit to, aby se pumpováním rozbilo $AA\cdots BB \cdots = aa\cdots bb \cdots$ mi do pumpované části dá nejvýše $BB\cdots = aa \cdots$

#### Generování palindromů

Jeden neterminál...

#### Převod mezi číselnými soustavy

Jde to v $L_2$ jen pokud lze určité množství cifer převést na jiné... vyjádřit jako stejnou $b_1^j = b_2^k$

> 8. Cvičení

### Monotónní gramatiky

#### Příklady

* Gramatika, která generuje $a^n b^n c^n$

Vygeneruji to ve špatném pořadí v neterminálech, napravím pořadí a potom to zterminálním

* Gramatika, která generuje číslo v jedné soustavě rovná se pozpátku číslo v druhé soustavě

Začnu s $0_a =' 0_b$ a budu obě strany inkrementovat o jedna

Jak převést libovolnou monotónní gramatiku na kontextový normální tvar

* Kontextový převod $ABC$ na $DEF$

...

> 9. Cvičení

## Typ 1 a typ 0

### Kontextové a omezený stroj

$\Rightarrow$  Simulujeme postup odzadu - máme pásku se slovem jazyka a při průchodu nedeterministicky nahradíme pravou stranu za levou a zkrátíme 

$\Leftarrow$ Stroj pomocí gramatiky budeme simulovat tak, že si neterminály budeme pamatovat aktuální stav a pásku - převedeme pravidla pozpátk

### Uzavřenost na jazykové operace

...