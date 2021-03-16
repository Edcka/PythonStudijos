#Kintamasis ima duomenis is konsoleje ivestu rodmenu
tekstas = input("Iveskite raidžių seką:")
#Kintamasis ima duomenis is konsoleje ivestu rodmenu, privalo buti skaicius
daliklis = int(input("Iveskite dalikli:"))
#Tikrinama ar ivesti duomenys atitinka uzduoties reikalavimus
if(0 > daliklis and len(tekstas)%daliklis!=0):
   print("Arba raidžių seka nėra dali iš " + daliklis + " arba duotas daliklis netinkamas")
else:
    #Laikinas sarasas kaupti kintamuosius is teksto
    temp = []
    #Kitanamasis skirtas sekti isimamus duomenis is teksto kintamojo
    skaiciuoklis = 0
    #Nesikeiciantis kintamasis, skirtas iteracijai
    konstanta = daliklis
    while(daliklis <=len(tekstas)):
        for i in range(skaiciuoklis, daliklis) :
            temp.append(tekstas[i])
        #Formatuojamas rezultatas
        rezultatas = list(dict.fromkeys(temp))
        #Isvedamas rezultatas
        print (''.join(rezultatas))
        skaiciuoklis += konstanta
        daliklis+=konstanta
    #Išvalomas laikinas masyvas
        temp.clear()
    