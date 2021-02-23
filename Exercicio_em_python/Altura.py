n = int(input("Quantas pessoas serão digitas? "))

nome = [0 for x in range(n)]
idade = [0 for x in range(n)]
altura = [0 for x in range(n)]

for i in range(n):
    print(f"Dados da {i+1}a pessoa: ")
    nome[i] = str(input("Nome: "))
    idade[i] =  int(input("Idade: "))
    altura[i] = float(input("Altura: "))
print()

menores = 0
media = 0
for i in range(n):
    media = media + altura[i] / n
    if idade[i] < 16:
        menores = menores + 1

pcMenores = (float(menores) / n) * 100

print(f"Altura média: {media:.2f}")
print(f"Pessoas com menos de 16 anos: {pcMenores:.1f}% ")

for i in range(n):
    if idade[i] < 16:
        print(nome[i])