Kdyby chtěl někdo Markdown a nebo našel nějakou nepřesnost: [Odkaz na Github](https://github.com/vesmil/MFF-Notes/blob/main/1b_letni/Systems_souhrn.md)

[Odkaz na light mode](./light.html) (až budu mít čas, tak to udělám normálně)

# C a C++

Známe z cvika a u zkoušky nebude

<br> 

>16.3.2021 - 3. Přednáška

# CPU

### Architektura

**Von Neumannova**\
Jedna sdílená sběrnice a na ní CPU, Paměť a I/O \
Vždy jedna transakce na sběrnici

**Harvardská** \
Instuction memmory je na CPU připojeno vlastní sběrnicí \
Doteď se používá v některých mikrocontrolerech\
Je potřeba více adresových prostorů na procesoru

#### Reálná

Pro paměť je k CPU vlastní sběrnice -- dokonce více paměťových kanálů

Grafika je buď přímo uvnitř procesoru a nebo přes PCIe

Z procesoru vede sběrnice (někdy DMI) do South Bridge\
V něm jsou periferie jako zvukovka, síťovka, …

Dřív býval i North bridge pro přístup k pamětím, ale ten se přesunul do procesoru

Nyní jsou všechny sběrnice sériové -- PCIe, SATA, USB, … \
Zároveň jsou všechnu sběrnice peer to peer

### Co je ale architektura?
 
* Instrukční sady (ISA) - jak se ten procesor má chovat podle instrukcí 
	* například i64 (rozšíření x86), MIPS, ARM, …

> x86 je údajně extrémně špatná

* Hardwarová architektura - třeba Skylake, Coffee Lake  … je to to jak výrobce implementoval ISA

> Pak debata na téma proč jsou aktuální instrukční sady špatné - zbytečně moc bloat instrukcí, ale když se pokoušeli o něco nového (např. Itanium), tak problém s portováním a pomalý emulátor
 
> Na mobilu je větší prostor pro zlepšení kvůli překladu při instalaci a častěji se tam zavádí nová architektura

Hlavní úkol procesoru je vykonávat jednoduché instrukce

### Třídy instrukcí

* Load
* Store
	* Dva nejdůležitější druhy instrukcí, ale jsou dost pomalé
	* Na rozumných architekturách to jsou jediné, které pracují s pamětí\
&nbsp; &nbsp; Ale třeba i64 zvládne inkrementovat číslo i v paměti
* Move -- mezi registry
* Aritmetické
* Jumps
	* Nepodmíněné x podmíněné 
	* Přímé (přímo adresa kam) x nepřímé (adresa kam je na adrese) x relativní adresa (o kolik se posunout dál)
* Call
	* Při volání funkcí je potřeba nějaký zásobník s návratovou adresou\
	&nbsp; &nbsp; Buď Hardwarový zásobník a nebo na to použiju registry

> Ještě tam v podstatě chybí porovnání

### Registry

* Obecné
* Integer a float
* Adresové
* Branch registry - skokové registry
* Příznakové registy
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
&nbsp; Dost se tomu snaží vyhnout, protože je pak problém třeba udělat překladač nebo poznat změnu

32-bitový EAX má ještě 16b podregistr AX a ten je rozdělený ještě na AH a AL

## Příklady

x86 není ortogonální a tedy libovolná instrukce nemůže pracovat s libovolným registrem

Jeho sepcializované registry: EAX je akumulátor, EBX je base, ECX je count, EDX je data, …

> Je to hodně nepříjemné

Segmentové registry - Datový, Kódový, Stack ...

Instruction pointer na aktuální vykonávanou instrukci

Oproti x86 má Itanium (IA-64) několikset registrů

### MIPS

32 registrů r0-r31 \
&nbsp; &nbsp; r0 je vždycky nula \
&nbsp; &nbsp; r31 je link register na `jal` -- návratová adresa, používá se jako `call`

Nemá HW stack ani flagy

> 23.3.2021 - 4. Přednáška

Od MIPS je odvozená RISC-V

#### Instrukce MIPS

x86 narozdíl od MIPS není schopná sečíst dvě věci a zapsat jinam

Operace známe už z principů and, ro, xor, … (místo not je negované or), shift, …

Proměnlivé x pevné kódování\
&nbsp; např. instrukce x86 jsou různě dlouhé, ale MIPS má pevně 32bitů

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

Zrada v tom, že každá instrukce třeba na x86 se z hlediska změny příznaků chová úplně jinak

Běžné flagy jsou zero, sign a carry

Jsou systémové a uživatelské příznaky a x86 je zmastila dohromady - musí se složitě schovávat

### Co všechno je v procesoru?

* Řadič paměti
* Hierarchie keší
* Jádra
* Registry
* Logický procesor
	* uvnitř jádra -- víc proudů instrukcí (u Intelu hyperthreading)

### Instrukce

Je to nějaký jednoduchý příkaz procesoru

Musí být nějak zakódovaná -- překlad přes assembler…  \
Ale i textovému zápisu instrukcí se říká assembler

Mají operandy -- jakoby argumentu (konstanty, adresy, registry)

Proud instrukcí je řízený program counterem

### ISA

**Klasifikace instrukční sady**

* CISC - komplexní sada
	* Někdy se musí mezipřekládat do mikrokódu	
* RISC - redukovaná sada
* VLIW - very long instruction word
	* Třeba 128 bitová instrukce - bývá třeba ve switchích
* EPIC - explicitly parallel instruction computer 
	* Je v tom explicitně jaký části mají být paralelně (mělo třeba Itanium)

Arm už není ani náhodou RISC 

U x86 rovnou instrukce odpovídají mikroinstrukci, takže to není úplně CISC \
teda pak tam jsou nějaké nepoužívané instrukce, které se překládají na mikro

**Ortogonalita** \
Už bylo -- to jestli jsou specializované registry a nebo jdou v instrukcích zaměnit

**Load-Execute-Store**\
To, že se pracuje jen s registrama a nedělá se třeba aritmetika v paměti

### Zjednodušene schéma

Každé jádro má 

* výpočetní jednotku (exuction unit)
* cache 
	* tři úrovně (L1 skoro stejně rychlá jako registr) 
	* L1 je rozdělená na instrukce a data
* vlákna
	* více vláken sdílí jednu výpočetní jednotku, protože běžně nebývá vytížená na 100%

Každé jádro má u sebe kousek svojí L3 a berou si navzájem po oboustranným ringu

Dělá se prefetch - odhadování jaká data budou potřeba

### Schéma jednoho jádra

Front-end čte instrukce a dekóduje je\
&nbsp; Coffee lake má 5-cestný dekodér, takže dékoduje 5 inst. v taktu \
&nbsp; Jeden z nich je komplexní, který je právě na překlad na mikroinstrukce

Po dekódoání operace spadnou do "bazénku" a pak čeká až bude moc jít na zpracování\
&nbsp; Out of order execution - celkem chaotické

> 30.3.2021 - 5. Přednáška

### Techniky pro zrychlení CPU

#### Pipeline

Rozdělit vykonávání na jednotlivé stages (reálně jich bývá 14-19)

V jednom čase mám rozdělaných několik instrukcí a každá je v jiné fázi\
&nbsp; Něco v instruction fetch, něco už se vykonává, něco práce s pamětí, …

**Náběh pipeline** je doba než se stihnout "naplnit" všechny procesy/stages \
**Doběh** v HW nenastane

Když vypadne, tak musí znovu nabíhat \
&nbsp; Například při podmíněném skoku musím při špatném odhadu veškerou práci zahodit \

> Technika pipeline se používá i jinde - zvuk, televize, … (zmínka o latenci)

Návrh je jednodušší a za jednotku času jsem schopný provést víc instrukcí \
&nbsp; Vzniká ale latence

#### Superskalarita

V každé stage se místo jedné instrukce jich nachází víc

Musí mít např. zdvojené jednotky

Dnešní procesory jsou dokonce 5-cestné

Jsou také asymetrické (nemusí se stejná stage zpracovávat stejně - viz. simple a complex dekódování instrukcí)

### Zpátky k schéma

Po dekódování jsou tedy v tom "bazénku" - Reservation station

Každý port do kterého pak instrukce z poolu pokračují umí něco jiného

Nakonec to vejde do reorder buffer, který výsledky vrátí zpět do správného pořadí (musí se řešit konflitky… )

<br>

# Paměť

> Dost z toho už máme znát ze zimního

Je organizována do bitů a ty jsou uskupovány do slov \
Každé slovo má má svoji N-bitovou adresu a umíme uložit 2^N slov\
Dnes se používá 8-bit slovo nebo-li byte

### Adresový prostor

Očíslování slov v paměti

Fyzicky je paměť jako dvourozměrný prostor \
Adresovaný po řádcích a sloupcích

Měnit řadky trvá delší dobu než slupce (pokud přistupuji sekvenčně, tak adresa nejprve roste po sloupcích)

Nejdůležitější u RAM je CAS - čas na přístup k sloupci \
Pak tam jsou i časy tRCD, tRP, RAS

### Reprezentace data

* Bezznaménková čísla (0 až 2^N -- 1)
* Znaménková (dvojkový doplněk)
* Float podle IEEE 754 - mantisa a exponent, …

### Endianita

Big endian - MSB first \
Little endian - LSB first

Skoro všechny procesory BE a nebo vybrat, Intel má LE

Síťové protokoly jsou BE, takže Intel musí převracet

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
Chvíli ho používáme a pak ho zahodíme\
&nbsp; Bud explicitně a nebo Java a spol mají garbage collector

Pozn. hodnoty a referance se mažou vždy (jsou lokální), ale musíme třeba mazat na co ukazovali

#### Faragmentace

Jeden z problémů alokace

Paměť je rozdělená do malých bloků abych si mohl pamatovat, co je zabrané 

Pamatovat si to po bytech by bylo nepraktické -- moc detailně a musel bych pak řešit zarovnání

**Interní** \
Data v bloku jsou menší než ten blok. S tím ale nic neudělám

**Externí** \
Mám hodně volného místa rozdrobené do nesouvislých malých bloků

#### Dynamická alokace paměti

##### Jak si pamatovat volné bloky?

* Spoják volných bloků (zabrané se většinou neevidují)
* Bitmapa

##### Alokační algoritmy

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

Pokud má volný blok kamaráda (volného souseda), tak je musím mergnout

Má to velkou interní fragmentaci (bloky jsou o dost větsí než potřeba)

> 6.4.2021 - 6. Přednáška

## Paměťová hierarchie

Sestupně podle rychlosti a zároveň vzestupně podle velikosti:

* Registry
* Cache
* RAM (a rychlejší SRAM)

Dále je to persistentní

* Persistent RAM
	* Je trochu pomalejší než RAM a musí se kvůli tomu opravit OS a programy
* SSD, flash
	* SSD a dál už není přímo adresovatelné procesorem -- používá se sběrnice a řadič
* HDD
	* Nejdéle trvá mechanický pohyb hlavou
* Pásky
	* Běžně na zálohy

## Cache

	Datová struktura ve které mám data, které bych znovu dlouho počítal

Hardware nebo software implementace

Pokud cache paměť dojde, tak použijeme stránkové algoritmy -- later

### Cache na CPU

Spoléhá na lokalitu přístupu -- předpokládáme, že pokud něco čteme z paměti, tak za nedlouhou dobu budeme číst něco těsně vedle

Již zmíněno L1 (doba přístupu 4 takty, desítky kB), L2, L3 (stovky taktů a jednotky MB)

Musíme řešit problémy, když chceme spolecčná data mezi jádry -- přesun mezi L3 \
Koherence keší a stará se o to procesor

### Cache pojmy

**Cache line** \
Cache není organizovaná po bytech, ale po jednotkách zvaných cache line (entry), které mají běžně 64B

**Cache hit** \
Tak se nazývá, když jsem trefil data ve cache (úspěšnost prý 97 %)

**Cache miss** \
Když se netrefím

**Cache line load** \
Musím načíst data, když nejsou v cache \
Pozor na to, že jsem do cache mohl i psát a proto pokud ji budu vyhazovat, tak se musí zapsat

**Cache line state** \
Používá se MESI protokol -- takže 4 stavy 

## Asociativní paměť

Dvojice klíč a hodnota

Dokážu tím očíslovat Cache lines v RAM

Velmi rychlá -- implementována hardwarově tak, že to nemusím celé procházet \
Stojí to hromadu tranzistorů, takže to není moc velké

## Systémy s více procesory

**Symmetric multiprocessing** \
&nbsp; Jedna sběrnice mezi RAM a CPUs \
&nbsp; Má limit pro kolik procesorů to je použitelné

**NUMA** (Non-uniform memory access) \
&nbsp; Každý procesor má svoji RAM \
&nbsp; Musí být ale dostupné mezi sebou\
&nbsp; Jsou navzájem propojené (ale ne každý s každým, protože to stojí piny) \
&nbsp; Přenos logicky stojí nějaký čas -- *NUMA factor*\
&nbsp; NUMA uzel je potom dvojice procesor a paměť

Vlastě se ale všechny systémy chovají jako NUMA, i když jen s jedním procesorem

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

Spuštění programu znamená načtení do paměti určité struktury:

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
	* Jsou v něm informace kam se vrátit z volání funkcí a lokální proměnné
* Halda (společná pro všechny)
	* Paměť určená na alokaci dat
	* Je na konci a jde směrem proti stacku (nebo obráceně)

## Linker

**Knihovna** \
Kolekce zkompilovaných kódů (modulů)

**Staické x dynamické knihovny** \
Ve statické se to přímo nakopíruje \
V dynamické si do executable jenom poznamenám, že potřebuji nějakou funkci a až za běhu se to sežene a nahraje do paměti -- je to dobré, protože dost knihoven se používá pořád dokola

**Linkování** \
Slepení výsledků různých překladů a knihoven do jednoho executable pro určitý OS

**Loader** \
Část OS, která musí načíst executable do paměti a např. sehnat dynamické knihovny

### Co všechno linker dělá

> V prezentaci je pak ukázka jak linkování vypadá… není vidět nic moc zajímavýho\
 Snad jen to, že se berou jen potřebné věci a slepování není přímo za sebe, ale po segmentech

Musí se také řešit to, že před linkování nevím, kam jaká adresa povede a proto používám v překladači jen relativní adresy od začátku segmentu (vytvořím relokaci v objektu)

V relokaci je i vůči jakém segmentu to je \
Např. v případě, že ukazuji do statických dat a ty se posunou (dá se mezi to nějaká další data)

Linker to musí po slepení opravit tak, že ke všem přičte absolutní adresu začátku zapsaného segmentu \
Loader provádí další relokaci při spuštění -- počítal jsem, že začátek soubouru je nula, ale co když ne

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

* pokud je to něco velkého, tak před tím ještě **return value**
	* pokud je to reference nebo malá hodnota, tak to být nemusí 
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
	* Obvykle na zásobníku, ale jde to i registry
	* V jakém pořadí se to na zásobník dává
* Návratová hodnota
	* Jestli se to dá do registru
	* Co dělat když je to nějaká velká struktura
* Registry -- které jsou scratch a můžou se zkazit, které se musí zachovat -- preserved

> V prezentaci příklady mandlování \
(Hlavně se tam v Céčku přidává velikost parametru a C++ to znetvoří)

> 20.04.2021 - 8. Přednáška

#### Call/return sequence (zodpovědnosti)

**V Céčku** \
Každá funkce se stará o svoje linky, machine state a lokální data (smazání a obnova) \
Naopak volající funkce se stará o parametry a return value

Některé volací konvence mají i to, že se volané smažou parametry -- některé procesory to dají jednou instrukcí \
&nbsp; Jde to ale jen u funkcí s pevným počtem parametrů

#### Předávání parametrů

**Hodnotou** \
Zkopíruje se to a je to pak jako lokální proměnná \
Čistý Céčko umí jen hodnotou

**Referencí** \
Předá se jen adresa \
V C++ je to `&`

Co jsou ale ukazatele? \
&nbsp; V C reference chyběly a proto to tam low level přidali `*` \
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

Je tam nějaká evidence volného místa

První krok je alokace -- alokační algoritmy \
&nbsp; Je to např. když zavoláme `new` (btw to vrátí ukazatel) \
&nbsp; &nbsp; C# a podobně se ukazatele snaží před programátory schovat

Naopak na konci musím dealokovat \
&nbsp; V některých je to explicitně -- C a C++ \
&nbsp; Občas se na to zapomínalo nebo nastaly vyjímky, takže se zavedla garbage collection \
&nbsp; &nbsp; Ono to se někdy samo uvolní \
&nbsp; &nbsp; Má to tendenci vzít všechnu možnou paměť

### Garbage collection

Automatické odstranění nepoužitých paměťových bloků

Vyhneme se nechtěným memory leakům (zabraná paměť na kterou už nic neukazuje), alokace je rychlá, … \
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
	* Používají podmíněný překlad

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

V první řadě je to **abstraktní stroj** \
&nbsp; Je to prezentováno přes API jádra -- systémové volání \
&nbsp; V první řadě to schovává komplexitu HW (např. nabízí soubory, … )

Dále musí **řídit zdroje** \
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

> Např vlastnost, že Windows není case sensitive je vlastnost Win32 knihovny

Windows microkernel už nezávisí na architektuře, protože o to se stará Hardware Abstraction

> Podle Yaghoba je ta architektura čistčí než ta Linuxu

# Zařízení

	Věc vyrobneá za určitým účelem …

Je k němu potřeba **device controller** (řadič) \
&nbsp; Ten se stará o signály, A/D konverzi \

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
&nbsp; Používá se dnes u disků \
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

Chci open file a rozhraní (ta knihovna) tedy zavolá syscall \
Musím najít a pak otevřít a zapamatovat si handle (identifikaci) toho souboru \
Až budu číst tak soubor znovu nehledám a nějak se moje žádost dostane až k ovladači\
&nbsp; (Prochází to mimo jiné device independent mezivrstvou)

Z ovladače to jde do řadiče, tam je nějaká HW komunikace podle protokolu a pak to jde zpět \
&nbsp; HW komunikace může proběhnou několikrát než se ten požadavek vrátí

> 04.05.2021 - 10. Přednáška

Nejnáročnější je domluva řadiče s ovladačem, že už je hotovo (navíc to trvá dlouho), takže se to dělá pomocí:

* **Polling** (očmuchávání xdd)
	* Procesor se periodicky dívá do paměti a čeká na změnu
	* Nevýhoda je, že musím aktivně něco dělat a má to zpoždění
* **Interrupt**
	* Zařízení dá signál procesoru, ten přestane dělat to co právě dělá a jde na ovladač přerušení
* **DMA (Direct memory access)**
	* Přesun bez pozornosti CPU pomocí DMA řadiče mezi dvěma místy a pak interrup
	* Vůbec nic nepřesouval procesor
	* Problém je když například prependuju hlavičku v TCP/IP -- opakovaně zbytečně kopíruju \
&nbsp; Používá se scatter/gather -- DMA vezme nesouvislá data a vytvoří z nich blok nebo naopak souvislý rozhází

<br>

# Přerušení

**Externí** \
Vyhrazené piny na CPU \
Jde to ale zakázat a povolit (v případě choulostivých operací) -- jen v kernel módu

**Exception (vyjímky)** \
Neočekávaně vyvolané instrukcí -- nedefinovaná operace, … \
Využití pro syscall softwarem

Nějak předdefinovaná -- např. pevná adresa kam jít \
Procesor starší generace tak může pomocí emulace použít novější instrukce a pak jít zpátky

Dva druhy -- trap (hlásí se až po vykonání) nebo fault (není schopna doběhnout a pak se to musí vrátit před)

#### Jak se to řeší

CPU nějak musí určit zdroj interptu

* Vnější přerušení -- IRQ řadič přijme signál od některého z pinů a pak pošle int procesoru
* Vyjímky mají určitá čísla

Na jakou adresu ale jít? Buď fixní a nebo hledá v interrupt table

Pak se ale musím vrátit mezi instrukce (nebo před) a tedy si schovat CPU state a pak ho načíst

<br> 

# Processing

**Program** \
Něco, co jsem zkompiloval a leží to na disku 

**Proces** \
Spuštěný program  - vykonává instrukce \
Je spravovaný OS - prostředky jako např. paměť (musí se evidovat a pak vrátit)\
Má paměť kterou jsme si již ukazovali (Code, Static data, … )

**Vlákno (Thread)** \
Jedna aktivita v procesu -- proud instrukcí pro CPU \
Má v sobě tzv. **kontext** procesoru -- všechny registry abych mohl pokračovat počítat \
Každé vlákno má svůj zásobník

> Na Linuxu je to trochu divně (procesy se sdílenou pamětí)

**Fiber** \
Menší jednotka než vlákno \
Dá se dodělat pro aplikaci pomocí knihoven \
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
Dynamická funguje tak, že jednou za čas se u ready procesů zvedne priorita a až se počítají tak se vynuluje \
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
	* Stručně: vybírám procesy podle toho, jak moc běžely a nechám je běžet podle toho, jak dlouho čekaly \
&nbsp;
	* Implementováno pomocí červeno-černého stromu indexovaného celkovým execution časem
	* Vypočítám si ještě maximum execution time (čas čekání vydělený počtem procesů)
	* Potom vybírám nejlevější uzel (uzel s nejmenším časem, jak dlouho běžel)
	* Až to dosáhne maximum execution time, tak se to znovu zařadí do stromu

<br>

# Soubory

	Abstraktní proud dat

**Operace** 

* Otevřít -- najít soubor na disku a poznamenat si jeho vlastnosti do objektu
* Zavřít -- odstraní se ten objekt a mapování (někdy zapsat cache)
* Číst a psát
* Seek -- dělá se abstrakce ukazovátka, kde právě jsem a seek to akorát posouvá

Soubory mají název jen kvůli uživatelům -- převádí se to na binární identifikaci

Z důvodu bezpečnosti OS soubory přečíslovává (nějaké mapování), aby procesy nemohly sahat jinam

> V procesech je to 1, 2, … a v OS random čísla

> 18.05.2021 - 12. Přednáška

**Přístup**

* Sekvenční (jen se posouvat dopředu a nebo rewind na začátek)
* Náhodný

**Typ** -- Rozpoznává se přes extension (přípona)

**Atributy** -- Název, timestampy, velikost, access práva, …

### Adresář

	Sada souborů 

Hlavně je to user-friendly a pomáhá to při hledání

V adresáři jsou atributy souborů

Nějaká hierarchie s kořenem

Operace (hledání, vypsání, … )

## File system

Datová struktura na úložišti

Musí umět

* Překládat jména souborů na binární reprezentaci -- rozkouskovává cestu a hledá pokračování v adresářích
* Pamatovat si lokaci dat souboru
* Management volných bloků (spoják, bitmapa)

Jsou **lokální** (FAT, NFTS, ext… ) a **síťové** file systémy (NFS, Samba, … )

Na disku můžu vyrobit různé partitions, klidně různých file systémů (to je v partition table)

#### FAT (File Allocation Table)

> Ještě z MS-DOSu, je celkem basic

Jedna struktura se stará o volné bloky a pozici souborů

Adresář je provozovaný jako speciální soubor \
V něm sekvence položek s fixní velikostí a atributy -- v každé položce je uložený první blok souboru (pak spoják)

Ten blok mi ukazuje do pole (to začíná od dvojky) a v tom poli je kam dál (0 znamená prázdno a -1 konec)

Na disku jsou tedy 

* Boot record -- ani nemusí být využitý
* FAT1 -- pevně danná velikost
* FAT2 (backup kopie)
* Root directory
* Data

Při hledání souboru musím lineárně projít celý adresář \
Špatně se ve spojáku skáče \
Jedna backup není úplně safe

#### ext2

> Původ Linux a taky celkem simple 

Založený na inodes (index nodes) -- reprezentují soubory

Opět adresář jako seznam fixních struktur -- je v tom jen název a odkaz na inode

* Boot record
* Skupina bloků 1
* Skupina bloků 2
* …
* Skupina bloků 3

V každé blockgrupě je

* Superblock (společný pro všechny) -- Kde co je a podobný věci
* Descriptor -- Jaká je to blockgrupa…
* Datová bitmapa -- Kde je volno v data blocích
* Inode bitmapa -- Kde je volno v inodech
* Inode table
	* V každe inode je info a odkazy na datové bloky
	* Nepřímé odkazy (prostý, dvojitý a trojitý) 
* Data block 

## Mechanika hard disků

Plotny na spindle a r/w hlavy na rameni \
Stopa (track) a sektory \
Blok -- stejný sektor na všech plotnách \
Cluster -- stejná dráha na všech plotnách

Pak se tam řeší výška hlavičky a rychlost rotace

> Dřív bylo uvnitř vakuum a teď helium

Největší bottleneck je mechanický pohyb hlavičky

## Disk scheduling algoritmus

Musíme nějak naplánovat zpracování žádostí k disku

> Dřív to dělal OS, teď disk

Doba na access = seek time (posuny hlavy) + čas na rotaci + čas na transfer (zanedbatelný)

* **First Come First Served** -- vznikají velké seeky
* **Shortest Seek Time First** -- jednou za čas velký seek, jediný problém je *vyhladovění* (žádost na kraji dlouho čeká)
* **Scan (výtah)** -- Beru nejkratší ale pouze jedním směrem (na kraji otočím)
	* CSCAN -- čte jen jeden směr a pak se jen vrátí na začátek
* LOOK (bez konců disku), CLOOK, FSCAN (dvě fronty), …

> 25.05.2021 - 13. Přednáška

## Virtuální paměť

**Virtuální adresový prostor (VAS)** \
&nbsp; ukazují do něj instrukce

**Fyzický adresový prostor (PAS)** \
&nbsp; ukazují do něj HW části \
&nbsp; Jednorozměrná sekvence očíslovaných bytů

Překládá se to hardwarově přes MMU (Memory managment unit) \
Je to zobrazení, které ale pro něco nemusí existovat (potom vyjímka)

Pomocí semgnetace nebo stránkování

### Proč?

* Hodí se větší adresový prostor (VAS může být větší než PAS) - ale to už dneska tolik nepotřebujeme
	* Přebytečnou virtuální paměť si totiž OS může oložit na disk
* Bezpečnost -- oddělím adresové prostory jednotlivých procesů

### Segmentace

#### Koncepty

* Virtuální adresový prostor je rozdělný na logické segmenty (stejné segmenty jako v linkování)
* Virtuální adresa je tvořená uspořádanou dvojcí číslo segmentu a offset
* Operační systém se pak stará o semgentační tabulku (pole indexované segmenty ve kterém je deskriptor) \
&nbsp; V deskriptoru je fyzická adresa, dělka a další atributy jako např. oprávnění, povolené instrukce, …

Kontroluje se chyba hledání neexistujícího indexu -- výpadek segmentu \
Když ho najdu, tak pořád musím kontrolovat oprávnění a maximální offset

Co když dojde prostor? - vyhození **celého segmentu** na disk a pak ho případně znovu načíst
 
* Spolu se špatným managmentem fyzické paměti je to hlavní důvod proč se dnes segmentace nepoužívá
 
### Stránkování

#### Koncepty

* VAS je rozdělený do stejně velkých částí (stránek) velikosti mocniny dvou
* PAS je opět rozdělených na stejně velké částí (rámce) se stejnou velikostí jako stránky
	* Celkem často se používají 4kB (na to je potřeba 12b)
* Někde bokem v paměti je pro každý proces stránkovací tabulka * Je indexovaná čísly stránek a každá položka obsahuje číslo rámce, atributy a příznak P
	* Page fault
* Jak vypadá virtuální adresa? Je to jedno číslo -- první bity jsou číslo stránky a zbytek bitů je offset
* Překlad díky tomu probíhá dost snadno 
	* Vezmu několik vyšších bitů VA, zjistím podle nich rámec, dám horní bity rámce před offset a to je hledaná fyzická adresa
	* Pokud mapování neexistuje, nastane page fault (výpadek stránky) 
* Výhoda oproti segmentaci je, že rámce nemusí být ve fyzické paměti souvisle za sebou a nemusím vyhazovat celý segment

#### Problémy

* Velikost - u 32-bit adresování je 2^20 (milion) 4kB rámců (20b na adresu rámce, 12b na offset)
	* Tím pádem bych potřeboval 4MB pro každý proces -- pokud každá entry potřebuje 1B
&nbsp;
* Rychlost

Paměť řeší víceúrovňová stránkovací tabulka
* Nepotřebujeme celý VAP
* PTAR ukazuje do první úrovně tabulky a z té se dozvím fyzickou adresu další úrovně 
* První úroveň je vždycky v paměti, ale ty ostatní můžou chybět
* Rychlost ale trpí ještě víc

Řešení rychlosti
* Zakešovat to
* TLB (Translation Lookaside Buffer)
	* Nemusím pak většinou prolézat celou tabulku (často používám byty u sebe)

> Fun fact N˚3: AMD zavedlo čtyřúrovňové adresování pro 64b a to ještě ne úplně xddd (jakože 48 bitů)

#### Algoritmus překladu adresy u stránkování

* Rozdělit adresu na offset a číslo stránky
* Zkontrolovat TLB, jestli nemá mapování
* Jinak projít celou stránkovací tabulku
	* Rozdelím číslo stránky na tolik částí kolik mám úrovní
	* Jdu do první úrovně, podívám se jestli je tam mapování pro další úroveň, jdu dál a takhle projdu všechny úrovně
	* Z poslední úrovně dostanu číslo rámce (to si dám do TLB)
* Aktualizuju příznaky A a D (Access a Dirty) ve stránkovací tabulkce a TLB
	* Jsou to dva bity, které říkají jestli jsem do toho přistoupil a zda jsem to změnil
* Dostanu fyzickou adresu slepením původního offsetu a rámce

#### Výpadek stránky - co to vlastně je?
 
* Handler musí zjistit kde ten problém se stránkováním nastal -- vím který proces teď běží
	* Třeba je to neoprávněný zápis, čtení ze systémové paměti, neexistující fyzická adresa…
* Systém se snaží zajistit, aby to mapování existovalo a prvně najde volný rámec
	* Upravím stránkovací tabulku a klid
	* Co když už ale není volná paměť? -- Musím najít oběť
	* K nalezení se používají algoritmy na výměnu stránek
	* Pak přijde na řadu bit A a D, protože musíme Dirty stránky uložit a oddělat stránky z TLB
	* Na volný frame po oběti načtu obsah a přenastavím stránkovací tabulku
* Vrátím to zpátky z handleru a znovu zkusím instrukci
 
> 01.06.2021 - 14. Přednáška

>  U toho jak to popisujeme se může stát, že 2B na rozhrání rámců způsobí 4 výpadky stránky (vytvořit tabulku, stránku a znovu)

#### Algoritmy na výměnu stránek

Použití v jakékoliv situaci, kde potřebujeme najít nějakou oběť a vyhodit ji při omezeném prostoru

##### Optimal page algorithm

Nahradím stránku, která bude nejdéle nepoužitá \
Je to jen teoreticky, protože to samozřejmně nedokážme říct a snažíme se k tomu přiblížit

##### Hodiny (Clock)

* Zoraginizuju si rámce do kruhu
* Ručička ukazuje na další rámec k nahrazení
* Pokud je A (Access) různý od nuly, tak A vynaluji a jdu dál
	* Když to ale je nula, tak to vyberu

##### NRU (Not Recently Used)

* Příznaky A se nulují pravidelně
* Rozdělím je do 4 tříd podle příznaků A a D (1 ← A:0 D:0; 2 ← A:0 D:1; ...)
* Vybírám pak od nejnižší třídy

##### LRU (Least Recently Used)

* Používám minulost pro předpovídání
* Jinými slovy vyberu to nejdéle nepoužitou stránku
* Implementuje se to HW
	* Cache, bit matrix
* Ale i SW
	* Nejjednoduší je zásobník, ale je to příliš neefektivní
	* Řeší se to aproximací -- **NFU**
	
##### NFU (Not Frequently Used)

* Každý rámec má svoje počítadlo
* Pravidelně nuluji A a když A==1, tak zvýšším počítadlo
* Vybere se rámec s nejnižším počítadlem
* Problém s vypadáváním nových stránek (dočasná ochrana na začátku) \
 a nevypadáním starých (snižování počítadel -- dělení 2)

#### Sdílená paměť

Propojení více procesů tak aby si viděly navzájem do adresových prostorů

Dělá se to tak, že se vyrobí sdílená paměť, připojí se na to procesy\
A potom se na různých místech namapují stránkovací tabulky, které ukazují na sdílené rámce

Stránkovací tabylky mají ve VA jinou adresu \
Nemůžeme používat ukazatele ve sdíleném adresovém prostoru, ale jenom offsety \
Hodí se na to dvoúrovňové stránkování se společnou tabulkou druhé úrovně

#### Paměťově-namapované soubory

Anonymní paměť se zapisuje do SWAPu, existuje ale druhý způsob

Stránky mapuji na obsah souboru

Když nastane výpadek stránky, tak se můžou použít data ze souboru

Problém s přidáváním dat (dostanu se za namapovaný stránky) a velikostí souboru

<br>
 
# Virtual machine

> Přetížený pojem, teď se budeme bavit o plné virtualizaci (ne VM procesu)

	V rámci OS umožníme vyrobit chráněné prostředí, které umožní spustit další OS 
	
	Je tam iluze, že že to běží na reálném HW

V případě problému ten problém vypadne a musí se o to postarat host (není to naštěstí příliš časté)

Výhody jsou

* Izolace (nelze se přes VM dostat ke zbytku počítače)
* Enkapsulace (mimo jiné VM snadno obnovím přes snapshoty)
* Kompatibilita (snadno se to přenáší na jiný HW)

## Kontejnery (Virtualizace na úrovni OS)

Hodně zjednodušená virtualizace - používá se reálný HW a ne virtualizovaný \
Sdílejí služby jádra, ale jsou to oddělené uživatelské prostory

Musí to umět kernel

> V prezentaci je pro představu jak to vypadá, virtualizační vrstva,…

<br> 

# Paralelní programování

**Paralelní počítání**

	Používá se více jader - instrukce jsou vykonávané současně

**Concurrent počítání**
	
	 Počítá se na jediném jádru (mutltiasking na jednom procesru)

Jaké má problémy používání více vláken současně?

### Race condition

Výsledek počítání závisí na naplánování vláken

Různě naplánované vlákna změní například pořadí prvků ve spojovém seznamu \
Ještě horší je ale provádění zároveň (co dřív v případě konfilktu zásahu do paměti)

**Příklad** \
Jeden sdílený spoják na dvou vláknech a každé chce vložit nový prvek \
Které vlákno ale proběhe první? -- bude to v náhodném pořadí \
Co když ale proběhnou zároveň? -- oba přidané prvky ukazují na následující a snažím se oba najednou do kořene…

#### Kritická sekce

Identifikuji kritickou sekci kódu, která může být vykonávána nejvýše jedním vláknem, aby nenastaly předchozí problémy

Omezení na jedno vlákno se nazývá mutal exclusion

## Synchronizace

Jak mutal exclusion udělat? (Zabránit rozbití integrity dat)

Buď se zamyká kritikcá sekce a nebo se procesy něčím řídí

Realizuje se pomocí **synchronizačních primitiv**

* Aktivní
	* Spotřebovávají čas procesoru (aktivní čekání)
* Pasivní (blokující)
	* V jádře OS je jednotka plánování zablokovaná do té doby než je přístup povolen
	
> Ty pasivní ale nejsou vždy výhodné, protože sys-calls na blokování jsou celkem drahé (desítky až stovky instrukcí)

Aktivní musí implementovat HW

* Atomické instrukce (Instrukce test-and-set nebo-li compare-and-swap)
	* Instrukce, která se provede celá bez přeršení (se zamklou pamětí) a buď se povede nebo nepovede
	* Vím adresu paměti o kterou "bojuji", starou hodnotu a novou hodnotu
	* Přečtu z paměti a porovnám s očekávanou starou hodnotu a podle toho to zapíšu

### Spin-lock

* Cyklus, který opakovaně zkouší atomickou intrukci do té doby než se povede
* Krátká latence (vhodné pro krátké čekání)

### Semafor

* Chráněné počítadlo a fronta procesů
* Je to blokující primitvum
* Atomické operace UP a DOWN uvnitř OS
	* DOWN (zamykání) -- pokud čítač není 0, tak se sníží, jinak jde do vlákno do fronty a zablokuju
	* UP (odemykání) -- pokud je počítadlo 0 a neprázdná fronta, tak vezmu z fronty a odblokuju to, jinak zvednu čítač

> Dám čítač na 1 a proces se začne provádět a sníží počítadlo, další přijde a zařadí se do fronty, až první odejde, tak jde další

### Mutex

Jenom LOCK a UNLOCK -- binární semafor

### Bariéra

Na bariéře se počká až se sejde určitý počet vláken

### V programovacích jazycích

**Monitor** -- v objektu je u instance zámek

Java má keyword `synchronized`

## Deadlock

Nekonečný kruh čekání

> Dvě vlákna, každé má zamklý jeden prostředek a obě potřebují oba prostředky aby to dokončily

### Coffmanovy podmínky

1. Prostředky mají ekluzivní režim (nejdou sdílet)
2. Vlákno něco drží a žádá o další
3. Nemůžu odebrat prostředky bez škody
4. Vznikne kruh v modelovacím grafu

## Alegorie klasických synchronizačních problémů

### Producer-consumer

Sklad s omezenou kapacitou, výrobci se zbožím a konzumenti

Problémy:

* Co když přijedou výrobce a konzument současně
* Co když se zaplní sklad zbytečným produktem
	* bloknu producenta
* Co když je sklad prázdný a přijede konzument
	* bloknu konzumenta

### Večeřící filozofové

N filozofů v kruhu a každý má po pravé straně vidličku, potřebuje ale na jídlo dvě vidličky

Jak realizovat synchronizaci tak, aby všichni filozofové někdy jedli?

Když naivně vezmu pravou vidličku a pak si čekám na levou, tak deadlock \
Zkusím ji teda zase rychle odložit a zkusím to znovu \
Pořád běží, ale nenají se -- starvation

<br>

---

<br>

> Zkouška bude jedna otázka

# Otázky u zkoušky z Discordu

1. ISA, co si pod tím představit, co musíme mít, Call-Execute-Return, Ortogonalita

2. Volací konvence, předávání parametrů funkcím, návratové hodnoty a pointery

3. Interrupty a jejich obsluha

4. Disk scheduling algoritmy a jejich význam + něco o access time obecně (FFS, SCAN, … )

5. Segmentace

6. Stránkování a algoritmy na výměnu stránek, VAS a PAS, TLB, vztah stránek a rámců, víceúrovňové stránkování, stránkovací tabulka, jak se rozřeže VA

7. Synchronizace, co je problém (race condition/critical section), mutal exclusion, atommické instrukce, primitiva aktivní/pasivní, jak funguje spinlock, TAS, semafor

8. Deadlock, příběh s filozofy a skladištěm
