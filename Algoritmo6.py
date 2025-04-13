#Biblioteca
import math

# Calcula a distância entre dois pontos no plano cartesiano
def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Entrada dos valores do primeiro ponto
x1 = float(input("Digite o valor de x1: ").replace(',', '.'))
y1 = float(input("Digite o valor de y1: ").replace(',', '.'))

# Entrada dos valores do segundo ponto
x2 = float(input("Digite o valor de x2: ").replace(',', '.'))
y2 = float(input("Digite o valor de y2: ").replace(',', '.'))

# Cálculo e saída da distância
distancia = calcular_distancia(x1, y1, x2, y2)
print(f"A distância entre os pontos é: {distancia:,.2f}".replace('.', ','))