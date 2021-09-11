'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1045

Leia 3 valores de ponto  flutuante, 𝐴, 𝐵 e 𝐶, e ordene-os em ordem decrescente,
de modo  que o lado 𝐴 representa o maior dos  três lados. A seguir, determine o
tipo  de  triângulo  que estes  três lados formam, com base nos seguintes casos,
sempre escrevendo uma mensagem adequada:

Se 𝐴 ≥ 𝐵 + 𝐶, apresente a mensagem: NAO FORMA TRIANGULO;
Se 𝐴² = 𝐵² + 𝐶², apresente a mensagem: TRIANGULO RETANGULO;
Se 𝐴² > 𝐵² + 𝐶², apresente a mensagem: TRIANGULO OBTUSANGULO;
Se 𝐴² < 𝐵² + 𝐶², apresente a mensagem: TRIANGULO ACUTANGULO;
Se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO;
Se apenas  dois  dos  lados  forem  iguais,  apresente  a  mensagem:  TRIANGULO
ISOSCELES.

Entrada:
A entrada  contem  três  valores de ponto flutuante de dupla precisão, na mesma
linha: 𝐴 (0 < 𝐴), 𝐵 (0 < 𝐵) e 𝐶 (0 < 𝐶).

Saída:
Imprima todas as classificações do triângulo especificado na entrada.

Exemplos:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
7.0 5.0 7.0                                 TRIANGULO ACUTANGULO
                                            TRIANGULO ISOSCELES
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
6.0 6.0 10.0                                TRIANGULO OBTUSANGULO
                                            TRIANGULO ISOSCELES
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
5.0 7.0 2.0                                 NAO FORMA TRIANGULO
------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
6.0 8.0 10.0                                TRIANGULO RETANGULO
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

if valor[0] >= valor[1] + valor[2]:
    print("NAO FORMA TRIANGULO")
else:
    if valor[0]**2 == valor[1]**2 + valor[2]**2:
        print("TRIANGULO RETANGULO")
    if valor[0]**2 > valor[1]**2 + valor[2]**2:
        print("TRIANGULO OBTUSANGULO")
    if valor[0]**2 < valor[1]**2 + valor[2]**2:
        print("TRIANGULO ACUTANGULO")
    if valor[0] == valor[1] and valor[1] == valor[2]:
        print("TRIANGULO EQUILATERO")
    if valor[0] == valor[1] and + valor[1] != valor[2] or valor[1] == valor[2] and valor[2] != valor[0]:
        print("TRIANGULO ISOSCELES")
