print("Vamos calcular o seu IMC?")

while True:

    try:
        print("Digite sua altura e peso utilizando ponto(.), exemplo: 1.70 de altura.")
        peso = float(input("Digite seu peso:"))
        altura = float(input("Digite sua altura:"))

        if peso <= 0 or altura <=0:
            print("Os numeros precisam ser positivos para fazer o calculo")
            continue

        media = peso / (altura * altura)
        print(f"Seu IMC é {media:.2f}/m2")
        print ("=-=" *10)
        print(f"Avaliando o seu IMC de: {media:.2f} ")
        print("IMC: <18,5kg/m2 ou menos - abaixo do peso")
        print("IMC >18,5 até 24,9kg/m2 - eutrofia (peso adequado)")
        print("IMC ≥25 até 29,9kg/m2 - sobrepeso")
        print("MC >30,0kg/m2 até 34,9kg/m2 - obesidade grau 1")
        print("=-="*10)

        if media <=18.5:
            print("Você esta abaixo do peso, precisa engordar um pouco para estar no peso adequado")

        elif 18.6<= media <=24.9:
            print("Parabêns, você esta no peso adequado")

        elif media >=25.0 <=29.9:
            print("você esta com sobrepeso, melhor se alimentar melhor daqui para frente")

        elif media >30.0:
            print("Você esta com obesidade grau I, precisa se alimentar melhor")

        break



    except ValueError:
        print("Você utilizou caracteres invalidos, tente de novo")






