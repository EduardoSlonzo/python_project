
n = int(input("Quantos elementos vai ter o verto? "))

vet = [0 for x in range(n)]

for i in range(n):
    vet[i] = int(input("Digite um numero: "))

soma = 0
pares = 0
for i in range(n):
    if vet[i] % 2 == 0:
        soma = soma + vet[i]
        pares = pares + 1

if pares == 0:
    print("NENHUM NUMERO PAR")
else:
    media = soma / pares
    print(f"Media dos pares = {media}")
