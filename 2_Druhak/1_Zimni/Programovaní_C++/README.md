# Úvod

Historie C++ a stuff kolem toho viz. prezentace

# Kompilace

V C/C++ je to jinak než v ostatních moderních jazycích \
Je to založené na textovém `include`

Dnes už ale není pouze textový

Funguje to tak, že v .cpp je implementace a .hpp je interface \
Dříve se změny nedělali v hlavičkových souborech tak často a změna v implemetnaci se nemusela rekompilovat

Generický kód je stejně rychlý jako pro jeden typ, protože při kompilaci se vyrábí nové tělo

Proces kompilace:

z .hpp a .cpp se přes cc++ vyrobí objects, ty pospojuje linker (spolu s knihovnami) do executable. Z té to pak vezme loader.

Sice v .o už je binary, ale to nejnáročnější se dnes odkládá do linkeru

# Kód

## Moduly

Potřeba header file

`#ifndef` před `#define`

C++20 má moduly jinak 

* nemá standardní koncovku (Microsoft specific je  ixx)
* místo `include` je `import` a místo `define` je `export`
* standard ale není zatím ready na to to použít

Proč? Importovat se ta knihovna bude už v binárce

## Header x source

**Header (.hpp)**

Definice typů, classes, konstant

**Sourc (.cpp)**

Definice non-inline funkcí a statických proměnných

---

Type definiion pomocí `using` -- dá se pojmenovat typ

Předávání odkazem x hodnotou ... -- zajímavost, že komplexní čísla jsou vlastně rychlejší hodnotou

Definice lokální variable je trochu divná - konstruktor v závorkách \
operátor `new` vrací odkaz - ale nepoužívat, špatná dealokace (`delete`)

Není garbage collector, ale místo toho se dá používat shared pointer, respektive rychlejší unique pointer

> 26.10.2021

Pokračování objekt vs reference vs pointer

Reference, ukazatele, chytré ukazatele, iterátory

(Const) L-value, R-value

> 02.11.2021

### Argumenty funkcí:

* levné kopírování . hodnotu
* potřeba měnit - modifikovatelná reference
* pokud nelze kopírovat - R value
* jinak const referenci

### Návratové hodnoty funkci

Pokud nechceme dát přístup do datové struktury (viz operátor []) tak skoro vždy vracíme hodnotou -- reference po skončení funkce může zaniknout

> 9.11.2021

Copy-ellision

> 16.11.2021  

Rule of five

Pokud potřebujeme destruktor, tak dost možná potřebujeme i další 4 metody

...

Spíš se tomu ale vyhýbat

Možné případy

> 23.11.2021

TODO

> 30.11.2021

TODO

> 7.12.2021

# Algoritmy

Sada generických funkcí pro práci s kontejnery

TODO

> 14.12.2021

# Funktory

> 21.12.2021

# Namespaces a classes































