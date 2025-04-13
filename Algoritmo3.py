#Função Paia 
def calcular_litros():
    # Entrada de dados
    preco_litro = float(input("Preço do litro da gasolina: ").replace(',', '.'))
    valor_pagamento = float(input("Valor a ser abastecido (em reais): ").replace(',', '.'))
    
    # Cálculo
    litros = valor_pagamento / preco_litro
    
    # Saída
    print(f"Com R${valor_pagamento:.2f}, você abastece {litros:.2f} litros.")
# Execução
calcular_litros()