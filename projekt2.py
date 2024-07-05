"""
projekt2.py: druhý projekt do Engeto Online Python Akademie 
author: Michal Šimek
email: simek.vys@seznam.cz
discord: smk6666
"""
import random

cara = "-" * len("I've generated a random 4 digit number for you.")

def generuj_cislo():
    """
    funkce vrátí list, jehož prvky jsou 4 náhodná celá čísla,
    první číslo nesmí být 0
    """
    cislo = [random.randint(1, 9)]
    while len(cislo)<4:
        a = random.randint(0, 9)
        if a not in cislo:
            cislo.append(a)
    #print(cislo)        
    return cislo


def vypis_uvod():
    print(f"""Hi there!
{cara}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{cara}          
Enter a number:
{cara}"""
    )

def vstup_hrace():
    """
    funkce vrátí string, korektně zadané 4 celá čísla,
    nesmí být duplicity, první číslo nesmí být 0,
    řízená nekonečná smyčka probíhá tak dlouho, dokud není
    korektní vstup zadán, vnořená funkce jsou_duplicity()
    testuje zadané číslo na duplicity
    """

    def jsou_duplicity(a:list):
        b = False
        for i in a:
            if a.count(i) > 1:
                b = True
        return b        
    while True:
        vstup = input()
        if len(vstup) == 4 and (not vstup.isdigit()):
            print("Vstup musí obsahovat jen čísla, zadej znovu.")
        elif vstup.isdigit() and len(vstup) != 4:
            print("Vstup musí být 4 čísla.")
        elif vstup.isdigit() and vstup[0] == "0":
            print("První číslo nesmí být 0.")      
        elif not vstup.isdigit():
            print("Vstup musí být 4 znaky - čísla.")
        elif jsou_duplicity(list(vstup)):
            print("Vstup nesmí obsahovat duplicity.")
        else:
            break
    return vstup

def pocet_krav_a_byku(cislo:list, vstup:list):
    cislo_bez_byku = cislo[:]
    vstup_bez_byku = vstup[:]
    byci = 0
    for a, b  in enumerate(cislo):
        if b == vstup[a]:
            byci += 1
            vstup_bez_byku.remove(b)
            cislo_bez_byku.remove(b)
    #print(cislo, vstup, cislo_bez_byku, vstup_bez_byku)
    kravy = 0
    for c in cislo_bez_byku:
        if c in vstup_bez_byku:
            kravy += 1
    return byci, kravy       

def vypis_vyhodnoceni(byci:int, kravy:int, pocet_vstupu:int):
    a = ["s","","s"]
    b = a[0:byci + 1]
    c = a[0:kravy + 1]
    d = ["", "es"]
    e = d[0:pocet_vstupu]

    if byci != 4:
        print(byci, "".join(list("bull")+[b[len(b) - 1]] + [","]), kravy, "".join(list("cow")+[c[len(c) - 1]]))
        print(cara)
    else:
        print(f"""Correct, you've guessed the right number
in {pocet_vstupu} {"".join(["guess"]+[e[len(e) - 1]])}!
{cara}"""
        )          
        if pocet_vstupu < 6:
            print("That's amazing.")
        elif pocet_vstupu < 10:
            print("That's average.")
        else:
            print("That's not so good.")    
          
def hlavni():
    vypis_uvod()
    cislo = generuj_cislo()
    pocet_vstupu = 0
    while True:    
        vstup = [int(a) for a in vstup_hrace()]
        byci, kravy = pocet_krav_a_byku(cislo, vstup)
        pocet_vstupu += 1
        vypis_vyhodnoceni(byci, kravy, pocet_vstupu)

        if byci == 4:
            break
 

if __name__ == "__main__":
    hlavni()