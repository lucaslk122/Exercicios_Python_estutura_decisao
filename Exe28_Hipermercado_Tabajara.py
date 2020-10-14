print("O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.Confira")
print("""                   Até 5 Kg                cima de 5 Kg
[1]File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
[2]Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
[3]Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg""")
print("Cada cliente pode levar apenas um tipo de carne porem, não há restrição da quantidade")
opção = int(input("Digite a opção da carne desejada: "))
cartão_tabajara = input("Voce possui o cartão tabajara? s/n : ").lower()
if opção == 1:
    filé_duplo = float(input("Digite a quantidade em kg: "))
    if filé_duplo <= 5:
        totalPagar = filé_duplo * 4.90
        if cartão_tabajara == "s":
            desconto = totalPagar - (totalPagar * 0.05)
            print(f"Filé duplo, {filé_duplo}Kg, total a pagar R${round(desconto,2)}, desconto de R${round(totalPagar * 0.05,2)}")
        else:
            print(f"Filé duplo, {filé_duplo}Kg,total a pagar R${round(totalPagar,2)}")
    else:
        totalPagar = filé_duplo * 5.80
        if cartão_tabajara == "s":
            desconto = totalPagar - (totalPagar * 0.05)
            print(f"Filé duplo, {filé_duplo}Kg, toal a pagar R${round(desconto,2)}, desconto de R${round(totalPagar * 0.05,2)}")
        else:
            print(f"Filé duplo, {filé_duplo}Kg,total a pagar R${round(totalPagar,2)}")
elif opção == 2:
    alcatra = float(input("Digite a quantidade em kg: "))
    if alcatra <= 5:
        totalPagar = alcatra * 5.90
        if cartão_tabajara == "s":
            desconto = totalPagar - (totalPagar * 0.05)
            print(f"Alcatra , {alcatra}Kg, total a pagar R${round(desconto,2)}, desconto de R${round(totalPagar * 0.05,2)}")
        else:
            print(f"Alcatra , {alcatra}Kg,total a pagar R${round(totalPagar,2)}")
    else:
        totalPagar = alcatra * 6.80
        if cartão_tabajara == "s":
            desconto = totalPagar - (totalPagar * 0.05)
            print(f"Alcatra , {alcatra}Kg, toal a pagar R${round(desconto,2)}, desconto de R${round(totalPagar * 0.05,2)}")
        else:
            print(f"Alcatra , {alcatra}Kg,total a pagar R${round(totalPagar,2)}")
elif opção == 3:
    Picanha = float(input("Digite a quantidade em kg: "))
    if Picanha <= 5:
        totalPagar = Picanha * 6.90
        if cartão_tabajara == "s":
            desconto = totalPagar - (totalPagar * 0.05)
            print(f"Picanha , {Picanha}Kg, total a pagar R${round(desconto,2)}, desconto de R${round(totalPagar * 0.05,2)}")
        else:
            print(f"Picanha , {Picanha}Kg,total a pagar R${round(totalPagar,2)}")
    else:
        totalPagar = Picanha * 7.80
        if cartão_tabajara == "s":
            desconto = totalPagar - (totalPagar * 0.05)
            print(f"Picanha , {Picanha}Kg, toal a pagar R${round(desconto,2)}, desconto de R${round(totalPagar * 0.05,2)}")
        else:
            print(f"Picanha , {Picanha}Kg,total a pagar R${round(totalPagar,2)}")

