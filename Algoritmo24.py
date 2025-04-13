# Entrada de dados
base_maior = float(input("Base maior: ").replace(',', '.'))
base_menor = float(input("Base menor: ").replace(',', '.'))
altura = float(input("Altura: ").replace(',', '.'))

# Cálculo da área usando a fórmula
area = ((base_maior + base_menor) * altura) / 2

# Exibição do resultado
print("Área: {:.2f}".format(area).replace('.', ','))