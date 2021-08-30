'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1059

Faça um programa que mostre os números pares entre 1 e 100, inclusive.

Entrada:
Neste problema extremamente simples de repetição não há entrada.

Saída:
Imprima  todos os números  pares entre 1 e 100, inclusive  se for o caso, um em
cada linha.

Exemplo:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
                                            2
                                            4
                                            6
                                            ...
                                            100
-------------------------------------------------------------------------------
'''

for num in range(1, 101):
    if num % 2 == 0:
        print(num)