n = int(input("Quantos numeros você vai digitar? "))

vet = [0 for x in range(n)]


for i in range(n):
    vet[i] = int(input("Digite um numero: "))

pares = 0
print("\nNumeros pares")
for i in range(n):
    if vet[i] % 2 == 0:
        print(vet[i], end=" ")
        pares = pares + 1

print(f"\n\nQuantidade de pares = {pares}")