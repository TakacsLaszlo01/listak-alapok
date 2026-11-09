magassagok = []
magassag = float(input("Adjon meg egy testmagasságot: "))
while magassag != 0:
    if magassag >= 130 and magassag <= 230:
        magassagok.append(magassag)
    else:
        print("A magasság 130 és 230 között lehet!")
    magassag = float(input("Adjon meg egy testmagasságot: "))

atlag = sum(magassagok) / len(magassagok)
kulonbseg = max(magassagok) - min(magassagok)

print(f"Az átlagmagasság {atlag:.1f} cm.")
print(f"A legmagasabb ember {kulonbseg:.1f} cm-rel magasabb a legalacsonyabbnál.")

if 180 in magassagok:
    print("Van 180 centis ember a listában.")