'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1071

Leia 2 valores inteiros 𝑋 e 𝑌. A seguir, calcule e mostre a soma dos números
ímpares entre eles.

Entrada:
A entrada contém dois valores inteiros.

Saída:
O programa  deve  imprimir  um valor  inteiro. Este  valor é a soma dos valores
ímpares que estão entre os valores fornecidos na entrada que deverá caber em um
inteiro.

Exemplos:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
6                                           5
-5
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
15                                          13
12
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
12                                          0
12
-------------------------------------------------------------------------------
'''

x = int(input())
y = int(input())

impar = 0

if x > y:
   temp = x
   x = y
   y = temp

for ind in range(x+1, y):
    if ind % 2 != 0:
        impar += ind

print(impar)