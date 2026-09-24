# Conversor de Temperaturas

## Descrição
Programa em Python para converter temperaturas entre as escalas Celsius, Fahrenheit e Kelvin.

## Mudança Realizada

Foi adicionado um **identificador de números abaixo de zero**, sem alterar a estrutura original do código.

### O que foi incluído:

Após a leitura da temperatura informada pelo usuário, o programa agora verifica se o valor é negativo:

```python
if temperatura < 0:
    print("Identificado: número abaixo de zero!")