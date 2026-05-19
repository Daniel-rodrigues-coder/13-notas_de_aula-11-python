# Notas de aula de 2026.1.11 - Python - Listas

## Informações gerais

- **Público alvo**: alunos da disciplina de **Introdução a lógica e programação** do curso de [Infoweb](https://diatinf.ifrn.edu.br/cursos/tecnico-em-informatica-para-internet/) na [DIATINF](https://diatinf.ifrn.edu.br/) no [CNAT-IFRN](https://portal.ifrn.edu.br/campus/natalcentral/)
- **Professor**: [L A Minora](https://github.com/leonardo-minora/)
- **Objetivo**:
  1. FIXME

---
## Notas de aula 
### Resumo da [parte 1](./14-Listas-parte_1.pdf)
1. Lista ou vetor
   - Uma lista é um tipo de objeto capaz de armazenar múltiplos valores.
   - Cada valor armazenado pela lista é chamado de elemento, os quais podem ser de qualquer tipo.
   - O tamanho de uma lista é igual à sua quantidade de elementos, o qual pode ser obtido por meio da função len.
2. Índice de listas
   - Os itens (elementos) da lista podem ser acessador individualmente através do seu índice.
   - O índice deve ser um valor inteiro. Consequentemente, variáveis inteiras e valores negativos podem ser utilizados como índices.
   - Índices com valores fora do intervalo geram um erro do tipo IndexError. O intervalo é igual `[-tamanho, (tamanho - 1)]`.
3. Operações na lista
   1. Inserir item
      - `append` adiciona item no final da lista
      - `insert` adiciona item no início da lista
   2. Criar lista com valor repetido
      - `*` para criar uma lista com o mesmo valor em todas as suas posições. Ex: `[1] * 5 # cria uma lista com 5 itens com valor 1`
   3. Copiar lista
      - `lista.copy()` cria uma nova lista com valores idênticos.
   4. Função contém valor `in`
      - `in` verifica se uma lista contém um valor específico. Ex: `valor in lista`.
   5. Inverter lista
      - `lista[::-1]`: cria uma cópia de `lista` com a ordem invertida dos itens. Também aplica a textos.
      - `list(reversed(lista))`: cria uma cópia de `lista` com a ordem invertida dos itens. Com adaptação, também aplica a textos.
      - `lista.reverse()`: inverte a ordem dos itens da `lista`.
2. Instrução `for`
   - Assim como os textos, a instrução `for` pode ser usada para iterar os elementos de uma lista.

### Resumo da [parte 2](/14-Listas-parte_2.pdf)
1. FIXME

### Exemplo de código em python

Exemplo de lista e do uso da função `len`.
```python
a = [1, 2, 3, 4]
b = ['A', 5, 3.8]
c = []
print(len(a)) # 4
print(len(b)) # 3
print(len(c)) # 0
```

Exemplo de `for` para iterar listas e textos.
```python
numeros = [1, 2, 3, 4]
for item in numeros:
   print(item)

texto = "isso é um texto"
for letra in texto:
   print(letra)
```

Acessando itens da lista com índice.
```python
a = ['x', 'y', 'z', 'w']
print(a[0]) # x
print(a[1]) # y
print(a[2]) # z
b = a[3]
print(b)    # w
```

Exemplo de soma de números (itens) de uma lista.
```python
### definindo a lista
numeros = [2, 4, 6]

### solução com while e índices
soma = 0
indice = 0
while indice < len(numeros):
  soma = soma + numeros[indice]
  indice = indice + 1
print(soma)

### solução com for e índices
soma = 0
for indice in range(len(numeros)):
  soma = soma + numeros[indice]
print(soma)

### solução com for sem índices
soma = 0
for numero in numeros:
  soma = soma + numero
print(soma)
```

Imprimindo os elementos de uma lista em ordem inversa.
```python
### definindo a lista
lista = ['x', 'y', 'z', 'w']

### solução com while
tamanho = len(lista) * -1
indice = -1
while indice >= tamanho:
  print(lista[indice])
  indice = indice - 1

# solução com for e range
tamanho = len(lista) * -1
for indice in range(-1, tamanho - 1, -1):
  print(s[indice])

``` 

Operações com lista
```python
# definir a lista
lista = ['A', 'B', 'C']

### adicionar no final
lista.append('D')
print(lista)            # ['A', 'B', 'C', 'D']

### adicionar no início
a.insert(0, '*')
print(lista)            # ['*', 'A', 'B', 'C', 'D']

### adicionar no início
a.insert(2, '*')
print(lista)            # ['*', 'A', '*', 'B', 'C', 'D']

### criar lista com valor repetido
lista_a = [0] * 5
print(lista_a)     	  # [0, 0, 0, 0, 0]
lista_b = [None] * 4  # None representa um valor vazio
print(lista_b)        # [None, None, None, None]

### copiar listas
lista_a = ['x', 'y', 'z']
lista_b = lista_a
lista_c = lista_a.copy()
lista_b[0] = 'W'    # modifica o valor nas listas a e b
print(lista_a)    # ['W', 'y', 'z']
print(lista_b)    # ['W', 'y', 'z']
print(lista_c)    # ['x', 'y', 'z']

### verificar se valor existe em lista
lista_a = [10, 20, 30]
numero = 30
print(5 in lista_a)       # False
print(20 in lista_a)      # True
print(numero in lista_a)  # True

### inverter a ordem dos itens numa lista
### inverter com cópia
nova_lista = lista[::-1]  # fatiamento (slicing) do python
print(nova_lista)  # Saída: ['C', 'B', 'A']
print(lista)       # Saída: ['A', 'B', 'C']

nova_lista = list(reversed(lista)) # usando funções de python
print(nova_lista)  # Saída: ['C', 'B', 'A']
print(lista)       # Saída: ['A', 'B', 'C']

### inverter a própria lista
lista.reverse()
print(lista)  # Saída: ['C', 'B', 'A']

### definindo um texto
texto = 'isso é um texto'
### inverter com fatiamento (slicing)
texto_invertido = texto[::-1]
print(texto)            # saída: 'isso é um texto'
print(texto_invertido)  # saída: 'otxet mu é ossi'
### inverter com funções
texto_invertido = ''.join(list(reversed(texto)))
print(texto)            # saída: 'isso é um texto'
print(texto_invertido)  # saída: 'otxet mu é ossi'
```


---


## Exercícios [Lista de exercícios](/lista.md)

### **Parte 1**
1. Qual é a saída (impressão) do programa abaixo?

```python
L = [51, 8, 31, 11, 1, 56]
i = 2
print(L[0])
print(L[3])
print(L[i])
print(L[i + 1])
print(L[-1])
print(L[-3])
print(L[-i])
print(L[L[4]])
print(L[2] - L[-4])
```

2. Qual é a saída (impressão) do programa abaixo?

```python
ls = [3, 5, 2]
s = 0
for v in ls:
  s = s + v
print(s)
```

3. Qual é a saída (impressão) do programa abaixo?

```python
n = 6
ls = [0] * n
for i in range(n):
  ls[i] = i * 2
print(ls)
```

4. Qual é a saída (impressão) do programa abaixo?

```python
n = 5
ls = []
for i in range(n):
  ls.append(1)
ls[0] = 5
ls[3] = -3
print(ls)
```

5. Qual é a saída (impressão) do programa abaixo?

```python
la = ['A', 'B', 'C']
lb = [4, 2, 3]
for i in range(len(la)):
  print(la[i] * lb[i])
```

6. Escreva uma função que tem uma lista como parâmetro e que retorna a soma dos elementos dessa lista. Escreva pelo menos dois testes da função no programa principal. Use estrutura de laços para percorrer os itens da lista. **Não use a função `sum`**.

| Exemplo de lista | Retorno esperado |
| ---------------- | ---------------- |
| [2, 5, 3]        | 10               |
| [1, 0, 9, 1, 5]  | 16               |

**Resposta**
```python
def somar_lista(L):
  soma = 0
  for i in L:
    soma += i
  return soma

# teste 1
print( somar_lista([2, 5, 3]) )
# teste 2
print( somar_lista([1, 0, 9, 1, 5]) ) 
```


7. Escreva uma função que tem uma lista como parâmetro e que retorna a média aritmética dos elementos dessa lista. Escreva pelo menos dois testes da função no programa principal.

| Exemplo de lista | Retorno esperado |
| ---------------- | ---------------- |
| [4, 5, 3]        | 4.0              |
| [1, 0, 9, 1, 5]  | 3.2              |

**Código a completar**
```python
def calcular_media_aritmetica(lista):
  pass

# teste 1
print( calcular_media_aritmetica([4, 5, 3]) )
# teste 2
print( calcular_media_aritmetica([1, 0, 9, 1, 5]) ) 
```


8. Escreva uma função que tem uma lista como parâmetro e que retorna a soma dos elementos divisíveis por 3. Escreva pelo menos dois testes da função no programa principal.

| Exemplo de lista  | Retorno esperado |
| ----------------- | ---------------- |
| [0, 6, -1, 12, 1] | 18.0             |
| [0, 1, -1, 8]     | 0.0              |

**Código a completar**
```python
def soma_dos_numeros_divisiveis_por_3(lista):
  pass

# teste 1
print( soma_dos_numeros_divisiveis_por_3([0, 6, -1, 12, 1]) )
# teste 2
print( soma_dos_numeros_divisiveis_por_3([0, 1, -1, 8]) ) 
```


9. Escreva uma função que tem uma lista como parâmetro e que retorna uma nova lista contendo os elementos da primeira lista que são divisíveis por 5. Escreva pelo menos dois testes da função no programa principal.

| Exemplo de lista  | Retorno esperado |
| ----------------- | ---------------- |
| [1, 1, 10, 15, 9] | [10, 15]         |
| [9, 1, -1, 8]     | []               |

**Código a completar**
```python
def criar_lista_com_itens_divisiveis_por_5(lista):
  pass

# teste 1
print( criar_lista_com_itens_divisiveis_por_5([1, 1, 10, 15, 9]) )
# teste 2
print( criar_lista_com_itens_divisiveis_por_5([9, 1, -1, 8]) ) 
```


10. Escreva uma função que tem uma lista como parâmetro e que imprime os elementos pares dessa lista com seus respectivos índices. Escreva pelo menos dois testes da função no programa principal.

| Exemplo de lista      | Retorno esperado |
| --------------------- | ---------------- |
| [2, 1, -1, 8]         | <table style="margin: 0; border-collapse: collapse; border: none;"><tbody><tr><th>Elemento</th><th>Índice</th></tr><tr><th>-------</th><th>------</th></tr><tr><td>2</td><td>0</td></tr><tr><td>8</td><td>3</td></tr></tbody></table> |
| [3, 1, -1, 5, 9, 13]  |  |

**Código a completar**
```python
def imprimir_numeros_pares(lista):
  pass

# teste 1
print( imprimir_numeros_pares([2, 1, -1, 8]) )
# teste 2
print( imprimir_numeros_pares([3, 1, -1, 5, 9, 13]) ) 
```


11. Escreva uma função que tem uma lista A como parâmetro e que retorna uma nova lista formada pelos dobros dos elementos de A. Escreva pelo menos dois testes da função no programa principal.

| Exemplo de lista | Retorno esperado |
| ---------------- | ---------------- |
| [2, 1, -1, 8]         | [4, 2, -2, 16]        |
| [3, 1, -1, 5, 9, 13]  | [6, 2, -2, 10, 18,26] |

12. Escreva uma função que tem duas listas A e B como parâmetros e que retorna uma nova lista contendo os elementos presentes tanto em A como em B (interseção). Escreva pelo menos três testes da função no programa principal.

| Exemplo de lista | Retorno esperado |
| ---------------- | ---------------- |
| [2, 1, -1, 8]<br />[0, 2, 5, 6, 9, 1, 3]        | [2, 1] |
| [3, 1, -1, 5, 9, 13]<br />[0, 1, 5, 4, 5, 6, 5] | [1, 5] |
| [2, 4, 6, 8, 10]<br />[1, 3, 5]                 | []     |


### **Parte 1**
1. FIXME