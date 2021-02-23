
N = int(input("Quantos casos de teste serão digitados? "))

totalCoelho = 0
totalSapo = 0
totalRato = 0


for i in range(N):
    cobaias = int(input("Quantidade de cobaias: "))
    tipoCobaia = str(input("Tipo de cobaia: "))

    if tipoCobaia == 'R':
        totalRato = totalRato + cobaias
    elif tipoCobaia == 'C':
        totalCoelho = totalCoelho + cobaias
    else:
        totalSapo = totalSapo + cobaias

totalCobaias = totalCoelho + totalRato + totalSapo
pcCoelho = (float(totalCoelho) / totalCobaias) * 100
pcSapo = (float(totalSapo) / totalCobaias) * 100
pcRato = (float(totalRato) / totalCobaias) * 100

print()
print("RELATORIO FINAL: ")
print(f"Total: {totalCobaias} cobaias")
print(f"Total de coelhos: {totalCoelho}")
print(f"Total de ratos: {totalRato}")
print(f"Total de sapos: {totalSapo}")
print(f"Percentual de coelhos: {pcCoelho:.2f}")
print(f"Percentual de ratos: {pcRato:.2f}")
print(f"Percentual de sapod: {pcSapo:.2f}")
