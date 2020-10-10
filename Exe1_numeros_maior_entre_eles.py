num1 = float(input("Digite um numero: "))
num2 = float(input("Digite um outro numero: "))
if num1 > num2:
    print(f"{num1} é maior que {num2}")
elif num1 < num2:
    print(f"{num2} é maior que {num1}")
else:
    print("Os dois são iguais")