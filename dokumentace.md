# Dokumentace

Program vypočítá na základě zadaných parametrů - *zobrazení, měřítko, poloměr Země* přepočtené souřadnice poledníků a rovnoběžek. Program je konkrétně zaměřen na 4 válcová tečná zobrazení, a to: Lambertovo, Braunovo, Marinovo a Mercatorovo. Uživatel má dále možnost zjistit mimo souřadnic poledníků a rovnoběžek i souřadnice jednotlivých bodů. **Výstupem programu** je seznam přepočtených souřadnic rovnoběžek a poledníků, příp. souřadnice zadaných bodů a grafické znázornění daného zobrazení pomocí "želví" grafiky.

## Jak program pracuje

#### Povinné uživatelské vstupy

Po spuštění programu je uživatel dotázán na **zobrazení**, se kterým chce počítat. Je možné zadat následující hodnoty:

- `L` - Lambertovo zobrazení
- `B` - Braunovo zobrazení
- `A` - Marinovo zobrazení
- `M` - Mercatorovo zobrazení

Pokud zadá uživatel jiný vstup, program uživatele upozorní a vyžaduje zadání jiné hodnoty tak dlouho, dokud není zadána korektní hodnota.

Dále zadává uživatel **měřítko**, které chce při výpočtu použít. Konkrétně uživatel zadává měřítkové číslo, tedy číslo `x` pokud uvažujeme měřítko ve formátu `1 : x`.  Zadané měřítkové číslo musí být nutně celočíselné a kladné, pokud tomu tak není, program uživatele upozorní a vyžaduje zadání jiné hodnoty, a to tak dlouho, dokud není zadána korektní hodnota. 

Dalším zadávaným parametrem je **poloměr Země**. Pokud je zadána hodnota `0`, tak je počítáno s poloměrem 6371,11 km.  Zadaný poloměr musí být kladné číslo, pokud tomu tak není je uživatel upozorněn a program požaduje zadání nové hodnoty dokud není hodnota poloměru korektní.

#### Výstupy  

##### seznamy přepočtených souřadnic

Po zadání výše popsaných parametrů program vypíše 2 seznamy přepočtených souřadnic. 

1. seznam  vzdáleností na svislé ose, kde by byly zakreslovány rovnoběžky od -90 do 90°, s intervalem 10°
2. seznam vzdáleností na vodorovné ose, kde by byly zakreslovány poledníky od -180 do 180°, taktéž s intervalem 10°

Výsledné hodnoty jsou uváděny v centimetrech.

Pokud některá hodnota překročila 100 cm, tak je místo ní ve výsledných seznamech zapsána "-".

##### Výpočet souřadnic bodu

Po výše uvedeném výpisu přepočtených souřadnic má uživatel možnost zjistit přepočtené souřadnice pro libovolný bod. Program se postupně dotazuje na zeměpisnou šířku a délku bodu, následně vypíše přepočtené souřadnice a táže se na další bod a to tak dlouho, dokud není zadán bod o souřadnicích (0,0). Pokud jsou zadány nekorektní hodnoty - zeměpisná šířka mimo interval <-90; 90> a zeměpisná délka mimo interval <-180; 180>, tak je uživatel upozorněn a program vyžaduje zadání nových souřadnic, a to dokud není není jejich hodnota v pořádku. 

V případě Mercatorova zobrazení taktéž není možné vypočítat přepočtené souřadnice pro bod o zeměpisné šířce -90° a 90° (tyto body se zobrazí v nekonečnu), uživatel je tak v tomto případě upozorněn a je vyzván k zadání souřadnic nových. 

##### Grafické znázornění zobrazení

Na závěr je pomocí "želví" grafiky vykreslena síť daného zobrazení. Síť je vykreslena tak, že 1 mm je vykreslen jako 1 px. 







 



 

