#Outra Função Paia
def calcular_ingredientes(qtd_sanduiches):
    # Pesos dos ingredientes em gramas
    peso_queijo, peso_presunto, peso_hamburguer = 50, 50, 100
    return (
        qtd_sanduiches * 2 * peso_queijo / 1000,  # Queijo em kg
        qtd_sanduiches * peso_presunto / 1000,    # Presunto em kg
        qtd_sanduiches * peso_hamburguer / 1000,  # Hambúrguer em kg
    )

# Entrada do usuário
quantidade = int(input("Digite a quantidade de sanduíches a fazer: "))
queijo, presunto, hamburguer = calcular_ingredientes(quantidade)

# Saída dos resultados
print(f"Para fazer {quantidade} sanduíches, será necessário:")
print(f"{queijo:.2f}".replace('.', ',') + f" kg de queijo, " +
      f"{presunto:.2f}".replace('.', ',') + f" kg de presunto e " +
      f"{hamburguer:.2f}".replace('.', ',') + f" kg de carne.")