
n = int(input("Quantas pessoas serão digitadas? "))

altura = [0 for x in range(n)]
genero = [0 for x in range(n)]

for i in range(n):
    altura[i] = float(input(f"Altura da {i+1}a pessoa: "))
    genero[i] = str(input(f"Genero da {i+1}a pessoa: "))

menor = altura[0]
maior = altura[0]
for i in range(n):
    if menor > altura[i]:
        menor = altura[i]
    else:
        if maior < altura[i]:
            maior = altura[i]
print(f"Menor altura = {menor:.2f}")
print(f"Maior altura = {maior:.2f}")


mulher = 0
homem = 0
for i in range(n):
    if genero[i] == 'f':
        mulher = mulher + altura[i]
    else:
        homem = homem + 1

media = mulher / n
print(f"Media das alturas das mulheres = {media:.2f}")
print(f"Numero de homens = {homem:}")
