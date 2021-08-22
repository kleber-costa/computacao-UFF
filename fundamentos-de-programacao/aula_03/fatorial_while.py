'''
Cálculo fatorial com while
'''

num = int(input("Digite um valor inteiro e positivo: "))
i = 1
fat = 1

while i <= num:
    fat = fat * i
    i += 1

print("O fatorial de", num, "=", fat)