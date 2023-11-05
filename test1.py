ekwipunek = [1,1,1,1]
maxhp = 25
hpg = 25   #atak i obrona gracza
atg = 1
obg = 0

rodzaj = 'wróg'
hpw = 5
atw = 1
obw = 0

from random import randint

#ekwipunek========================================

def utrac(x):
    ekwipunek.pop(x)
    ekwipunek.insert(x,0)

def podnies(x):
    ekwipunek.pop(x)
    ekwipunek.insert(x,1)

def wyekowaniekod(x):
    ekwipunek.pop(x)
    ekwipunek.insert(x,2)

def odekwipowanie():
    i=0
    while i < len(ekwipunek):
        if ekwipunek[i] == 2:
            ekwipunek.pop(i) 
            ekwipunek.insert(i,1) 
        i += 1
    atg = 1
    obg = 0

def wyekwipuj():
    print('Możesz wyekwipować:')
    if ekwipunek[0] == 1: print('- miecz')
    if ekwipunek[1] == 1: print('- tarcze')
    if ekwipunek[2] == 1: print('- toporek')
    if ekwipunek[3] == 1: print('- duży miecz (dwuręczny)')
    else:
        i=[]
        for el in ekwipunek:
            if el != 2: i.append(el)
        if sum(i) == 0: print('nie masz nic co możesz wyekwipować')
    print('Masz obecnie wyekwipowany:') 
    if ekwipunek[0] == 2: print('- miecz')
    if ekwipunek[1] == 2: print('- tarcze')
    if ekwipunek[2] == 2: print('- toporek')
    if ekwipunek[3] == 2: print('- duży miecz (dwuręczny)')
    else:
        i=[]
        for el in ekwipunek:
            if el == 2: i.append(el)
        if sum(i) == 0: print('nie masz nic co masz wyekwipowane')
    print('Czy chcesz wyekwipować nowe żeczy? tak/nie')
    inp=input()
    if inp == 'tak':
        print('Podaj co chcesz wyekwipować.')
        odekwipowanie()
        i=0
        while i<2:
            inp = input()
            if inp == 'miecz':
                if ekwipunek[0] == 1: wyekowaniekod(0); i += 1; atg =+ 2
                else: print('nie możesz wyekwipować tego przedmiotu')
            elif inp == 'tarcze':
                if ekwipunek[1] == 1: wyekowaniekod(1); i += 1; obg =+ 3
                else: print('nie możesz wyekwipować tego przedmiotu')
            elif inp == 'toporek':
                if ekwipunek[2] == 1: wyekowaniekod(2); i += 1; atg =+3
                else: print('nie możesz wyekwipować tego przedmiotu')
            elif inp == 'duży miecz':
                if ekwipunek[3] == 1: wyekowaniekod(3); i += 2; atg =+6
                else: print('nie możesz wyekwipować tego przedmiotu')
            elif inp == 'nic': i += 1
            else: print('błąd')
            if i > 2:
                print('Masz za dużo wyekwipowane.Twoja ')
                print('postać ma tylko dwie ręce. Wybież')
                print('jeszcze raz co chcesz wyekwipować.')
                i = 0
                odekwipowanie()

# ekwipunek.pop(2) 
# ekwipunek.insert(2,'tu')     #gdzie?,co?

#dostępne_ataki=====================================

def atak():
    print('Dostępne ataki:')
    if ekwipunek[0] == 2:
        print('ataki mieczem:')
        print('-pchnięcie')
        print('-cięcie')
    if ekwipunek[2] == 2:
        print('ataki toporkiem:')
        print('-cios przebiijający')
        print('-zwykły cios')
    if ekwipunek[3] == 2:
        print('ataki dużym mieczem:')
        print('-cios z nad głowy')
        print('-rąbnięcie')
    if sum(ekwipunek) >= 0:
        print('zwykłe ataki:')
        print('-kopniak')
        print('-sierpowy')
    while True:
        inp = input()
        if inp == 'pchnięcie':
            if ekwipunek[0] == 2:
                i = randint(0,4)
                if i == 3: i = 5; print('cios krytyczny')
                global hpw
                global atg
                global obw
                hpw = hpw - atg - i + obw
                break
            else:
                print('nie możesz tego zrobić')
        if inp == 'cięcie':
            if ekwipunek[0] == 2:
                global hpw
                global atg
                global obw
                i = randint(1,2)
                hpw = hpw - atg - i + obw
                break
            else:
                print('nie możesz tego zrobić')
        if inp == 'cios przebijający':
            if ekwipunek[2]:
                i = randint(0,1)
                global hpw
                global atg
                global obw
                obw = obw - randint(0,1)
                hpw = hpw - atg - i + obw
                break
            else:
                print('nie możesz tego zrobić')
        if inp == 'zwykły cios':
            if ekwipunek[2]:
                i = randint(4,6)
                global hpw
                global atg
                global obw
                obw = obw + randint(0,1)
                hpw = hpw - atg - i + obw
                break
            else:
                print('nie możesz tego zrobić')
        if inp == 'cios z nad głowy':
            if ekwipunek[3] == 2:
                i = 0
                global hpw
                global atg
                global obw
                obw = obw - randint(0,2)
                hpw = hpw - atg - i + obw
                break
            else:
                print('nie możesz tego zrobić')
        if inp == 'rąbnięcie':
            if ekwipunek[3]:
                i = randint(0,4)
                global hpw
                global atg
                global obw
                hpw = hpw - atg - i + obw
                break
            else:
                print('nie możesz tego zrobić')
        if inp == 'kopniak':
            i = randint(0,1)
            global hpw
            global atg
            global obw
            hpw = hpw - atg - i + obw
            break
        if inp == 'sierpowy':
            i = 0
            global hpw
            global atg
            global obw
            hpw =+ - atg - i + obw
            break
        else:
            print('nie możesz tego zrobić')



atak()

print(hpw, atw ,obw)

