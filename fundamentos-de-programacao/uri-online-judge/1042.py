'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1042

Leia 3 valores  inteiros, todos na mesma  linha, e ordene-os em ordem crescente.
No final, mostre os valores em ordem crescente, uma linha em branco e em seguida
, os valores na sequência como foram lidos.

Entrada:
A entrada contém três números inteiros.

Saída:
Imprima a saída conforme foi especificado.

Exemplos:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
7 21 -14                                    -14
                                            7
                                            21

                                            21
                                            7
                                            -14
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
-14 21 7                                    -14
                                            7
                                            21

                                            21
                                            7
                                            -14
-------------------------------------------------------------------------------
'''

linha = input()
lista = linha.split()
valor = [0] * 3

def converte(valores):
    for ind in range(3):
        valor[ind] = int(valores[ind])

    return valor


def crescente(valores):
    valores.sort()
    for ind in range(3):
        print(valores[ind])

    print()
    return valores


def decrescente(valores):
    count = 2
    while count >= 0:
        print(valores[count])
        count -= 1

    return None


valor = converte(lista)
ordenada = crescente(valor)
decrescente(ordenada)
