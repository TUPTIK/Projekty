import classes 

pulka = [];users = [];user_in_use = []

def wst():
    print('')
    print('==========/\==========')
    print('')

def new_book():
    pulka.append(classes.Ksienga(user_in_use[0].name))
    wst()

def tytles():
    for el in range(len(pulka)):
        pulka [el].tyt
    wst()

def info_sz():
    print('Podaj tytul ktury chcesz sprawdzic.')
    ty = input()
    for el in range(len(pulka)):
        if pulka [el].dane['tytul'] == ty:
            pulka [el].inf(user_in_use[0].name,user_in_use.rang)
            wst();return None
    print('nie ma takiej książki')
    wst()
        
def register():
    users.append(classes.Usrer())
    wst()

def login():
    print('podaj nazwe uzytkownika')
    nazwa = input()
    for el in range(len(users)):
        if users[el].name == nazwa:
            print('podaj haslo')
            if users[el].haslo == input():
                for i in user_in_use:user_in_use.pop[0]
                user_in_use.append(users[el]); wst()
                return None
            else: print('zle haslo');wst();return None
    print('nie ma takiego uzytkownika  :(');wst()

def zmien():
    print('podaj tytul ksiomzki kturej dane chcesz zmienić')
    ty = input()
    for el in range(len(pulka)):
        if pulka [el].dane['tytul'] == ty:
            pulka[el].change(user_in_use[0].name,user_in_use[0])
    wst()

def user0():
        print('musisz sie zalogować')
        print('jesli nie masz konta utwuz je')
        print('A --> utwuz konto')
        print('B --> zaloguj sie')
        inp = input()
        if inp == 'A':
            register()
        elif inp == 'B':
            login()
        else: print('nieznana komenda')
        wst()

def wyloguj():
    user_in_use.pop(0)



while True:
    if len(user_in_use) == 0: user0()
    else:
        print('co chcesz zrobic?')
        print('A --> stwuz nowa ksiamzke')
        print('B --> zobacz wszystkie tytuly')
        print('C --> sprawdz dane konkretnej ksiamzki')
        print('D --> stworz nowe konto')
        print('E --> zaloguj sie na inne konto')
        print('F --> zmien opis jakiejs ksiomzki')
        print('G --> wyloguj sie')
        inp = input()
        if inp == 'A': new_book()
        elif inp == 'B':tytles()
        elif inp == 'C':info_sz()
        elif inp == 'D':register()
        elif inp == 'E':login()
        elif inp == 'F':zmien()
        elif inp == 'G':wyloguj()
        wst()


