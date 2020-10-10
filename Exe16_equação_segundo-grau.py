import math

print("Calculo das raizes de uma equação de 2º grau")
a = float(input("Digite o valor de A: "))
if a == 0:
    print("Essa equação não pode ser do segundo grau,o programa sera encerrado")
else:
    b = float(input("Digite o valor de B: "))
    c = float(input("Digite o valor de C: "))
    delta = math.pow(b,2) - (4*a*c)
    if delta < 0:
        print("A raiz é negativa, logo são soluções complexas, o programa será encerrado")
    elif delta == 0:
        x = -b/(2*a)
        print(f"A equação possui aoenas uma raiz real sendo ela {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / 2*a
        x2 = (-b - math.sqrt(delta)) / 2*a
        print(f"A equação possui duas raizes distintas sendo elas {round(x1,3)} e {round(x2,3)}")