# 4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.

from datetime import datetime

data_nascimento_str = input("Digite sua data de nascimento (formato: DD/MM/AAAA): ")

try:

    data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")

    data_hoje = datetime.now()

    dias_vivo = (data_hoje - data_nascimento).days

    print(f"Você está vivo há aproximadamente {dias_vivo} dias.")

except ValueError:
    print("Data inválida. Use o formato correto: DD/MM/AAAA")