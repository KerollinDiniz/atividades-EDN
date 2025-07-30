# 3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
# a - deve ter pelo menos 8 caracteres.
# b - deve conter pelo menos um número.

senha = input("Digite sua senha: ")

tem_oito_caracteres = len(senha) >= 8
tem_numero = any(char.isdigit() for char in senha)

if tem_oito_caracteres and tem_numero:
    print("Senha válida.")
else:
    print("Senha inválida. A senha deve ter pelo menos 8 caracteres e conter ao menos um número.")