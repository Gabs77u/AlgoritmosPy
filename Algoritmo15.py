# Calcula a quantidade de água e suco para X litros de refresco

litros_refresco = float(input("Quantidade de refresco desejada (litros): ").replace(',', '.'))

# Cálculo
litros_agua = (litros_refresco * 8) / 10
litros_suco = (litros_refresco * 2) / 10

# Resultado
print(f"Para {litros_refresco:.2f} litros de refresco, será necessário:")
print(f"{litros_agua:.2f} litros de água")
print(f"{litros_suco:.2f} litros de suco")