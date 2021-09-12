'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1047

Leia a hora  inicial, minuto inicial, hora  final e minuto final de um jogo. A
seguir  calcule a duração  do jogo. OBS: O jogo tem  duração  mínima de um (1)
minuto e duração máxima de 24 horas.

Entrada:
Quatro números inteiros representando a hora de início e fim do jogo.

Saída:
Mostre a seguinte mensagem:
O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)

Exemplos:

-------------------------------------------------------------------------------
Entrada                                  Saída
-------------------------------------------------------------------------------
7 8 9 10                                 O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)
-------------------------------------------------------------------------------
Entrada                                  Saída
-------------------------------------------------------------------------------
7 7 7 7                                  O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)
-------------------------------------------------------------------------------
Entrada                                  Saída
-------------------------------------------------------------------------------
67 10 8 9                                O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)
-------------------------------------------------------------------------------
'''

linha = input()
lista = linha.split()
valor = [0] * 4


def ocupa(valores):
    for ind in range(len(valores)):
        valor[ind] = int(valores[ind])
    return valor


valor = ocupa(lista)

if valor[2] == valor[0] and valor[3] == valor[1]:
    horas = 24
    minutos = 0
else:
    if valor[2] - valor[0] < 0:
        horas = 24 + (valor[2] - valor[0])
    else:
        horas = valor[2] - valor[0]
    if valor[3] - valor[1] < 0:
        minutos = 60 + (valor[3] - valor[1])
        horas -= 1
    else:
        minutos = valor[3] - valor[1]

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (horas, minutos))