DiaTrabalhos = int(input("Entre com a quantidade de dias trabalhados: "))
HorasTrabalhadas = float(input("Entre com as horas trabalhadas: "))
SalarioBruto = float(round(DiaTrabalhos*HorasTrabalhadas,2))
if SalarioBruto < 900:
    SalarioLiquido = SalarioBruto - (SalarioBruto*0.03)
    print(f"Salario Bruto R${SalarioBruto}")
    print("IR: Isento")
    print(f"FGTS(11%)  R${SalarioBruto*0.11}")
    print(f"Total de descontos R${SalarioBruto*0.03}")
    print(f"Salario liquido R${SalarioLiquido}")
elif SalarioBruto <= 1500:
    ir = SalarioBruto*0.05
    descontoSindicato = SalarioBruto*0.03
    SalarioLiquido = SalarioBruto - descontoSindicato - ir
    print(f"Salario Bruto R${SalarioBruto}")
    print("IR: 5%")
    print(f"FGTS(11%)  R${SalarioBruto*0.11}")
    print(f"Total de descontos R${descontoSindicato + ir}")
    print(f"Salario liquido R${SalarioLiquido}")
elif SalarioBruto <= 2500:
    ir = SalarioBruto*0.1
    descontoSindicato = SalarioBruto*0.03
    SalarioLiquido = SalarioBruto - descontoSindicato - ir
    print(f"Salario Bruto R${SalarioBruto}")
    print("IR: 10%")
    print(f"FGTS(11%)  R${SalarioBruto*0.11}")
    print(f"Total de descontos R${descontoSindicato + ir}")
    print(f"Salario liquido R${SalarioLiquido}")
else:
    ir = SalarioBruto*0.2
    descontoSindicato = SalarioBruto*0.03
    SalarioLiquido = SalarioBruto - descontoSindicato - ir
    print(f"Salario Bruto R${SalarioBruto}")
    print("IR: 20%")
    print(f"FGTS(11%)  R${SalarioBruto*0.11}")
    print(f"Total de descontos R${descontoSindicato + ir}")
    print(f"Salario liquido R${SalarioLiquido}")