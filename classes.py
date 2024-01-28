from uuid import uuid4

class Ksienga:
    def __init__(self,us):
        self.user = us
        self.dane ={
            'tytul' : 'xxx',
            'autor' : 'xxx',
            'gatunek' : 'xxx',
            'opis' : 'xxx',
            'liczba stron' : 'xxx',
            'IP' : uuid4
        }
        self.twoz()

    def tyt(self):
        print(self.dane['tytul'])

    def inf(self,us,rang):
        if self.user == us: rang = 1
        if rang == 0:
            for k,v in self.dane.items():
                print(f"{k} : {v}")
        if rang == 1:
            for k,v in self.dane.items():
                print(f"{k} : {v}")
            print('To twoj tytul (mozesz zmieniac jego opis)')
        elif rang == 2:
            for k,v in self.dane.items():
                print(f"{k} : {v}")
            print(f'twurca: {self.user}')

    def twoz(self):
        print("podaj tytul:")
        self.dane["tytul"] = input()
        print("podaj imie autora:")
        self.dane["autor"] = input()
        print("podaj gatunek:")
        self.dane["gatunek"] = input()
        print("podaj opis: (jest zmienialny)")
        self.dane["opis"] = input()
        print("podaj liczbe stron:")
        self.dane["liczba stron"] = input()

    def change(self,us,rang):
        if self.user == us: rang = 1
        if rang == 0:
            print('ERROR ')
            print('nie masz uprawnien do wprowadzania zmian')
        elif range > 0:
            print('podaj nowy opis ksiazki')
            self.dane['opis'] = input()

class Ksienga_istniejomca:
    def __init__(self,lst):
        self.dane ={
            'tytul' : lst[0],
            'autor' : lst[1],
            'gatunek' : lst[2],
            'opis' : lst[3],
            'liczba stron' : lst[4],
            'IP' : uuid4
        }

    def tyt(self):
        print(self.dane['tytul'])
    
    def inf(self,rang):
        if rang == 0:
            for k,v in self.dane.items():
                print(f"{k} : {v}")
        elif rang == 1:
            for k,v in self.dane.items():
                print(f"{k} : {v}")

    def change(self,rang):
        if rang == 0:
            print('ERROR ')
            print('nie masz uprawnien do wprowadzania zmian')
        elif range > 0:
            print('podaj nowy opis ksiazki')
            self.dane['opis'] = input()

class Usrer():
    def __init__(self) -> None:
        print("podaj imie uzytkownika:")
        self.name = input()
        print("podaj haslo:")
        self.haslo = input()
        self.rang = 0

    def zmien_haslo(self):
        print('podaj stare haslo')
        if input() == self.haslo:
            print("podaj nowe haslo:")
            self.haslo = input()
        else: print('zle haslo')

class Admin():
    def __init__(self) -> None:
        print("podaj imie administratora:")
        self.name = input()
        print("podaj haslo:")
        self.haslo = input()
        self.rang = 2

    def zmien_haslo(self):
        print('podaj stare haslo')
        if input() == self.haslo:
            print("podaj nowe haslo:")
            self.haslo = input()
        else: print('zle haslo')

