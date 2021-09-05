'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1151

A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série
de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à
soma dos 2 anteriores. Escreva um  algoritmo que leia um inteiro N (N < 46) e
mostre os N primeiros números dessa série.

Entrada:
O arquivo de entrada contém um valor inteiro N (0 < N < 46).

Saída:
Os valores devem  ser mostrados  na mesma linha, separados  por um espaço em
branco. Não deve haver espaço após o último valor.

Exemplo:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
5                                           0 1 1 2 3
-------------------------------------------------------------------------------
'''

N = int(input())
anterior, proximo = 0, 0
fibonacci = []

while proximo < N:
    fibonacci.append(str(proximo))
    proximo += anterior
    anterior = proximo - anterior
    if proximo == 0:
        proximo += 1

print(' '.join(fibonacci))