
from random import randint, choice,choices

imie = 'bezimienny'
ekwipunek = [1,1,1,1]
gold = 45
maxhp = 25
hpg = 25   #atak i obrona gracza
atg = 5
obg = 2

rodzaj = 'brak_wroga'
hpw = 5
atw = 1
obw = 0

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
    global atg
    global obg
    i=0
    while i < len(ekwipunek):
        if ekwipunek[i] == 2:
            ekwipunek.pop(i) 
            ekwipunek.insert(i,1) 
        i += 1
    atg = 1
    obg = 0

def wyekwipuj():
    global atg
    global obg
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


#pomieszczenia====================================

map = []
dosmap = [1,1,2,3,4,4]  #5

while len(map) < 3:
    i = randint(1, len(dosmap)) - 1
    j = dosmap [i]
    map.append(j)
    dosmap.pop(i)

def pom1():
    global atw
    global obw
    global hpw
    global rodzaj
    global gold
    print('----------------||----------------')
    print('Po chwili marszu wchodzisz do')
    print('sporego i jasnego pomieszczenia.')
    print('Na jego sierodku stoi stół z')
    print('lampką oliwną. Wokół stołu siedzi')
    print('troje goblinów grających w pokera.')
    print('Na twój widok wszystkie wstają z')
    print('wrogimi okrzykami i żucają się na')
    print('ciebie uzbrojone w noże ...')
    print('----------------||----------------')
    inp = input()
    if inp=='gram w karty'or inp=='gram z goblinami'or inp=='karty' or inp=='gram'and gold>= 45:
        print('----------------||----------------')
        print('Gobliny spoczątku nie chcą z tobą')
        print('grać. Jednak po daniu każdemu po')
        print('15 sztuk złota na dobry początek')
        print('zapraszają cie do stołu. Szybko')
        print('okazuje się że wszystkie są')
        print('beznadziejne w karty. Ograłeś')
        print('wszystkie co do grosz. Wygrany z')
        print('przyjemnie wypełnioną sakiewką')
        print('ruszasz dalej.')
        print('----------------||----------------')
        i = randint(85, 125)
        gold += i
        print(f'Wygrałeś {i} golda.')
        print(f'Masz obecnie {gold} golda.')
        input()
        return('False')
    else:
        atw = 6
        obw = 3
        hpw = 15
        rodzaj = 'gobliny-hazardziści'
        return('True')

def pom2():
    global atw
    global obw
    global hpw
    global rodzaj
    print('----------------||----------------')
    print('Po jakimś czasie marszu starymi')
    print('i opuszczonymi lochami znajdujesz')
    print('wyglądający na nowy tunel. Po')
    print('przejściu nim chwili znajdujesz')
    print('wzmacnianie dżwi zza których')
    print('słyszysz kżyki bólu.')
    print('----------------||----------------')
    print('otwierasz je? tak/nie')
    while True:
        inp = input()
        if inp == 'nie':
            return('False')
        elif inp == 'tak':
            print('----------------||----------------')
            print('Odrazu po wejściuwidzisz widzisz')
            print('gigantyczną sale tortur. Przy')
            print('jednej z maszyn wielki kat właśnie')
            print('dobijał jakąś osobe. Na twój widok')
            print('kat wydał nieludzki wrzask ')
            print('wściekłości i żucił się na ciebie.')
            print('----------------||----------------')
            atw = 8
            obw = 0
            hpw = 50
            rodzaj = 'kat'
            input()
            return('True')

def pom3():
    global atw
    global obw
    global hpw
    global rodzaj
    print('----------------||----------------')
    print('Po kolejnych godzinach wędrówki')
    print('docierasz do grota z wielkim ')
    print('jeziorem na sierodku. Przez dziurę')
    print('w suficie widać księżyc. Po chwili')
    print('po jezioże przechodzi fale jagby')
    print('coś dużego się zanużyło. Nagle z')
    print('pot wody wyskakuje kaczy król ')
    print('----------------||----------------')
    atw = 1
    obw = 0
    hpw = 20
    rodzaj = 'kaczy król'
    input()
    return('True')

def pom4():
    global atw
    global obw
    global hpw
    global rodzaj
    print('----------------||----------------')
    print('Idziesz jak gdyby nic. Od zwykły')
    print('kolejny korytaż. Jednak już do')
    print('niego wchodząc czujesz że coś jest')
    print('ne tak. Z pod nóg uciekają ci całe')
    print('stada szczurów. Sgąd ih tu tyle?')
    print('Po smrodzie i zjedzonych zwłokach')
    print('zaczynasz rozumieć ,jednak kiedy')
    print('chciałeś droge zastawia ci cała')
    print('horda szczurów ...')
    print('----------------||----------------')
    input()
    atw = 4
    obw = -2
    hpw = 15
    rodzaj = 'szczurki'
    return('True')

# def pom5():     #dokończ
#     global atw
#     global obw
#     global hpw
#     global rodzaj
#     print('----------------||----------------')
#     print('pom5')
#     print('----------------||----------------')
#     atw = 1
#     obw = 0
#     hpw = 10
#     rodzaj = 'wróg'

#następny_pokój===================================

def next_door():
    global map
    if map [1] == 1:
        if pom1() == 'True':
            walka()
        else: return('False')
    elif map [1] == 2:
        if pom2() == 'True':
            walka()
        else: return('False')
    elif map [1] == 3:
        if pom3() == 'True':
            walka()
        else: return('False')
    elif map [1] == 4:
        if pom4() == 'True':
            walka()
        else: return('False')
    # elif map [1] == 5:
    #     if pom5() == 'True':
    #         walka()
    #     else: return('False')
    map.pop(1)

#jeszcze_żyjecie?=================================

def zyjecie():
    if hpg <= 0:
        print('----------------||----------------')
        print('Bul z wielu ran zaczyna słabnąć.')
        print('Zaczynasz rozumieć że umierasz.')
        print('Jesteś zaskoczony że to tak tługo')
        print('trwa. Tracisz świadomość. Widziś')
        print('światło ...')
        print('- o  m ó j  B O Ż E ! ...')
        print('----------------||----------------')
        return('Lose')
    elif hpw <= 0:
        return('Win')
    elif hpw > 0 and hpg > 0:
        return('Draw')

#loot=============================================

def loot():
    global gold
    if rodzaj == 'gobliny-hazardziści':
        print('----------------||----------------')
        print('Po zaskakująco ciężkiej walce')
        print('udaje ci się zadać ostatni cios')
        print('ostatniemu z goblinów. Zdyszany')
        print('ale terz uśmiechnięty podchodzisz')
        print('do stolika by wypić niedopity')
        print('alkochol ale też zabrać całkiem')
        print('pokaźną pule nagród.')
        print('----------------||----------------')
        i = randint(70, 85)
        gold += i
        print(f'Zbierasz {i} golda.')
        print(f'Masz obecnie {gold} golda.')
        input()
    elif rodzaj == 'kat':
        print('----------------||----------------')
        print('Kilka ostatnich mocnych ciosów i')
        print('po długiej walce wielki kat leży')
        print('na ziemi. Z zaciekawieniem patżysz')
        print('na jego toporek u pasa.')
        print('---------------||----------------')
        if ekwipunek [2] == 0:
            print('czy podnosisz toporek? tak/nie')
            while True:
                inp = input()
                if inp == 'tak':
                    podnies(2)
                    break
                elif inp == 'nie':
                    break
                else:
                    print('błąd')
        i = randint(27, 150)
        gold += i
        print(f'Zbierasz {i} golda.')
        print(f'Masz obecnie {gold} golda.')
        input()
    elif rodzaj == 'kaczy król':
        print('----------------||----------------')
        print('Ta walka okazała się być łatwiejsza')
        print('niż mogłeś przypuszczać. Po chwili')
        print('walki upitoliłeś przerośniętej')
        print('kaczce łeb. Kdyby nie fakt, że nie')
        print('masz dostępu zjadłbyś teraz')
        print('potrawke z kaczki. Znajdujesz przy')
        print('nodze kaczki przywiązaną sakiewke.')
        print('----------------||----------------')
        i = randint(40, 60)
        gold += i
        print(f'Zbierasz {i} golda.')
        print(f'Masz obecnie {gold} golda.')
        input()
    elif rodzaj == 'szczurki':
        print('----------------||----------------')
        print('Po niezbyt trudnej walce zabierasz')
        print('trupowi sakiewke i odchodzisz.')
        print('----------------||----------------')
        i = randint(20,30)
        gold += i
        print(f'Zbierasz {i} golda.')
        print(f'Masz obecnie {gold} golda.')
        input()

#walka============================================

def atakgr():
    global hpw
    global obw
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
                if atg + i >obw:
                    hpw = hpw - atg - i + obw
                    print(f'Zadajesz {atg + i-obw} hp')
                else:
                    print('nie zadajesz żadnych obrażeń')
                break
            else:
                print('nie możesz tego zrobić')
        if inp == 'cięcie':
            if ekwipunek[0] == 2:
                i = randint(1,2)
                if atg + i >obw:
                    hpw = hpw - atg - i + obw
                    print(f'Zadajesz {atg + i-obw} hp')
                else:
                    print('nie zadajesz żadnych obrażeń')
                break
            else:
                print('nie możesz tego zrobić')
        if inp == 'cios przebijający':
            if ekwipunek[2]:
                obw = obw - randint(0,1)
                i = randint(0,1)
                if atg + i >obw:
                    hpw = hpw - atg - i + obw
                    print(f'Zadajesz {atg + i-obw} hp')
                else:
                    print('nie zadajesz żadnych obrażeń')
                break
            else:
                print('nie możesz tego zrobić')
        if inp == 'zwykły cios':
            if ekwipunek[2]:
                i = randint(4,6)
                obw = obw + randint(0,1)
                if atg + i >obw:
                    hpw = hpw - atg - i + obw
                    print(f'Zadajesz {atg + i-obw} hp')
                else:
                    print('nie zadajesz żadnych obrażeń')
                break
            else:
                print('nie możesz tego zrobić')
        if inp == 'cios z nad głowy':
            if ekwipunek[3] == 2:
                i = 0
                obw = obw - randint(0,2)
                if atg + i >obw:
                    hpw = hpw - atg - i + obw
                    print(f'Zadajesz {atg + i-obw} hp')
                else:
                    print('nie zadajesz żadnych obrażeń')
                break
            else:
                print('nie możesz tego zrobić')
        if inp == 'rąbnięcie':
            if ekwipunek[3]:
                i = randint(0,4)
                if atg + i >obw:
                    hpw = hpw - atg - i + obw
                    print(f'Zadajesz {atg + i-obw} hp')
                else:
                    print('nie zadajesz żadnych obrażeń')
                break
            else:
                print('nie możesz tego zrobić')
        if inp == 'kopniak':
            i = randint(0,1)
            if atg + i >obw:
                hpw = hpw - atg - i + obw
                print(f'Zadajesz {atg + i-obw} hp')
            else:
                print('nie zadajesz żadnych obrażeń')
            break
        if inp == 'sierpowy':
            i = 0
            if atg + i >obw:
                hpw = hpw - atg - i + obw
                print(f'Zadajesz {atg + i-obw} hp')
            else:
                print('nie zadajesz żadnych obrażeń')
            break
        else:
            print('nie możesz tego zrobić')

def atakwr():
    global hpg
    global obw
    global rodzaj
    global atw
    if rodzaj == 'gobliny-hazardziści':
        i = sum(choices([1,1,1,1,2,2,3]))
        if i == 1:
            print('gobliny bezładnie dźgają')
            i = randint(-2,1)
            if i + atw > obg:
                print(f'zadją ci {atw + i-obg} hp')
                hpg = hpg - atw - i+obg
            else:
                print('nie zadają ci żadnych obrażeń')
        elif i == 2:
            print('gobliny przeprowadzają szarże')
            if atw - obg >= 0:
                print(f'zadją ci {atw -obg} hp')
                hpg = hpg - atw - i+obg
            else:
                print('nie zadają ci żadnych obrażeń')
        elif i == 3:
            print('gobliny prubują cię otoczyć')
            if randint(0,1) == 1:
                print('i im się to udaje')
                i = randint(2,4)
                if i + atw > obg:
                    print(f'zadją ci {atw + i-obg} hp')
                    hpg = hpg - atw - i+obg
                else:
                    print('nie zadają ci żadnych obrażeń')
            else:
                print('nieudaje się to im przez co się odsłaniają')
                obw += -randint(1,2)
                i = randint(0,2)
                if atw >= obg + i:
                    hpg += -atw + i+obg
                    print(f'gobliny nieudolnie zadają ci {atw - i-obg} hp')
                else:
                    print('nie udaje im się zadać ci żadnych obrażeń')
    elif rodzaj == 'kat':
        i = sum(choices([1,1,2,2,3]))
        if i == 1:
            print('Kat atakuje cię toporkiem który miał u pasa.')
            i = randint(-1,1)
            if i + atw > obg:
                print(f'zadją ci {atw + i-obg} hp')
                hpg = hpg - atw - i+obg
            else:
                print('nie zadają ci żadnych obrażeń')
        elif i == 2:
            print('Kat żucz w ciebie kawałkami maszyn do tortur')
            if randint(1,5) > 1:
                i = randint(2,4)
                if i + atw > obg:
                    print(f'zadją ci {atw + i-obg} hp')
                    hpg = hpg - atw - i+obg
                else:
                    print('nie zadają ci żadnych obrażeń')
            else:
                print('kat niczym cię nie trafia')
        elif i == 3:
            print('Kat szarżyje na ciebie i atakuje na wszelkie sposoby.')
            i = randint(1,3)
            if i + atw > obg:
                print(f'zadją ci {atw + i-obg} hp')
                hpg = hpg - atw - i+obg
            else:
                print('nie zadają ci żadnych obrażeń')
    elif rodzaj == 'kaczy król':
        i = sum(choices([1,1,2]))
        if i == 1:
            print('Król ciebie dziobie.')
            i = randint(1,4)
            if i + atw > obg:
                print(f'zadją ci {atw + i-obg} hp')
                hpg = hpg - atw - i+obg
            else:
                print('nie zadają ci żadnych obrażeń')
        elif i == 2:
            print('Kaczy król wzywa posiłki.')
            i = randint(0,1)
            if i + atw > obg:
                print(f'zadją ci {atw + i-obg} hp')
                hpg = hpg - atw - i+obg
            else:
                print('nie zadają ci żadnych obrażeń')
    elif rodzaj == 'szczurki':
        i = sum(choices([1,1,2]))
        if i == 1:
            print('Szczury zalewają cię falą do kolan.')
            i = randint(-1,1)
            if i + atw > obg:
                print(f'zadją ci {atw + i-obg} hp')
                hpg = hpg - atw - i+obg
            else:
                print('nie zadają ci żadnych obrażeń')
        elif i == 2:
            print('szczury boleśnie gryzą cie w stopy')
            i = randint(1,2)
            if i + atw > obg:
                print(f'zadją ci {atw + i-obg} hp')
                hpg = hpg - atw - i+obg
            else:
                print('nie zadają ci żadnych obrażeń')

def walka():
    global rodzaj
    print(f"Walczysz z {rodzaj} .")
    while zyjecie() == 'Draw':
        print(f'obecnie masz {hpg} hp, {obg} obrony i {atg} ataku')
        print('')
        print(f'wróg ma obecnie {hpw} hp, {obw} obrony i {atw} ataku')
        input()
        atakgr()
        if zyjecie() != 'Draw':
            break
        print(f'wróg ma obecnie {hpw} hp, {obw} obrony i {atw} ataku')
        print('')
        print(f'obecnie masz {hpg} hp, {obg} obrony i {atg} ataku')
        input()
        atakwr()
    if zyjecie() == 'Win':
        print(f'Gratuluje wygrałeś ze {rodzaj}.')
        input()
        loot()
        rodzaj = 'brak_wroga'
        return(True)
    elif zyjecie() == 'Lose':
        return(False)

#testy============================================

wyekwipuj()
next_door()
