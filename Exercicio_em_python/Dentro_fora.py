
N = int(input("Quantos numeros você vai digitar? "))
dentro = 0
fora = 0

for i in range(0, N):
    x = int(input("Digite um nuemro: "))
    if x >= 10 and x <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1

print(f"{dentro} Dentro")
print(f"{fora} Fora")
