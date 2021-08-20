'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1017

Joaozinho quer  calcular e mostrar a quantidade de litros de combustível gastos
em  uma  viagem, ao  utilizar  um  automóvel  que  faz 12 KM/L. Para  isso, ele
gostaria  que você o auxiliasse  através de um simples programa. Para efetuar o
cálculo,  deve-se  fornecer o  tempo gasto na  viagem (em horas) e a velocidade
média  durante a mesma (em km/h). Assim,  pode-se obter distância percorrida e,
em seguida,  calcular  quantos litros seriam  necessários. Mostre o valor com 3
casas decimais após o ponto.

Entrada:
O arquivo de entrada contém dois inteiros. O primeiro é o tempo gasto na viagem
(em horas) e o segundo é a velocidade média durante a mesma (em km/h).

Saída:
Imprima  a  quantidade de  litros  necessária  para realizar a viagem, com três
dígitos após o ponto decimal.

Exemplos:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
10                                          70.833
85
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
2                                           15.333
92
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
22                                          122.833
67
-------------------------------------------------------------------------------
'''

tempo = int(input())
velocidade = int(input())

print('{:.3f}'.format((velocidade * tempo / 12)))