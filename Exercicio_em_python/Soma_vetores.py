n = int(input("Quantos valores vai ter cada vetor? "))

a = [0 for x in range(n)]
b = [0 for x in range(n)]
c = [0 for x in range(n)]

print("Digite os valores do vetor A:")
for i in range(n):
    a[i] = int(input())

print("Digite os valores do vetor B: ")
for i in range(n):
    b[i] = int(input())

print("Vetor Resultante: ")
for i in range(n):
    c[i] = a[i] + b[i]
    print(c[i])
