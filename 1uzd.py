#Apbrėžiama TekstoSkaiciuokle funkcija, su kintamaisiais: tekstas,
# teigiami, neigiami.
def TekstoSkaiciuokle(tekstas,teigiami,neigiami):
    #Kintaieji yra konvertuojami į string elemntus
    #Norint išvengti įvesties klaidų.
    tekstas = str(tekstas)
    teigiami = str(teigiami)
    neigiami = str(neigiami)
    #Kintamasis skirtas rezultato išveščiai
    balas = 0
    #Ciklas, kuris tikrina teksto raides, rades raides iš Teigiami ar Neigiami sąraš0, jas prideda prie Balas kintamojo.
    for char in tekstas:
        if  char in teigiami:
            balas=balas+1
        if char in neigiami:
            balas=balas-1
#Kadangi ne sąraše ęsantys kintamieji vertinami nuliu, ši funkcija padeda išvengti tuščios įvesties klaidų, jas praleisdama.    
        else:
            continue
    #Išspauzdinamas rezultatas ( Balas ) į konsolę.
    return print(balas)

TekstoSkaiciuokle("keturiolika", "ktur", "ila")