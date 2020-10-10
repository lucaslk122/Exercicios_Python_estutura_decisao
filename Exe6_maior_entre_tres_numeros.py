
num1 = float(input("Digite um numero; "))
num2 = float(input("Digite um numero; "))
num3 = float(input("Digite um numero; "))
maior = max(num1,num2,num3)
print(f"O maior valor é {maior}")

"""
#Outra solução possivel

num1 = float(input("Digite um numero; "))
num2 = float(input("Digite um numero; "))
num3 = float(input("Digite um numero; "))
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
    print(f"O maior numero é {maior}")
if num3 > num1 and num3 > num2:
    maior = num3
    print(f"O maior numero é {maior}")
"""