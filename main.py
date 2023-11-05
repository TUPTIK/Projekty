import eqat
#statystyki=========================================
imie = "bezimienny"
hp = 25
mana = 15
złoto = 0


#funkcje_ekwipunku==================================

def podnies(x):
    eqat.ekwipunek.pop(x)
    eqat.ekwipunek.insert(x,1)

def utrac(x):
    eqat.ekwipunek.pop(x)
    eqat.ekwipunek.insert(x,0)

#fabułapokuj_wstęp==================================
print("----------------||----------------")
print("Budzisz się gdzieś. Tak to dobry")
print("opis. Nie masz bladego pojęcia")
print("gdzie ty właściwie jesteś...")
print("----------------||----------------")                         
                                                                    

inp = input()
if inp == "cheathp":
    print("cheat hp on")
    hp == 99999
    print("")

print("----------------||----------------")
print("Nikłe światło księżyca wpadające")
print("przez jakąś kratke w suficie")
print("oświetla mały częściowo zalany")
print("loch. Na wszystkich ścianach")
print("widać pleśń. Z zaskoczeniem")
print("zauważyłeś w promieniach księżyca")
print("lekko lśniący miecz...")
print("----------------||----------------")
print("")
print("Czy bieżesz miecz? tak / nie")
print("")

while True:  #dokończ
    inp = input()
    if inp == "nie":
        print("----------------||----------------")
        print("Wolisz się nie zbliżać do")
        print("podejżanego miecza. Postanawiasz")
        print("ruszyć dalej w ciemności. Po chwili")
        print("marszu na oślep potykasz się o coś")
        print("i upadasz kalecząc się dotkliwie w")
        print(f"ręke twoje hp wynosi {hp - 2}")
        hp -= 2
        break
    elif inp == "tak":    #dokończ
        print("----------------||----------------")
        print("Po podniesieniu miecza poświata")
        print("znika. Zaskoczony patżysz w")
        print("ciemność która jakby zgęstniała.")
        print("Światło księżycz najpierw osłabło")
        print("a potem całkiem znikneło z strachem")
        print("rozglądasz się w okoł. Słyszysz")
        print("jakiś plusk. Coś tu oz tobą jest...")
        print("----------------||----------------")
        eqat.podnies(0)
        print(eqat.ekwipunek)
        #
        #   walka
        #
        break
    else:
        print("zła komenda")
input()
print("")
print("----------------||----------------")
print("Po wszystkim ruszasz dalej w ")
print("ciemny tunel. Nic nie widźąc mijasz")
print("kilka rozgałęzień tunelu. W pewnym")
print("momęcie dostżegarz światło. Z nowym")
print("zapałem ruszasz dalej...")
print("----------------||----------------")

#fabuła_0============================================
