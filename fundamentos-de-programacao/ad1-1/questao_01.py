
raio = input()
pi = 3.1415

while raio != '':
    raio = int(raio)
    area: float = raio ** 2 * 3.1415
    perimetro: float = 2 * pi * raio
    if raio % 2 != 0:
        print("Área e Perímetro do Círculo de Raio {} são: {:.2f} e {:.2f}".format(raio, area, perimetro))
    else:
        divisores = []
        contador = 1
        while contador <= raio:
            if raio % contador == 0:
                divisores.append(contador)
            contador += 1
        print("Divisores de %d são:" % raio, ' '.join(map(str, divisores)))
    raio = input()