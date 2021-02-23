N = int(input("Quantos casos você vai digitar? "))

for i in range(0, N):
    x = float(input("Entre com  o numerador: "))
    y = float(input("Entre com o denominador: "))

    if y == 0:
        print("Divisão impossivel!")
    else:
        divisao = x / y
        print(f"Divisão = {divisao}")