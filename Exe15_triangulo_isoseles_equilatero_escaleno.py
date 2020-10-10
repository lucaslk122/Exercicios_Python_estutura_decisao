print("Entre com os dados de um trangulo")
lado1 = int(input("Lado 1: "))
lado2 = int(input("Lado 2: "))
lado3 = int(input("Lado 3: "))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print("Triângulo equilatero")
    elif lado1 != lado2 != lado3 != lado1:
        print("Triângulo escaleno")
    else:
        print("Triângulo isósceles")
else:
    print("Os lados não foram um triangulo")