'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1020

Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a
em anos, meses e dias.

Obs.: apenas  para  facilitar  o  cálculo, considere o ano  com  365 dias e um
mês com 30 dias. Nos casos  de teste nunca haverá  uma situação que permite 12
meses  e  alguns  dias, como  360, 363  ou 364. Este é apenas um exercício com
objetivo de testar raciocínio matemático simples.

Entrada:
O arquivo de entrada contém um valor inteiro.

Saída:
Imprima a saída conforme exemplo fornecido.

Exemplos:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
400                                         1 ano(s)
                                            1 mes(es)
                                            5 dia(s)
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
800                                         2 ano(s)
                                            2 mes(es)
                                            10 dia(s)
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
30                                          0 ano(s)
                                            1 mes(es)
                                            0 dia(s)
-------------------------------------------------------------------------------
'''

entrada = int(input())
anos = entrada // 365
meses = entrada % 365 // 30
dias = entrada % 365 % 30

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(anos, meses, dias))