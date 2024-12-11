row = [] #lista che contiene tutte le colonne delle tabelline
for i in range(10):
    colonna = [] #crea una nuova colonna
    for j in range(10):
        colonna.append((i + 1) * (j + 1)) #aggiunge i numeri alla colonna
    row.append(colonna) #aggiunge la colonna alla matrice

for k in row:
    print(k)

tabellina = int(input("Quale tabellina scegli?"))
index = int(input("Quale numero moltiplica?"))

if (type(tabellina) == int and tabellina > 0 and tabellina <= 10) and (type(index) == int and index > 0 and index <= 10):
    result = row[tabellina - 1][index - 1] #ricava il numero dalle liste
    print(result)
else:
    print("Number is out of range")



