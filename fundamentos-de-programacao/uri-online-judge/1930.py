'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1930

Você vai viajar e planeja levar na viagem todos os seus vários equipamentos
eletrônicos: celular, tablet, notebook, ponto de acesso wifi, câmeras, etc,
e sabe  que necessitará  de várias tomadas  de energia para  conectar todos
esses  equipamentos. Você é informado  de que ficará  em um quarto de hotel
que contém apenas uma tomada de energia disponível. Precavido, você comprou
quatro  réguas de tomadas, permitindo assim ligar vários aparelhos na única
tomada do quarto de hotel. Você pode, também, ligar uma régua em outra para
aumentar  ainda mais  o número de tomadas  disponíveis. No entanto, como as
réguas  têm muitas  tomadas, você  resolve escrever um programa que, dado o
número de tomadas em cada régua, determine o número máximo de aparelhos que
podem ser conectados à energia num mesmo instante.

Entrada:
A entrada  consiste de  uma linha com quatro números inteiros, 𝑇1, 𝑇2, 𝑇3 e
𝑇4, indicando o número de tomadas de cada uma das quatro réguas (2 ≤ 𝑇𝑖 ≤ 6)

Saída:
Seu programa deve produzir uma única linha contendo um único número inteiro
, indicando o número máximo de aparelhos que podem ser conectados à energia
num mesmo instante.

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
2 4 3 2                                     8
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
6 6 6 6                                     21
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
2 2 2 2                                     5
-------------------------------------------------------------------------------
'''

t1, t2, t3, t4 = map(int, input().split())

print(t1 + t2 + t3 + t4 - 3)
