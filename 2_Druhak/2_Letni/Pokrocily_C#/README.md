# Pokročilý C#

> 1. Přednáška

## Požadavky...

## Extension metody

`Fraction.ToFtraction(d)`, kde `d` je double se nám nelíbí, jak to opravit? Můžeme si vytvořit konstruktor nebo rozšířeného potomka... meh

Statická extension metoda - ToFraction(this double d) {...}

> 2. Přednáška

## Method overloading

## Generická metoda

Překlad JITem až za runtime

Pořadí metod

> 3. Přednáška

### Omezení typů v generice - Constraits

### Generické extension metody

### Generické typy

### Dědičnost

> 4. Přednáška

Constrait je sice lepší při rozšiřování programu, ale za to jsou věci, které nejdou (komplexní čísla - jen s reflection)

Kdybychom chtěli trii, tak při popisu dictionary do dalšího levelu, tak můžu udělat **rekurzivní definici** nodes
Problém je, že se nedědí konstruktory

### Explicitní implementace

Dva interface se společnou metodou - příklad na reader a writer
Když chci použít metodu jen pro jeden interface (např. zavřít psací část), dá se použít explicitní implementace

Musí ale být jasné, který se má zavolat (pokud by obě byly explicitně implementované)

Další problém by mohl nastat pokud by interfaces chtěli pro metodu jiný nárvratový typ - opět explicitně

IConvertable a volání jeho metod jen pokud se na to díváme pod tímhle interface

### Generika... covariance, contravarinace, invariance

Převoditelnost - například pole stringů lze převést na pole objektů
`in` a `out` keywords

> 5. Přednáška

### Vyjímky u variance

### Variance funguje jen u referenčních typů

### Diamantová dědičnost

### Tabulka virtuálních metod vs interfacová TVM

Volání z interface je pomalé

Pokud je něco generické podle interface, je to velký rozdíl

### Abstract x Interface

Struktura array segement, (bonus je span)

# 6. Přednáška

*Motivace - potřebujeme předat funkci na výběr range*

## Delegát

Obdobné ukazateli na funkci z C++

Silně typovaný

`.Invoke()`, `.Combine()`, `InvocationList()`, `Remove()`  - existují ale pro ně syntaktické zkratky

### Generický delegát

### Standardní delegáti

`Action, Func, Predicate...`

### Pomocné metody

`TrueForAll(), FindIndex(), RemoveAll(), EraseAll(), ...`

### Anonymní metoda a lambda funkce

# 7. Přednáška

## Lambda funkce

Volná proměnná a následná variable capture

### Rychlý úvod do C++ a lambda funkcí tam

#### Capture by value

Pokud potřebujeme ukládat v průběhu nějakou proměnnou, tak se používá trik s třídou Scope, která má v sobě tu lambdu a pak value

#### Capture by reference

Lepší, ale problém s životností reference

Kdy co použít?

### Jak to funguje v C#

Prodloužení životnosti capture by refernce

Lazy enumeration

Scope a životnost... nepříjemný overhead

# 8. Přednáška

https://www.youtube.com/watch?v=B_TBkxpN7Mk

https://www.youtube.com/watch?v=NiWnxpDBBYM

### Raw string

## Namespaces

`namespace A.B` je to samé jako `namespace A { namespace B { ... }}`

Obvykle hledání v aktuálním jménem prostoru, jinak skok o jeden výše
Hledání od kořene pomocí `global::`

Můžeme explicitně pojmenovat "namespace stromek" jedné assembly - `extern alias`
Hodí se například při používání OpenGL a DIrectX zároveň

### Nested types

* v CLR to je `X.A+B`
* Připodobnění k friend class

Soukromý kontrakt...

## Kolekce

`IEnumerable<T>`...
`IEnumerator<T>`...

Prázdný enumerátor, úprava při procházení, ...

# 9. Přednáška

https://www.youtube.com/watch?v=oBzEvWgjb58&feature=youtu.be

Enumerace na dvou kolekcích...

`yield return ` - uchovává stav algoritmu
Ten se chová na konci špatně - vrací `default` místo `invalidOperationException`

*Příklad se stavovým automatem*

`Range` - indexy odkud kam...

Chyba při implementaci enumerátorů - kontrola se hodí hned při inicializaci

Lazy Enumerace...

# 10. Přednáška

https://youtu.be/7ed7U2BNr-c
https://youtu.be/Xi0vzQ_RH08
https://youtu.be/yZypNOymFqQ
https://youtu.be/htVR_XaGzbI

## Anonymní třídy

Například `new T{x = 5}`...
Při deklaraci je potřeba napsat `var`

C# se dívá na již vygenerované anonymní třídy a kontroluje parametry ve stejném pořadí

### Tuples

Silně typovaná n-tice

Je to třída a tedy to má nepříjemný overhead
Od C# 7 ale máme `ValueTuple` , který je struct

Dekonstrukce... a podtržítko, když mě něco nezajímá (pozor pokud to někdy je pojmenování)
Decontructor - možnost implicitně nadefinovat

Mohu pracovat i s `item1, item2...`

## LINQ

Nějaká klíčová slova, která tvoří dotaz obdobný databázi

Query expression se pak převede...

Lazy evaluace, rozdíl při změně pořadí...

# 11. Přednáška

https://youtu.be/y9TmL-8qC_A

## Paralelismus

> Koncept vlákna, scheduler, ...

Abychom simulovali současný běh, tak nemusíme mít více vláken - stačí `yield`

`Thread` a statická `CurrentThread`

> Vysvětlení Thread Local Storage (TLS)

`new Thread(...)` - vyrobení nového vlákna, argument je delegát
`t.Start()` - se následně spustí (mezi vyrobením a spuštěním můžu nastavit například prioritu)

**Stavy vláken** - unstarted, running (neznamená že fakt běží), ended

* `t.IsAlive()` nám řekne, jestli běží
* `t.Abort()` ho zabije - dá se to ale chytnout jako každá jiná vyjímka

Předání argumentů do `t.Start(object o)`, ale jenom pouze jeden
Lepší je ale když to vlákno při vytváření dostane instanční delegát (`j.Run()`)

Cyklus s kontrolou `IsAlive()` - **aktivní čekání**
`thread.Yield` - vzdáme se vlákna v OS a tedy semiaktivní čekání
`thread.Sleep(<ms to wait>)` - o trochu lepší **semiaktivní **čekání (není přesné)

Metoda `Join()`

**Thread Safety** - ne vždy můžeme používat datové struktury s vlákny

# 12. Přednáška

Problémy se **statickým konstruktorem** - pozor na vznik **deadlocku**

### Lock a mutex

Když pracujeme se **sdílenými daty**, očekáváme konzistenci - využijeme mutal exclusion

Zapíše se pomocí `lock(zámek) { ... }` - pasivní čekání než se zámek odemkne

Ke každé instanci je připojený zámek - slouží k tomu `sys block`

**Lock-free algoritmy** - nepotřebují zámek, ale stále jsou blokující (více na přednášce pokročilé pokročilé přednášce)
**Wait-free algoritmy** - Garantován maximální čas čekání

Thread-safe `Console` - zamyká se buffer
Příklad - pokud je kritická sekce velice krátká, tak se chování paralelismu hodně změní

Statická třída si může alokovat nový prázdný objekt a z toho udělat zámek

Lock používá `Monitor.Enter(x) ...`
Pozor, že po zámku monitoru musí být `try { ... }` a `finally { Monitor.Exit(x) }`

Co když zamykám dva objekty? - možný **deadlock**, musíme zamykat v konzistentním pořadí

Dá se využít `Monitor.TryEnter(x)` - ta nezamyká, ale může vzniknout **livelock**

`SysBlock` je lock a **conditional variable** (`Wait(), Pulse(), PulseAll()`)... podobné jak C++

Je lepší program řešit rovnou pro více vláken než dvě a tedy pozor na race condition, když se podmínka rozbije v průběhu
Přiklad **producent, fronta, konzument** - producent vzbudí a konzument spotřebuje obě dřív než může konzumovat druhý probuzený

Pro konec konzumenta není vůbec dobrý `abort()` - používá se otrávená pilulka
Je dobrý chytat aborty pro převod do konzistentního stavu

Kromě monitoru jsou i jiné způsoby - `...Slim` třidy

`WaitHandle` - jsou v OS a tedy velice pomalé (jejich výhoda je že jsou sdílené mezi procesy)

* `Mutex` - zámek ale bez objektu
* `Semaphore` - zobecnění mutexu
* `ResetEvent` - auto je podobná cv

WaitHandle umí `WaitAny` - ... , `WaitAll()` - zamkne všechny nebo žádný

# 13. Přednáška

### Threading model - Winforms

Jak neblokovat zpracováváním událostí interakci s UI? - Vytváření nových vláken...
Jak pracovat z jiných vláken s UI prvky? - Threading model... Dá se to přes volání `Invoke()`

Mám k dispozici i `InvokeRequired()`, prioritní...

Obecně `Post()` - asynchronní, `Send()` - synchronní

`[ThreadStatic]` - pozor počáteční hodnota jen v hlavním vláknu, `ThreadLocal<int>` je v tomhle praktičtější

---

\* cast 2 - ThreadPool, Task:
https://youtu.be/wwCAxRRJwTk
https://youtu.be/t2Ul4EtnsBQ

\* cast 3 - Task.Wait(), planovani Tasku do vlaken - TaskScheduler, stav
Tasku vs. stav vlakna Thread vs. stav vlakna v OS,
TaskScheduler.FromSynchronizationContext, Task<T> jako koncept "future",
task continuations pomoci .ContinueWith(), TaskCompletionSource jako koncept
"promise":
https://youtu.be/Pk3-0-tr_ds
https://youtu.be/dmqQAt86hy0
https://youtu.be/FkarLl-Tbsk

---

### Zadání Aho-Croasick

Variace na producent, konzument - kontrolovat maximální délku

Winforms - timer, listbox, ...

Prohledat systém a najít soubory s podmínkou

`System.IO` - `Directory` a `File`, resp. `DirectoryInfo` a `FileInfo`

Crawleři budou přidávat soubory na prohledání do fronty s maximální délkou
Z té si to budou brát searcheři - pokud tam nic není, tak pasivní čekání

Zakázané `System.Collections.Concurrent` a `System.Threading.Task` a `ThreadingPool` a `WaitHandler`

Dole zobrazená statistika - soubory (splňující, všechny, chybné), množství dat a čas

Prohledat soubory jako bytes ve všech encoding - `Encoding default` - `GetBytes`
