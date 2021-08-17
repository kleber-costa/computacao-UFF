entrada = int(input())
anos = entrada // 365
meses = entrada % 365 // 30
dias = entrada % 365 % 30

print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(anos, meses, dias))