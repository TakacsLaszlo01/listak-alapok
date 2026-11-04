tantargyak = []
tantargy = input("Adjon meg egy tantárgyat: ")

while tantargy != "":
    if tantargyak.__contains__(tantargy):
        tantargyak.append(tantargy)
    else:
        print("A megadott tantárgy már szerepel a listában.")
    tantargy = input("Adjon meg egy tantárgyat: ")

tan_atlagok = []
n = len(tantargyak)