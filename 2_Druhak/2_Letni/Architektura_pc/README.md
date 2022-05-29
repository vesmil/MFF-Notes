# Architektura počítačů

[Stránka 1](https://d3s.mff.cuni.cz/teaching/nswi143/), [Stránka 2](https://d3s.mff.cuni.cz/legacy/teaching/computer_architecture/), [Záznamy](https://cunicz.sharepoint.com/:f:/s/d3s-teaching/EmarrFhUHvJNn64sxL9lyV0BJk8q6uIzTEE-fKzFxVqkDQ)

> 1. Přednáška

## Úvod...

**Tranzistor** - vypínač řízený signálem
**Integrovaný obvod** - spojení tranzistorů

Volatilní paměť - **DRAM** a **SRAM** (nepotřebuje refresh a je rychlejší)
Sekundární paměť - **HDD** a **SSD**

Vstup, výstup, ...

Obří rozsah programů...
**Abstrakce** - vrstvy od uživatele přes algoritmus až po strojový kód

> 2. Přednáška

## Výkon

**Moorův zákon** - zmenšování tranzistorů pro CPU, kapacita DRAM...
Výkon je ovlivňován *algoritmy, programovacími jazyky, kompilátorem, architekturou, CPU, pamětí, I/O, ...*

**Měření výkonu** na základě `execution time` a `throughput` (záleží na požadovaném využití)
$$
\text{Peformance} = \frac{1}{\text{Execution time}}
$$
Rozdíl mezi `wall-clock time` a `processor time` (uživatel a CPU)
$$
\text{CPU execution time} = \frac{\text{CPU clock cycles}}{\text{CPU clock rate}} 
\\
\\
\text{CPU clock cycles} = \text{CPI}^* \times \text{Number of instructions}
$$

$^*\text{CPI} := \text{Clock cycles per instruction}$ 

>  Jak výše zmíněné (algoritmy...) ovlivňují počet instrukcí, CPI a takt?

Příklad se zlepšováním části programu...

Číslo $\text{MIPS} := \text{Million pnstructions per second}$ je ne vždy použitelné (různé instrukce)
Lepší měření pomocí exeucition time pro konkrétní workload - **SPEC**

Problém kolem 2004 s dodáváním a odváděním energie - **snížení napětí **(ale problém rozpoznání 0 a 1)

**Paralelismus** nezlepší sekvenční program, paralelizování je náročné *(konkrétní problémy v prezentaci...)*

**Amdahlův zákon** o zrychlení celku po zlepšení pouze části

Pro paralelismus je $n \in \N$ je počet jader a $B \in \langle 0,1\rangle$ je práce, která nejde paralelizovat
$$
\text{Speedup}(n) = \frac{1}{B + \frac{1}{n} (1 - B)}
$$
Říká nám, že později zvyšování počtu jader je stále méně efektivní

*Bývají různé algoritmy pro určitý počet jader*

**Make common case fast**...

> 3. Přednáška

## Logické obvody

### Úvod

High level voltage (logická jedna)
Low level voltage (logická dva)

**Logická funkce** ($f: B^k \rightarrow B$) je daná tabulkou

Booleovská algebra...
Univerzální jsou `NAND`, případně `NOR`

**Logické bloky** jsou nějaké černé skříňky, které vykonávají funkci (vrstvíme bloky)

* **Kombinační** - bezstavové, reprezentují logické funkce
* **Sekvenční** - má paměť, interní stav, sekvence kroků

CPU počítá po **slovech**, umí logicky posouvat, ...

### Značení hradel

![Logic gates](README.assets/22e2d43d.png)

*Jednotlivá implementace hradla má vliv na elektrické vlastnosti - především spotřeba*

CMOS logika se snaží o to, aby nikde netekl proud, důležité je napětí (velká dynamická spotřeba ale)

### Binární sčítačka

Půl sčítačka - výsledek díky `XOR` a carry díky `AND`
Úplná - dvě půlsčítačky a jejich carry `OR`

$n$-bitová z několika úplných

Pokročilejší verze viz. ADS 2

> 4. Přednáška

## Sekvenční obvody



> 5. Přednáška



> 6. Přednáška

## Datapath

### Multi-cycle datapath

Proměnná doba instukce - ne analogicky, ale podle počtu cyklů

> 7. Přednáška

## Vyjímky





