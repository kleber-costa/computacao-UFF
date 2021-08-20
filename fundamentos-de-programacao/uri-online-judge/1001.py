'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1001

Leia 2 valores inteiros  e armazene-os nas variáveis 𝐴 e 𝐵. Efetue a soma de 𝐴
e  𝐵  atribuindo o seu  resultado na  variável 𝑋. Imprima  𝑋 conforme  exemplo
apresentado abaixo. Não  apresente  mensagem alguma além daquilo que está sendo
especificado e não esqueça de imprimir a quebra de linha após o resultado.

Entrada:
A entrada contém dois valores inteiros.

Saída:
Imprima o  conteúdo da  variável 𝑋  conforme exemplo  abaixo, com  um espaço em
branco  antes e  depois da igualdade.  Obs: O X está em maiúsculo e deve ter um
espaço antes e um espaço depois do sinal de igualdade.

Exemplos:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
10                                          X = 19
9
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
-10                                         X = -6
4
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
15                                          X = 8
-7
-------------------------------------------------------------------------------
'''

a = int(input())
b = int(input())

x = a + b

print("X =", x)