'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1015

Leia os quatro valores  correspondentes aos eixos 𝑥 e 𝑦 de dois pontos quaisquer
no  plano, 𝑝1 = (𝑥1 , 𝑦1) e 𝑝2 = (𝑥2 , 𝑦2) e  calcule  a  distância  entre  eles,
mostrando 4 casas decimais após a vírgula, segundo a fórmula:

𝑑𝑖𝑠𝑡𝑎𝑛𝑐𝑖𝑎 = √((𝑥2 − 𝑥1)² + (𝑦2 − 𝑦1)²)

Entrada:
A entrada  contém duas  linhas de  dados. A primeira  linha  contém dois valores
de ponto  flutuante, 𝑥1 e 𝑦1 , e a segunda  linha  contém outros dois valores de
ponto flutuante, 𝑥2 e 𝑦2.

Saída:
Calcule e imprima o valor da  distância segundo a fórmula fornecida, com 4 casas
após o ponto decimal.

Exemplos:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
1.0 7.0                                     4.4721
5.0 9.0
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
-2.5 0.4                                    16.1484
12.1 7.3
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
2.5 -0.4                                    16.4575
-12.2 7.0
-------------------------------------------------------------------------------
'''

import math

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

distancia = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

print("%0.4f" % distancia)