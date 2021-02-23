print("Digite os valores das coordenadas x e y: ")
x = int(input())
y = int(input())

while x != 0 and y != 0:
    if x > 0 and y > 0:
        print("QUADRANTE Q1")
    else:
        if x > 0 and y < 0:
            print("QUADRANTE Q4")
        else:
            if x < 0 and y < 0:
                print("QUADRANTE Q3")
            else:
                print("QUADRANE Q2")

    print("Digite os valores das coordenadas x e y: ")
    x = int(input())
    y = int(input())
