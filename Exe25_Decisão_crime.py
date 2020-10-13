print("Voce está sob suspeita de um assassinato")
print("Para cada pergunta a seguir, responda 1 para sim ou 0 para não")
pergunta1 = int(input("Telefonou para a vítima? "))
pergunta2 = int(input("Esteve no local do crime? "))
pergunta3 = int(input("Mora perto da vítima? "))
pergunta4 = int(input("Devia algo para a vítima? "))
pergunta5 = int(input("Já trabalhou com a vítima? "))
soma_perguntas = pergunta1 + pergunta2 + pergunta3 + pergunta4 + pergunta5
if soma_perguntas == 5:
    print("Assassino")
elif soma_perguntas == 3 or soma_perguntas == 4:
    print("Cumplice")
elif soma_perguntas == 2:
    print("Suspeito")
else:
    print("Inocente")
