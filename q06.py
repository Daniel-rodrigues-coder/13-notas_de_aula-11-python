lista = []
n = int(input('digite qnt de números: '))
for n in range (n):
    num = int(input("digite os números: "))
    lista.append(num)
print(lista)
lista.append(lista.pop(0))
print(lista)