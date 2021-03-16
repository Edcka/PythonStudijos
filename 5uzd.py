#Funkcijas teksto apdorojimui
def suspausti(tekstas):
    #Žodynas skirtas sudėti naudojamas raides ir jų pasikartojimo skaičių
    temp={}
    #Rezultato string kintamasis
    result=" "
    #Iteracija per tekstą naudoajnt kekvieną raidę
    for char in tekstas:
        #Jeigu randama pasikartojanti raidė pridedamas vienetas prie jos Value reikšmės saraše
        if char in temp:
            temp[char] = temp[char]+1
        else:
        #Jeigu randama unikali raidė, pridedama į sąrašą, kaip Key value
            temp[char] = 1
    for key, value in temp.items():
        #Sugeneruojamas rezultato String išvedimui į ekraną.
        result += str(key) + str(value)
    #Gražinamas rezultato kintamasis
    return result
tekstas = str(input("Iveskite teksta kompresijai : "))
print(suspausti(tekstas))   