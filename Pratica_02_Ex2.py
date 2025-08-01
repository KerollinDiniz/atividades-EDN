# Exercício 2 - Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja.
# Use as seguintes informações:
# - Nome do produto: "Camiseta"
# - Preço original: R$ 50.00
# - Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

nome_produto = "Camiseta"
preco_original = 50.00
desconto_percentual = 20  # em %

valor_desconto = preco_original * (desconto_percentual / 100)
preco_final = preco_original - valor_desconto

print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {desconto_percentual}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final com desconto: R$ {preco_final:.2f}")