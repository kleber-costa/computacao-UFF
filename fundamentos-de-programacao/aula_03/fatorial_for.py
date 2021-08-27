'''
Cálculo fatorial com for
'''

num = int(input("Digite valor inteiro e positivo: "))
fat = 1

for i in range(1, num + 1):
    fat *= i

print("O fatorial de", num, "=", fat)