print("Verificação de uma data")
dia = int(input("Digite o dia no formato dd: "))
mes = int(input("Digite o mês no formato mm: "))
ano = int(input("Digite o dia no formato aaaa: "))
validação = False
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia <= 31 and dia >= 1:
        validação = True
elif mes == 4 or mes ==6 or mes == 9 or mes == 11:
    if dia <=30 and dia >= 1:
        validação = True
elif mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or (ano %400 == 0):
        if dia <= 29 and dia >= 1:
            validação = True
        else:
            validação = False
if (validação):
    print("Data é valida")
else:
    print("Data invalida")

