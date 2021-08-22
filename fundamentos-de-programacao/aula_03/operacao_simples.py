'''
Calcular operação simples
'''

valores = input("Entre com dois inteiros positivos: ").split()
x = int(valores[0])
y = int(valores[1])
print("Informe o operador:\n(+)\t\tAdição\n(-)\t\tSubtração\n(*)\t\tMultiplicação\n(//)\tDivisão inteira\n(/)\t\tDivisão\n(%)\t\tMódulo\n(**)\tPotenciação")
op = input("Operador: ")

if op == "+":
    resultado = x + y
elif op == "-":
    resultado = x - y
elif op == "*":
    resultado = x * y
elif op == "//":
    resultado = x // y
elif op == "/":
    resultado = x / y
elif op == "**":
    resultado = x ** y
elif op == "%":
    resultado = x % y
else:
    resultado = None

if resultado == None:
    print(op, ": Operador inexistente!!")
else:
    print(x, op, y, "=", resultado)