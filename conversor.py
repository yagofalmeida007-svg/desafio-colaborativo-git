print("=== CONVERSOR DE TEMPERATURAS ===")

while True:
    print("6 - Celsius para Fahrenheit")
    print("5 - Fahrenheit para Celsius")
    print("4 - Celsius para Kelvin")
    print("3 - Kelvin para Celsius")
    print("2 - Fahrenheit para Kelvin")
    print("1 - Kelvin para Fahrenheit")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção de 1 a 6 ou 0 para sair: "))

    if opcao == 0:
        print("Programa encerrado.")
        break

    temperatura = float(input("Digite a temperatura: "))

    if opcao == 1:
        resultado = (temperatura * 9 / 5) + 32
        print("Resultado:", resultado, "°F")

    elif opcao == 2:
        resultado = (temperatura - 32) * 5 / 9
        print("Resultado:", resultado, "°C")

    elif opcao == 3:
        resultado = temperatura + 273.15
        print("Resultado:", resultado, "K")

    elif opcao == 4:
        resultado = temperatura - 273.15
        print("Resultado:", resultado, "°C")

    elif opcao == 5:
        resultado = (temperatura - 32) * 5 / 9 + 273.15
        print("Resultado:", resultado, "K")

    elif opcao == 6:
        resultado = (temperatura - 273.15) * 9 / 5 + 32
        print("Resultado:", resultado, "°F")

    else:
        print("Opção inválida.")
