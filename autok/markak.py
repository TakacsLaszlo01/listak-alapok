markak = ["BMW", "Ferrari", "Volkswagen", "Opel", "Toyota"]

# összes elem soronként
for marka in markak:
    print(marka)

marka = input("Adjon meg egy autómárkát: ")
#listában szerepel-e egy elem
if markak.__contains__(marka):
    print("A megadott márka már szerepel a listában!")
else:
    #lista végére beszúrás
    markak.append(marka)
    print("Sikeresen felvettük a márkát a listába!")

#ömlesztett kiírás
print(markak)

#darabszám
hossz = len(markak)
print(f"Jelenleg {hossz} db márka van a listában.")

#összes elemen végigmegy indexelve
for i in range(0, hossz):
    print(markak[i])

tovabbi_markak = ["Mercedes", "Audi", "Haas",
    "Aston Martin", "Renault"]
#egyik lista elemeinek hozzáadása a másikhoz
markak.extend(tovabbi_markak)
print(markak)

