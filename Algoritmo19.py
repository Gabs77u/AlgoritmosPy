#Função para calcular a média ponderada
def calcular_media_ponderada(nota1, nota2):
    return (nota1 * 2 + nota2 * 3) / 5

# Entrada das notas
nota1 = float(input("Digite a primeira nota: ").replace(',', '.'))
nota2 = float(input("Digite a segunda nota: ").replace(',', '.'))

# Cálculo da média
media = calcular_media_ponderada(nota1, nota2)

# Exibe o resultado
print("A média ponderada é: {}".format(str(media).replace('.', ',')))