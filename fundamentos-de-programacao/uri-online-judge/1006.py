'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1006

Leia 3 valores, no caso, variáveis 𝐴, 𝐵 e 𝐶, que são as três notas de um aluno.
A seguir, calcule a média do  aluno, sabendo que a  nota 𝐴 tem peso 2, a nota 𝐵
tem peso 3 e a nota 𝐶 tem peso 5. Considere que cada nota pode ir de 0 até 10.0
, sempre com uma casa decimal.

Entrada:
A entrada contém três valores com uma casa decimal, de dupla precisão
(double).

Saída:
Imprima a  variável MEDIA  conforme  exemplo abaixo, com 1 dígito  após o ponto
decimal e com um espaço em branco antes e depois da igualdade. Assim como todos
os  problemas, não esqueça de imprimir o fim de linha após o resultado.

Exemplos:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
5.0                                         MEDIA = 6.3
6.0
7.0
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
5.0                                         MEDIA = 9.0
10.0
10.0
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
10.0                                        MEDIA = 7.5
10.0
5.0
-------------------------------------------------------------------------------
'''

A = float(input()) * 2
B = float(input()) * 3
C = float(input()) * 5

media = (A + B + C) / 10

print("MEDIA = %0.1f" % media)