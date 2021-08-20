'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1002

A fórmula  para calcular a área de uma circunferência é:area = π ∙ raio 2.
Considerando para este problema que π = 3,14159. Efetue o cálculo da área,
elevando o valor de raio ao quadrado e multiplicando por π.

Entrada:
A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a
variável raio.

Saída:
Apresentar a mensagem "A=" seguido  pelo valor da variável area, conforme
exemplo  abaixo, com 4 casas  após o ponto decimal. Utilize  variáveis de
dupla precisão (double). Como todos os problemas, não esqueça de imprimir
o fim de linha após o resultado, caso contrário, você receberá
"Presentation Error".

Exemplos:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
2.0                                         A=12.5664
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
100.64                                      A=31819.3103
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
150.0                                       A=70685.7750
-------------------------------------------------------------------------------
'''

raio = float(input())

print("A=%1.4f \n" % (raio ** 2 * 3.14159))
