print("Frutaria Samofalov, bem vindo")
print("Disponibilizamos de maças e morangos,de acordo com a tabela a seguir")
print(""" Morango até 5Kg, R$2.50/Kg, acima é R$2.20/kg
 Maças até 5Kg, R$1,80/Kg, acima é R$1.50/Kg""")
print("Tambem damos desconto de 10% se comprar mais de 8Kg em fruta ou o valor total ultrapassar R$25.00")
morango_kilos = float(input("Digite quantos kilos de morango voce vai comprar: "))
maças_kilos = float(input("Digite quantos kilos e mmaça voce vai comprar: "))
PesoTotal = morango_kilos + maças_kilos
if morango_kilos <= 5:
    TotalPagar_morangos = morango_kilos * 2.50
    print(f"Voce comprou {morango_kilos}Kg de morango e vai pagar R${round(TotalPagar_morangos,2)} ")
else:
    TotalPagar_morangos = morango_kilos * 2.20
    print(f"Voce comprou {morango_kilos}Kg de morango e vai pagar R${round(TotalPagar_morangos,2)} ")
if maças_kilos <= 5:
    TotalPagar_maça = maças_kilos * 1.80
    print(f"Voce comprou {maças_kilos}Kg de maça e vai pagar R${round(TotalPagar_maça,2)} ")
else:
    TotalPagar_maça = maças_kilos * 1.50
    print(f"Voce comprou {maças_kilos}Kg de maça e vai pagar R${round(TotalPagar_maça,2)} ")
if PesoTotal > 8 or (TotalPagar_morangos + TotalPagar_maça > 25):
    total_apagar = (TotalPagar_morangos + TotalPagar_maça) - ((TotalPagar_morangos + TotalPagar_maça) * 0.1)
    print(f"voce vai pagar {round(total_apagar,2)} por ter comprado {PesoTotal}Kg em frutas")