ekwipunek = [0,0,0,0]

def podnies(x):
    ekwipunek.pop(x)
    ekwipunek.insert(x,1)

def utrac(x):
    ekwipunek.pop(x)
    ekwipunek.insert(x,0)

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
                if ekwipunek[0] == 1: wyekowaniekod(0); i += 1
                else: print('nie możesz wyekwipować tego przedmiotu')
            elif inp == 'tarcze':
                if ekwipunek[1] == 1: wyekowaniekod(1); i += 1
                else: print('nie możesz wyekwipować tego przedmiotu')
            elif inp == 'toporek':
                if ekwipunek[2] == 1: wyekowaniekod(2); i += 1
                else: print('nie możesz wyekwipować tego przedmiotu')
            elif inp == 'duży miecz':
                if ekwipunek[3] == 1: wyekowaniekod(3); i += 2
                else: print('nie możesz wyekwipować tego przedmiotu')
            else: print('błąd')
            if i > 2:
                print('Masz za dużo wyekwipowane.Twoja ')
                print('postać ma tylko dwie ręce. Wybież')
                print('jeszcze raz co chcesz wyekwipować.')
                i = 0
                odekwipowanie()


