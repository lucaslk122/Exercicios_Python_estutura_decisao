turno = input("Qual perido voce estuda? V para vespertino, D para diurno ou N para noturno: ").upper()
if turno == "V":
    print("Boa Tarde")
elif  turno == "D":
    print("Bom dia")
elif turno == "N":
    print("Boav Noite")
else:
    print("Entrada invalida")