'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1072

Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que
serão lidos em seguida.

Mostre  quantos  destes  valores X estão  dentro do intervalo [10,20] e quantos
estão fora do intervalo, mostrando essas informações.

Entrada:
A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o
número de casos de teste.

Cada caso de teste a seguir é um valor inteiro X (−10⁷ < X < 10⁷).

Saída:
Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão fora
(out) do intervalo.

Exemplo:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
4                                           2 in
14                                          2 out
123
10
-25
-------------------------------------------------------------------------------
'''

N = int(input())
IN, OUT = 0, 0

if N < 10000:
    for i in range(N):
        num = int(input())
        if 10 <= num <= 20:
            IN += 1
        else:
            OUT += 1

print("{} in\n{} out".format(IN, OUT))