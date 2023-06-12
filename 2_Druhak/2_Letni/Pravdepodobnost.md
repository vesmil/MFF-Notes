# Pravděpodobnost a statistika

https://iuuk.mff.cuni.cz/~samal/vyuka/PSt1/

> 1. [Přednáška](https://dl1.cuni.cz/pluginfile.php/1158428/mod_resource/content/1/pst1-po.pdf)

**Příklad s polynomy...**

## Základní pojmy

**Prostor elementárních jevů** (sample space) - například u kostky $\{ 1,2,3,4,5,6 \}^n$

**Prostor jevů** (event space) neboli $\sigma$ algebra - $\mathcal{F} \subseteq \mathcal{P}(\Omega)$ a musí platit
	$\bullet$ $\emptyset \in \mathcal{F}$, $\Omega \in \mathcal{F}$
	$\bullet$ $A \in \mathcal{F} \Rightarrow \Omega / A \in \mathcal{F}$					($A^C$ je také v event space)
	$\bullet$ $A_1, \cdots \in \mathcal{F} \Rightarrow \bigcup_i^\infty A_i \in \mathcal{F}$		(Sjednocení jevů)

> Proč nevybrat celou potenční množinu? Občas je moc velká

**Pravděpodobnost** $P: \mathcal{F} \rightarrow [0,1]$ a musí platit
	$\bullet$ $P(\emptyset) = 0$ a $P(\Omega) = 1$
	$\bullet$ Pravděpodobnost sjednocení disjunktních jevů je součet pravděpodobností

**Pravděpodobnostní prostor** je trojice $(\Omega, \mathcal{F}, P)$

**Šance** (odds) je akorát $\frac{P(A)}{P(A^C)}$

**Jistý jev** znamená $P(A) = 1$
**Nemožný jev** znamená $P(A) = 0$, například $P(\emptyset) = 0$

## Vlastnosti

1. $P(A) + P(A^C) = 1$
2. $A\subseteq B \Rightarrow P(A) \leq P(B)$
3. $P(A \cup B) = P(A) + P(B) - P(A\cap B)$
4. $P(\bigcup A_i) \leq \sum_i P(A_i)$ - Booleova nerovnost neboli subaditivita

#### Důkazy

1. $A \cup A^C = \cdots = \Omega$
2. $B = A \cup B \setminus A$ a potom $P(B) = P(A) + P(B\setminus A) \geq P(A)$
3. Podobně
4. Pomocí zdisjunktnění - viz. obrázek v prezentaci

## Příklady prostorů

**Konečný uniformní** - $P(A) = |A| / |\Omega|$, $\mathcal{F} = \mathcal{P}(\Omega)$

**Diskrétní** - jsou dány $p_1, \cdots$, kde $\sum_i p_i = 1$ a potom $P(A) = \sum_{i: \omega_i \in A} p_i$

**Spojitý** (geometrický) - $\Omega \subseteq R^d$ pro vhodné $d$ a $P(A) = \int_A f(x)dx$

> Představy postupně - bedna s míčky, bedna s míčky s různou pravděpodobností a náhodná trefa terče

## Podmíněná pravděpodobnost

Pravděpodobnost $A$ pokud před tím nastal jev $B$ je $P(A | B) = \frac{P(A\cap B)}{P(B)}$

> 2  Přednáška

### Zřetězené podmiňování

$P(A_1 \cap A_2 \cap \cdots) = P(A_1) \cdot P(A_2 | A_1) \cdot P(A_3 | A_1 \cap A_2) \cdots$

### Věta o úplné pravděpodobnosti - rozbor všech možností

Spočetný systém množin $B_1, B_2, \cdots \in \mathcal{F}$ je rozklad, pokud jsou všechny množiny disjunktní a sjednocením dají $\Omega$
$$
P(A) = \sum_i P(B_i) \cdot P(A|B_i)
$$

### Gambler's ruin

Hráči s penězi $a$ a $b$ hrají opakovaně spravedlivou hru o 1 Kč, dokud někdo nepřijde o všechny peníze 
Šance na výhru prvního hráče je $\frac{a}{a+b}$

Spočítá se rozepsáním rekurze $p(a) = \frac{1}{2}p(a+1) + \frac{1}{2}p(a-1)$, kde s okrajovými podmínkami máme dostatek rovnic

### Bayesova věta

$$
P(B_j\ |\ A) = \frac{P(B_j)P(A\ |\ B_j)}{\sum_i P(B_i)P(A\ |\ B_i)}
$$

*Důkaz:* Akorát třikrát rozepíšeme z definice

### Nezávislost jevů

**Pro dva** - pokud platí $P(A\ |\ B) = P(A) \cdot P(B)$

**Obecně** - každá konečná podmnožina je nezávislá
**Po dvou nezávislé** - ...

> 3. Přednáška

## Náhodná veličina

> Vzdálenost od středu, počet hodů než padne šestka, ...

Funkce $X : \Omega \rightarrow \mathbb{R}$, pokud pro všechna $x$ platí $\set{\omega \in \Omega : X(\omega) = x} \in \mathcal{F}$

**Pravděpodobností funkce náh. veličiny** -  $p_X(x) = P(\{ X = x \})$

### Bernoulliho/alternativní rozdělení

*Příklad* - počet orlů $X$ při jednom hodu nespravedlivou mincí s pravděpodobností $p$
Značíme $X \sim Bern(p)$
$$
p_X(1) = p \\
p_X(0) = 1 - p \\
\text{...pro ostatní nulová}
$$

*Identifikátorová náhodná veličina je další příklad Bernoulliho* 

### Geometrické rozdělení

*Příklad* - kolikátým hodem kostkou padla první šestka
$$
p_X(k) = (1-p)^{k-1} \cdot p
$$

### Binomické rozdělení

*Příklad* - počet orlů $X$ při $n$ hodech nespravedlivou mincí s pravděpodobností $p$
Značíme $X \sim Bin(n,p)$

Další příklad s počtem červených při tahání míčků z bedny s vracením
$$
p_X(k) = \binom{n}{k} p^k (1-p)^{n-k}
$$

### Hypergeometrické

*Příklad* - počet červených míčků při tahání bez vracení
$$
p_X(k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}
$$
Zdůvodnění vybírání dvou množin

### Poissonovo

*Příklad* - počet doručených emailů...
$$
p_X(k) = \frac{\lambda^k}{k!} e^{-\lambda}
$$

To, že to vůbec pravděpodobnost je plyne z Taylorova...

Můžeme pozorovat, že $Pois(\lambda)$ je limitou $Bin(n,\lambda / n)$... neboli pro velká $n$ může binomická aproximovat Possionem

## Střední hodnota

Pro diskrétní náhodnou veličinu $X$ definujeme
$$
\mathbb{E}(X) = \sum_{x\in Im(X)} x \cdot P(X = x)
$$

Suma ale musí dávat smysl (ne například $1-1+1-1+\cdots$)

Protože na diskrétním pravděpodobnostním prostoru můžeme počítat průměr přes všechny výsledky, tak platí
$$
\mathbb{E}(X) = \sum_{\omega \in \Omega} X(\omega) \cdot P({\omega})
$$

### Naivní statistik

Skládání funkcí nám dá opět náhodnou veličinu $Y = g(X)$

Počet hodnot $Y$ je zjevně spočetný a pro důkaz musíme především ověřit $Y^{-1}(y)=\set{\omega\in\Omega : g(X(\omega) = y)} \in \mathcal{F}$ pro všechna $y \in Im(y)$
$$
\bigcup_{x\in Im(X)g(x)=y}X^{-1}(x)
$$
A jeho **pravidlo** zní

$$
\mathbb{E}(g(X)) = \sum g(x)P(X=x)
$$

Na první pohled se totiž může zdát, že se jedná o definici... důkaz ale je potřeba

$$
P(Y=y) = \sum_{x\in Im(X), g(X) = y}P(X=x) \\
...
$$

> 4. Přednáška

### Vlastnosti

* $P(X\geq0)=1 \Rightarrow \mathbb{E}(X) \geq 0$ a pokud $\mathbb{E}(X) = 0$, tak $P(X=0)=1$
* $\mathbb{E}(X) \geq 0 \Rightarrow P(X\geq 0) > 0$
* $\mathbb{E}(a \cdot X +b) = a \cdot \mathbb{E}(X)+n$
* $\mathbb{E}(X) + \mathbb{E}(Y) \mathbb{E}(X + Y)$

*Příklad s házením znovu na jedničku a šestku...*

### Podmíněná střední hodnota

...

### Věta o úplné střední hodnotě

Celkovou můžu dostat z rozkladu na podmíněné...

### Formule pro střední hodnotu celočíselné n.v.

$$
\mathbb{E}(X)=\sum_{n=0}^\infty P(X>n)
$$

## Rozptyl

$$
\text{var}(x) = \mathbb{E}((X-\mathbb{E}X)^2)
$$

Směrodatná odchylka je $\sigma_X = \sqrt{\text{var}(X)}$ 
$$
var(X) = \mathbb{E}(X^2) - \mathbb{E}(X)^2 = \cdots
$$
Dále platí
$$
\text{var}(aX + b) = a^2 \text{var}(X)
$$

## Vlastnosti rozdělení

### Bernoulliho

Pro $X\sim Bern(p)$:

$$
\mathbb{E}(X) = p \\
\text{var}(X) = p - p^2
$$

### Geometrické

Pro $X\sim Geom(p)$:

$$
\mathbb{E}(X) = \frac{1}{p} \\
\text{var}(X) = \frac{1-p}{p^2}
$$

### Binomické

Pro $X\sim Bern(p)$:

Střední hodnotu můžeme vypočítat jako součet indikátorových veličin a tedy $np$, lepší je to ale obecněji
$$
\mathbb{E}(X) = \sum_{k=0}^{n} k \cdot P(X=n) = \cdots = np \\
\text{var}(X) = np(1-p)
$$

### Hypergeometrické

Pro $X\sim Hyper(N,K,n)$:

$$
\mathbb{E}(X) = n \frac{K}{N} \\
\text{var}(X) = n \frac{K}{N}(1 - \frac{K}{N}) \frac{N-n}{N-1}
$$

### Poissonovo

Pro $X\sim Pois(\lambda)$:

$$
\mathbb{E}(X) = \lambda \\
\text{var}(X) = \lambda
$$


> 5. Přednáška

## Náhodné vektory

*Budeme chtít dvě náhodné veličiny spojit v jeden objekt*

### Sdružená pravděpodobnostní funkce

Funkce $p_{X,Y} : \mathbb{R}^2 \rightarrow [0,1]$
$$
p_{X,Y}(x,y) = P(\set{\omega \in \Omega : X(\omega) = x \ \& \ Y(\omega) = y })
$$
To tvoří pravděpodobnostní prostor, pokud jsou všechny pravděpodobnosti definované

### Marginální rozdělení

$$
p_X(x) = P(x=x) = \sum_{Y\in Im(Y)} P(X=x \ \& \ Y = y) = \sum_{Y\in Im(Y)}p_{X,Y}(x,y)
$$

### Nezávislost náhodných veličin

Diskrétní náhodné veličiny jsou nezávislé pokud $P(X=x \ \& \ Y = y) = P(X = x)P(Y=y)$

Z funkcí $p_X$ a $p_Y$ tedy můžeme zjistit $p_{X,Y}$

### Funkce náhodného vektoru

Suma přes všechny $x,y$...

### Součet

Pro $Z = X + Y$
$$
P(Z=z) = \sum_{x \in ImX} P(X=x \ \& \ Y = z-x)
$$
A pokud jsou $X$ a $Y$ nezávislé, tak navíc můžeme použít rozložení o pár řádků výše

*Příklad se sčítáním dvou uniformních a následně dvou binomických*

### Vlastnosti střední hodnoty (součet, součin)

$$
\mathbb{E}(g(X,Y)) = \sum_{x \in ImX} \sum_{y \in ImY} g(x,y) P(X=x \ \& \ Y = y)
$$

Dále platí
$$
\mathbb{E}(aX + bY) = a\mathbb{E}(X) + b\mathbb{E}(Y)
$$
Pro nezávislé $X,Y$
$$
\mathbb{E}(XY) = \mathbb{E}(X) \mathbb{E}(Y)
$$

### Kovariance

$$
\text{cov}(X,Y) = \mathbb{E}((X-\mathbb{E}X)(Y-\mathbb{E}Y)) = \mathbb{E}(XY) - \mathbb{E}(X)\mathbb{E}(Y)
$$

#### Vlastnosti

* $\text{var}(X) = \text{cov}(X,X)$
* $\text{cov}(X,aY+bZ+c) = a \cdot \text{cov}(X,Y) + b \cdot \text{cov}(X,Z)$
* kovariance nezávislých je nula (ale nejen tehdy)

### Korelace

Normovaná kovariance (je mezi $-1$ a $1$)
$$
\varrho (X,Y) = \frac{\text{cov}(X,Y)}{\sqrt{\text{var}(X)\text{var}(Y)}}
$$
Korelace neznamená příčinou souvislost (může být náhodná)
Naopak nekorelace neznamená nesouvislost

### Rozptyl součtu

$$
... TODO
$$



Pro $X_1, \cdots , X_n$ nezávislé
$$
\text{var}(X) = \sum_{i=1}^n \text{var}(X_i)
$$

### Podmíněné rozdělení

Zkoumá rozdělení veličiny podmíněné jevem
$$
p_{X|A}(x) := P(X = x\ |\ A) \\
p_{X|Y}(x|y) := P(X = x\ |\ Y=y)
$$
Z toho lze pozorovat, že
$$
p_{X|Y}(x|y) = \frac{p_{X,Y}(x,y)}{p_Y(y)} = \cdots
$$


> 6. Přednáška

## Obecné náhodné veličiny

...
$$
\set{\omega \in \Omega : X(\omega) \leq x} \in \mathcal{F}
$$
A tedy i diskrétní náhodná veličina je náhodná veličina

### Distribuční funkce

$$
F_X(x) := P(X\leq x) = P(\set{\omega \in \Omega : x(\omega) \leq x})
$$

#### Vlastnosti

* Neklesající funkce a zprava spojitá funkce
* $\lim_{x\rightarrow-\infty} F_X(x) = 0$
* $\lim_{x \rightarrow \infty} F_X(x) = 1$

## Spojité náhodné veličiny

### Hustota

Pokud existuje funkce $f_X$ (hustota) taková, že:
$$
F_X(x) = P(X\leq x) = \int_{-\infty}^x f_X(t)dt
$$

#### Vlastnosti funkce s hustotou

* $P(X=x) = 0$
* $P(a \leq X \leq b) = \int_{a}^{b}f_X(t)dt$

### Střední hodnota

$$
\mathbb{E}(X) = \int_{-\infty}^{\infty} x \cdot f_X(t)\ dt
$$

...pokud integrál má smysl

 Může také použít diskrétní n.v. pro aproximaci, když uvážíme $Y=\lfloor \frac{X}{\delta}\rfloor \delta$
$$
...
$$


> 7. Přednáška

### Pravidlo naivního statistika

$$
\mathbb{E}(g(X)) = \int_{-\infty}^{\infty} g(x) \cdot f_X(x)\ dx
$$

### Linearita pro diskrétní i spojité

$$
\mathbb{E}(a_1 X_1 + \cdots + a_n X_n) = a_1 \mathbb{E}(X_1) + \cdots + a_n \mathbb{E}(X_n)
$$

### Rozptyl

$$
\text{var}(X) := \mathbb{E}((X-\mu)^2) = \int_{-\infty}^\infty (x - \mu)^2 \cdot f_X(x) \ dx
$$

Respektive opět $var(X) = \mathbb{E}(X^2) - \mathbb{E}(X)^2$ a tedy se nám hodí $\mathbb{E}(X^2) = \int_{-\infty}^\infty x^2 \cdot f_X(x) \ dx$

## Příklady spojitých rozdělení

### Uniformní rozdělení

$X\sim U(a,b)$ pokud $f_X(x) = 1/(b-a)$ pro $x \in [a,b]$ a jinak $0$.

Distribuční funkce $F_X(x) = (x-a)/(x-b)$ pro $x \in [a,b]$, $F_X(x) = 0$ pro ... a $F_X(x) = 1$ ...
$$
\mathbb{E}(X) = \frac{a+b}{2} \\
\mathbb{E}(X^2) = \frac{a^2+ab+b^2}{3} \\
\\
\boxed{\text{var}(X) = \frac{(b-a)^2}{12}}
$$

### Exponenciální rozdělení

$$
F_X(x) = 
	\begin{cases}
    	0                     & \text{pro } x \leq 0 \\
    	1 - e^{-\lambda x}    & \text{jinak} 
	\end{cases} \\
$$

$$
\mathbb{E}(X) = \cdots = \frac{1}{\lambda} \\
\mathbb{E}(X^2) = \cdots = \frac{2}{\lambda^2} \\
\\
\boxed{\text{var}(X) = \frac{1}{\lambda^2}}
$$

#### Souvislost exponenciálního a geometrického

Nechť $X \sim Exp(\lambda)$ a $Y \sim Geom(p)$
Máme tedy $P(X \geq n\delta) = e^{-\lambda n \delta}$ pro ... a ...

Aproximace $X$ pomocí $Y$...

### Standardní normální rozdělení

$X\sim N(0,1)$
$$
f_X(x) = \frac{1}{\sqrt{2\pi}} \cdot e^{-x^2/2}
$$
Tuto funkci někdy také značíme jako $\varphi$ a příslušnou distribuční funkci značíme $\Phi$

#### Obecné normální

$X \sim N(\mu, \sigma^2)$

...
$$
\mathbb{E}(X) = \mu \\
\text{var}(X) = \sigma^2
$$

#### Odolnost vůči součtu

Součet náhodných veličin normálního rozdělení je také normální n.v.

#### Význam

Dobrá aproximace součtu mnoha nezávislých n.v.

Užitečné pravidlo $3\sigma$ (resp. $68-95-99.7$ rule):
$$
P(\mu - \sigma \leq X \leq \mu + \sigma) \dot= 0.68 \\
P(\mu - 2\sigma \leq X \leq \mu + 2\sigma) \dot= 0.95 \\
P(\mu - 3\sigma \leq X \leq \mu + 3\sigma) \dot= 0.97
$$

### Cauchyho rozdělení

$f(x) = \frac{1}{\pi(1+x^2)}$ a $F(X)$ ...

Nemá střední hodnotu

### Další rozdělení

* Gamma rozdělení
* Beta rozdělení
* $\chi^2$ rozdělení (chí-kvadrát)
* Studentova $t$-distribuce

## Náhodné vektory

### Sdružená distribuční funkce




> 8. Přednáška

## Kvantilová funkce

univerzalita



Konvoluce

