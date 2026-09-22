# Conversor de Temperaturas em Python

## Sobre o projeto

Este projeto é uma versão melhorada de um **Conversor de Temperaturas em Python**. O programa permite realizar conversões entre as escalas **Celsius, Fahrenheit e Kelvin**.

A primeira versão do programa realizava as conversões básicas, porém foram adicionadas melhorias para tornar o sistema mais seguro, organizado e fácil de utilizar.

## Conversões disponíveis

O programa possui 6 opções de conversão:

1. Celsius para Fahrenheit
2. Fahrenheit para Celsius
3. Celsius para Kelvin
4. Kelvin para Celsius
5. Fahrenheit para Kelvin
6. Kelvin para Fahrenheit

## Melhorias realizadas

### 1. Correção da ordem das opções

Na versão anterior, havia uma diferença entre a numeração apresentada no menu e as conversões realizadas pelo código.

A numeração foi reorganizada para que cada opção corresponda corretamente à conversão apresentada ao usuário.

### 2. Tratamento de erros na escolha da opção

Foi adicionado um tratamento para impedir que o programa seja encerrado quando o usuário digitar uma letra ou outro valor inválido.

Foi utilizado o `try/except`:

```python
try:
    opcao = int(input("Escolha uma opção de 1 a 6: "))
except ValueError:
    print("Erro: digite apenas números inteiros de 1 a 6.")
```

Dessa forma, o programa informa o erro e permite que o usuário tente novamente.

### 3. Validação das opções

O programa verifica se a opção escolhida está entre **1 e 6**.

Caso o usuário digite um número fora desse intervalo, uma mensagem de erro é apresentada:

```text
Erro: escolha apenas uma opção entre 1 e 6.
```

### 4. Tratamento de erros na temperatura

Também foi adicionada uma validação para a temperatura digitada.

O programa aceita números inteiros e decimais, como:

```text
25
25.5
-10
-10.5
```

Caso o usuário digite um texto ou valor que não possa ser convertido para número, o programa apresenta uma mensagem de erro.

### 5. Verificação do zero absoluto

Foi adicionada uma verificação para evitar temperaturas fisicamente impossíveis abaixo do **zero absoluto**.

Os limites considerados são:

* Celsius: `-273.15 °C`
* Fahrenheit: `-459.67 °F`
* Kelvin: `0 K`

Por exemplo, uma temperatura abaixo de `0 K` não é aceita pelo programa.

### 6. Uso do `while`

Foi utilizado o comando `while` para permitir que o usuár
