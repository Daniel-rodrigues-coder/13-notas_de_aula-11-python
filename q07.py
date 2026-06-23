lista = []
n = int(input('digite qnt de números: '))
for n in range (n):
    num = int(input("digite os números: "))
    lista.append(num)
print(lista)
lista.insert(0,lista.pop(-1))
print(lista)