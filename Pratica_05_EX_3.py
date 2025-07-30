# 3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
# a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
# b - Preço final: Determina o novo preço após o desconto.
# c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
# d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.

def calcular_desconto(preco, porcentagem):

    return preco * (porcentagem / 100)

try:
    preco_normal = float(input("Digite o preço do produto (R$): "))
    desconto_percentual = float(input("Digite o percentual de desconto (%): "))

    valor_desconto = calcular_desconto(preco_normal, desconto_percentual)
    preco_final = preco_normal - valor_desconto

    print(f"\nPreço original: R$ {preco_normal:.2f}")
    print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
    print(f"Preço final com desconto: R$ {preco_final:.2f}")

except ValueError:
    print("Por favor, digite valores numéricos válidos.")