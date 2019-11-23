import math
from turtle import forward, penup, pendown, left, exitonclick, right, setup, speed, pensize, screensize

def cm_and_round(a):
    """
    Prevadi ziskane hodnoty na cm a zaokrouhluje na 1 des. misto.
    :param:
    a -- cislo vzniknuvsi dosazenim do rovnice daneho zobrazeni, ktere prevadim na cm
    :return:
    a_cm -- hodnota v cm zaokrouhlena na 1 des. misto, pokud je vetsi nez 100 cm, je misto hodnoty vracena "-"
    a_cm_2 -- totez jako a_cm, vraci ale vsechny hodnoty - i ty vetsi nez 100 cm - pro graficke znazorneni
    """
    a_cm = round((a / (meritko / 100000)), 1)
    a_cm2 = a_cm
    if abs(a_cm) >=100:
        a_cm = "-"
    return(a_cm, a_cm2)

def vypis(rp):
    """
    Vypisuje vysledne hodnoty x a y v cm
    :param:
    rp -- tupple obsahujici 2 seznamy - hodnoty pro rovnobezky (na 1. miste) a poledniky
    """
    print("Rovnobezky:", rp[0])
    print("Poledniky:", rp[1])

def pol_rovnice(zem_delka):
    """
    Prepocet zemepisne delky dle zobrazeni
    :param:
    zem_delka -- zemepisna delka, kterou chci prepocitat
    :return:
    x_cm - prepoctena hodnota v cm, pokud je vetsi nez 100 cm, tak je misto hodnoty vracena "-"
    x_cm_2 - totez jako x_cm, jen pocita pro vsechny hodnoty - i pro ty vetsi nez 100 cm - pro graficke znazorneni
    """
    x = R*math.radians(zem_delka)
    (x_cm, x_cm_2) = cm_and_round(x)  # volam fci pro prevod na cm a zaokrouhleni
    return(x_cm, x_cm_2)

def rovn_lambert(zem_sirka):
    """
    Prepocet zemepisne sirky dle lambertova zobrazeni
    :param
    zem_sirka -- zemepisna sirka, kterou chci prepocitat
    :return:
    y_cm -- prepoctena hodnota v cm, pokud vetsi nez 100 cm, tak se misto ni vraci "-"
    y_cm_2 -- prepoctena hodnota v cm, zahrnuje i hodnoty vetsi nez 100 cm - pro graficke znazorneni
    """
    y = R*math.sin(math.radians(zem_sirka))
    (y_cm, y_cm_2) = cm_and_round(y)
    return(y_cm, y_cm_2)

def rovn_marin(zem_sirka):
    """
    Prepocet zemepisne sirky dle marinova zobrazeni
    :param
    zem_sirka -- zemepisna sirka, kterou chci prepocitat
    :return:
    y_cm -- prepoctena hodnota v cm, pokud vetsi nez 100 cm, tak se misto ni vraci "-"
    y_cm_2 -- prepoctena hodnota v cm, zahrnuje i hodnoty vetsi nez 100 cm - pro graficke znazorneni
    """
    y = R*math.radians(zem_sirka)
    (y_cm, y_cm_2) = cm_and_round(y)
    return(y_cm, y_cm_2)

def rovn_braun(zem_sirka):
    """
    Prepocet zemepisne sirky dle braunova zobrazeni
    :param:
    zem_sirka -- zemepisna sirka, kterou chci prepocitat
    :return:
    y_cm -- prepoctena hodnota v cm, pokud vetsi nez 100 cm, tak se misto ni vraci "-"
    y_cm_2 -- prepoctena hodnota v cm, zahrnuje i hodnoty vetsi nez 100 cm - pro graficke znazorneni
    """
    y = 2*R*math.tan((math.radians(zem_sirka))/2)
    (y_cm, y_cm_2) = cm_and_round(y)
    return(y_cm, y_cm_2)

def rovn_mercator(zem_sirka):
    """
    Prepocet zemepisne sirky dle mercatorova zobrazeni
    :param:
    zem_sirka -- zemepisna sirka, kterou chci prepocitat
    :return:
    y_cm -- prepoctena hodnota v cm, pokud vetsi nez 100 cm, tak se misto ni vraci "-"
    y_cm_2 -- prepoctena hodnota v cm, zahrnuje i hodnoty vetsi nez 100 cm - pro graficke znazorneni
    """
    d = math.radians(90 - zem_sirka)  # polarni vzdalenost v rad
    if d == 0:
        return("-", "-") # osetreni rovnobezky 90 - nekonecno
    else:
        cotg_d_pul = (math.cos(d / 2)) / (math.sin(d / 2))  # cotg z poloviny polarni vzdal
        y = R * math.log(cotg_d_pul)
        (y_cm, y_cm_2) = cm_and_round(y)
        return(y_cm, y_cm_2)

# tvroba poledniku - pro vsechny zobrazeni stejne
def tvorba_poledniku():
    """Vypocet souradnic poledniku
    :return:
    poledniky -- seznam prepoctenych hodnot poledniku v cm, kde misto hodnot vetsich nez 100 cm je "-"
    poledniky_kresleni -- seznam prepoctenych hodnot pro poledniky v cm, zahrnuje i hodnoty vetsi nez 100 cm - pro graficke znazorneni
    """
    poledniky = []
    poledniky_kresleni = []
    for zd in range(-180, 181, 10):
        (x_cm, x_cm_2) = pol_rovnice(zd)# volam fci pro prevod na cm a zaokrouhleni
        poledniky.append(x_cm)
        poledniky_kresleni.append(x_cm_2) # pro vytvoreni seznamu bez "-" pro vykreslovani
    return(poledniky, poledniky_kresleni)

def lambert():
    """"
    Vypocet hodnot pro rovnobezky a poledniky dle Lambertova zobrazeni, vraci seznam x a y hodnot v cm
    :return
    rovnobezky -- seznam prepoctenych hodnot rovnobezek v cm, kde misto hodnot vetsich nez 100 cm je "-"
    pol_cm -- seznam prepoctenych hodnot poledniku v cm, kde misto hodnot vetsich nez 100 cm je "-"
    rovnobezky_kresleni -- seznam prepoctenych hodnot rovnobezek v cm, zahrnuje i hodnoty vetsi nez 100 cm - pro graficke znazorneni
    poledniky_kresleni -- seznam prepoctenych hodnot poledniku v cm, zahrnuje i hodnoty vetsi nez 100 cm - pro graficke znazorneni
    """
    (pol_cm, poledniky_kresleni) = tvorba_poledniku()
    rovnobezky = []
    rovnobezky_kresleni = []

    for zs in range(-90, 91, 10):   # rovnobezky
        (y_cm, y_cm_2) = rovn_lambert(zs)
        rovnobezky.append(y_cm)
        rovnobezky_kresleni.append(y_cm_2)
    return(rovnobezky, pol_cm, rovnobezky_kresleni, poledniky_kresleni)

def marin():
    """"
    Vypocet hodnot pro rovnobezky a poledniky dle Marinova zobrazeni, vraci seznam x a y hodnot v cm
    :return
    rovnobezky -- seznam prepoctenych hodnot rovnobezek v cm, kde misto hodnot vetsich nez 100 cm je "-"
    pol_cm -- seznam prepoctenych hodnot poledniku v cm, kde misto hodnot vetsich nez 100 cm je "-"
    rovnobezky_kresleni -- seznam prepoctenych hodnot rovnobezek v cm, zahrnuje i hodnoty vetsi nez 100 cm - pro graficke znazorneni
    poledniky_kresleni -- seznam prepoctenych hodnot poledniku v cm, zahrnuje i hodnoty vetsi nez 100 cm - pro graficke znazorneni
    """
    (pol_cm, poledniky_kresleni) = tvorba_poledniku()
    rovnobezky = []
    rovnobezky_kresleni = []

    for zs in range(-90, 91, 10):   # rovnobezky
        (y_cm, y_cm_2) = rovn_marin(zs)
        rovnobezky.append(y_cm)
        rovnobezky_kresleni.append(y_cm_2)
    return(rovnobezky, pol_cm, rovnobezky_kresleni, poledniky_kresleni)

def braun():
    """"
    Vypocet hodnot pro rovnobezky a poledniky dle Braunova zobrazeni, vraci seznam x a y hodnot v cm
    :return
    rovnobezky -- seznam prepoctenych hodnot rovnobezek v cm, kde misto hodnot vetsich nez 100 cm je "-"
    pol_cm -- seznam prepoctenych hodnot poledniku v cm, kde misto hodnot vetsich nez 100 cm je "-"
    rovnobezky_kresleni -- seznam prepoctenych hodnot rovnobezek v cm, zahrnuje i hodnoty vetsi nez 100 cm - pro graficke znazorneni
    poledniky_kresleni -- seznam prepoctenych hodnot poledniku v cm, zahrnuje i hodnoty vetsi nez 100 cm - pro graficke znazorneni
    """
    (pol_cm, poledniky_kresleni) = tvorba_poledniku()
    rovnobezky = []
    rovnobezky_kresleni = []

    for zs in range(-90, 91, 10):   # rovnobezky
        (y_cm, y_cm_2) = rovn_braun(zs)
        rovnobezky.append(y_cm)
        rovnobezky_kresleni.append(y_cm_2)
    return (rovnobezky, pol_cm, rovnobezky_kresleni, poledniky_kresleni)

def mercator():
    """"
    Vypocet hodnot pro rovnobezky a poledniky dle Mercatorova zobrazeni, vraci seznam x a y hodnot v cm
    :return
    rovnobezky -- seznam prepoctenych hodnot rovnobezek v cm, kde misto hodnot vetsich nez 100 cm je "-"
    pol_cm -- seznam prepoctenych hodnot poledniku v cm, kde misto hodnot vetsich nez 100 cm je "-"
    rovnobezky_kresleni -- seznam prepoctenych hodnot rovnobezek v cm, zahrnuje i hodnoty vetsi nez 100 cm - pro graficke znazorneni
    poledniky_kresleni -- seznam prepoctenych hodnot poledniku v cm, zahrnuje i hodnoty vetsi nez 100 cm - pro graficke znazorneni
    """
    (pol_cm, poledniky_kresleni) = tvorba_poledniku()
    rovnobezky = []
    rovnobezky_kresleni = []

    for zs in range(-90, 91, 10):  # rovnobezky
        (y_cm, y_cm_2) = rovn_mercator(zs)
        rovnobezky.append(y_cm)
        rovnobezky_kresleni.append(y_cm_2)
    return(rovnobezky, pol_cm, rovnobezky_kresleni, poledniky_kresleni)


def bod():
    """
    Ziska od uzivatele zemepisnou sirku a delku zadaneho bodu, zkontroluje a pripadne upozorni na nekorektni vstupy
    :return
    zs -- korektni zemepisna sirka zadaneho bodu
    zd -- korektni zemepisna delka zadaneho bodu
    """
    while True:
        zs = float(input("zem sirka bodu"))
        zd = float(input("zem delka bodu"))
        if (zs < -90 or zs > 90) or (zd < -180 or zd > 180):  # poreseni vstupu mimo rozsah
            print("zadany neplatne souradnice bodu - zadejte nove")
            continue
        elif zobrazeni =="M" and (zs == -90 or zs == 90):
            print("zadany bod se zobrazi v nekonecnu - zadejte prosim novy bod")
            continue
        return(zs, zd)

def priprava_seznamu(list_rovn, list_pol):
    """Upravi ziskane seznamy rovnobezek a poledniku pro nasledne graficke znazorneni. Vraci upravene seznamy.
    :return:
    rovn_upr -- upraveny seznam prepoctenych souradnic pro rovnobezky pro graficke vykresleni
    pol_upr -- upraveny seznam prepoctenych souradnic pro poledniky pro graficke vykresleni
    """
    if zobrazeni == "M":
        rovn_upr = list_rovn[list_rovn.index(0) + 1 : -1]
        pol_upr = [(i + (-list_pol[0])) * 10 for i in list_pol]  # prevod na vzdalenosti na kresleni - aby byly vsechny kladne a mohlo se kreslit odspodu a prevod na mm
        pol_upr.remove(0)
        return(rovn_upr, pol_upr)
    rovn_upr = list_rovn[list_rovn.index(0)+1:]
    pol_upr = [(i + (-list_pol[0]))*10 for i in list_pol] # prevod na vzdalenosti na kresleni - aby byly vsechny kladne a mohlo se kreslit odspodu a prevod na mm
    pol_upr.remove(0)
    return(rovn_upr, pol_upr)

def zelva_sit_rovn(list_rovn_upr, list_pol_upr, anti_kumul_r):
    """Kresli sit rovnobezek.
    :param
    list_rovn_upr -- upraveny seznam rovnobezek (vystup z fce priprava_seznamu)
    list_pol_upr -- upraveny seznam poledniku (vystup z fce priprava_seznamu)
    anti_kumul_r -- upraveny seznam rovnobezek obsahujici navic hodnotu 0 na prvnim miste -- tedy posunuty seznam
    rovnobezek, ktery slouzi k vypoctu vzdalenosti mezi jednotlivymi rovnobezkami
    anti_kumul_p -- upraveny seznam poledniku obsahujici navic hodnotu 0 na prvnim miste -- tedy posunuty seznam
    poledniku, ktery slouzi k vypoctu vzdalenosti mezi jednotlivymi rovnobezkami
    """
    # posunuti na stred
    screensize(list_pol_upr[-1] + 100, list_rovn_upr[-1]*20 + 100)
    speed(100)
    left(180)
    penup()
    forward(list_pol_upr[-1]/2)
    left(180)
    pendown()
    count = 0 # pomocna promenna slouzici pro pocitani cyklu
    for y, z in zip(list_rovn_upr, anti_kumul_r): # prochazi upraveny seznam souradnic a pomocny seznam k vypoctu vzdalenosti mezi rovnobezkami
        count += 1
        if count == 1:
            pensize(2) # silneji vyznaceny rovnik
        forward(list_pol_upr[-1])
        pensize(1)
        left(180)
        forward(list_pol_upr[-1])
        right(90)
        forward((y - z) * 10) # posun o vzdalenost danych dvou rovnobezek
        right(90)
        if count ==len(list_rovn_upr):
            forward(list_pol_upr[-1])
            right(90)
            forward(list_rovn_upr[-1]*10)
            right(90)
            count2 = 0
            for y2, z2 in zip(list_rovn_upr, anti_kumul_r): # rovnobezky na jizni polokouli
                count2 += 1
                forward(list_pol_upr[-1])
                left(180)
                forward(list_pol_upr[-1])
                right(90)
                forward((y2 - z2) * 10)
                right(90)
                if count2 == len(list_rovn_upr):
                    forward(list_pol_upr[-1])
                    break

def zelva_sit_pol(list_rovn_upr, list_pol_upr, anti_kumul_p):
    """Kresli sit poledniku

    :param:
    list_rovn_upr -- upraveny seznam rovnobezek (vystup z fce priprava_seznamu)
    list_pol_upr -- upraveny seznam poledniku (vystup z fce priprava_seznamu)
    anti_kumul_p -- upraveny seznam poledniku obsahujici navic hodnotu 0 na prvnim miste -- tedy posunuty seznam
    poledniku, ktery slouzi k vypoctu vzdalenosti mezi jednotlivymi poledniky
    """
    right(90)
    count = 0
    for p, q in zip(list_pol_upr, anti_kumul_p):
        count +=1
        if count ==(list_pol_upr.index(list_pol_upr[-1]/2)) + 2: # nulty polednik vykreslen silneji
            pensize(2)
        if zobrazeni =="M":
            presah = (list_pol_upr[-1] - anti_kumul_p[-2])/4
            forward(list_rovn_upr[-1] * 20 + presah)
            right(180)
            forward(list_rovn_upr[-1] * 20 + presah)
            forward(presah)
            left(180)
            forward(presah)
            pensize(1)
            right(90)
            forward(p - q) # posun o vzdalenost mezi dvema poledniky
            left(90)
            if count == len(list_pol_upr):
                forward(list_rovn_upr[-1] * 20 + presah)
                right(180)
                forward(list_rovn_upr[-1] * 20 + presah)
                forward(presah)
                left(180)
                forward(presah)
                break
        else:
            forward(list_rovn_upr[-1]*20)
            pensize(1)
            right(180)
            forward(list_rovn_upr[-1]*20)
            left(90)
            forward(p-q)
            left(90)
            if count ==len(list_pol_upr):
                break
    exitonclick()

# vstupy od uzivatele - zobrazeni, meritko, polomer
zobrazeni = input("Zadejte zobrazeni")
while zobrazeni not in("L", "A", "B", "M"):
    print("Bylo zadano neplatne zobrazeni \n Zadejte nektere z nasledujicich: \n L (Lambertovo zobrazeni), "
          "A (Marinovo zobrazeni, B (Braunovo zobrazeni), M (Mercatorovo zobrazeni)")
    zobrazeni = input("Zadejte zobrazeni")


meritko = int(input("Zadejte meritko"))
while meritko <= 0:
    print("Bylo zadano neplatne meritko")
    meritko = int(input("Zadejte meritko"))


R = float(input("Zadejte polomer Zeme"))
while R < 0:
    print("Zadan neplatny polomer Zeme")
    R = float(input("Zadejte polomer Zeme"))
if R ==0:
    R = 6371.11


if zobrazeni == "L":
    vypis(lambert()[0:2])
    while True: # vypocet souradnic zadaneho bodu
        souradnice = bod()
        if souradnice ==(0,0):
            break
        (zs, zd) = souradnice
        x_cm = pol_rovnice(zd)[1] # tato funkce vraci vsechny hodnoty i ty vetsi nez 100 cm
        y_cm = rovn_lambert(zs)[1]
        print(f" prepocitane souradnice: \n  x: {x_cm}, y: {y_cm}")

elif zobrazeni =="A":
    vypis(marin()[0:2])
    while True: # vypocet souradnic zadaneho bodu
        souradnice = bod()
        if souradnice == (0, 0):
            break
        (zs, zd) = souradnice
        x_cm = pol_rovnice(zd)[1]
        y_cm = rovn_marin(zs)[1]
        print(f" prepocitane souradnice: \n  x: {x_cm}, y: {y_cm}")

elif zobrazeni =="B":
    vypis(braun()[0:2])
    while True: # vypocet souradnic zadaneho bodu
        souradnice = bod()
        if souradnice == (0, 0):
            break
        (zs, zd) = souradnice
        x_cm = pol_rovnice(zd)[1]
        y_cm = rovn_braun(zs)[1]
        print(f" prepocitane souradnice: \n  x: {x_cm}, y: {y_cm}")

elif zobrazeni =="M":
    vypis(mercator()[0:2])
    while True: # vypocet souradnic zadaneho bodu
        souradnice = bod()
        if souradnice == (0, 0):
            break
        (zs, zd) = souradnice
        x_cm = pol_rovnice(zd)[1]
        y_cm = rovn_mercator(zs)[1]
        print(f" prepocitane souradnice: \n  x: {x_cm}, y: {y_cm}")

# zavolani upravenych seznamu pro graficke znazorneni
poledniky_kresleni = tvorba_poledniku()[1]

if zobrazeni =="L":
    rovnobezky_kresleni = lambert()[2]
elif zobrazeni =="A":
    rovnobezky_kresleni = marin()[2]
elif zobrazeni =="B":
    rovnobezky_kresleni = braun()[2]
elif zobrazeni =="M":
    rovnobezky_kresleni = mercator()[2]

(rovn_upr, pol_upr) = priprava_seznamu(rovnobezky_kresleni, poledniky_kresleni)

# seznamy slouzici k vypoctu vzdalenosti mezi jednotlivymi rovnobezkami resp. poledniky
# jedna se o posunute seznamy rovnobezek/poledniku, ktere slouzi k vypoctu vzdalenosti mezi dvema rovnobezkami/poledniky
anti_kumul_r = rovn_upr.copy()
anti_kumul_r.insert(0,0)
anti_kumul_p = pol_upr.copy()
anti_kumul_p.insert(0,0)


zelva_sit_rovn(rovn_upr, pol_upr, anti_kumul_r)
zelva_sit_pol(rovn_upr, pol_upr, anti_kumul_p)