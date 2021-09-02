'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1073

Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1
até N, inclusive N, se for o caso.

Entrada:
A entrada contém um valor inteiro N (5 < N < 2000).

Saída:
Imprima o quadrado  de cada um dos valores pares, de 1 até N, conforme o exemplo
abaixo.

Tome cuidado! Algumas  linguagens tem por padrão  apresentarem como saída 1e+006
ao invés de 1000000  o que ocasionará  resposta errada. Neste  caso, configure a
precisão adequadamente para que isso não ocorra.

Exemplo:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
6                                           2^2 = 4
                                            4^2 = 16
                                            6^2 = 36
-------------------------------------------------------------------------------
'''

N = int(input())

if 5 < N < 2000:
    for i in range(1, N+1):
        if i % 2 == 0:
            pot = i ** 2
            print("{}^2 = {}".format(i, pot))
