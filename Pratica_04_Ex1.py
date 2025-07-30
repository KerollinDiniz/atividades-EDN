# 1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).

n1 = float(input("Informe o primeiro número: "))
operador = input("Informe o operador (+, -, *, /): ")
n2 = float(input("Informe o segundo número: "))

if operador == "+":
    resultado = n1 + n2
elif operador == "-":
    resultado = n1 - n2
elif operador == "*":
    resultado = n1 * n2
elif operador == "/":
    if n2 != 0:
        resultado = n1 / n2
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Operador inválido"

print(f"Resultado: {resultado}")