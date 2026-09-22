print("=== CONVERSOR DE TEMPERATURAS ===")

def verifica_zero_absoluto(temp, unidade_origem):
    """Retorna False se a temperatura for menor que o zero absoluto."""
    if unidade_origem == 'C' and temp < -273.15:
        return False
    elif unidade_origem == 'F' and temp < -459.67:
        return False
    elif unidade_origem == 'K' and temp < 0:
        return False
    return True

while True:
    print("\nMenu de Opções:")
    print("1 - Celsius para Fahrenheit")
    print("2 - Celsius para Kelvin")
    print("3 - Fahrenheit para Celsius")
    print("4 - Fahrenheit para Kelvin")
    print("5 - Kelvin para Celsius")
    print("6 - Kelvin para Fahrenheit")
    print("0 - Sair")

    
    try:
        opcao = int(input("\nEscolha uma opção de 1 a 6 ou 0 para sair: "))
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
        continue

    if opcao == 0:
        print("Programa encerrado.")
        break
    
    if opcao not in [1, 2, 3, 4, 5, 6]:
        print("Erro: Opção inválida. Escolha um número presente no menu.")
        continue

    
    try:
        temperatura = float(input("Digite a temperatura: "))
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um valor numérico.")
        continue

    
    if opcao in [1, 2]:
        unidade = 'C'
    elif opcao in [3, 4]:
        unidade = 'F'
    elif opcao in [5, 6]:
        unidade = 'K'

    
    if not verifica_zero_absoluto(temperatura, unidade):
        print(f"Erro: A temperatura informada ({temperatura} {unidade}) está abaixo do zero absoluto. Tente novamente.")
        continue


    if opcao == 1:
        resultado = (temperatura * 9 / 5) + 32
        print(f"Resultado: {resultado:.2f} °F")
        
    elif opcao == 2:
        resultado = temperatura + 273.15
        print(f"Resultado: {resultado:.2f} K")
        
    elif opcao == 3:
        resultado = (temperatura - 32) * 5 / 9
        print(f"Resultado: {resultado:.2f} °C")
        
    elif opcao == 4:
        resultado = (temperatura - 32) * 5 / 9 + 273.15
        print(f"Resultado: {resultado:.2f} K")
        
    elif opcao == 5:
        resultado = temperatura - 273.15
        print(f"Resultado: {resultado:.2f} °C")
        
    elif opcao == 6:
        resultado = (temperatura - 273.15) * 9 / 5 + 32
        print(f"Resultado: {resultado:.2f} °F")