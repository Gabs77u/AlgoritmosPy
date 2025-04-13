# Calcula o total de litros de refrigerante
latas = int(input("Quantidade de latas de 350ml: ").replace(',', '.'))
garrafas_600ml = int(input("Quantidade de garrafas de 600ml: ").replace(',', '.'))
garrafas_2l = int(input("Quantidade de garrafas de 2 litros: ").replace(',', '.'))

# Soma os litros de todas as embalagens
total_litros = latas * 0.35 + garrafas_600ml * 0.6 + garrafas_2l * 2

# Exibe o total de litros
print("Total de litros comprados:", str(total_litros).replace('.', ','))