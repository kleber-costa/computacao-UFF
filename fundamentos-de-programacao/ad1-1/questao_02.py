
qtd = int(input())
soma, menor, maior = 0, 0, 0

for i in range(qtd):
    entrada = int(input())
    soma += entrada
    if entrada < menor:
        menor = entrada
    if entrada > maior:
        maior = entrada

media: float = soma / qtd
print("\nSoma: {}\nMédia: {:.2f}\nMenor: {}\nMaior: {}".format(soma, media, menor, maior))

