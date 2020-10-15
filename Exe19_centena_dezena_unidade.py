numero = int(input("Entre com um numero inteiro e menor que 1000: "))
if numero > 1000:
    print("Numero invalido")
else:
    unidade = numero % 10
    numero = (numero - unidade) / 10
    dezena = int(numero % 10)
    numero = (numero - dezena) / 10
    centena = int(numero)
    print(f"{centena} centena(s) , {dezena} dezena(s) e {unidade} unidade(s)")

