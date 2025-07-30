# 4 - Criar um código que serve para analisar números digitados pelo usuário, 
# classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.

qtd_pares = 0
qtd_impares = 0

while True:
    entrada = input("Digite um número (ou 'sair' para encerrar): ")

    if entrada.lower() == 'sair':
        break

    numero = int(entrada)

    if numero % 2 == 0:
        qtd_pares += 1
    else:
        qtd_impares += 1

print(f"Quantidade de números pares: {qtd_pares}")
print(f"Quantidade de números ímpares: {qtd_impares}")
