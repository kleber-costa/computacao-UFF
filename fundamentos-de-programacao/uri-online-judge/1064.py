'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1064

Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos.
Na próxima linha, deve-se  mostrar a média de  todos os valores positivos digitados,
com um dígito após o ponto decimal.

Entrada:
A entrada  contém 6 números  que podem ser valores  inteiros ou de ponto  flutuante.
Pelo menos um destes números será positivo.

Saída:
O primeiro valor de saída é a quantidade de valores  positivos. A próxima linha deve
mostrar a média dos valores positivos digitados.

Exemplo:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
7                                           4 valores positivos
-5                                          7.4
6
-3.4
4.6
12
-------------------------------------------------------------------------------
'''

positivos, soma = 0, 0

for i in range(6):
    num = float(input())
    if num > 0:
        positivos += 1
        soma += num

media = soma / positivos
print('{} valores positivos\n{:.1f}'.format(positivos, media))