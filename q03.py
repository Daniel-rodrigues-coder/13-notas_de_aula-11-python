lista = []
qnt = int(input('digite qnt de números: '))
pares = 0
for qnt in range (qnt):
    num = int(input("digite os números: "))
    lista.append(num)
    if num % 2 == 0:
        pares += 1
print(pares)
