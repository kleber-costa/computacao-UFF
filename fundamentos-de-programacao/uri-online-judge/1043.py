'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1043

Leia  3  valores  reais (𝐴, 𝐵 e 𝐶) e  verifique  se  eles  formam  ou  não um
triângulo. Em caso  positivo, calcule  o perímetro do  triângulo e apresente a
mensagem: Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem 𝐴 e 𝐵 como base e 𝐶 como
altura, mostrando a mensagem: Area = XX.X

Entrada:
A entrada contém três valores reais, na mesma linha.

Saída:
O resultado deve ser apresentado com uma casa decimal.

Exemplos:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
6.0 4.0 2.0                                 Area = 10.0
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
6.0 4.0 2.1                                 Perimetro = 12.1
-------------------------------------------------------------------------------
'''

linha = input()
lista = linha.split()
valor = [0] * 3

def ocupa(valores):
    for ind in range(len(valores)):
        valor[ind] = float(valores[ind])
    return valor

valor = ocupa(lista)
valor.sort(reverse=True)

if valor[0] < valor[1] + valor[2]:
    P = valor[0] + valor[1] + valor[2]
    print("Perimetro = %1.1f" % P)
else:
    A = ((valor[0] + valor[1]) * valor[2])/2
    print("Area = %1.1f" % A)