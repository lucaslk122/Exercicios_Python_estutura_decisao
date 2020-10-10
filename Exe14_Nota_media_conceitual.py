nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))
media = (nota1 + nota2)/2
if media < 4:
    print("Conceito E")
    print(f"Suas notas foram {nota1} e {nota2},portanto a média é {media} e voce está REPROVADO")
elif media < 6:
    print("Conceito D")
    print(f"Suas notas foram {nota1} e {nota2},portanto a média é {media} e voce está REPROVADO")
elif media < 7.5:
    print("Conceito C")
    print(f"Suas notas foram {nota1} e {nota2},portanto a média é {media} e voce está APROVADO")
elif media < 9:
    print("Conceito B")
    print(f"Suas notas foram {nota1} e {nota2},portanto a média é {media} e voce está APROVADO")
else:
    print("Conceito A")
    print(f"Suas notas foram {nota1} e {nota2},portanto a média é {media} e voce está APROVADO")

