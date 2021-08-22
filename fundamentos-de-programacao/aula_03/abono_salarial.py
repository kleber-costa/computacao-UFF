'''
Abono Salarial
'''

salario = float(input("Diga seu salário atual: "))
tempo = int(input("Diga quantos anos completos tem de serviço: "))

if tempo <= 1:
    print("Seu salário se mantém o mesmo: {:.2f}".format(salario))
else:
    if tempo <= 10:
        salario = salario * 1.10
    else:
        salario = salario * 1.25
    print("Seu novo salário, com abono: {:.2f}".format(salario))
