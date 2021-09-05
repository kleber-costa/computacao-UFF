'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1018
Leia  um  valor inteiro. A seguir,  calcule o menor  número de  notas  possíveis
(cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100,
50,  20,  10,  5,  2  e  1. A seguir, mostre o VALOR  LIDO e a relação  de notas
necessárias.

Entrada:
A entrada contém um valor inteiro N (0 < N < 1000000).

Saída:
Imprima  o  valor lido e, em seguida, a quantidade mínima de notas de cada tipo
necessárias, conforme  o exemplo  fornecido. Não  esqueça  de imprimir o fim de
linha após cada linha.

Exemplos:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
576                                         576
                                            5 nota(s) de R$ 100,00
                                            1 nota(s) de R$ 50,00
                                            1 nota(s) de R$ 20,00
                                            0 nota(s) de R$ 10,00
                                            1 nota(s) de R$ 5,00
                                            0 nota(s) de R$ 2,00
                                            1 nota(s) de R$ 1,00
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
11257                                       11257
                                            112 nota(s) de R$ 100,00
                                            1 nota(s) de R$ 50,00
                                            0 nota(s) de R$ 20,00
                                            0 nota(s) de R$ 10,00
                                            1 nota(s) de R$ 5,00
                                            1 nota(s) de R$ 2,00
                                            0 nota(s) de R$ 1,00
-------------------------------------------------------------------------------
'''

valor = int(input())
print(valor)

def div(entrada, divisao):
    inteiro = entrada // divisao
    print("{} nota(s) de R$ {},00".format(inteiro, divisao))
    resto = entrada % divisao
    return resto

cem = div(valor, 100)
cinquenta = div(cem, 50)
vinte = div(cinquenta, 20)
dez = div(vinte, 10)
cinco = div(dez, 5)
dois = div(cinco, 2)
um = div(dois, 1)

