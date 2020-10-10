prod1 = float(input("Valor do primeiro produto: "))
prod2 = float(input("Valor do segundo produto: "))
prod3 = float(input("Valor do terceiro produto: "))
menor = prod1
if prod2 < prod1 and prod2 < prod3:
    menor = prod2
    print(f"Voce deve comprar o produto 2")
elif prod3 < prod1 and prod3 < prod2:
    menor = prod3
    print(f"Voce deve comprar o produto 3")
else:
    print(f"Voce deve comprar o produto 1")