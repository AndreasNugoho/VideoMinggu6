#Andreas Nugroho 
#71200646
#Helmi sedang kesulitan mencari kata terpendek dan terpanjang dari sebuah kalimat.
#bantulan helmi membuat program percarian kata terpendek dan terpanjang. 

#input
#kalimat(str)

#proses
#pemilahan kata terpanjang dan terpendek (perulangan)

#output
#kata terpanjang dan terpendek

def panjang_pendek(str1):
    kata =""
    semua_kata = []
    str1 = str1 + " "

    for i in range(0, len(str1)):
        if (str1[i] != ' '):
            kata = kata + str1[i]
        else:
            semua_kata.append(kata)
            kata = ""
    terpendek = terpanjang =semua_kata[0]

    for k in range(0, len(semua_kata)):
        if (len(terpendek) > len(semua_kata[k])):
            terpendek = semua_kata[k]
        if (len(terpanjang) < len(semua_kata[k])):
            terpanjang = semua_kata[k]
    return terpendek,terpanjang

str1 = input("Masukkan Kalimat : ")
print ("Kalimat Anda:\n"+str1)
terpendek,terpanjang = panjang_pendek(str1)
print ("Kata Terpendek: "+ terpendek)
print ("Kata Terpanjang: "+ terpanjang)
