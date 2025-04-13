# Entrada do salário inicial
salario_inicial = float(input("Digite o salário inicial do funcionário: "))

# Cálculos
salario_com_aumento = salario_inicial * 1.15  # Aumento de 15%
salario_final = salario_com_aumento * 0.92   # Desconto de 8%

# Saída formatada
print(f"Salário inicial: R$ {salario_inicial:,.2f}".replace('.', ','))
print(f"Salário com aumento: R$ {salario_com_aumento:,.2f}".replace('.', ','))
print(f"Salário final: R$ {salario_final:,.2f}".replace('.', ','))