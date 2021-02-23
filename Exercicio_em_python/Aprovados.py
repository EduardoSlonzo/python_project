
n = int(input("Quantos alunos serão digitados? "))

nome = [0 for x in range(n)]
nota1 = [0 for x in range(n)]
nota2 = [0 for x in range(n)]

for i in range(n):
    print(f"Digite nome, primeira nota e segunda nota do {i+1}o aluno: ")
    nome = str(input())
    nota1 = float(input())
    nota2 = float(input())

soma = 0
print("Alunos aprovados: ")
for i in range(n):
    soma = soma + nota1[i] + nota2[i]
    media = soma / 2
    if media >= 6:
        print(nome[i])
