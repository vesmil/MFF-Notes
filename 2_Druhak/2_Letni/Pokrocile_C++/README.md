# C++

[Web](https://www.ksi.mff.cuni.cz/teaching/nprg051-web/), [Záznamy](https://web.microsoftstream.com/channel/5462777b-8c94-42a7-990e-6339eab25ac8)

> 1. Přednáška

## Šablony

Co může být v šabloně? - Typ, int, list intů, jiná šablona (a pointer) 
Co může být šablonou? - Třídy, funkce, typy, proměnné

Instanciace šablon - explicitně specifikováno, deduction guides, ...
Implicitně, explicitně, mixed

> 2. Přednáška

### Validita šablon

### Koncepty

### Variadické šablony

> 3. Přednáška

### Perfect forwarding

### References and values

> 4. Přednáška

> 5. Přednáška

> 6. Přednáška

### Deduction

`auto`

`decltype`

### Initializers

`initializer_list`

> 7. Přednáška

## Type system

> 8. Přednáška

> 9. Přednáška

## Paralelní programování

### Race condition

**Simple demo** se spojáky... už bylo na systémech

### Co máme k dispozici?

*C++ 11* - atomické instrukce, low-level vlákna, futures, synchronizační primitiva, paměť pro konkrétní vlákno, ...
*C++ 14* - sdílený timed mutex
*C++ 17* - paralelní algoritmy a shared mutex
*C++ 20* - stop tokeny, semafor, coordination typy

### Thread

Přímo v konstruktoru vytváření vlákna (fork), `join()` pro připojení zpátky, destruktor kontroluje `joinable()`

`detach()` - po odpojení nelze zavolat `join()`
statická funkce `hardware_concurrency()` nám řekne kolik máme procesorů

### Jthread

Podobné, ale má stop token

### Co dát do threadu?

Rozdíl pro - Copy, move, const reference, reference (monitor)

### Futures

`std::future<T>`

`std::shared_future<T>`

`std::async` - dá se tomu funkce a až bude potřeba výsledek tak se zavolá `get()`
`std::packaged_task<T>` - musím `get_future()`, spustit vlákno a pak až `get()`
`std::promise<T>` - nejnižší level, ...

#### Exceptions

`___.set_exception(std::make_exception_ptr(...))` - vyvolá se až při `get()`

> 10. Přednáška

...

> 11. Přednáška

### Semafor

...

### Coordination types

* **Latches** - Blokuje vlákna do očekávaného počtu, je jen na single use
* **Barriers** - Obdobný, ale po propuštění vláken se resetuje

### Stop tokens

Asynchronní requesty na ukočení exekuce

### Thread-local storage

...

### Paralelní algoritmy

Execution policy - seq, par, par_unseq, unseq
`for_each`, `reduce`, `scan`, `...`

> Občas paralelní algoritmy nedosahovaly dobrých výsledků... takže stejně se to udělá sekvenčně

### Executors

...C++ 23

### Concurrency

Řetězení událostí

### Transakční paměť

Pokus od Intelu, nyní se pracuje na verzi 2

## Pokročilé paralelní

### Memory models



