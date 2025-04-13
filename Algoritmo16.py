# Função para calcular o volume de uma caixa d'água cilíndrica
def calcular_volume(raio, altura):
    return 3.14159 * (raio ** 2) * altura

# Entrada
raio = float(input("Raio da base (m): ").replace(',', '.'))
altura = float(input("Altura (m): ").replace(',', '.'))

# Saída
print(f"Volume: {str(calcular_volume(raio, altura)).replace('.', ',')} m³")