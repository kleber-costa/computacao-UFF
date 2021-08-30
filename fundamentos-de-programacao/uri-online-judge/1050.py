'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1050

Leia um número inteiro que representa um código de DDD para discagem interurbana.
Em seguida, informe à qual  cidade o DDD pertence, considerando a tabela abaixo:

==============================
+    DDD     DESTINATION     +
------------------------------
+    61      Brasilia        +
-----------------------------
+    71      Salvador        +
------------------------------
+    11      Sao Paulo       +
------------------------------
+    21      Rio de Janeiro  +
------------------------------
+    32      Juiz de Fora    +
------------------------------
+    19      Campinas        +
------------------------------
+    27      Vitoria         +
------------------------------
+    31      Belo horizonte  +
==============================

Se a entrada for  qualquer outro DDD que  não esteja  presente na tabela acima, o
programa deverá informar:

DDD nao cadastrado

Entrada:
A entrada consiste de um único valor inteiro.

Saída:
Imprima o nome da cidade correspondente ao DDD existente na entrada. Imprima DDD
nao cadastrado caso não existir DDD correspondente ao número digitado.

Exemplos:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
11                                          Sao Paulo
-------------------------------------------------------------------------------
'''

entrada = input()

if entrada == '61':
    print('Brasilia')
elif entrada == '71':
    print('Salvador')
elif entrada == '11':
    print('Sao Paulo')
elif entrada == '21':
    print('Rio de Janeiro')
elif entrada == '32':
    print('Juiz de Fora')
elif entrada == '19':
    print('Campinas')
elif entrada == '27':
    print('Vitoria')
elif entrada == '31':
    print('Belo Horizonte')
else:
    print('DDD nao cadastrado')
