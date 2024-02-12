

#zad1
#   Zolnierzu jako niezabardzo ale jednak wykwalifikowany informatyk jesteś potrzebny swojemu 
#kraju! Masz stworzyć system dla naszej fabryki czolgow. Przy urzyciu klasy masz nadawac karzdemu 
#kolejnemu czolgowi(obiektowi) numer seryjny i musisz zaprogramowac informacje o ilości 
#wyprodukowanych czolgow.

#zad2
#   Niestety ale nasza armia odniosla straty w czolgach. Potrzebujemy informacji o ilości sprawnych  
#maszyn. Ztworz funkcje cls w ktorej podasz liczbe straconych maszyn i która zaktualizuje liczbe 
#sprawnych (liczba wyprodukowanych maszyn ma byc nie tknienta) dodatkowo ta funkcja ma podac wszystkie 
#inne dane.





#zad1========================================================

# class Czolg:
#     wyprodukowano = 0
#     def __init__(self):
#         Czolg.wyprodukowano += 1
#         self.numer_s = Czolg.wyprodukowano

#     @classmethod
#     def ilosc(cls):
#         print(cls.wyprodukowano)

#     def inf(self):
#         print(self.numer_s)


# c1=Czolg()
# c2=Czolg()
# c1.inf()
# c1.ilosc()
# c2.inf()
# c2.ilosc()

#zad2========================================================

# class Czolg:
#     wyprodukowano = 0
#     sprawne = 0
#     def __init__(self):
#         Czolg.wyprodukowano += 1
#         Czolg.sprawne += 1
#         self.numer_s = Czolg.wyprodukowano

#     @classmethod
#     def straty(cls,a):
#         if a <= cls.sprawne:
#             cls.sprawne -= a
#             print(f'jeszcze sprawne jest: {cls.sprawne}')

#     @classmethod
#     def ilosc(cls):
#         print(f'wyprodukowano: {cls.wyprodukowano}')
#         print(f'sprawne: {cls.sprawne}')
#         print(f'zniszczone: {cls.wyprodukowano-cls.sprawne}')

#     def inf(self):
#         print(f'numer seryjny: {self.numer_s}')
#         # Czolg.ilosc()
        


# c1=Czolg()
# c2=Czolg()
# c1.inf()
# c2.inf()
# Czolg.ilosc()




