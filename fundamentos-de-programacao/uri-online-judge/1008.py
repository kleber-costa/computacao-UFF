'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1008

Escreva um programa  que leia o número  de um funcionário, seu  número de horas
trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário.
A seguir, mostre  o número e o salário do funcionário, com duas casas decimais.

Entrada:
O arquivo  de entrada  contém  2  números  inteiros e 1 número  com duas  casas
decimais, representando o número, quantidade de horas trabalhadas e o valor que
o funcionário recebe por hora trabalhada, respectivamente.

Saída:
Imprima o número e o salário do funcionário, conforme exemplo fornecido, com um
espaço em  branco antes e depois  da igualdade. No caso do salário, também deve
haver um espaço em branco após o $.

Exemplos:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
25                                          NUMBER = 25
100                                         SALARY = U$ 550.00
5.50
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
1                                           NUMBER = 1
200                                         SALARY = U$ 4100.00
20.50
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
6                                           NUMBER = 6
145                                         SALARY = U$ 2254.75
15.55
-------------------------------------------------------------------------------
'''

numero = int(input())
horas = int(input())
valor = float(input())

print("NUMBER = %d" % numero)
print("SALARY = U$ %0.2f" % (horas * valor))