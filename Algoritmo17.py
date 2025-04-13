#Função para calcular a multiplicação de três número
def obter_numero(mensagem):
    return float(input(mensagem).replace(',', '.'))

# Entrada de dados
n1 = obter_numero("Digite o primeiro número: ")
n2 = obter_numero("Digite o segundo número: ")
n3 = obter_numero("Digite o terceiro número: ")

# Processamento e saída
print(f"O resultado da multiplicação é: {str(n1 * n2 * n3).replace('.', ',')}")