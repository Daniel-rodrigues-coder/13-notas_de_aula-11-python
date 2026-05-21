# Exercícios — Listas em Python

> **Público alvo**: alunos da disciplina de Introdução a Lógica e Programação
> **Objetivo**: praticar o uso de listas para resolver problemas de programação
> **Observação**: questões inspiradas em formatos recorrentes da **OBI (modalidade Programação)**.

---

## Como ler estas questões

Nas provas da OBI, normalmente você recebe:

- um **enunciado** dizendo o que o programa deve fazer;
- uma seção de **entrada**, explicando o que será lido com `input()`;
- uma seção de **saída**, explicando o que deve ser impresso com `print()`;
- um ou mais **exemplos**.

Neste arquivo, cada questão foi reescrita nesse formato e com explicações mais detalhadas para quem está começando.

---

## Nível Fácil (20 questões) — referência: OBI Programação Nível 1

### 1. Soma da fila
Você recebeu uma fila com `N` números inteiros. Seu programa deve somar todos os valores da lista e mostrar o resultado final.
Para resolver, percorra a lista inteira e acumule a soma em uma variável.

**Entrada**
- A primeira linha contém um inteiro `N`, quantidade de elementos da lista.
- A segunda linha contém `N` inteiros separados por espaço.

**Saída**
- Imprima a soma de todos os elementos.

**Exemplo**
```text
Entrada
5
3 1 4 1 5

Saída
14
```

### 2. Maior e menor
Dada uma lista de números inteiros, descubra qual é o menor valor e qual é o maior valor.
A ideia é percorrer a lista comparando os elementos com os melhores valores encontrados até o momento.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima primeiro o menor valor e depois o maior valor, separados por espaço.

**Exemplo**
```text
Entrada
6
8 2 10 -3 7 4

Saída
-3 10
```

### 3. Contagem de pares
Seu programa deve contar quantos números pares existem na lista.
Lembre-se de que um número é par quando o resto da divisão por 2 é igual a 0.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a quantidade de elementos pares.

**Exemplo**
```text
Entrada
7
2 5 8 11 14 7 20

Saída
4
```

### 4. Acima da média
Primeiro calcule a média aritmética dos valores da lista. Depois conte quantos elementos são maiores que essa média.
Essa questão é útil para praticar duas passagens pela lista: uma para somar e outra para contar.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a quantidade de elementos estritamente maiores que a média.

**Exemplo**
```text
Entrada
5
1 2 3 4 10

Saída
1
```

### 5. Inversão simples
Você deve imprimir os elementos da lista na ordem inversa.
O primeiro elemento da saída será o último da entrada, e assim por diante.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a lista invertida, com os elementos separados por espaço.

**Exemplo**
```text
Entrada
4
9 1 7 3

Saída
3 7 1 9
```

### 6. Rotação à esquerda
Faça uma rotação de 1 posição para a esquerda.
Isso significa que o primeiro elemento vai para o final, e todos os outros avançam uma posição para a esquerda.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a lista após a rotação.

**Exemplo**
```text
Entrada
5
10 20 30 40 50

Saída
20 30 40 50 10
```

### 7. Rotação à direita
Faça uma rotação de 1 posição para a direita.
Nesse caso, o último elemento passa a ser o primeiro da lista.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a lista após a rotação.

**Exemplo**
```text
Entrada
5
10 20 30 40 50

Saída
50 10 20 30 40
```

### 8. Presença de valor
Dado um valor `X`, diga se ele aparece ou não na lista.
Se o valor existir em pelo menos uma posição, a resposta é positiva.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.
- A terceira linha contém o valor `X`.

**Saída**
- Imprima `SIM` se `X` estiver na lista e `NÃO` caso contrário.

**Exemplo**
```text
Entrada
6
4 8 1 9 2 7
9

Saída
SIM
```

### 9. Primeira ocorrência
Dado um valor `X`, descubra em qual índice ele aparece pela primeira vez.
Se ele não aparecer na lista, imprima `-1`.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.
- A terceira linha contém `X`.

**Saída**
- Imprima o índice da primeira ocorrência de `X`, ou `-1`.

**Exemplo**
```text
Entrada
7
5 3 8 3 9 3 1
3

Saída
1
```

### 10. Última ocorrência
Agora você deve encontrar a última posição em que `X` aparece na lista.
Se `X` não existir na lista, a saída também deve ser `-1`.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.
- A terceira linha contém `X`.

**Saída**
- Imprima o índice da última ocorrência de `X`, ou `-1`.

**Exemplo**
```text
Entrada
7
5 3 8 3 9 3 1
3

Saída
5
```

### 11. Contagem de X
Conte quantas vezes o valor `X` aparece na lista.
Mesmo que ele apareça muitas vezes, a saída deve ser apenas a quantidade total.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.
- A terceira linha contém `X`.

**Saída**
- Imprima o número de ocorrências de `X`.

**Exemplo**
```text
Entrada
8
2 1 2 3 2 4 5 2
2

Saída
4
```

### 12. Troca de sinal
Crie uma nova lista em que cada valor seja substituído pelo seu oposto.
Ou seja, números positivos viram negativos, negativos viram positivos e zero continua zero.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a nova lista.

**Exemplo**
```text
Entrada
5
3 -2 0 8 -7

Saída
-3 2 0 -8 7
```

### 13. Zerar negativos
Percorra a lista e substitua todos os números negativos por `0`.
Os demais valores devem ser mantidos exatamente como estavam.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a lista após as substituições.

**Exemplo**
```text
Entrada
6
4 -1 7 -8 0 2

Saída
4 0 7 0 0 2
```

### 14. Dobrar pares
Crie uma nova lista em que apenas os números pares sejam multiplicados por 2.
Os números ímpares devem permanecer iguais.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a lista resultante.

**Exemplo**
```text
Entrada
5
2 3 4 5 6

Saída
4 3 8 5 12
```

### 15. Remover repetidos (ordem mantida)
Gere uma nova lista sem elementos repetidos, mas mantendo a ordem da primeira vez em que cada valor apareceu.
Se um número aparecer várias vezes, apenas a primeira ocorrência deve ficar.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a lista sem repetições.

**Exemplo**
```text
Entrada
8
4 2 4 3 2 1 3 5

Saída
4 2 3 1 5
```

### 16. Interseção simples
Você recebeu duas listas `A` e `B`.
Monte uma nova lista contendo os valores que aparecem nas duas listas, sem repetir elementos na resposta.

**Entrada**
- A primeira linha contém `N`, tamanho da lista `A`.
- A segunda linha contém `N` inteiros.
- A terceira linha contém `M`, tamanho da lista `B`.
- A quarta linha contém `M` inteiros.

**Saída**
- Imprima os elementos que aparecem em `A` e `B`, na ordem em que surgem em `A`.
- Se não houver interseção, imprima `VAZIA`.

**Exemplo**
```text
Entrada
5
1 4 2 8 3
6
7 2 9 4 10 2

Saída
4 2
```

### 17. Diferença simples
Dadas duas listas `A` e `B`, imprima os elementos de `A` que não aparecem em `B`.
A ordem dos elementos deve ser a mesma da lista `A`.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém os `N` elementos de `A`.
- A terceira linha contém `M`.
- A quarta linha contém os `M` elementos de `B`.

**Saída**
- Imprima os elementos de `A` que não pertencem a `B`.
- Se nenhum elemento servir, imprima `VAZIA`.

**Exemplo**
```text
Entrada
6
5 2 8 2 1 9
3
2 7 9

Saída
5 8 1
```

### 18. Prefixos acumulados
Construa uma nova lista em que cada posição guarda a soma de todos os elementos desde o início até aquele ponto.
Por exemplo, a terceira posição da nova lista deve guardar a soma dos três primeiros valores da lista original.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a lista de prefixos acumulados.

**Exemplo**
```text
Entrada
5
2 1 3 4 2

Saída
2 3 6 10 12
```

### 19. Maior diferença entre vizinhos
Compare cada elemento com o próximo da lista e calcule a diferença absoluta entre eles.
Seu programa deve informar a maior dessas diferenças.

**Entrada**
- A primeira linha contém `N` (`N >= 2`).
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a maior diferença absoluta entre dois vizinhos consecutivos.

**Exemplo**
```text
Entrada
5
10 3 8 -1 4

Saída
9
```

### 20. Lista palíndroma
Uma lista é chamada de palíndroma quando ela é igual à sua reversa.
Seu programa deve verificar se isso acontece.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima `SIM` se a lista for palíndroma e `NÃO` caso contrário.

**Exemplo**
```text
Entrada
5
1 3 5 3 1

Saída
SIM
```

---

## Nível Médio (30 questões) — referência: OBI Programação Nível 2

### 1. Moda com desempate
A moda é o valor que mais aparece na lista.
Se houver empate entre dois ou mais valores, escolha o menor deles.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a moda da lista.

**Exemplo**
```text
Entrada
8
5 2 5 3 2 2 5 1

Saída
2
```

### 2. Segundo maior distinto
Encontre o segundo maior valor diferente da lista.
Se todos os valores forem iguais, imprima `NÃO EXISTE`.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima o segundo maior valor distinto, ou `NÃO EXISTE`.

**Exemplo**
```text
Entrada
6
4 9 1 9 7 3

Saída
7
```

### 3. Segmento crescente máximo
Percorra a lista e descubra o tamanho do maior trecho contíguo em que cada valor é maior que o anterior.
Os elementos desse trecho precisam estar lado a lado.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima o tamanho do maior segmento estritamente crescente.

**Exemplo**
```text
Entrada
8
1 2 5 3 4 6 7 1

Saída
4
```

### 4. Segmento não decrescente máximo
Agora o trecho pode manter valores iguais ou crescer.
Seu objetivo é encontrar o maior segmento contíguo em que cada elemento seja maior ou igual ao anterior.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima o tamanho do maior segmento não decrescente.

**Exemplo**
```text
Entrada
7
1 2 2 2 1 3 3

Saída
4
```

### 5. Remoção de picos
Um elemento é um pico se for maior que o vizinho da esquerda e maior que o vizinho da direita.
Considere apenas elementos que têm dois vizinhos. Remova todos os picos e imprima a lista restante.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a lista sem os picos.

**Exemplo**
```text
Entrada
7
1 5 2 8 3 4 4

Saída
1 2 3 4 4
```

### 6. Compressão por frequência
Dado um inteiro `K`, cada valor pode aparecer no máximo `K` vezes na lista de saída.
Se um número aparecer mais vezes, mantenha apenas as primeiras `K` ocorrências.

**Entrada**
- A primeira linha contém `N` e `K`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a lista comprimida.

**Exemplo**
```text
Entrada
10 2
3 1 3 3 2 1 1 2 2 2

Saída
3 1 3 2 1 2
```

### 7. Par com soma alvo
Verifique se existem dois elementos diferentes da lista cuja soma seja exatamente `S`.
Você precisa dizer apenas se existe ou não pelo menos um par válido.

**Entrada**
- A primeira linha contém `N` e `S`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima `SIM` se existir tal par e `NÃO` caso contrário.

**Exemplo**
```text
Entrada
6 11
4 7 1 9 2 6

Saída
SIM
```

### 8. Dois índices da soma
Semelhante à questão anterior, mas agora você deve informar os índices de um par `i` e `j`, com `i < j`, cuja soma seja `S`.
Se houver vários pares possíveis, pode imprimir qualquer um deles.

**Entrada**
- A primeira linha contém `N` e `S`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima dois índices `i` e `j`, separados por espaço, ou `-1 -1` se não existir solução.

**Exemplo**
```text
Entrada
5 10
1 4 6 8 2

Saída
1 2
```

### 9. Três valores da soma
Agora a pergunta é se existe uma trinca de elementos diferentes cuja soma seja `S`.
Seu programa não precisa mostrar a trinca, apenas dizer se ela existe.

**Entrada**
- A primeira linha contém `N` e `S`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima `SIM` ou `NÃO`.

**Exemplo**
```text
Entrada
6 12
4 1 7 3 2 9

Saída
SIM
```

### 10. Sublista de soma S
Uma sublista contígua é um trecho formado por elementos consecutivos da lista.
Verifique se existe algum trecho cuja soma seja exatamente `S`.

**Entrada**
- A primeira linha contém `N` e `S`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima `SIM` se existir pelo menos uma sublista contígua com soma `S`, ou `NÃO`.

**Exemplo**
```text
Entrada
7 9
2 1 3 4 2 1 5

Saída
SIM
```

### 11. Quantidade de sublistas com soma S
Agora, em vez de verificar apenas a existência, conte quantas sublistas contíguas possuem soma igual a `S`.

**Entrada**
- A primeira linha contém `N` e `S`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a quantidade de sublistas válidas.

**Exemplo**
```text
Entrada
5 3
1 2 1 1 2

Saída
3
```

### 12. Produto máximo de dois elementos
Escolha dois elementos distintos da lista de forma que o produto entre eles seja o maior possível.
Lembre-se de que dois números negativos também podem gerar um produto grande.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima o maior produto possível.

**Exemplo**
```text
Entrada
5
-10 -3 2 4 5

Saída
30
```

### 13. Diferença mínima absoluta
Entre todos os pares de elementos distintos da lista, encontre a menor diferença absoluta possível.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a menor diferença absoluta.

**Exemplo**
```text
Entrada
6
8 1 5 12 3 9

Saída
1
```

### 14. Mesclagem ordenada
Você receberá duas listas já ordenadas em ordem crescente.
Seu programa deve intercalar os elementos para formar uma única lista também ordenada.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros em ordem crescente.
- A terceira linha contém `M`.
- A quarta linha contém `M` inteiros em ordem crescente.

**Saída**
- Imprima a lista mesclada em ordem crescente.

**Exemplo**
```text
Entrada
4
1 4 7 10
5
2 3 6 8 9

Saída
1 2 3 4 6 7 8 9 10
```

### 15. Junção alternada
Misture os elementos das duas listas alternando um elemento de `A`, depois um de `B`, e assim por diante.
Quando uma lista acabar, acrescente o restante da outra no final.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém os `N` elementos de `A`.
- A terceira linha contém `M`.
- A quarta linha contém os `M` elementos de `B`.

**Saída**
- Imprima a lista resultante.

**Exemplo**
```text
Entrada
3
1 2 3
5
10 20 30 40 50

Saída
1 10 2 20 3 30 40 50
```

### 16. Rotação por K posições
Rotacione circularmente a lista `K` posições para a direita.
Se `K` for maior que `N`, use apenas o efeito equivalente dentro do tamanho da lista.

**Entrada**
- A primeira linha contém `N` e `K`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a lista após a rotação.

**Exemplo**
```text
Entrada
5 7
1 2 3 4 5

Saída
4 5 1 2 3
```

### 17. Eliminação em rodada
Coloque os elementos da lista em fila circular e remova repetidamente cada segundo elemento até sobrar apenas um.
Seu programa deve informar qual valor resta no final.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima o único valor restante.

**Exemplo**
```text
Entrada
5
10 20 30 40 50

Saída
30
```

### 18. Fila de atendimento
Você deve simular uma fila.
Haverá operações de entrada (`ENTRA x`) e saída (`SAI`). Ao final, mostre o estado da fila.

**Entrada**
- A primeira linha contém `Q`, o número de operações.
- Cada uma das próximas `Q` linhas contém uma operação.

**Saída**
- Imprima os elementos restantes na fila, do primeiro para o último.
- Se a fila estiver vazia, imprima `VAZIA`.

**Exemplo**
```text
Entrada
5
ENTRA 7
ENTRA 2
SAI
ENTRA 9
ENTRA 1

Saída
2 9 1
```

### 19. Pontuação acumulada
Uma lista representa ganhos e perdas em sequência.
Para cada prefixo da lista, calcule a soma acumulada e determine o maior saldo já alcançado.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima o maior valor entre todas as somas de prefixos.

**Exemplo**
```text
Entrada
6
3 -1 4 -2 5 -6

Saída
9
```

### 20. Sublista de soma máxima
Entre todas as sublistas contíguas possíveis, encontre a que possui a maior soma total.
Seu programa deve imprimir apenas esse valor máximo.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a maior soma de uma sublista contígua.

**Exemplo**
```text
Entrada
8
-2 1 -3 4 -1 2 1 -5

Saída
6
```

### 21. Janela de tamanho fixo
Dado um tamanho `W`, observe todas as sublistas contíguas de tamanho exatamente `W`.
Seu programa deve descobrir qual delas tem a maior soma.

**Entrada**
- A primeira linha contém `N` e `W`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a maior soma entre todas as janelas de tamanho `W`.

**Exemplo**
```text
Entrada
7 3
2 5 1 8 2 4 3

Saída
15
```

### 22. Empate em votação
Cada número da lista representa um voto para um candidato identificado por um ID inteiro.
Descubra o vencedor. Se houver empate na maior quantidade de votos, imprima `EMPATE`.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros, representando os votos.

**Saída**
- Imprima o ID do vencedor ou `EMPATE`.

**Exemplo**
```text
Entrada
7
3 1 3 2 2 3 2

Saída
EMPATE
```

### 23. Classificação por notas
Cada competidor tem uma nota.
Ordene os competidores por nota decrescente e, em caso de empate, pelo menor índice original.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros, as notas.

**Saída**
- Imprima os índices dos competidores na ordem da classificação.

**Exemplo**
```text
Entrada
5
90 70 90 80 70

Saída
0 2 3 1 4
```

### 24. Inversão parcial
Você deve inverter apenas o trecho da lista entre os índices `L` e `R`, inclusive.
Os demais elementos devem continuar nas mesmas posições.

**Entrada**
- A primeira linha contém `N`, `L` e `R`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a lista após a inversão do trecho.

**Exemplo**
```text
Entrada
6 1 4
10 20 30 40 50 60

Saída
10 50 40 30 20 60
```

### 25. Movimento de bloco
Remova da lista o bloco entre os índices `L` e `R` e insira esse bloco imediatamente após a posição `P`.
Considere que `P` está fora do intervalo removido.

**Entrada**
- A primeira linha contém `N`, `L`, `R` e `P`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a lista resultante.

**Exemplo**
```text
Entrada
7 1 3 5
1 2 3 4 5 6 7

Saída
1 5 6 2 3 4 7
```

### 26. Distância entre repetidos
Se um valor aparece mais de uma vez, a distância entre duas ocorrências pode ser medida pela diferença entre seus índices.
Seu programa deve encontrar a menor distância entre duas ocorrências iguais.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a menor distância.
- Se não houver repetidos, imprima `-1`.

**Exemplo**
```text
Entrada
8
4 7 1 9 4 2 1 8

Saída
4
```

### 27. Verificação de permutação
Determine se a lista é uma permutação dos números de `1` até `N`.
Isso significa que todos esses números aparecem exatamente uma vez.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima `SIM` se for uma permutação de `1` até `N`, ou `NÃO`.

**Exemplo**
```text
Entrada
5
3 1 5 2 4

Saída
SIM
```

### 28. Reconstrução por diferenças
Você conhece o primeiro valor da lista e também as diferenças entre elementos consecutivos.
Com essas informações, reconstrua a lista original.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém o primeiro valor `A[0]`.
- A terceira linha contém `N - 1` inteiros, que representam `A[i] - A[i-1]`.

**Saída**
- Imprima a lista reconstruída.

**Exemplo**
```text
Entrada
5
10
2 -1 4 -3

Saída
10 12 11 15 12
```

### 29. Balanceamento de cargas
Cada posição da lista representa a carga de uma máquina.
Você pode mover uma unidade de carga apenas entre máquinas vizinhas. Descubra o número mínimo de movimentos para deixar todas com a mesma carga. Se isso não for possível, imprima `-1`.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima o número mínimo de movimentos, ou `-1`.

**Exemplo**
```text
Entrada
3
1 0 2

Saída
1
```

### 30. Empacotamento guloso
Você recebeu uma sequência de pesos e uma capacidade máxima `C`.
Percorra a lista na ordem dada, formando grupos consecutivos. Sempre que adicionar o próximo item ultrapassar `C`, comece um novo grupo.

**Entrada**
- A primeira linha contém `N` e `C`.
- A segunda linha contém `N` inteiros, os pesos.

**Saída**
- Imprima a quantidade de grupos formados.

**Exemplo**
```text
Entrada
6 10
2 3 5 4 6 1

Saída
3
```

---

## Nível Difícil (10 questões) — referência: OBI Programação Sênior

### 1. Contagem de inversões
Um par `(i, j)` forma uma inversão quando `i < j` e `A[i] > A[j]`.
Seu programa deve contar quantos pares assim existem na lista.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a quantidade de inversões.

**Exemplo**
```text
Entrada
5
2 4 1 3 5

Saída
3
```

### 2. Maior subsequência crescente (LIS)
Uma subsequência não precisa ser contígua, mas deve manter a ordem original dos elementos.
Descubra o tamanho da maior subsequência estritamente crescente.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima o tamanho da LIS.

**Exemplo**
```text
Entrada
8
10 9 2 5 3 7 101 18

Saída
4
```

### 3. Subsequência bitônica máxima
Uma subsequência bitônica primeiro cresce e depois decresce.
Seu programa deve encontrar o maior tamanho possível de uma subsequência desse tipo.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima o tamanho da maior subsequência bitônica.

**Exemplo**
```text
Entrada
8
1 4 6 8 5 3 2 1

Saída
8
```

### 4. K-ésimo menor em janela
Para cada janela contígua de tamanho `W`, determine qual é o `K`-ésimo menor elemento dentro dessa janela.
Depois imprima as respostas de todas as janelas, na ordem em que elas aparecem.

**Entrada**
- A primeira linha contém `N`, `W` e `K`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima os valores correspondentes a cada janela.

**Exemplo**
```text
Entrada
6 3 2
5 1 4 2 6 3

Saída
4 2 4 3
```

### 5. Mediana deslizante
Em cada janela contígua de tamanho `W`, calcule a mediana.
Considere que `W` será ímpar, de modo que a mediana é o valor central após ordenar os elementos da janela.

**Entrada**
- A primeira linha contém `N` e `W`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a mediana de cada janela.

**Exemplo**
```text
Entrada
7 3
2 1 5 7 2 0 5

Saída
2 5 5 2 2
```

### 6. Soma máxima com restrição de distância
Escolha elementos da lista para maximizar a soma total, mas dois elementos escolhidos não podem estar a menos de `D` posições um do outro.
Seu programa deve imprimir apenas a melhor soma possível.

**Entrada**
- A primeira linha contém `N` e `D`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a soma máxima.

**Exemplo**
```text
Entrada
6 2
5 1 2 10 6 2

Saída
17
```

### 7. Partição em K segmentos
Divida a lista em `K` segmentos contíguos não vazios.
Entre todas as formas de particionar, escolha aquela em que a maior soma entre os segmentos seja a menor possível.

**Entrada**
- A primeira linha contém `N` e `K`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima o menor valor possível para a maior soma de segmento.

**Exemplo**
```text
Entrada
5 2
7 2 5 10 8

Saída
18
```

### 8. Número de sublistas com soma em intervalo [L, R]
Conte quantas sublistas contíguas possuem soma entre `L` e `R`, inclusive.
A soma da sublista deve estar dentro do intervalo dado.

**Entrada**
- A primeira linha contém `N`, `L` e `R`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima a quantidade de sublistas válidas.

**Exemplo**
```text
Entrada
5 3 5
1 2 3 1 1

Saída
6
```

### 9. Atualização e consulta dinâmica
Você receberá uma lista inicial e depois várias operações.
Algumas operações alteram o valor de uma posição, e outras pedem a soma dos elementos em um intervalo.

**Entrada**
- A primeira linha contém `N` e `Q`.
- A segunda linha contém `N` inteiros.
- Cada uma das próximas `Q` linhas contém uma operação no formato:
  - `SET i x` para definir `A[i] = x`
  - `SUM l r` para consultar a soma de `A[l]` até `A[r]`

**Saída**
- Para cada operação `SUM`, imprima uma linha com a resposta.

**Exemplo**
```text
Entrada
5 4
1 2 3 4 5
SUM 1 3
SET 2 10
SUM 1 3
SUM 0 4

Saída
9
16
22
```

### 10. Menor rotação lexicográfica
Considere todas as rotações circulares possíveis da lista.
Seu programa deve informar o índice inicial da rotação que gera a menor lista em ordem lexicográfica.

**Entrada**
- A primeira linha contém `N`.
- A segunda linha contém `N` inteiros.

**Saída**
- Imprima o índice da melhor rotação.

**Exemplo**
```text
Entrada
5
3 4 5 1 2

Saída
3
```

---

Se quiser, posso também transformar estas questões em uma versão com **gabarito resumido**, **dicas por questão** ou **arquivo separado por nível**.
