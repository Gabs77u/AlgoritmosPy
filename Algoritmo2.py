# Preços
preco_pao, preco_broa = 0.12, 1.50

# Entrada
quantidade_paes = int(input("Digite a quantidade de pães vendidos: ").replace(',', '.'))
quantidade_broas = int(input("Digite a quantidade de broas vendidas: ").replace(',', '.'))

# Cálculos
total_arrecadado = quantidade_paes * preco_pao + quantidade_broas * preco_broa
valor_poupanca = total_arrecadado * 0.10

# Saída
print(f"Total arrecadado: R$ {total_arrecadado:,.2f}".replace('.', ','))
print(f"Valor a ser guardado na poupança: R$ {valor_poupanca:,.2f}".replace('.', ','))