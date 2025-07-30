# 2 - Criar um código que registre as notas de alunos e calcular a média da turma.

qtd_alunos = int(input("Informe o número de alunos: "))
soma_notas = 0

for i in range(qtd_alunos):
    nota = float(input(f"Informe a nota do aluno {i + 1}: "))
    soma_notas += nota

media = soma_notas / qtd_alunos
print(f"Média da turma: {media:.2f}")