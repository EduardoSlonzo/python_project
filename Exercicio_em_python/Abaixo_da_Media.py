n = int(input("Quantos elementos vai ter o vetor? "))

vet = [0 for x in range(n)]
soma = 0

for i in range(n):
    vet[i] = float(input("Digite um numero: "))
    soma = soma + vet[i]

media = soma / n
print(f"\nMedia do vetor = {media:.3f}")

print("Elementos abaixo da media: ")
for i in range(n):
    if vet[i] < media:
        print(vet[i])
