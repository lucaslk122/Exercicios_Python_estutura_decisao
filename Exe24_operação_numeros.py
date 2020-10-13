
print("A partir das opções a seguir, digite a operação desejada e em seguida, digite os dois numero")
print("""
          [1] Soma
          [2] Subtração
          [3] Divisão
          [4]multiplicação""")
opção = int(input("Digite sua opção: "))
numero1 = float(input("Primeiro numero: "))
numero2 = float(input("Segundo numero: "))
if opção == 1:
    soma = numero1 + numero2
    if soma > 0 :
        print("Numero positivo")
    if soma % 2 == 0:
        print("Numero par")
    if soma == round(soma):
        print("Numero inteiro")
    if soma < 0:
        print("Numero negativo")
    if soma % 2 != 0:
        print("Numero impar")
    if soma != round(soma):
        print("Numero decimal")
elif opção == 2:
    subtração = numero1 - numero2
    if subtração > 0 :
        print("Numero positivo")
    if subtração % 2 == 0:
        print("Numero par")
    if subtração == round(subtração):
        print("Numero inteiro")
    if subtração < 0:
        print("Numero negativo")
    if subtração % 2 != 0:
        print("Numero impar")
    if subtração != round(subtração):
        print("Numero decimal")
elif opção == 3:
    divisão = numero1 / numero2
    if divisão > 0 :
        print("Numero positivo")
    if divisão % 2 == 0:
        print("Numero par")
    if divisão == round(divisão):
        print("Numero inteiro")
    if divisão < 0:
        print("Numero negativo")
    if divisão % 2 != 0:
        print("Numero impar")
    if divisão != round(divisão):
        print("Numero decimal")
elif opção == 4:
    multiplicação = numero1 * numero2
    if multiplicação > 0 :
        print("Numero positivo")
    if multiplicação % 2 == 0:
        print("Numero par")
    if multiplicação == round(multiplicação):
        print("Numero inteiro")
    if multiplicação < 0:
        print("Numero negativo")
    if multiplicação % 2 != 0:
        print("Numero impar")
    if multiplicação != round(multiplicação):
        print("Numero decimal")
else:
    print("Opção invalida, reinicie o programa e forneça uma opção válida")
