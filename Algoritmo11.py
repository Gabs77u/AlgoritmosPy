# Função para calcular o salário bruto com base nas horas trabalhadas
def calcular_salario_bruto(horas_normais, horas_extras):
    return (horas_normais * 10) + (horas_extras * 15)

# Aplica desconto de 10% para calcular o salário líquido
def calcular_salario_liquido(salario_bruto):
    return salario_bruto * 0.9

# Entrada de dados do usuário
horas_normais = int(input("Horas normais trabalhadas: ").replace(',', '.'))
horas_extras = int(input("Horas extras trabalhadas: ").replace(',', '.'))

# Cálculo dos salários
salario_bruto = calcular_salario_bruto(horas_normais, horas_extras)
salario_liquido = calcular_salario_liquido(salario_bruto)

# Exibição dos resultados
print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"Salário Líquido: R${salario_liquido:.2f}")