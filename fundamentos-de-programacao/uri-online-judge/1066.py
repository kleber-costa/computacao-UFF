'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1066

Leia 5 valores inteiros. A seguir, mostre quantos valores digitados foram pares,
quantos  valores  digitados  foram  ímpares, quantos  valores  digitados  foram
positivos e quantos valores digitados foram negativos.

Entrada:
A entrada contém 5 valores inteiros quaisquer, um por linha.

Saída:
Imprima a mensagem  conforme o exemplo  fornecido, uma  mensagem por linha, não
esquecendo o final de linha após cada uma.

Exemplo:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
-5                                          3 valor(es) par(es)
0                                           2 valor(es) impar(es)
-3                                          1 valor(es) positivo(s)
-4                                          3 valor(es) negativo(s)
12
-------------------------------------------------------------------------------
'''

impares, pares, positivos, negativos = 0, 0, 0, 0

for i in range(5):
    num = int(input())
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)".format(pares,impares, positivos, negativos))