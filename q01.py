lista = []
soma = 0
i = 0
n = int(input("digite a quantidade de números da lista: "))
lista.append(n)
for n in range (n):
    num = int(input("digite os números: "))
    lista.append(num)
    soma += num
print(soma)