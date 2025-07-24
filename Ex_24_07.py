# Exercício 5 - Verificador de Maioridade
# Crie um programa que verifica se uma pessoa atingiu a maioridade (18 anos ou mais).
# O programa deve solicitar que o usuário digite sua idade e, em seguida,
# exibir uma mensagem apropriada com base na idade informada.

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")