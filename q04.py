lista = []
media = 0
n = int(input('digite qnt de números: '))
for n in range (n):
    num = int(input("digite os números: "))
    lista.append(num)
med = sum(lista) / len(lista)

print(lista)

for numeros in lista:
    if numeros > med:
        media += 1
print(media)
