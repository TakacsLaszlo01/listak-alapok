print("Hello world!", end="\t")
print("Viszlát világ!")

magassag = 7
szelesseg = 9
for sor in range(magassag):
    for oszlop in range(1, szelesseg):
        n = sor * szelesseg + oszlop
        print(n, end="\t")
    n = (sor + 1) * szelesseg
    print(n)