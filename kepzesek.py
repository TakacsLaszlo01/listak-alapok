kepzesek = ["gimnázium", "pénzügy és számvitel", "rendészet", "logisztika", "informatika és távközlés"]
#a
for kepzes in kepzesek:
    print(kepzes)
#b
kepzesek.insert(1, "nyelvi előkészítő")
#c
print(kepzesek[-4:])
#d
uj_kepzes = input("Adjon meg egy új képzést.")
if uj_kepzes in kepzesek:
    kepzesek.append(uj_kepzes)
else:
    print("Ez már szerepel a listában.")

print(kepzesek)