n = int(input("Quantos casos você vai digitar? "))

for i in range(0, n):
    print("Digite tres numeros: ")
    x = float(input())
    y = float(input())
    z = float(input())
    media = (x * 2 + y * 3 + z * 5) /10
    print(f"Media = {media:.1f}")
