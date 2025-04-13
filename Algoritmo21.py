# Entrada de dados
salario_fixo = float(input("Digite o salário fixo do funcionário: ").replace(',', '.'))
vendas = float(input("Digite o valor das vendas do funcionário: ").replace(',', '.'))

# Processamento
comissao = vendas * 0.04
salario_final = salario_fixo + comissao

# Saída de dados
print(f"Comissão: R$ {comissao:.2f}".replace('.', ','))
print(f"Salário final: R$ {salario_final:.2f}".replace('.', ','))