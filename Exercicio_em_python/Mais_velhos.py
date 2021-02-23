
n = int(input("Quantas pessoas você vai digitar? "))

nomes = [0 for x in range(n)]
idades = [0 for x in range(n)]

for i in range(n):
     print(f"Dados da {i+1}a pessoa: ")
     nomes = str(input("Nome: "))
     idades = int(input("Idade: "))

maiorIdade = idades[0]
maior = 0

for i in range(n):
    if idades[i] > maiorIdade:
        maiorIdade = idades[i]
        maior = i

print(f"Pessoa mais velha: {nomes[maior]}")
