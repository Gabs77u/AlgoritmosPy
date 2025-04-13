# Função para calcular a área de uma pizza
def calcular_area_pizza(raio):
    return 3.14 * (raio ** 2)

# Entrada do usuário: raio da pizza
raio = float(input("Digite o raio da pizza em cm: ").replace(',', '.'))

# Chama a função para calcular a área
area = calcular_area_pizza(raio)

# Exibe o resultado
print(f"A área da pizza é {area:.2f}".replace('.', ',') + " cm²")