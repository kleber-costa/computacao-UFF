'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1157

Ler um número inteiro N e calcular todos os seus divisores.

Entrada:
A entrada contém um valor inteiro.

Saída:
Escreva todos os divisores de N, um valor por linha.

Exemplo:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
6                                           1
                                            2
                                            3
                                            6
-------------------------------------------------------------------------------
'''

N = int(input())

for i in range(1, N+1):
    if N % i == 0:
        print(i)