print("Bem vindo ao posto de gasolima Samofalov")
print("O preço do Alcool é R$1,90/L e da gasolina é R$ 2,50/L")
print("Damos desconto para o litro de cada combustivel, para alcool, até de 20L é 3% de desconto por litro,acima disso é 5%. A gasolina até 20L é 4% de desconto por litro,acima disso é 6% por litro.")
combutivel = input("Digite A para álcool ou G para gasolina: ").upper()
if combutivel == "A":
    litros = float(input("Quantos litros deseja abastecer? "))
    if litros < 20:
        litros_pagar = litros*1.90 - (litros*0.03)
        print(f"Voce está abastacendo {litros}L de álcool e vai pagar R${round(litros_pagar,2)}")
    else:
        litros_pagar = litros*1.90 - (litros*0.05)
        print(f"Voce está abastacendo {litros}L de álcool e vai pagar R${round(litros_pagar,2)}")
else:
    litros = float(input("Quantos litros deseja abastecer? "))
    if litros < 20:
        litros_pagar = litros*2.50 - (litros*0.04)
        print(f"Voce está abastacendo {litros}L de gasolina e vai pagar R${round(litros_pagar,2)}")
    else:
        litros_pagar = litros*2.50 - (litros*0.06)
        print(f"Voce está abastacendo {litros}L de gasolina e vai pagar R${round(litros_pagar,2)}")