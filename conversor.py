```python
print("=== CONVERSOR DE TEMPERATURAS ===")
print("6 - Celsius para Fahrenheit")
print("5 - Fahrenheit para Celsius")
print("4 - Celsius para Kelvin")
print("3 - Kelvin para Celsius")
print("2 - Fahrenheit para Kelvin")
print("1 - Kelvin para Fahrenheit")

opcao = int(input("Escolha uma opção 1 a 6: "))
temperatura = float(input("Digite a temperatura: "))

if opcao == 1:
    resultado = (temperatura * 9 / 5) + 32
    print("Resultado:", round(resultado, 2), "°F")

elif opcao == 2:
    resultado = (temperatura - 32) * 5 / 9
    print("Resultado:", round(resultado, 2), "°C")

elif opcao == 3:
    resultado = temperatura + 273.15
    print("Resultado:", round(resultado, 2), "K")

elif opcao == 4:
    resultado = temperatura - 273.15
    print("Resultado:", round(resultado, 2), "°C")

elif opcao == 5:
    resultado = (temperatura - 32) * 5 / 9 + 273.15
    print("Resultado:", round(resultado, 2), "K")

elif opcao == 6:
    resultado = (temperatura - 273.15) * 9 / 5 + 32
    print("Resultado:", round(resultado, 2), "°F")

else:
    print("Opção inválida.")
```
