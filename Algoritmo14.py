# Entrada de dados
altura_pessoa = float(input("Altura da pessoa (m): ").replace(',', '.'))
sombra_pessoa = float(input("Sombra da pessoa (m): ").replace(',', '.'))
sombra_predio = float(input("Sombra do prédio (m): ").replace(',', '.'))

# Cálculo
altura_predio = (altura_pessoa * sombra_predio) / sombra_pessoa

# Saída
print("Altura do prédio: {:.2f} metros.".format(altura_predio).replace('.', ','))