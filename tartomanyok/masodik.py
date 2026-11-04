telepulesek = ["Szolnok", "Jászberény", "Törökszentmiklós", "Mezőtúr", "Karcag", "Tiszafüred"]

# a) feladat
for telepules in telepulesek:
    print(telepules)

# b) feladat - 
uj_telepules = input("Adjon meg egy településnevet: ")
telepulesek.append(uj_telepules)

# c) feladat - beszúrni az utolsó elem elé
telepulesek.insert(-1, "Kunhegyes")
print(telepulesek)

# d-e) feladat - lista bővítése
kiegeszites = ["Jászapáti", "Tiszaföldvár", "Kunszentmárton"]
telepulesek.extend(kiegeszites)

#f) feladat - ömlesztett kiírása egy résztartománynak
print(telepulesek[2:6])