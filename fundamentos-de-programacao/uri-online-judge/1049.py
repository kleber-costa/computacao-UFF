'''
https://www.urionlinejudge.com.br/judge/pt/problems/view/1049

Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível
segundo o esquema  abaixo, da esquerda  para a direita. Em seguida  conclua qual
dos animais seguintes foi escolhido, através das três palavras fornecidas.

vertebrado
    ave
        carnivoro   = aguia
        onivoro     = pomba
    mamifero
        onivoro     = homem
        hebivoro    = vaca
invertebrado
    inseto
        hematofago  = pulga
        herbivoro   = lagarta
    anelideo
        hematofago  = sanguessuga
        onivoro     = minhoca

Entrada:
A entrada  contém 3 palavras, uma em  cada linha, necessárias para identificar o
animal segundo a figura acima, com todas as letras minúsculas.

Saída:
Imprima o nome do animal correspondente à entrada fornecida.

Exemplos:

-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
vertebrado                                  homem
mamifero
onivoro
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
vertebrado                                  aguia
ave
carnivoro
-------------------------------------------------------------------------------
Entrada                                     Saída
-------------------------------------------------------------------------------
invertebrado                                minhoca
anelideo
onivoro
-------------------------------------------------------------------------------
'''

entrada1 = input()
entrada2 = input()
entrada3 = input()

if entrada1 == 'vertebrado':
    if entrada2 == 'ave':
        if entrada3 == 'carnivoro':
            print('aguia')
        elif entrada3 == 'onivoro':
            print('pomba')
    elif entrada2 == 'mamifero':
        if entrada3 == 'onivoro':
            print('homem')
        elif entrada3 == 'herbivoro':
            print('vaca')
elif entrada1 == 'invertebrado':
    if entrada2 == 'inseto':
        if entrada3 == 'hematofago':
            print('pulga')
        elif entrada3 == 'herbivoro':
            print('lagarta')
    elif entrada2 == 'anelideo':
        if entrada3 == 'hematofago':
            print('sanguessuga')
        elif entrada3 == 'onivoro':
            print('minhoca')
