'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1133

Escreva  um programa que  leia 2 valores X e Y e que imprima  todos os valores
entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.

Entrada:
O arquivo  de  entrada  contém  2 valores  positivos  inteiros  quaisquer, não
necessariamente em ordem crescente.

Saída:
Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente.

Exemplo:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
10                                          12
18                                          13
                                            17
-------------------------------------------------------------------------------
'''

valor1 = int(input())
valor2 = int(input())

for i in range(valor1, valor2):
    if i % 5 == 2:
        print(i)
    elif i % 5 == 3:
        print(i)