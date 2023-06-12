> 2. Přednáška - 06.10.2021

## Barevné vidění

> Principy lidského zrakového systému a barevného vidění.

> Jak barvy vnímá člověk? Příklad vady barevného vidění.

> Příklady několik zásad, kterých bychom se měli držet při navrhování barevných schemat.

Spektrum viditelného světla je **400 - 700 nm**
Prostor všech spekter má nekonečnou dimenzi - my vnímáme 3 a tedy nedokážeme rozeznat vše (metamery)

Grassman - **odstín** (dominantní vlnová délka), **saturace** (čistota barvy), **jas** (intenzita)

Aditivní skládání barev - prostor barev je lineární

Lidské oko má **čípky **(vnímání barev) a **tyčinky **(citlivější na světlo)

Čípky S,M,L s různou citlivostí na barvu
Barvoslepost kvůli podobnosti čípků M a L

Na sítnici se informace již předzpracovává (třeba z modré se vezme jenom rozdíl)

Disperze světla - jinak se zaostřují různé barvy podle jasové složky (barevná aberace)
Zrcadlovky to řeší různám materiálem

Integrační schopnost sítnice - rozmazávání složek

Dokážeme lépe rozeznávat vertikální a horizontální čáry než šikmé

Setrvačnost, očekávání, vliv okolí...

Doporučené zásady jsou používat barvy střízlivě, nekreslit modrou tenké a malé objekty, nemít červené nebo zelené pozadí, nekreslit vedle sebe syté vzdálené, ...

> 3. Přednáška - 13.10.2021

## Vektor a rastr

> Základní rozdíly mezi rastrovou a vektorovou grafikou?

> Které operace s obrázkem nejdou dobře dělat v rastrovém prostředí, ale jsou bez problémů ve vektorové grafice?

Při vytváření obrazu hledáme zobrazení z reálného světa do světa barev 
Diskretizace obrazu - pixely a jejich hodnoty

Vektor vs rastr... otáčení a zmenšování rastru ho rozbije

Formáty pixelů, formát SVG, ...

Vektorový výstup prakticky není a překládá se

## Barevné systémy

> Jak se barvy reprezentují na počítači?

> Které barevné systémy se hodí pro zadávání laickým uživatelem a které se hodí pro barevný tisk?

> Jak se kombinují barvy na monitoru a jak na papíře?

Proběhl experiment jak namíchat všechny barvy - pomocí **RGB** ale musíme mít zápor
Následně definice barev X,Y,Z jejichž kombinací (nezáporně) se vytvoří libovolná barva
Y je přibližně jas, ... RGB a **XYZ **se mezi sebou dají lineárně převádět

Dá se to znormalizovat a zakreslit ve 2D pomocí x,y (zafixuje se jas)
Vznikne "podkova" - spektrum námi videtlných barev

**Doplňkové** barvy jsou ty, které se složí na bílou (jsou i přísnější definice)
**Syté barvy** jsou barvy na obvod podkovy (resp. barvy ve spektru)

Bílá - Izoenergetická s třetinami, NTSC, planck podle teplotu

Subtraktivní a aditivní skládání barev (vydávání vs pohlcování světla)
Převádění mezi RGB a **CMY(K)**: $C = 1 - R,\ M = 1 - G,\ Y = 1 - B$

Barevný systém **YIQ** - při barevném vysílání v TV, kvůli kompatibilitě

**HSV**... - vhodný pro uživatele (z RGB se sytost počítá přes maximum a minimum...)

Další jsou LS, TekHVC, PANTONE, Munsellův, ...

> 4. Přednáška - 20.10.2021

## [Gamma](https://cgg.mff.cuni.cz/~pepca/lectures/pdf/icg-05-gamma.pdf)

> Nelinearita zobrazovacího zařízení (CRT monitoru)

> Co je gamma-korekce a na co by se mohla užitečně použít?

Lidské oko vnímá relativně (vnímáme rozdíl cca. 1%)
CRT zároveň vyzařovali nelineárně s hodnotou napětí a $I = K(V + \epsilon)^\gamma$

Je to přibližně inverzní

Gamma korekce se prováději pro to aby se rozsah pixelu efektivně využil a pro zobrazení na jiných zařízeních - fuckup se skrytým konverzními funkcemi

## Formáty souborů

> Který grafický formát (druh komprese, rozlišení) byste použili pro běžné úkoly: archivace digitálních fotografií, posílání fotek z dovolené babičce emailem, podklady pro tisk časopisu posílané do redakce, ..

Digitální fotoaprát - Bayerova maska (na hranách), zpracování RAW, ...

Formáty pixelu - paleta, černobílá, true-color, HI-color

Rastrové (BMP, PNG, GIF, TIFF, ...) a vektorové formáty (CDR, SVG, AI)

Bezeztrátová komprese (RLE, LZ) a ztrátová (JPEG)
Rozklad prokládaný nebo progresivní

**PBM/PGM/PPM** - basic rastrový formát bez komprese, různé formáty pixelu
**Targa** - původně HW, několik formátů (paleta, RGB, RGBα), komprese (bez, RLE, ...)
**GIF** - paleta, animace, LZW komprese (hodně dobrá, ale patentovaná), 4 fázové
**PNG** - true-color, spojitá průhlednost, deflate komprese, 7 fázové prokládaní
**JPEG** - správně je to jen (nastavitelná) komprese... nevhodná pro písmo, ...

**SVG** - ...

> 5. Přednáška - 27.10.2021

## HDR (velký dynamický rozsah)

> K čemu se používá HDR grafika? Čím je lepší než běžná (LDR) grafika?

> Popište postup, jak obyčejným digitálním fotoaparátem pořídit HDR obrázek. Které scény by na to byly vhodné a které ne?

> Čím se interně liší HDR rastrový obrázek od normálního (třeba GIF, JPEG)?

V závislosti na expozici světlá nebo tmavá místa

Pixely jsou floating point a pořídí se více fotografií s různou expozicí
Musí se převést do normální škály (tone mapping)

Formát souboru **.hdr** nám umožní efektivnější uložení (4B na pixel) (dále např .exr)

Křivka citlivosti senzoru...

## Kompozice

> Jak se implementuje poloprůhlednost v rastrovém obrázku? Co se tam přidává?

> Jaký výpočet byste použili při kombinaci dvou poloprůhledných pixelů metodou "A over B" (obrázek A je před obrázkem B)


Pro průjhlednost přidáme $\alpha$ kanál, často přenásobíme alfou ostatní kanály

Operace skládání dvou pixelů: žádný, jenom jeden, přes, uvnitř, mimo, na povrchu, xor
Podle toho je pro A i B nějaká konstanta F, tou se to vynásobí a pak se to sečte

Jsou i operace darken, fade, opaque

Operátor přičetní jde jen v případě disjunktních ploch

> 6. Přednáška - 03.11.2021

## Filtrace

> Jakou metodou byste rozmazali rastrový obrázek? (navrhněte metodu/vzorec, klidně vaši vlastní)

Ekvalizace histogramu - snaha mít vyrovnaný histogram
Kumulovaný histogram - hodnota pro je $x$ je všechno meněí včetně $x$ (neklesající křivka) - při ekvalizaci kumolovaný histogram přímka

Po převodu do HSV se dobře pracuje s sytostí a odstínem

**Matematická definice obrazu** je zobrazení z $R^2$ do $R^n$ - vektor hodnot pro jednotlivé pixely

Konvoluce a diskrétní konvoluce - definice skládání funkcí (souvislost s Fourierovou transformací)

Představa pokládání matice na pixely:
Gauss rozmazání (v podstatě vážený průměr), Detekce hran, Sobel, Laplacián, Zaostření, Emboss, Neuniformní...

**Nelineární** - medián (na potlačení šumu), minimum (eroze - ztmavení na nejtmavšího souseda) a maximum (dilitace)

Potlačování šumu - gauss a medián už známe, neizotropické filtrování (vrstevnice), rotující maska (malý rozptyl)

## Kreslení čar

> Popište princip tzv."midpoint" (Bresenhamových) algoritmů na kreslení čar (doporučený příklad: úsečka nebo kružnice se středem v počátku)

DDA algoritmus - parametrické vyjádření, spočítá směrnici a zjišťuje hranice

Bresenhamův algoritmus - vyhne se celým číslům tak, že porovnává přelezení poloviny...

Algoritmy s více kroky najednou...

Stejně se to použije u kriužnice, tam to stačí spočítat pro osminu a dělá se to bez odmocnění

> 7. Přednáška - 10.11.2021

## Vyplňování mnohouhelníka

> V tzv. "scanline" algoritmu na vyplňování n-úhelníka v rovině se používá záznam popisující hranu mnohoúhelníka. Které datové položky obsahuje?

> Co je anti-aliasing? Uveďte na jakých principech může být založen (jen princip, nemusíte psát detaily).

Pravidla - buď všechny vnitřní body a nebo jen liché plochy zvenku

Když vykreslujeme liché, tak seřadíme hrany a kreslíme úseky na přeskáčku - zametání roviny
Když vybarvujeme všechno, tak předpracujeme hrany a máme čítač, jestli jsme museli točit a podle něj vybarvujeme

Šrafování je otočení a pak každý k-tý řádek

## Antialiasing

Kreslí se všechny do kterých se zasahuje a akorát se počítá intenzita

Převzorkování - nakreslí se ve vyšším rozlišení a potom se to sníží

## Písmo

Je vektorové a rastrové (správně bit mapa pro každou velikost)

Škálování vektoru je neprofesionální, ale snadné, škálování rastru je hnus

Fontcache, subpixelové posunutí, ...

Distance field - akcelerována na GPU, kódování vzdálenosti do textury, ...

Clear type používá LCD monitor pro subpixelové posuny

## Kódování rastru

Úsporné uložení rastru nebo bitové masky

**RLE** - koherence ve vodorovném směru

> Popište princip datové struktury "Kvadrantový strom" (quad-tree)

**Kvadrantový strom** - Rekurzivně dělím obraz na čtvrtiny a kontroluji jednobarevnost

Přímočaře je to pomalé (některé hodnoty se čtou několikanásobně)
Strom se tedy buduje od spodu

Můžeme tak snadno dělat množinové operace s bit maskou (průnik a kontrola podstromu) 

Implementační detaily - rozšíření nemocniny dvojky, společné podvětve, ukládání bitmapy, pokud je to nevýhodné
Obdobně jako Huffman se to dá uložit lineárně (sourozenecká vlastnost)

**Řádkový seznam změn(X-transition)** - pokud mám jen bity, tak mi stačí si pamatovat, kdy došlo ke změně

**TODO **- zobrazování mochrome nebo zobrazení barev jako optional

## 3D

> 8. Přednáška - 24.11.2021

## Grafický systém a transformace

**GPU** - Reprezentace, překlad na trojúhelníky, ořeže se to, normalizuje, rozloží na fragmenty (pixely), stínování, ...

 ...historický pohled na GPU a ukázka her

> Proč se používají homogenní transformační matice? (3x3 ve 2D, 4x4 ve 3D)

> Napište matici otočení kolem osy Z o úhel α (jde o 3D transformaci)

> Jak byste postupovali při odvozování otočení kolem libovolné osy o daný úhel ve 3D? (stačí 
> naznačit postup, není třeba to přesně odvodit)

> Co je transformace tuhého tělesa (Rigid Body Transform) a čím byste ji charakterizovali? Lze to 
> nějak poznat na homogenní matici 4x4?

Elementární transformace - posunutí (nejde násobení maticí - není homomorfismus), otočení, zvětšení, zkosení...

Homogenní souřadnice (řešení hledání přímky pro dva body a hledání bodů pro dvě přímky...) přidáme si dimenzi
Představíme si, že přidáme jakoby body protínání v nekonečnu - vektory budou mít třetí služku nulu a body nenulu
Najednou půjde i posunutí maticí

Skládání transformací pro rychlost na více bodech

Souřadné systémy (od spodu, shora) a pravotočivý/levotočivý

Přenos polopřímky do osy z - přeneseme do počátku, otočíme kolem z, otočíme kolem x, dvě inverze
Díky tomu můžeme otočit kolem libovolné osy, zrcadlit 

Inverzní matice - invertovat, udělat opačné kroky a nebo transpozice pro ortonormální (rotační)

Převod mezi souřadnými systémy - Přeneseme polopřímku do osy a pak otočíme ať se shoduje x,y
Respektive můžu provést translaci a potom to přepsat do řádků

> 9. Přednáška - 01.12.2021

## Projekce

> Jaká je běžná posloupnost transformací prováděných v systému, který zobrazuje 3D scénu na obrazovce? (uvažujte jako základní prvky scény "vrcholy")

> Jaká je nejpřirozenější projekce (ze 3D do 2D) a čím byste ji definovali?

> Navrhněte, kterými údaji byste popsali "perspektivní kameru"

Dva systémy - **rovnoběžné **paprsky nebo **ze středu** projekce

Rovnoběžné se dělí na kolmé a kosúhlé

Kolmé - Mongeova projekce (3 promítací směry), Axonometrie (isometrie, dimetrie, trimetrie)
Kosoúhlé - Kabinetní (středoškolská) a kavalírní (bizarní) projekce

Středové - jednobodová perspektiva (když dvě zůstávají rovnoběžky), dvoubodová a tříbodová...

Implementace rovnoběžných
	kolmé - pozorovatel a převedou se souřadné systémy
	kosoúhlé - navíc přenásobit maticí jakoby zkosení

Pro středové je dán střed, směr pohledu, vzdálenost průmětny, svislý vektor
Opět se pozorovatel převede do středu a pak se provede perspektivní zkreslení

Na GPU se omezí ještě maximální (i v nekonečnu) a minimální vzdálenost a zorné pole (zorný kvádr)

Problém s linearitou - diferenční algoritmy
Používá se perspektivně korektní interpolace - vydělíme si to vzdáleností od pozorovatele a přidáme veličinu

## Reprezentace 3D scény

> Navrhněte jeden systém povrchové reprezentace 3D scény, ve kterém se dostatečně rychle hledají sousední stěny, vrcholy, apod. Rámcově tento systém popište.

Objemové (definovaný i vnitřek) a povrchové reprezentace

Objemové - **buněčný model** s voxely, oktanový strom, ... a **CSG** strom (el. tělesa, transformace a množinové op.)
Zobrazují se pak převedením do povrchové nebo vrháním paprsku

Povrchové - drátový model, **VHS(T)** - v tělesech stěny, vnich hrany..., **okřídlená hrana** - 2-manifold (okolí v kruhu)
Nějaké další informace v databázi (barva, materiál, umělá hrana, textura - souřadnice do bitmapy)

Vertex buffer a index buffer v paměti GPU

Alternativně datová struktura corner table - tabulka vrcholů a tabulka rohů (informace protějšího rohu)
Rossignac to pěkně optimalizoval na cca. 9b na vrchol

Eulerovy zákony $V-H+S = 2$, nedovoluje ale díry
Umožňuje nějakou dobrou knihovnu - zajišťování korektnosti

> Přednáška - 08.12.2021

## Hierarchie

> Vyjmenujte výhody hierarchické reprezentace 3D scény (můžete přitom stručně popsat, jak by mohla být hierarchie implementována, věnujte pozornost zejména uložení scény na disk)

Složitější scény se skládají z menších - reprezentace strom

Instancing (více kopií), parametrická konstrukce (velikost, barva, ...), relativní transformace

Změna souřadných systémů před zobrazením - model, světové, pozorovatel, ořezat, perspektivní dělení, okénko...

Formáty: PHIGS, Openinventor (nadstavba nad OpenGL), VRML, OpenSG, ...

Scene graph - výsledek získáme in-order průchodem, dva objekty můžou třeba sdílet vrcholu tvaru, ale jiný materiál

## Matematika

> Jaké jsou výhody reprezentace orientace pomocí kvaternionu? (můžete rámcově kvaternion definovat, není potřeba uvádět důkazy ani pokročilé vlastnosti)

> Jaký je pricip zadání Hermitovy interpolační křivky? (není nutné psát vzorec)



## OpenGL

> Jaká je základní architektura GPU (uvažujte jen vykreslování 3D scény složené z trojúhelníků)?

> Jak GPU typicky řeší viditelnost? Budou správně nakresleny trojúhelníky, které se v prostoru prosekávají?

> Které části zpracování v GPU lze zvenku ovlivnit pomocí tzv. "shaderů"? (napište co víte, nemusí to být úplně přesné)

> Jak se data 3D scény typicky do GPU předávají? (jde o koncepci, ne o technické detaily)

**Vertex shader** - vlastní zpracování každého vrcholu
**Geometry shader** - umožní například zjemnit (přidat polygony)
**Fragment shader** - obarvuje jednotlivé pixely

Jazyky: GLSL a HLSL
Ale nelze dělat modularitu shaderů (pokusy - CgFx, .Fx)

Geometrická primitiva - body, úsečky, trojúhelníky (proužek a vějíř),  čtyřúhelníky (jenom softwarově)

Výhodné je mít v GPU buffery (vertex buffer, index buffer ) a do toho se dávají jen instrukce co s tím

Jak vypadá main... cold start, resize, events, ...

> 11. Přednáška - 15.12.2021

## Viditelnost

> Vyberte si jeden z algoritmů viditelnosti 3D scény a středně podrobně ho popište.

### Malířův algoritmus

Kreslení ploch odzadu (třídění, otestujeme konflikt - minimax resp. otestovat všechny vrcholy za a nakonec všechno)

Zjednodušená varianta s těžištěm (hloubkové třídění)

Pokud budeme mít navzájem překrývající plochy, tak malíř nejde
Můžeme ale nějaký tvar rozdělit

### Z-buffer

Jenom při kreslení pixelů testuje jejich hloubku (float)

Velká paralelizace, není nutné třídění (nemusí se všechno vejít do paměti)
Na druhou stranu zbytečně zatěžujeme fragment shader, z-fighting, poloprůhledné se předzpracují

Můžeme interpolovat jenom $1/z$

> 12. Přednáška - 22.12.2021

## Stínovaní

> Která data potřebujeme mít ve scéně zadaná, abychom mohli objekty stínovat?

> Které znáte stínovací (interpolační) metody?

> Alespoň kvalitativně popište jednoduchý model odrazu světla na povrchu 3D tělesa.

> Kterými parametry by byl definován materiál (vlastnost povrchu) pro Phongův osvětlovací model?

### Phong

Lokální model odrazu světla - část je odraz a část difůze

Difůze se získá z koeficientu, barvy, intenzity a cosinu a ještě se přičítá sekundární, které neumíme spočítat přesně
Lesklý odraz se získá podobně, ale cosinus skalárního součinu $\vec{r}$ a $\vec{v}$ bude umocněný na velikost odlesku

Chci aby součet konstant byl 1 (ochrana proti přetečení, ale až tolik se to neřeší)

Oprava se vzdáleností zdroje - úplně je to nepraktické pro počítače, takže je ve jmenovateli polynom

Blinnovo zjednodušení - udělá se půlící vektor a tím se nahrazuje

### Spojité stínování

Flat shading, Gourdova interpolace (barvy), Fongova interpolace (normály do každého pixelu)

Výpočet normály ve vektorech se v případě nouze dá dělat průměrem ze stěn

Správný systém musí některé hrany nechávat



> 13. Přednáška - 05.01.2022

## Ray-tracing

> Na jakém principu pracuje paprsková zobrazovací metoda "Ray-tracing"? Stručně algoritmus 
> popište.
