# Entrada
# Solicita o peso do prato ao usuário e substitui vírgula por ponto
peso_prato = float(input("Digite o peso do prato em quilos: ").replace(',', '.'))

# Processamento e saída 
# Calcula e exibe o valor a pagar
preco_por_quilo = 12.00  # Preço por quilo em reais
valor_a_pagar = peso_prato * preco_por_quilo
print(f"O valor a pagar é: R${valor_a_pagar:.2f}")