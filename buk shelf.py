import classes 

b1=0;b2=0;b3=0;b4=0;b5=0;b6=0;b7=0;b8=0;b9=0;b10=0
b11=0;b12=0;b13=0;b14=0;b15=0;b16=0;b17=0;b18=0;b19=0;b20=0
b21=0;b22=0;b23=0;b24=0;b25=0;b26=0;b27=0;b28=0;b29=0;b30=0
b31=0;b32=0;b33=0;b34=0;b35=0;b36=0;b37=0;b38=0;b39=0;b40=0
b41=0;b42=0;b43=0;b44=0;b45=0;b46=0;b47=0;b48=0;b49=0;b50=0
u1=0;u2=0;u3=0;u4=0;u5=0;u6=0;u7=0;u8=0;u9=0;u10=0
magazyn = [
    b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,
    b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,
    b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,
    b31,b32,b33,b34,b35,b36,b37,b38,b39,b40,
    b41,b42,b43,b44,b45,b46,b47,b48,b49,b50]
pulka = []
zusers = [u1,u2,u3,u4,u5,u6,u7,u8,u9,u10]
users = [];user_in_use = []

def new_book():
    magazyn [0] = classes.Ksienga(user_in_use[0].name)
    pulka.append(magazyn [0])
    magazyn.pop(0)

def tytles():
    for el in pulka:
        pulka [el].tyt

def info_sz():
    print('Podaj tytul ktury chcesz sprawdzic.')
    ty = input()
    for el in pulka:
        if pulka [el].dane['tytul'] == ty:
            pulka [el].inf(user_in_use[0].name,user_in_use.rang)
            return None
        
def register():
    zusers [0]= classes.Usrer
    users.append(zusers[0])

def login():
    print('podaj nazwe uzytkownika')
    nazwa = input()
    for el in users:
        if users[el].name == nazwa:
            print('podaj haslo')
            if users[el].haslo == input():
                for i in user_in_use:user_in_use.pop[0]
                user_in_use.append(users[el])
                return None
            else: print('zle haslo');return None
    print('nie ma takiego uzytkownika  :(')

def zmien():
    print('podaj tytul ksiomzki kturej opis chcesz zmienic')
    ty = input()
    for el in pulka:
        if pulka [el].dane['tytul'] == ty:
            pulka[el].change(user_in_use[0].name,user_in_use[0])

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
        inp = input()
        if inp == 'A': new_book()
        elif inp == 'B':tytles()
        elif inp == 'C':info_sz()
        elif inp == 'D':register()
        elif inp == 'E':login()
        elif inp == 'F':zmien()


