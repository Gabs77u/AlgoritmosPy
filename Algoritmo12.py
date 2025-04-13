# Calcula o gasto total para marcar os frangos
def calcular_gasto_total(frangos):
    return frangos * (4.00 + 3.50 * 2)

# Entrada do número de frangos
numero_frangos = int(input("Número de frangos: "))

# Exibe o gasto total
print(f"Gasto total: R${calcular_gasto_total(numero_frangos):.2f}".replace('.', ','))