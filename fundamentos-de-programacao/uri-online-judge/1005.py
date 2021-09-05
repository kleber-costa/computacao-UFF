'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1005

Leia dois valores de ponto  flutuante de dupla  precisão A e B, que correspondem
a 2 notas de  um aluno. A seguir, calcule a  média  do aluno, sabendo que a nota
A tem  peso 3,5 e a nota B  tem peso 7,5 (a soma dos  pesos portanto é 11). Você
deve assumir que cada nota pode ir de 0,0 até 10,0, sempre com uma casa decimal.

Entrada:
A entrada contém 2 valores, um por linha, com uma casa decimal cada um.

Saída:
Calcule e imprima a variável  MEDIA, conforme exemplo abaixo, com 5 dígitos após
o ponto  decimal e com um espaço em branco  antes e depois da igualdade. Utilize
variáveis de dupla  precisão (double) e, como em todos os problemas, não esqueça
de imprimir o fim de linha após o resultado.

Exemplos:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
5.0                                         MEDIA = 6.43182
7.1
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
0.0                                         MEDIA = 4.84091
7.1
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
10.0                                        MEDIA = 10.00000
10.0
-------------------------------------------------------------------------------
'''

num1 = float(input()) * 3.5
num2 = float(input()) * 7.5
MEDIA = (num1 + num2) / 11

print("MEDIA = {:.5f}".format(MEDIA))