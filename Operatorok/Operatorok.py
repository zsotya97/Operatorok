#Adatok beolvasához az osztály
class Muveletek(object):
    def __init__(self,sor):
        split = sor.split()
        self.szam1=int(split[0])
        self.muvelet=split[1]
        self.szam2=int(split[2])

#6. feladat Metódus
def Szamolas(sor):
    split =sor.split()
    szam1=int(split[0])
    muvelet=split[1]
    szam2=int(split[2])
    try:
        muveletek = ["/", "mod" ,"div", "*", "-", "+" ]
        if  muvelet==muveletek[0]:
            return str(szam1/szam2)
        elif muvelet==muveletek[1]:
            return str(int(szam1/szam2))
        elif muvelet==muveletek[2]:
            return str(int(szam1%szam2))
        elif muvelet==muveletek[3]:
            return str(float(szam1 * szam2))
        elif muvelet==muveletek[4]:
            return str(int(szam1 - szam2))
        elif muvelet==muveletek[5]:
            return str(int(szam1 + szam2))
        else : return "Hibás operátor"
    except:
        return "Egyéb hiba!"


#Adatok beolvasása
Beolvas = open("kifejezesek.txt","r")
lista = []
for x in Beolvas:
    lista.append(Muveletek(x.strip()))
Beolvas.close()

#2. feladat
print("2. feladat: Kifejezések száma: %d" %len(lista))
maradekos = 0
for x in lista:
    if x.muvelet =="mod":
        maradekos+=1

#3. feladat
print(f"3. feladat:Kifejezések maradékos osztással: {maradekos}")


#4. feladat
print("4. feladat:", end=" ")
van = False
for x in lista:
    if(x.szam1%10==0 and x.szam2%10==0): 
        van=True
        break
kivalogatas = []
szoveg = "Van ilyen kifejezés" if van==True else "Nincs ilyen kifejezés"
print(szoveg)


#5. feladat
print("5. feladat: Statisztika")

for x in lista:
    szam = 0
    for y in kivalogatas:
        if(x.muvelet==y):
            szam+=1
    if(szam==0):
        kivalogatas.append(x.muvelet)

for x in kivalogatas:
    szam=0
    for y in lista:
        if y.muvelet ==x:
            szam+=1
    print(f'\t{x} -> {szam} db')

#7. feladat
while True:
    kifejezes = input("7. feladat: kérek egy kifejezést: (pl.: 1 + 1): ")
    if(kifejezes=="vége"): break
    else:
        szam = Szamolas(kifejezes)
        print(f"\t{kifejezes} = {szam}")

#8. feladat    
print("8. feladat: eredmenyek.txt")
kiiras = open("eredmenyek.txt","w",)
for x in lista:
    kifejezes =f"{x.szam1} {x.muvelet} {x.szam2}"
    szam = Szamolas(kifejezes)
    kiiras.write(f"{kifejezes} = {szam}\n")
kiiras.close()
    

    
