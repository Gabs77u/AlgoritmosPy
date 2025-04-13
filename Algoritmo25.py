# Entrada dos valores
salario_minimo = float(input("Salário-mínimo: ").replace(',', '.'))
salario_funcionario = float(input("Salário do funcionário: ").replace(',', '.'))

# Cálculo e saída
print("O funcionário ganha {:.2f} salários-mínimos.".format(salario_funcionario / salario_minimo).replace('.', ','))