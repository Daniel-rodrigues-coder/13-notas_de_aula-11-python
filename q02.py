lista = []
n = int(input('digite qnt de números: '))
for n in range (n):
    num = int(input("digite os números: "))
    lista.append(num)

    maior = max(lista)
    menor = min(lista)
print(maior, menor)