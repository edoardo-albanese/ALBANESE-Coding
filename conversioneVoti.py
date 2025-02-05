num = input("Inserisci il voto: ")
did_cast = false

try:
    float(num)
    did_cast = true
except ValueError:
    print("Inserire il numero a cifre")

if did_cast:
    if num <= 100 and num ≥ 90:
        print("A")
    elif num ≥ 80:
        print("B")
    elif num ≥ 70:
        print("C")
    elif num ≥ 60:
        print("D")
    elif num ≥ 0:
        print("F")
    else:
        print("Il numero è fuori dal range 0-100")