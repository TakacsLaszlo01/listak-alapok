elemek = [8, "macska", False, 3.14]
print(elemek)

print(elemek[0])
hossz = len(elemek)
print(f"A lista {hossz} elemből áll.")

print(elemek[len(elemek)-1])
print(elemek[-1])

print()
for elem in elemek:
    print(elem)

szamok = [9, -3, 6.7, 13, -10, 100, -576]
#Összes negatív szám kiírása.
print("Az összes negatív szám: ")
for szam in szamok:
    if szam < 0:
        print(szam)

tartomany = szamok[1:5]
print(tartomany)

tartomany = szamok[0 : len(szamok) : 2]
print(tartomany)