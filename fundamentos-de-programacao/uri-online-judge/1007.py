'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1007

Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a
diferença do produto de A e B pelo produto de C e D segundo a fórmula:
DIFERENCA = (A * B - C * D).

Entrada:
O arquivo de entrada contém 4 valores inteiros.

Saída:
Imprima a mensagem DIFERENCA com  todas as letras maiúsculas, conforme
exemplo abaixo, com um espaço em branco antes e depois da igualdade.

Exemplo:
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
5                                           DIFERENCA = -26
6
7
8
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
0                                           DIFERENCA = -56
0
7
8
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
5                                              DIFERENCA = 86
6
-7
8
-------------------------------------------------------------------------------
'''

A = int(input())
B = int(input())
C = int(input())
D = int(input())

print("DIFERENCA = %d" % (A * B - C * D))