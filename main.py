import scripts

#fabułapokuj_wstęp==================================
print("----------------||----------------")
print("Budzisz się gdzieś. Tak to dobry")
print("opis. Nie masz bladego pojęcia")
print("gdzie ty właściwie jesteś...")
print("----------------||----------------")                         

input()

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
        print(f"ręke twoje hp wynosi ")    #zrub coś z tym
        
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
        scripts.podnies(0)
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
print("momęcie dostżegasz światło. Z nowym")
print("zapałem ruszasz dalej...")
print("----------------||----------------")

#fabuła_0============================================

if scripts.next_door() == 'True':
    scripts.walka

if scripts.next_door() == 'True':
    scripts.walka

if scripts.next_door() == 'True':
    scripts.walka
