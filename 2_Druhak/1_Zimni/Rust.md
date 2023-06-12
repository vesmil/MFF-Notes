# Úvod

* `cargo new example`
* `cargo run`

! - macro (println, vec)

tool cargo-watch

Everything is imutable by default \
you can mark for modification by `mut`

Move by default \
you can't use data structe after it was given to a function

You have to specify if borrow by reference (`&`) is mutable or not `&mut`

&str and Strings ared differnt - have to use .to_string()

Return looks like 
```
fn hello() -> String {
	let text = "...".to_string();
	text // or return text;	
}
```

For web we will need hyper and tokio 

Quite complicated request, response

> 25.10.2021

# Types

Function to check the type:
```
fn type_of<T>(_: &T) -> String {
	std::any::type_name::<T>().to_string()
}
```

```
let a = b"Text"  # &[u8;4]
let b = "Text"   # &str
```

`.to_string()` creates `string` \
To get `&str` we have to ref it (`&`)

We have to use `println!("{}",s)` which is a macro and it's resolved at runtime

> TODO diff macro vs func

For example array doesn't have `display` so can't print it \
but... you can display for debug "{:?}"

You can't add to an array, so you have to use vector

```
let mut array = vec![1,2,3]
array.push(4)
````

Mutable borrow is not allowed when borrowing elswhere

```
use std::io::{self, BufRead, Write}

fn input(prompt: &str) -> String {
	print!("{}", prompt);
	io::stdout.flush().unwrap();
	
	io::stdin.lock()stdin.lines().next().unwrap().unwrap()
}
```

> 08.11.2021

> 22.11.2021

# Builders a optional property

```
struct City {
	name: String,
	population: Option<i32>
}
```

Můžu to pak nastavit na `Some(...)` nebo None

Můžu věcit schovat do `mod`ulu a pak specifikuji use::modul_name; \
Musím ale dát všechny věci `pub`lic

Můžu naše optional property vyřešit pěkněji přes konstruktor

```
imp City {
	pub fn new(name: String) -> City {
		City {
			...
		}
	}
}
```

Pokud vrátím referenci na název a zničím objekt, tak nemůžu moji referenci na název použít

To můžu ještě vylepšit takzvaným builder patternem

Je to něco ve smyslu Builder::new(...).set_param(...)...build();

# Vlastnictví objektů

Předám-li objekty do property něčeho jiného, tak to nemůžu použít dále

Musím tedy použít reference, ale u referencí je potřeba introducnout lifetime

Standardně se to dělá pomocí `&'a City`... jenomže ten lifetime musíme vytvořit, např. `impl Path<'_> a struct<'_>...`

> 6.12.2021

# Polymorfismus

můžeme buď přes enumeration (něco jako union v céčku) nebo traits

Uděláme si trait a potom uvnitř něj implementujeme funkce pro jednoltivé objekty

Stejně to ale nemůžeme dát do vectoru, ten musí být homogení

Můžeme si ale vytvořit `&dyn` odkazy na ty objekty a ty už jdou, ale i `Box<dyn Shape>`  můžu dát do vectoru

