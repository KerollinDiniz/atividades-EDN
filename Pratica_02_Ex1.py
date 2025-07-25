# Exercício 01 - Conversor de Moeda
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
# - Valor em reais: R$ 100.00
# - Taxa do dólar: R$ 5.20
# - Taxa do euro: R$ 6.15
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

valor_real = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_em_dolar = valor_real / taxa_dolar
valor_em_euro = valor_real / taxa_euro

print(f"Valor em real: R$ {valor_real:.2f}")
print(f"Convertido em dólar: US$ {valor_em_dolar:.2f}")
print(f"Convertido em euro: € {valor_em_euro:.2f}")