n = int(input("Quantos numeros você vai digitar? "))

vet = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = int(input("Digite um nuemro: "))


print("Numeros Negativos:")
for i in range(0, n):
    if vet[i] < 0:
        print(vet[i])
