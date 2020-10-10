num1 = float(input("Numero 1: "))
num2 = float(input("Numero 2: "))
num3 = float(input("Numero 3: "))
numeros = [num1,num2,num3]
lista = sorted(numeros,key=int, reverse=True)
print(lista)