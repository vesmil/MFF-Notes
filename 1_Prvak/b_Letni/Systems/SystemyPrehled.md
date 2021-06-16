# C a C++

Známe z cvika a u zkoušky nebude

&nbsp; 

# CPU

>16.3.2021

### Architektura

#### Von Neumannova

Jedna sdílená sběrnice a na ní CPU, Paměť a I/O

Vždy jedna transakce na sběrnici

```
CPU <-----> Memory
       |
       v
      I/O
```

#### Harvardská

Doteď se používá v nějakých mikrocontrolerech

Je potřeba více adresových prostorů

```
Instruction <---> CPU <---> Memory
  Memory                | 
                        v
                       I/O
```

#### Reálná

Vlastní sběrnice pro paměť - dokonce více paměťových kanálů

Buď přímo uvnitř procesoru a nebo přes PCIe grafa

Do procesoru vede sběrnice (někdy DMI) do South Bridge\
V něm jsou perfiferie jako zvukovka, síťovka, …

Dřív býval i North bridge pro přístup k pamětím, ale ten se přesunul do procesoru
 pro přístup k pamětím
Nyní jsou všechny sběrnice sériový, kvůli fyzikálním důvodům - PCIe, SATA, USB, … \
Zároveň jsou všechnu sběrnice peer to peer, protože je to víc ez

### Co je ale architektura?
 
* Instrukční sady (ISA) - jak se ten procesor má chovat podle instrukcí 
	* například i64 (rozšíření x86)\
	&nbsp; &nbsp; Ta je údajně extrémně špatná
* Hardwarová architektura - třeba Skylake, Coffee Lake  … je to to jak výrobce implementoval ISA

Debata na téma proč jsou nové instrukční sady špatné - zbytečně moc bloat instrukcí, ale když se pokoušeli o něco nového (např. Itanium), tak většina musela běžet na Itaniu\
Na mobilu je větší prostor pro zlepšení kvůli pozdějšímu překladu a častěji se zavádí nová architektura

> Hlavní úkol procesoru je vykonávat jednoduché instrukce

### Třídy instrukcí

* Load
* Store
	* Dvě nejdůležitější druhy instrukcí, ale jsou dost pomalé
	* Na rozumných architekturách to jsou jediné, které pracují s pamětí\
&nbsp; &nbsp; Ale třeba i64 inkrementuje i v paměti
* Move 
* Aritmetické
* Jumps
	* Nepodmíněné x podmíněné (ty dělají počítač počítačem)
	* Přímé (přímo adresa kam) x nepřímé (kam je v proměnné) x relativní adresa (o kolik se posunout dál)
* Call
	* Při volání funkcí je potřeba nějaký zásobník s návratovou adresou\
	&nbsp; &nbsp; Buď Hardwarově a na to jsou i procesrové instrukce a nebo na to použiju registry

> Ještě tam v podstatě chybí porovnání

### Registry

* Obecné
* Integer a float
* Adresové
* Branch registry - skokové registry
* Příznakové registry
* Predikátové registry - každá instrukce má bit podle toho, jestli se má provést (Nemusím skákat)
* Aplikační
* Systémové
* Vektorové - např. jednou instrukcí sečíst 4 floaty
* …

> Architektury nemívají všechny druhy registrů

#### Pojmenovávání

* 99 % má přímé pojmenování registrů
* Zásobníkový přístup k instrukcím a v podstatě nezávisí na přímých názvech

#### Aliasing

Překrývání registrů - x86 to třeba má \
&nbsp; Dost se tomu snaží vyhnout, protože je problém třeba udělat překladač nebo poznat změnu

32-bitový EAX má ještě 16b podregistr AX a ten je rozdělený ještě na AH a AL

## Příklady

x86 není ortogonální a tedy libovolná instrukce nemůže pracovat s libovolným registrem

Jeho sepcializované registry: EAX je akumulátor, EBX je base, ECX je count, EDX je data, …

> Je to hodně nepříjemné

Segmentové registry - Datový, Kódový, Stack ...

Instruction pointer na aktuální vykonávanou instrukci

Oproti x86 má Itanium (IA-64) několik set registrů

### MIPS

32 registrů r0-r31 \
&nbsp; &nbsp; r0 je vždycky nula \
&nbsp; &nbsp; r31 je link register na `jal` -- návratová adresa, používá se jako `call`

Nemá stack (myšleno hardwarově), flagy

> 23.3.2021

Od MIPS je odvozená RISC-V

#### Instrukce MIPS

x86 narozdíl od MIPS není schopná sečíst dvě věci a zapsat jinam

Operace známe už z principů and, ro, xor, … (místo not je negace or), shift, …

Proměnlivé x pevné kódování\
&nbsp; např. instrukce x86 jsou různě dlouhé a MIPS má 32bitů

Ještě celkem dlouhé porovnání, ale idc…

### ABI

Nějaké doporučené předpisy od autora ISA, které se musí dodržovat, aby všechny aplikace fungovaly

Registry mají také svoje aliasy \
Např. registry pro návratové hodnoty, funkční argumenty, přechodné (temp), uložené přechodné… 

Preserve - jestli je potřeba registry zachovoat volanou funkcí\
Temporaries se nejspíše přepíšou, ale saved temporaries tam musí volaná funkce vrátit

Je často preferované napsat $sp (jako stack pointer) než $r29 \
Mimo to je tam global pointer, frame pointer (místo od kterého se posouvá), …

### Příznaky

Mají je jenom některé ISA

Zrada v tom, že každá instrukce se z hlediska změny příznaků chová úplně jinak

Běžné flagy jsou zero, sign a carry

Jsou systémové a uživatelské příznaky a x86 je zmastila dohromady - musí se schovávat

### Co všechno je v procesoru?

* Řadič paměti
* Hierarchie keší
* Jádra
* Registry
* Logický procesor
	* uvnitř jader - víc proudů instrukcí (u Intelu hyperthreading)
* Instrukce 

### Instrukce

Je to nějaký jednoduchý příkaz procesoru

Musí být nějak zakódovaná - překlad přes assembler…  \
Ale i textovému zápisu instrukcí se říká assembler

Mají operandy - v podstatě argumentu (konstanty, adresy, registry)

Proud instrukcí - řízený PC (program counter)

### ISA

**Klasifikace instrukční sady**

* CISC - komplexní sada
	* Dřív byl dopřeklad do mikrokódu	
* RISC - redukovaná sada
* VLIW - very long instruction word
	* Třeba 128 bitová instrukce - bývá třeba ve switchích
* EPIC - explicitly parallel instruction computer 
	* Je v tom explicitně jaký části mají být paralelně (mělo třeba Itanium)

Arm už není ani náhodou RISC 

U x86 rovnou instrukce odpovídají mikroinstrukci a pak tam jsou nějaké staré nepoužívané instrukce, které se ještě musí překládat, takže to není úplně CISC

**Ortogonalita** \
Už bylo - to jestli jsou specializované registry nebo jdou zaměnit

**Load-Execute-Store**\
To, že se pracuje jen s registrama a nedělá se třeba aritmetika v paměti

### Zjednodušene schéma

Každé jádro má 

* výpočetní jednotku (exuction unit)
* cache 
	* tři úrovně (L1 skoro stejně rychlá jako registr) 
	* L1 je rozdělená na instrukce a data
* vlákna
	* více vláken sdílí jednu výpočetní jednotku, protže ta nebývá moc vytížená

Každé jádro má u sebe kousek svojí L3 a berou si navzájem po oboustranným ringu

Dělá se prefetch - odhadování jaká data budou potřeba

### Schéma jednoho jádra

Front end čte instrukce a dekóduje je\
&nbsp; Coffee lake má 5-cestný dekodér, takže dékoduje 5 inst. v taktu \
&nbsp; Jeden z nich je komplexní, který je právě na překlad na mikroinstrukce

Po dekódoání operace spadnou do "bazénku" a pak čeká až bude moc jít na zpracování\
&nbsp; Out of order execution - celkem chaotické provádění

### Techniky pro zrychlení CPU

> 30.3.2021

#### Pipeline

Rozdělit vykonávání na jednotlivý stages (reálně jich bývá 14-19)

V jednom čase mám rozdělaných několik instrukcí a každá je v jiné fázi\
&nbsp; Něco v instruction fetch, něco už se vykonává, něco práce s pamětí, …

**Náběh pipeline** je doba než se stihnout "naplnit" všechny procesy/stages \
**Doběh** v HW nenastane

Když vypadne, tak musí znovu nabíhat \
&nbsp; Například při podmíněném skoku musím při špatném odhadu veškerou práci zahodit \
&nbsp; Cca. 95 % odhadne

Technika pipeline se používá i jinde - zvuk, televlize, … \
&nbsp; Příklad zpoždení digitální televize

Návrh je jednodušší a za jednotku času jsem schopný provést víc instrukcí \
&nbsp; Vzniká ale latence

#### Superskalarita

V každé stage se místo jedné instrukce jich nachází víc

Musí mít např. zdvojené jednotky

Dnešní procesory jsou dokonce 5-cestné

Jsou také asymetrické (nemusí se stejná stage zpracovávat stejně - viz. simple a complex dekódování instrukcí)

### Zpátky schéma

Po dekódování jsou tedy v tom "bazénku" - Reservation station

Každý port do kterého pak instrukce pokračují umí něco jiného

Pak to vejde do reorder buffer, který výsledky vrátí zpět do správného pořadí (musí se řešit konflitky…)

&nbsp; 

# Paměť

> Dost z toho už máme znát ze zimního

Je organizována do bitů a ty jsou uskupovány do slov \
Každé slovo má má svoji N-bitovou adresu a umíme uložit 2^N slov\
Dnes se používá 8-bit slovo nebo-li byte

### Adresový prostor

Očíslování slov v paměti

Fyzicky je paměť jako dvourozměrný prostor \
Adresované po řádcích a sloupcích

Měnit řadky trvá delší dobu než slupce, ale pokud přistupuji sekvenčně, tak adresa nejprve roste po sloupcích

Nejdůležitější u RAM je CAS - čas na přístup k sloupci\
Pak tam jsou i časy tRCD, tRP, RAS

### Reprezentace data

* Bezznaménková čísla [0 - 2^N - 1]
* Znaménková (dvojkový doplněk)
* Float podle IEEE 754 - mantisa a exponent, …

### Endianita

Big endian - MSB first \
Little endian - LSB first

Skoro všechny procesory BE a nebo vybrat, Intel má LE

V sítích jsou taky BE, takže Intel musí převracet

### Zarovnání dat

*Příklad se structem*

**Vnitřní zarovnání** \
&nbsp; Každý typ je zarovnaný v paměti na násobek svojí velikosti

**Vnější zarovnání**\
&nbsp; Když dám structy do pole, tak se to rozbije \
&nbsp; &nbsp; Musím tedy položky pole zarovnávat na násobek největšího základního typu

### Alokování paměti

Úkol je najít blok nevyužité paměti o dostatečné velikosti

Předtím než program naběhne se vezme heap (neboli arena či pool)

A pak při běhu alokujeme například při `new` v C# \
Chvíli ho používáme\
A pak ho zahodíme\
&nbsp; Bud explicitně a nebo Java a spol mají garbage collector

Pozn. hodnoty a referance se mažou vždy (jsou lokální), ale musíme třeba mazat na co ukazovali

#### Faragmentace

Jeden z problémů alokace

Paměť je rozdělená do malých bloků abych si mohl pamatovat, co je zabrané 

Pamatovat si to po bytech by bylo nepraktické -- moc detailně a musel bych pak řešit zarovnání

**Interní**
Data v bloku jsou menší než ten blok. S tím ale nic neudělám

**Externí**
Pokud mám hodně volné místo rozdrobené do nesouvislých malých bloků

#### Dynamická alokace paměti

##### Jak si pamatovat volné bloky?

* Spoják volných bloků (zabrané se většinou neevidují)
* Bitmapa

##### Alokační algoritmy

> **Často to prý bude u zkoušky**

* First fit
	* Vezmu první volné místo
	* Musím ho rozštípnout
	* Je to jednoduché a rychlé, ale na druhou stranu může ničit velké bloky
* Next fit
	* Pamatuji si, kde jsem skončil a z toho místa pokračuji
	* O něco lepší, akorát si musím pamatovat to, kde jsem skončil
* Best fit
	* Neberu první, ale vezmu to, kam to nejlépe fitne
	* Nechá to velké bloky, ale je to pomalé a vytvoří to hromadu nepoužitelně malých
* Worst fit
	* Dám to do největšího bloku
	* Očivindě nejhorší, protže ničí velké bloky

##### Buddy memory allocation

> Dobré to vidět názorně

Bloky o velikosti 2^N

A najdu nejbližší vyšší mocninu dvojky k tomu, co chi alokovat \
Někde mám seznam volných bloků velikostí všech mocnin dvojky, takže to do toho dám\
Pokud je jen větší, tak ho rozštěpím

Konstantní alokace

Pokud má volnej bok kamaráda (volného souseda), tak je musím mergnout

Má to velkou interní fragmentaci

> 6.4.2021

## Paměťová hierarchie

Sestupně podle rychlosti a zároveň vzestupně podle velikosti:

* registry
* cache
* RAM (a rychlejší SRAM)

Dále je to persistentní

* persistent RAM
	* Je trochu pomalejší než RAM a musí se kvůli tomu opravit OS a programy
* SSD, flash
	* SSD a dál už není přímo adresovatelné procesorem -- používá se sběrnice a řadič
* HDD
	* Nejdéle trvá mechanický pohyb hlavou
* pásky
	* Běžně na zálohy

## Cache

Datová struktura ve které mám data, které bych jinak musel znovu dlouho počítat

Hardware nebo software implementace

Pokud paměť dojde, tak použijeme stránkové algoritmy -- later

### Cache na CPU

Spoléhá na lokalitu přístupu -- předpokládáme, že pokud něco čteme z paměti, tak za nedlouhou dobu budeme číst něco těsně vedle

Již zmíněno L1 (doba přístupu 4 takty, desítky kB), L2, L3 (stovky taktů a jednotky MB)

Musíme řešit problémy, když chceme data mezi jádry -- přesun přes L3 \
Koherence keší a stará se o to procesor

Hot data musí být co nejblíže

### Cache pojmy

**Cache line** \
&nbsp; Keš není organizovaná po bytech, ale po jednotkách cache line (entry), která má dnes běžně 64B

**Cache hit** \
&nbsp; Tak se nazývá, když jsem trefil data ve cache (úspěšnost prý 97 %)

**Cache miss** \
&nbsp; Když se netrefím

**Cache line load** \
&nbsp; Musím načíst data, když nejsou v cache \
&nbsp; Pozor na to, že jsem do cache mohl i psát a proto pokud ji budu vyhazovat, tak se musí zapsat

**Cache line state** \
&nbsp; používá se MESI protokol -- 4 stavy 

## Asociativní paměť

Dvojice klíč a hodnota

Dokážu tím očíslovat Cache lines v RAM

Velmi rychlá -- implementována hardwarově tak, že to nemusím celé procházet \
Stojí to hromadu tranzistorů, takže to není moc velké

## Systémy s více procesory

**Symmetric multiprocessing** \
&nbsp; Jedna sběrnice mezi RAM a CPUs \
&nbsp; Má limit pro kolik procesorů to jde 

**NUMA** (Non-uniform memory access) \
&nbsp; Každý procesor má svoji RAM \
&nbsp; Musí být ale dostupné mezi sebou… a taky že jsou \
&nbsp; Jsou navzájem propojené (ale ne každý s každým, protože to stojí piny) \
&nbsp; To ale stojí nějaký čas -- *NUMA factor*

Vlastě se ale všechny systémy chovají jako NUMA, ale tak to nevadí, když je jen jeden procesor

&nbsp;

# Programovací jazyky

## Překladač

Nějaká černá skříňka, která z kódu vyrobí něco spustitelného nebo chybovou hlášku

**Formální popis** \
Stručně překladač je zobrazení slov z vstupního jazyka generovnaného gramatikou do výstupního jazyka generováného jinou gramtikou a nebo přijímaného automatem

Jazyk má nějaká pravidla a lexikální elemty (while, do, …)

> Tohle je spíš jen teaser na AutoGram

### Praktický pohled na překlad

1. Preprocesor zpracuje zdrojový kód, postará se o věci jako `include` a vytvoří `.pp` soubor

2. Ten spolu s rozhraním dostane překladač a vyrobí z něj `asm` (asembler texťák instrukcí)

3. Assembler pak z `.asm` vyrobí binární podobu `.obj`

4. Až budu mít přeložené všechny zdrojáky, tak to spolu s objekty knihoven dostane linker a ten už konečně vyrobí executable

> Rozdíl mezi interface a knihovnou je v tom, že v interface není implementace a knihovna je pak už binární

OS pak z programu udělá proces -- spuštění

Dnes se skoro celý proces dělá z uživatelského hlediska v jednom překladači





&nbsp; 

# Operační systémy 



### Účel

## CPU módy

User mód x kernel mód

## Architektura

* Monolitická
* Vrstvená
* Mikrokernel

### V praxi

...

&nbsp; 

# Zařízení

## Topologie

## Zacházení

## Komunikace

### Přerušení

&nbsp; 

# Počítáním, multitasking, ...

&nbsp;

# Soubory

> 25.05.2021 - 13. Přednáška

## Virtuální paměť

_VAS - virtuální adresový prostor a PAS - fyzický adresový prostor_

### Základní koncepty
* ...
* ...
* Hardwarové překládání adres (memory managment unit)

### Proč?
* Hodí se větší adresový prostor (VAS je větší než PAS) - ale to už dneska tolik nepotřebujeme
* Bezpečnost - oddělím adresové procesi jednotlivých procesů

### Segmentace

#### Koncepty
* Virtuální adresový prostor je rozdělný na logické segmenty
* Virtuální adresa je tvořená dvojcí číslo segmentu a ofset
* Operační systém se pak stará o semgentační tabulku (pole, které si pamatuje původní fyzickou adresu, délku a atributy každého segmentu)
_atributy jsou například oprávnění (read only, ...), povelené instrukce, zda je to systémová paměť_

Kontroluje se chyba hledání neexistujícího indexu.

Co když dojde prostor? - vyhození na fyzický disk _(To ale trvá celkem dlouho)_ ...pak ho ale zase znovu potřebuji a proto ho pak načítám
* Hlavní důvod proč se dnes segmentace nepoužívá
 
### Stránkování
#### Koncepty
* VAS je rozdělený do stejně velkých částí (stránek) velikosti mocniny dvou
* PAS je opět rozdělených na stejně velké částí (rámce) se stejnou velikostí jako stránky
  * celkem často se používají 4Kb
* Někde bokem v paměti je pro každý proces stránkovací tabulka
  * je indexovaná čísly stránek a každá položka obsahuje číslo rámce a atributy
  * page fault
* Jak vypadá virtuální adresa? První bity jsou číslo stránky a zbytek bitů je offset 
  * překlad probíhá extrémně snadno - vezme několik vyšších $n$ bitů, zjistí podle nich rámec, dá horních $n$ bitů rámce před offset a to je hledaná fyzická adresa
  * Pokud mapování neexistuje, nastane page fault (vápadek stránky)
* Výhoda oproti segmentaci je, že rámce nemusí být ve fyzické paměti souvisle za sebou

#### Problémy
* Velikost - u 32-bit je 20 miliónů (12 bitů) 4k rámců
  * To se řeší více úrovněma
* Rychlost

Paměť řeší víceúrovňová stránkovací tabulka
* Nepotřebujeme celý VAP
* První úroveň je vždycky v paměti, ale ty ostatní můžou chybět
* Paměti ale trpí ještě víc - jak to vyřešit?

Řešení rychlosti
* **Zakešovat to**
* TLB (Translation Lookaside Buffer)
  * Nemusím pak většinou prolézat celou tabulku (často používám byty u sebe)

> BTW: AMD zavedlo čtyřúrovňové adresování pro 64b a to ještě ne úplně xddd (jakože 48 bitů)

#### Algoritmus překladu adresy u stránkování
* rozdělit adresu na offset a stránků
* zkontrolovat TLB, jestli nemá mapování
  * jestli to tam je, tak nice, jinak...
* projít celou stránkovací tabulku
  * rozdelím číslo stránky na tolik částí kolik mám úrovní
  * jdu do první úrovně, podívám se jestli je tam mapování pro další úroveň, jdu dál a takhle projdu všechny úrovně
  * z poslední úrovně dostanu číslo rámce a to si dám do TLB
* aktualizuju bity A a D (Access a Dirty) ve stránkovací tabulkce a TLB
* dostanu fyzickou adresu slepením původního offsetu a rámce

#### Výpadek stránky - co to vlastně je?
* Handler musí zjistit kde ten problém se stránkováním nastal
  * třeba je to neoprávněný zápis, čtení ze systémové paměti, ...
  * zkoušela pracovat s pamětí mimo fyzickou
* Systém se snaží zajistit, aby to mapování existovalo a prvně tedy najde rámec
  * co když už ale není volná paměť?
  * musím najít oběť
  * přijde na řadu bit A a D, protože musíme Dirty stránky uložit a oddělat stránky z TLB
  * na volný frame po oběti načtu obsah a přenastavím stránkovací tabulky
* Vrátím to zpátky z Handleru a znovu zkusím instrukci

> 01.06.2021 - 14. Přednáška

	Pozn. U toho jak to popisujeme se může stát, že 2B na rozhrání můžou způsobit 4 výpadky stránky (vytvořit tabulku, stránku a znovu)

#### Algoritmy na výměnu stránek

V jakékoliv situaci, kde potřebujeme najít nějakou oběť a vyhodit ji při omezeném prostoru

##### Algoritmus pro nalezení optimální stárnky (Optimal page algorithm)

Nahradím stránku, která bude nejdéle nepoužitá

Je to ale teoreticky, protože to samozřejmně nedokážme říct

###### Hodiny
* Zoraginizuju si rámce do kruhu
* Ručička ukazuje na další rámec k nahrazení
* Pokud je A (Access) různý od nuly, tak A vynaluji a jdu dál
	* Když to ale je nula, tak to vyberu

###### NRU (Not Recently Used)
* Příznaky A se nulují pravidelně
* Rozdělím je do 4 tříd podle příznaků A a D (1 - 0 0; 2 - 0 1; ...)
* Vybírám pak od nejnižší třídy

###### LRU (Least Recently Used)
* Používám minulost pro předpovídání
* Jinými slovy vyberu to nejdéle nepoužitou stránku
* Implementuje se to HW
	* Cache, ...
* ALe i SW
	* Nejjednoduší je zásobník, ale je to příliš neefektivní
	* Řeší se to aproximací
	
###### NFU (Not Frequently Used)
* Každý rámec má svoje počítadlo
* Pravidelně nulují A a případně zvýšší počítadlo
* Vybere se počítadlo s nejnižším počítadlem
* Problém s vypadáváním nových stránek (dočasná ochrana) a nevypadáním starých (snižování počítadel - dělení 2)

#### Sdílená paměť

Propojení více procesů tak aby si viděli navzájem do adresových prostorů

Jiná adresace kvůli kolizi (hádám), takže se používá jen offset

#### Paměťově-namapované soubory

Stránky mapuji na obsah souboru

Když nastane výpadek stránky, tak se můžou použít data ze souboru

Problém s přidáváním dat

&nbsp;
 
# Virtualizace

	Přetížený pojem, teď už se budeme bavit o plné virtualizaci

V rámci (host) OS umožníme vyrobit chráněné prostředí, které umožní spustit jiný OS (s iluzí, že to běží na reálném HW)

V případě problému ten problém vypadne a musí se o to postarat host (není to naštěstí příliš časté)

Výhody jsou
* izolace (nelze se přes VM dostat ke zbytku počítače)
* enkapsulace (mimo jiné VM snadno obnovím přes snapshoty)
* kompatibilita (snadno se to přenáší na jiný HW)

## Kontejnery (Virtualizace na úrovni OS)

Hodně zjednodušená virtualizace - používá se reálný HW a ne virtualizovaný

Musí to umět kernel

&nbsp; 

# Paralelní programování

Procesy jsou vykonávané současně

## Paralelní počítání

Používá se více jader

## Concurrent počítání

Počítá se na jediném jádru


### Race condition

Výsledek počítání závisí na naplánování vláken

Různě naplánované vlákna změní například pořadí prvků ve spojovém seznamu

Ještě horší je ale serializace (co procesor provede dřív v např. případě konfilktu zásadhu do paměti) - na přednášce ukázka nezařazení prvku do spojáku

#### Kritická sekce

Identifikuji kritickou sekci kódu, která může být vykonávána nejvýše jedním vláknem, aby nenastaly předchozí problémy

&nbsp; 

# Synchronizace

Řeší se to také synchornizací

Touto ochranou se ale zavedou další nepžíjemné jevy

Buď se například zamyká kritikcá sekce a nebo se procesy něčím řídí

Realizuje se pomocí **synchronizačních primitiv**
* Aktivní
	* Spotřebovávají čas procesoru (aktivní čekání)
* Pasivní
	* V jádře OS je jednotka plánování zablokovaná do té doby než je přístup povolen
	
		Ty blokující ale nejsou vždy výhodné, jak by se mohl zdát, protože sys-calls jsou celkem drahé (desítky až stovky instrukcí)

Implementuje také HW
* Atomické instrukce (Instrukce test-and-set nebo-li compare-and-swap)
	* Musí se provést celá bez přerušení (zamkne se i paměť)

### Spin-Lock
* Aktivní čekání přes test-and-set
* krátká latence (vhodné pro krátké čekání)

### Semafor
* chráněné počítadlo...

Mutex

## Deadlock

Nekonečný kruh čekání

## Alegorie

### Producer-consumer

### Filozofové

&nbsp;

---

&nbsp;

# Otázky u zkoušky z Discordu

> Zkouška bude jedna otázka

1. ISA
	* *Co si pod tím představit, co musíme mít, Call-Execute-Return, Ortogonalita* \
&nbsp;

2. Předávání parametrů funkcím, návratové hodnoty a pointery

3. Volací konvence

4. Stránkování a algoritmy na výměnu stránek\
	* *Proč se to dělá, že jde o VAS a PAS, že je nějaká TLB, vztah stránek a rámců, víceúrovňové stránkování, k čemu je stránkovací tabulka, jak se rozřeže VA na více částí*\
&nbsp;

5. Synchronizace
	* *Co je za problém (race condition/critical section), primitiva aktivní/pasivní+kdy je co lepší; jak funguje spinlock, TAS, dopodrobna semafor, atomičnost* \
&nbsp;

6. Deadlock, příběh s filozofy a skladištěm
