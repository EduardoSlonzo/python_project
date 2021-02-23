n = int(input("Quantos numeros você vai digitar? "))

vet = [0 for x in range(n)]

for i in range(n):
    vet[i] = float(input("Digite um numero: "))

maior = vet[0]

for i in range(n):
    if maior < vet[i]:
        maior = vet[i]
        posi = i

print(f"\nMAIOR VALOR = {maior:.1f}")
print(f"Posição do maior vetor = {posi}")

