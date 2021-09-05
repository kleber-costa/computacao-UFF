'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1117

Faça um programa que leia as notas  referentes às duas avaliações de um aluno.
Calcule e  imprima a média semestral. Faça com que o algoritmo só aceite notas
válidas (uma nota válida deve  pertencer ao intervalo [0,10]). Cada  nota deve
ser validada separadamente.

Entrada:
A entrada contém vários valores reais, positivos ou negativos. O programa deve
ser encerrado quando forem lidas duas notas válidas.

Saída:
Se uma nota  inválida for lida, deve ser  impressa a mensagem "nota invalida".
Quando duas notas válidas forem lidas, deve ser impressa a mensagem "media = "
seguido do valor do cálculo. O valor  deve ser apresentado com duas casas após
o ponto decimal.

Exemplo:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
-3.5                                        nota invalida
3.5                                         nota invalida
11.0                                        media = 6.75
10.0
-------------------------------------------------------------------------------
'''

count, soma = 0, 0

while count < 2:
    entrada = float(input())
    if 0 <= entrada <= 10:
        count += 1
        soma += entrada
    else:
        print('nota invalida')

print('media = {:.2f}'.format((soma / 2)))