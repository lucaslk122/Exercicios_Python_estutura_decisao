salario = float(input("Entre com o seu salario R$:"))
if salario <= 280:
    reajuste = 20/100
    aumento = salario*reajuste
    NovoSalario = salario + aumento
    print(F"Seu salario era de R${salario} e agora passa a ser de R${NovoSalario},reajuste de {reajuste*100}% , um aumento de R${aumento}")
elif salario < 700:
    reajuste = 15/100
    aumento = salario*reajuste
    NovoSalario = salario + aumento
    print(F"Seu salario era de R${salario} e agora passa a ser de R${NovoSalario},reajuste de {reajuste*100}% ,aumento de  R${aumento}")
elif salario < 1500:
    reajuste = 10/100
    aumento = salario*reajuste
    NovoSalario = salario + aumento
    print(F"Seu salario era de R${salario} e agora passa a ser de R${NovoSalario},reajuste de {reajuste*100}% ,aumento de  R${aumento}")
else:
    reajuste = 5/100
    aumento = salario*reajuste
    NovoSalario = salario + aumento
    print(F"Seu salario era de R${salario} e agora passa a ser de R${NovoSalario},reajuste de {reajuste*100}% ,aumento de  R${aumento}")
