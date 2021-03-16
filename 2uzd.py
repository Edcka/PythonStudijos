#Sukuriama funkcija saraso filtravimui
def Filtras(sarasas):
#Laikinas kintamasis saraso reiksmem saugoti
    temp = []
#Cinklas kuris i laikina sarasa sudeda reiksmes is saraso, kurios atitinka logine salyga buti tarpe nuo 10-100
    for reiksme in sarasas:
        if reiksme in range(10,100):
            temp.append(reiksme)
        else:
            continue
#Grazinamos reiksmes (Vidurkis, minimumas, maksimumas ir kintamuju sarase suma )
    return (sum(temp)/len(temp)),min(temp), max(temp),  sum(temp)

#Funkcija kviecianti Filtro funkcija kekvienam sarasui, sarasu masyve.
def Filtrasb(sarasas):
    #sukuriamas laikinas masyvas, placeholder
    temp = []
#kekvienam segmentui iskviecia pirma funkcija
    for each in sarasas:
        temp.append(Filtras(each))
    return temp
    
data_list= [[1, 10, 34, 110, 400, 30, 20],[-5, -10, 55, 120, 30], [2, 67, 23, 78, 200],]

print(Filtrasb(data_list))