# Solicita ao usuário que insira a temperatura em Celsius
celsius = float(input("Digite a temperatura em Celsius: ").replace(',', '.'))

# Converte a temperatura de Celsius para Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Exibe a temperatura convertida em Fahrenheit
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")