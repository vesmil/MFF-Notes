# INCOMPLETE

# C a C++

Známe z cvika a u zkoušky nebude

<br> 

# CPU

>16.3.2021 - 3. Přednáška

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
  Memory	            | 
	                    v
	                   I/O
```

#### Reálná

Vlastní sběrnice pro paměť - dokonce více paměťových kanálů

Buď přímo uvnitř procesoru a nebo přes PCIe grafa

Do procesoru vede sběrnice (někdy DMI) do South Bridge\
V něm jsou perfiferie jako zvukovka, síťovka, …

Dřív býval i North bridge pro přístup k pamětím, ale ten se přesunul do procesoru
 pro přístup k pamětím \
Nyní jsou všechny sběrnice sériové, kvůli fyzikálním důvodům - PCIe, SATA, USB, … \
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

> 23.3.2021 - 4. Přednáška

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

> 30.3.2021 - 5. Přednáška

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

Pak to vejde do reorder buffer, který výsledky vrátí zpět do správného pořadí (musí se řešit konflitky… )

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

> 6.4.2021 - 6. Přednáška

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
&nbsp; NUMA uzel je potom dvojice procesor a paměť

Vlastě se ale všechny systémy chovají jako NUMA, ale tak to nevadí, když je jen jeden procesor

<br>

# Programovací jazyky

## Překladač

Nějaká černá skříňka, která z kódu vyrobí něco spustitelného nebo chybovou hlášku

**Formální popis** \
Stručně překladač je zobrazení slov z vstupního jazyka generovnaného gramatikou do výstupního jazyka generováného jinou gramtikou a nebo přijímaného automatem

Jazyk má nějaká pravidla a lexikální elemty (while, do, … )

> Tohle je spíš jen teaser na AutoGram

### Praktický pohled na překlad

1. **Preprocesor** zpracuje zdrojový kód, postará se o věci jako `include` a vytvoří `.pp` soubor

2. Ten spolu s rozhraním dostane **překladač** a vyrobí z něj `asm` (asembler texťák)

3. **Assembler** pak z `.asm` vyrobí binární podobu `.obj`

4. Až budu mít všechny zrojkáky jako obj. tak to spolu s obj. knihoven dostane **linker** a ten vyrobí executable

Dnes se skoro celý proces dělá z uživatelského hlediska v jednom překladači

> Rozdíl mezi interface a knihovnou je v tom, že v interface není implementace a knihovna je pak už binární

OS pak z programu udělá proces -- spuštění

> 13.04.2021 - 7. Přednáška

Spuštění programu znamená načtení do paměti určité struktury, ta má podle tradičního pohledu čtyři části

* Kód
	* Sekce kódu s instrukcemi a občas i data
* Statická data
	* Globální proměnné
* Stack (zásobník)
	* Jsou v něm informace kam se vrátit z volání funkcí a lokální proměnné
* Heap (Halda)
	* Paměť určená na alokaci dat
	* Je na konci a jde směrem proti stacku (nebo obráceně)

Reálný detailnější pohled potom je

* Kód
* Konstanty
	* Jenom read-only
* Inicializovaná statická data
* Neinicializovaná statická data
	* Data zde se nulují až za běhu (ještě před main)
* Zásobník pro první vlákno
* …
* Zásobník pro vlákno n
	* Jak odhadnout jak velký má být zásobník? Několik mega a většinou nepřeteče
* Halda (společná pro všechny)

## Linker

**Knihovna** \
Kolekce zkompilovaných kódů (modulů)\

**Staické x dynamické knihovny** \
Ve statické se to přímo nakopíruje \
V dynamické si do executable jenom poznamenám, že potřebuji nějakou funkci a až za běhu se to sežene a nahraje do paměti -- je to dobré, protože dost knihoven se používá pořád dokola

**Linkování** \
Slepení výsledků různých překladů a knihoven do jednoho executable pro určitý OS

**Loader** \
Část OS, která musí načíst executable do paměti a např. sehnat dynamické knihovny

### Co všechno linker dělá

> V prezentaci je pak ukázka jak linkování vypadá… není vidět nic moc zajímavýho, snad jen to, že se berou jen potřebné věci a slepování není přímo za sebe, ale přímo za sebou jsou podsegmenty

Musí se také řešit to, že před linkování nevím, kam jaká adresa povede a proto používám v překladači jen relativní adresy od začátku segmentu (vytvořím relokaci v objektu)

V relokaci je i vůči jakém segmentu to je \
&nbsp; Např. v případě, že ukazuji do statických dat a ty se posunou (dá se mezi to nějaká další data)

Linker to musí po slepení opravit tak, že ke všem přičte absolutní adresu začátku zapsaného segmentu

> Loader provádí další relokaci při spuštění -- počítal jsem, že začátek soubouru je nula, ale co když ne

Další věc je, že linker hledá entry point (to btw není main) a ten musí být jen jeden

Když napíšeme, že je něco public, tak tu informaci dostane object -- sekce public

> Btw u C je to divně, že cokoliv globálního není static, tak je public

Když použijeme něco od někud jinud -- sekce extern

Po prvním průchodu si označím publicy a externy a potom je správně slinkuju

## Run-time (běhová podpora)

Jazyk potřebuje statickou podporu (překladač a rozhraní na knihovny) při překladu \
A dynamickou podporu za běhu (běhové prostředí, volací konvence, knihovny)

## Volání funkce 

Každá funkce dostane aktivační záznam -- určitá datová struktura mimo kterou funkce nesahá

Volající funkce v aktivačním záznamu připraví 
* pokud je to něco velkýho, tak před tím ještě **return value**
	* pokud je to reference nebo malá hodnota, tak to být nemusí \
* **parametry**

Pak si tam sama funkce schová
* kam se chce vrátit -- **return address**
* aktivační záznam volající funkce -- **control link**
* některé registry, které se musí zachovat -- **saved machine status**
	* Ukazuje i na frame pointer volající funkce

Tady je **frame pointer** - ukazatel na aktivační záznam

* Lokální data
* Temp data

### Volací konvence

> Hodí se aby to měly všechny překladače abychom mohli spojit jinak zkompilované zdrojáky

* Mandlování veřejných jmen
	* Linkování funguje hloupě, že provnává stringy publiců a externů
	* Takže musíme použít mangling na jméno, abychom funkci mohli například přetížit
* Musí se domluvit kdo co uklízí (aktivační záznam na zásobníku, … ) -- Cal/return sekvence
* Jak se předávají parametry
	* Obvykle na zásobníku, ale jde to i registrama
	* V jakém pořadí se to na zásobník dává
* Návratová hodnota
	* Jestli se to dá do registru
	* Co dělat když je to nějaká velká struktura
* Registry -- které jsou scratch a můžou se zkazit, které se musí zachovat -- preserved

> V prezentaci příklady mandlování

Hlavně se tam v Céčku přidává velikost parametru a C++ to znetvoří

> 20.04.2021 - 8. Přednáška

#### Call/return sequence (zodpovědnosti)

**V Céčku** \
Každá funkce se stará o svoje linky, machine state a lokální data (smazání a obnova) \
Naopak volající funkce se stará o parametry a return value

Některé volací konvence ale dělají i to, že se smažou parametry -- některé procesory to mají jednou instrukcí \
&nbsp; Jde to jen u funkcí s pevným počtem parametrů

#### Předávání parametrů

**Hodnotou** \
Zkopíruje se to a je to pak jako lokální proměnná \
Čistý Céčko umí jen hodnotou

**Referencí** \
Předá se jen adresa \
V C++ je to `&`

Co jsou ale ukazatele? \
&nbsp; V C reference chyběli a proto to tam low level přidali `*` \
&nbsp; Rozdíl je v tom, že to není fixní a taky musíme říct, že chceme měnit hodnotu reference

### Proměnné

Pojmenovaný kousek paměti, který drží hodnotu

Má nějaký typ 

Kde to leží?
* Statická data (např. globální proměnné v C)
* Zásobník (např. lokální data v C)
* Halda (např. dynamická paměť v C#)
* Slovník (je to např. v Pythonu)
	* jakoby mapa a až za běhu se zjišťuje kde co leží a jaký je to typ

### Halda

Dynamická paměť ze které si při výpočtu můžu brát

> Data v ní mají větší životnost než v zásobníku

Je tam nějaká ta evidence volného místa

První krok je ale alokace -- alokační algoritmy \
&nbsp; Je to např. když zavoláme `new`, btw to vrátí ukazatel \
&nbsp; &nbsp; C# a podobně se ukazatele snaží schovat

Naopak na konci musím dealokovat \
&nbsp; V některých je to explicitně -- C a C++ \
&nbsp; Občas se na to zapomínalo nebo nastaly vyjímky, takže se zavedla garbage collection \
&nbsp; &nbsp; Ono to se někdy samo uvolní \
&nbsp; &nbsp; Má to tendenci vzít všechnu možnou paměť

### Garbage collection

Automatické odstranění nepoužitých paměťových bloků

Vyhneme se nechtěným memory leakum (zabraná paměť na kterou už nic neukazuje), je rychlá alokace, … \
Na druhou stranu je to nepředvídatelné (životní cyklus) a má to vliv na výkon

#### GC strategie

* Trasování
	* průchod a zjišténí, které objekty jsou dosažitelné (živé)
	* pozor ale na zacyklení
* Počítání referencí
	* Kolikrát co použiju -- problém s cykly (ukazatele navzájem mezi více objekty)
* Reálně se používají pokročilejší

### Přenositelnost

#### Přenositelnost zdrojového kódu

Je potřeba si dávat pozor na:

* CPU architekturu
	* Rozdílné velikosti základních typů na procesorech
	* Někde jsou i fixní typy
* Překladače
	* Údajně mají "vlastní příchutě"
	* Například drobné syntaktické změny a knihovny -- naštěstí ISO 
* OS
	* Často potřebuji systémové volání, když něco nemám v knihovně (Linux x Windows, … )
	* Používají podmíněné překlad

#### Binární přenositelnost

**Přenositelnost VMkem** \
Překladač to přeloží do mezikódu (bytecode, CIL, … ) \
To se předhodí do nějakého nativního VM (JRE, CLR, … ), který mezikód interpretuje v sandboxu

To ale bylo dost pomalé

Používá se **JIT (Just-in-Time)** \
Postupně se za běhu zdroják dopřekládá na nativní kód a zakešuje to na disk

**AOT (Ahead-of-Time)** \
To bylo pořád nepříjemné a proto se např. na Androidech distribuje mezikód a přeloží se to při instalaci

<br>

# Operační systémy 

> 27.04.2021 - 9. Přednáška

Nemá to úplně přesnou definici, ale je to definováno účelem

V první řadě je to abstraktní stroj \
&nbsp; Je to prezentováno přes API jádra -- systémové volání \
&nbsp; V první řadě to schovává komplexitu HW (např. nabízí soubory, … )

Dále musí řídit zdroje \
&nbsp; Na jednom Hw běží více aplkikací

## Dva režimy (CPU módy)

**User mód** \
Dostupný všem aplikacím, ale má omezený přístup

**Kernel mód** \
Používá ho OS nebo dokonce jen jeho část

V aplikacích použijem sys. call, který je potřeba uďělat v kernel mode -- musí se to přepnout\
Kernel mód dělá user akce a nebo se přepne zpět triviálně, ale jak to udělat obráceně?

* Když se aplikace zkouší dělat systémvou instrukci přímo, tak ji OS killne
* Musí být nějak dodefinovaná instrukce (ISA) a nebo se používá trik s vyvoláním chyby
* Po přepnutí začneme na nějaké dobře definované adrese a parametry předáme přes registry 

## Architektura

* Monolitická
	* Velká kolosální věc, která celá běží privilegovaně
	* Nemá to pořádně strukturu (kromě entry point ze kterého je něco jako switch servisních procedur a ty pak vedou dál na utility procedury)
	* Tak se to hlavně dělalo dřív -- např. Linux\
&nbsp;
	* Výhoda je, že to dost efektivní
	* Na druhou stranu bezpečnostní díry a dřív se to špatně rozšiřovalo (teď moduly) \
&nbsp;

* Vrstvená
	* Vzniklo z monolitu, akorát se to rozdělilo do vrstev
	* Lze vžy používat jen sousední vrstvu \
&nbsp;
	* Je to snadněji rozšířitelné, snazší realizovat, … \
	* Návrh rozhraní je dost náročný  \
&nbsp;

* Mikrokernel
	* Z názvu je zřejmé, že se snaží o nejmenší velikost jádra
	* Hlavně zajišťuje komunikaci mezi jednotlivými moduly -- předávání zpráv
	* Windows je postavený na konceptu mikrokernelu \
&nbsp;
	* snadno rozšiřitelný, bezpečný a spolehlivý

<!-- TODO dát tam lokální image -->
<center>
<img  src="https://upload.wikimedia.org/wikipedia/commons/5/5d/Windows_2000_architecture.svg" width="420"> 

*Kernelová architektura Windows*
</center>
<br>

> Např vlastnost, že Windows není case sensitive je vlastnost Win32 knihovny a ne Windows

Windows microkernel už nezávisí na architektuře, protože o to se stará Hardware Abstraction

> Podle Yaghoba je ta architektura čistčí než ta Linuxu

# Zařízení

	"Věc vyrobneá za určitým účelem"

Je k němu potřeba **device controller** (řadič) \
&nbsp; Ten se stará o signály, A/D konverzi \
&nbsp; Nějaká topologie zařízení…

A softwarově potom **device driver** (ovladač) \
&nbsp; Abstraktní interface

Kde zjistit jakou má zařízení adresu? \
&nbsp; Při bootu (BIOS, UEFI) se projdou zařízení, každé dostane nějakou adresu v paměti a vytvoří se jejich tabulky

## Topologie

**Sdílená sběrnice (bus)** \
Jeden drát z device controller na který se připojí ostatní zařízení \
&nbsp; Musí se tam řesit arbitrace, protože zařízení je tam hodně \
&nbsp; Taky je omezená kapaciu sběrnice

**Star** \
Zařízení p2p na řadič
&nbsp; Používá se dnes u disků\
&nbsp; Nevýhoda je složitější konstrukce řadiče (více vývodů, … )

**Ring** \
Orientovaná kružnice ze zařízení \
&nbsp; Levnější řešení

**Tree** \
Uspořádané do grafového stromu a DC je v kořeni \
&nbsp; Může se větvit pomocí hub \
&nbsp; Např. USB 

Typicky se nedovoluje přidávání zařízení \
Např. USB protokol to kontroluje a povoluje

## Zacházení se zařízením

Tohle řeší OS

Většina kódu OS je nezávislá na ovladačích a řadičích

> Na uživatelské úrovni neděláme přímo syscalls, ale používáme knihovnu kvůli přenositelnosti

Rozhraní (ta knihovna) tedy zavolá syscall \
Řekne, že chce např. otevřít file systém \

Musím najít a pak otevřít a zapamatovat si handle (identifikaci) toho souboru \

Až budu číst tak soubor znovu nehledám a nějak se moje žádost dostane až k ovladači\
&nbsp; (Prochází to mimo jiné device independent mezivrstvou)

Z ovladače to hde do řadiče, tam je nějaká HW komunikace podle protokolu a pak to jde zpět \
&nbsp; HW komunikace může proběhnou několikrát než se ten požadavek vrátí

> 04.05.2021 - 10. Přednáška

Nejnáročnější je domluva řadiče s ovladačem, že už je hotovo (navíc to trvá dlouho), takže se to dělá pomocí:

* **Polling** (očmuchávání xdd)
	* Procesor se periodicky dívá do paměti a čeká na změnu
	* Nevýhoda je, že musím aktivně něco dělat a má to zpoždění
* **Interrupt**
	* Zařízení dá signál procesoru, ten přestane dělat to co právě dělá a jde na ovladač přerušení
* **DMA**
	* Přesun bez pozornosti CPU pomocí DMA řadiče mezi dvěma místy a pak interrup
	* Vůbec nic nepřesouval procesor
	* Problém je když například prependuju hlavičku v TCP/IP -- opakovaně zbytečně kopíruju \
&nbsp; Používá se scatter/gather -- DMA vezme data v paměti a vytvoří z nich blok nebo naopak to rozhází

<br>

# Přerušení

**Externí** \
Vyhrazené piny na CPU \
Jde to ale zakázat a povolit (v případě choulostivých operací)

**Exception (vyjímky)** \
Neočekávaně vyvolané instrukcí -- nedefinovaná operace, …

Nějak předdefinovaná -- např. pevná adresa kam jít \
Procesor starší generace tak může pomocí emulace použít novější instrukce a pak jít zpátky

Dva druhy -- trap (hlásí se až po vykonání) nebo fault (není schopna doběhnout a pak se to musí vrátit před)

**Software** \
Speciální instrukce, které mouhou být použité např. pro syscall

#### Jak se to řeší

CPU nějak musí určit zdroj interptu

* Vnější přerušení -- IRQ řadič přijme signál od některého z pinů a pak pošle int procesoru
* Vyjímky mají určitá čísla

Na jakou adresu ale jít? Buď fixní a nebo hledá v interrupt table

Pak se ale musím vrátit mezi instukce (nebo před) a tedy si schovat CPU state a pak ho načíst

<br> 

# Processing

**Program** \
Něco, co jsem zkompiloval a leží to na disku 

**Proces** \
Spuštěný program  - vykonává instrukce \
Spravovaný OS - prostředky jako např. paměť (musí se evidovat a pak vrátit)\
Má paměť kterou jsme si již ukazovali (Code, Static data, … )

**Vlákno (Thread)** \
Jedna aktivita v procesu - proud instrukcí pro CPU \
Má v sobě tzv. **kontext** procesoru -- všechny registry abych mohl pokračovat počítat \
Každé vlákno má svůj zásobník

> Na Linuxu je to trochu divně (procesy se sdílenou pamětí)

**Fiber** \
Menší jednotka než vlákno \
Dá se dodělat pro aplikaci pomocí knihoven\
Mívají kooperativní scheduling

**Scheduler** \
Část OS, která přiďěluje výpočetní zdroje (výkon procesoru) vláknům

> Na Woknech je to hnusný

**Multitasking** \
Souběžně spuštěných několik procesů -- musí se přehazovat procesy

**Multiprocessing** \
Více procesorů na jednou \
Náročný job pro scheduler

**Context** -- již bylo u vlákna

**Context switch** \
Proces uložení aktuálního kontextu a obnovení nějakého jiného

> 11.05.2021 - 11. Přednáška

## Plánování

### Real-time scheduling

RT proces má start (release) time a stop time (deadline)

Realese time tedy říká od kdy do kdy po události se musí spustit proces

Deadline do kdy to musí být hotovo \
**Hard deadline** -- nemá smysl to dělat, když to nestihnu \
**Soft deadline** -- pořád to ještě má cenu zkusit

### Stavový diagram plánování

Každá jednotka plánování (vlákno) má v sobě stav

* **Created** -- čeká to na spuštění (release time)
* **Ready** -- schopná běžet, ale ještě nemá k dispozici CPU
* **Running** -- self-explanatory… když běží moc dlouho, tak se to z toho hodí zase do ready
* **Blocked** -- když to čeká např. na čtení souboru
* **Terminated** -- když z running skončí

### Multitasking

Představa, že mám jen jedno jádro a chci střídat procesy, jak je ale střídat?

* Kooperativně
	* OS se o to nestará a všechny procesy spolu spolupracují

* Preemptivně
	* Každá plánovací jednotka dostane svůj časový slot (time-slice)
	* Když to během něho neskončí, tak na konci slotu dostane interrupt (timer) a hodí se to na ready

### Možné různé cíly plánovače

* Maximalizovat CPU vuyžití (v případě, že to potřebuju)
* Spravedlivé rozdělení
* Maximalizovat propustnost (počet procesů za určitý čas)
* Minimalizovat dobu jednoho procesu
* Minimalizovat čas v ready stavu
* Minimalizovat čas na odpověď (v interaktivních aplikacích)

### Priorita procesu

	Číslo, které vyjadřuje důležitost procesu

> Fun fact: pochází to od vojáků v Americe

Statická x dynamická priorita

Statická se přidělí na začátku a skoro se nemění \
Dynamická funguje tak, že jednou za čas se u ready procesů zvedne priorita a až se počítají tak se vynuluje

Celková pak vznikne jako jejich součet

### Plánovací algoritmy

#### Nepreemptivní

* **First come, first serve** -- basic fronta, vypočítám proces a jde další

* **Shortest job first** -- musíme vědět odhad jak dlouho proces bude zhruba trvat 

* **Longest job first** 

#### Preemptivní

* **Round Robin** 
	* Nějaká fronta (třeba prioritizovaná) a každý proces do CPU  dostane time-slice
	* Když to nestihne, tak jde na konec fronty

> Fun fact N˚2: je to z kruhové podpisového archu např. na protestech

* **Multilevel feedback-que**
	* Několik front, jdu od shora a najdu první neprázdnou
	* Vezmu si z ní první plánovací jednotku a pokud vyčerpá všechen čas, tak jde do nižší
	* V nižších frontách je větší time slice \
&nbsp;
* **Comletly fair scheduler (CFS)**
	* Z Linux jádra
	* Stručně vybírám procesy podle toho, jak moc běžely a nechám je podle toho, jak dlouho čekaly \
&nbsp;
	* Implementováno pomocí červeno-černého stromu indexovaného celkovým execution časem
	* Vypočítám si ještě maximum execution time (čas čekání vydělený počtem procesů)
	* Potom vybírám nejlevější uzel (uzel s nejmenším časem, jak dlouho běžel)
	* Až to dosáhne maximum execution time, tak se to znovu zařadí do stromu

<br>

# Soubory

	Nějaký abstraktní proud dat

**Operace** 

* Otevřít -- najít soubor na disku a poznamenat si jeho vlastnosti do objektu
* Zavřít -- odstraní se ten objekt a mapování (někdy zapsat cache)
* Číst a psát
* Seek -- dělá se abstrakce ukazovátka, kde právě jsem a seek to akorát posouvá

Soubory mají název jen kvůli uživatelům -- převádí se to na nějakou binární identifikaci

Z důvodu bezpečnosti OS soubory přečíslovává (nějaké mapování) aby procesy nemohly sahat jinam

> 18.05.2021 - 12. Přednáška

**Přístup**

* Sekvenční (jen se posouvat dopředu a nebo rewind)

* Náhodný

**Typ**\
&nbsp; Rozpoznává se přes extension (přípona)

**Atributy** \
&nbsp; Název, timestampy, velikost, access práva, …

### Adresář

	Sada souborů 

Hlavně je to user-friendly a pomáhá to při hledání

V adresáři jsou atributy souborů

Nějaká hierarchie s kořenem

Operace (hledání, vypsání, … )

### File system

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

>  U toho jak to popisujeme se může stát, že 2B na rozhrání můžou způsobit 4 výpadky stránky (vytvořit tabulku, stránku a znovu)

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

<br>
 
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

<br> 

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

<br> 

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

<br>

---

<br>

# Otázky u zkoušky z Discordu

> Zkouška bude jedna otázka

1. ISA
	* *Co si pod tím představit, co musíme mít, Call-Execute-Return, Ortogonalita* \
&nbsp;

2. Disk scheduling algoritmy a jejich význam + něco o access time obecně

2. Předávání parametrů funkcím, návratové hodnoty a pointery

3. Volací konvence

7. Interrupty a jejich obsluha

4. Stránkování a algoritmy na výměnu stránek\
	* *Proč se to dělá, že jde o VAS a PAS, že je nějaká TLB, vztah stránek a rámců, víceúrovňové stránkování, k čemu je stránkovací tabulka, jak se rozřeže VA na více částí*\
&nbsp;

5. Synchronizace
	* *Co je za problém (race condition/critical section), primitiva aktivní/pasivní+kdy je co lepší; jak funguje spinlock, TAS, dopodrobna semafor, atomičnost* \
&nbsp;

6. Synchronizační primitiva, stačilo vysvětlit k čemu jsou (concurrent computing -> race condition -> mutual exclusion -> atomic instructions), popsat spinlock a semafor a říct, jestli jsou aktivní nebo pasivní.

6. Segmentace

6. Deadlock, příběh s filozofy a skladištěm
