'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1153

Ler um valor N. Calcular e escrever seu respectivo fatorial.
Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

Entrada:
A entrada contém um valor inteiro N (0 < N < 13).

Saída:
A saída contém um valor inteiro, correspondente ao fatorial de N.

Exemplo:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
4                                           24
-------------------------------------------------------------------------------
'''

N = int(input())
fat = 1

if 0 < N < 13:
    for i in range(1, N + 1):
        fat *= i

print(fat)