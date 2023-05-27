> 05.10.2021

# Úvod

Opakování basic konceptů - CIL, CLR, JIT compiler

C# JITuje po metodách

Někdy můžeme metodu zavolat na prázdno

S CILem jsou i metadata

ildasm.exe v vs cmd na dekompilaci
ILSpy přímo ukáže původní zdroják z exe - obluscator na schování metadat

> 12.10.2021

# Import knihoven

Můžeme buď přidat refernci na projekt nebo přidat přímo dllko (ve výsledku to samé)

Ukázka toho, že když dll smažeme, ale funkci potřebujeme ve funkci, tak na to přijde až JIT

CLR a BCL (Base class library) je .NET

> .NET verze...

native x managed - kód ve spustitelném souboru

Jak se to spustí, když v exe nebo dll není přímo zdrojový kód

Buď pomocí importu ze kterého to nevyskočí a nebo to zavolá CLR

> 19.10.2021  

### Features

C# 9 - top level statements

C# 10 - global usings, implicit usings

používání `var` a kdy použít interface

### Strings in C#

System.String je to samé keyword pro string... kvůli tomu aby jiná class se mohla jmenovat String

Analogicky pro char

Stringy jsou immutable

> příklad s porovnáváním konkatenace přes `--`, `Equals` a porvnání referencí

string intern

Stringbuilder se snadným přidáváním stringů

> 26.10.2021

> 02.11.2021

### Konstruktor 

`.ctor`

Loader heap - kusy kódu, metadata, ...

GC heap

Prvně se v GC heapu naalokuje prostor (vynuluje se) a pak až konstruktor

Konstruktor předka se volá mezi inicializací a tělem konstruktoru

Statické metody se spustí konstruktor těsně před callem

### Životnost proměných

## ...

Operátor `nameof()` -- Z názvu proměnné udělá řetězec

# Vyjímky

V C# jen potomci SystemException \
CIL to ale nechcekuje

> 9.11.2021 Nebyla

> 16.11.2021

Pokračování exceptions

> 23.11.2021

Properties, ...

Initi only setter

> 30.11.2021

Refernce a hodnota

> 7.12.2021

## Hodnotové proměnné

`nullable` value types - struktura `Nullable<T>` s boolem, jestli má hodnotu a hodnotou

Má předefinované operace, takže se šíří - zároveň i jakási ternární logika

## Referenční proměnné

Ref na haldu - na celé objekty

Kompatibilní s nullem - `nullable ref types` - feature, která **vypne** nullovatelné reference

`a??b` ... a dá se i `...?[...]?...() ?? : dobule.NaN`

## Ukazatel (pointer)

stack, heap, static, ... - žádné omezení, žádný garbage collector a nejde s tím pracovat bezpečně

## Tracking reference

Musí to ukazovat na relativně save věci - musí to být na elementární prvek, nesmí to být do kódu, ...

Pořád to má omezení, že s tím nejde pracovat jako s číslem 

# Reference v metodách

## `out` a `ref`

`out` je v podstatě `ref` bez inicializace a do `out` se vždycky zapíše

## Metody try

 Bez vyhazování vyjímek, např. `int.TryParse(..., out ...)`



Z indexeru dostaun kopii hodnoty - je lepší struktury dělat imutable

>14.12.2021

# Dědičnost

`(a as B)?.m()`





























