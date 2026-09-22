print("=== CONVERSOR DE TEMPERATURAS ===")
while True:
    print("\n--------------------------------")
    print("6 - Celsius para Fahrenheit")
    print("5 - Fahrenheit para Celsius")
    print("4 - Celsius para Kelvin")
    print("3 - Kelvin para Celsius")
    print("2 - Fahrenheit para Kelvin")
    print("1 - Kelvin para Fahrenheit")
    print("0 - Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 0:
        print("Programa encerrado.")
        break
    if opcao < 1 or opcao > 6:
        print("Opção inválida! Tente novamente.")
        continue
    temperatura = float(input("Digite a temperatura: "))
    if temperatura < 0:
        print("Identificado: número abaixo de zero!")
    if (opcao == 1 or opcao == 3) and temperatura < 0:
        print("Temperatura inválida! Kelvin não pode ser negativa.")
        continue
    if opcao == 1:
        resultado = (temperatura - 273.15) * 9 / 5 + 32
        print(f"Resultado: {resultado:.2f} °F")
    elif opcao == 2:
        resultado = (temperatura - 32) * 5 / 9 + 273.15
        print(f"Resultado: {resultado:.2f} K")
    elif opcao == 3:
        resultado = temperatura - 273.15
        print(f"Resultado: {resultado:.2f} °C")
    elif opcao == 4:
        resultado = temperatura + 273.15
        print(f"Resultado: {resultado:.2f} K")
    elif opcao == 5:
        resultado = (temperatura - 32) * 5 / 9
        print(f"Resultado: {resultado:.2f} °C")
    elif opcao == 6:
        resultado = (temperatura * 9 / 5) + 32
        print(f"Resultado: {resultado:.2f} °F")