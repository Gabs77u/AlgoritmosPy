# Função que calcula o valor total arrecadado
def calcular_valor_total(qtd_pequenas, qtd_medias, qtd_grandes):
    preco_pequena, preco_media, preco_grande = 10, 12, 15
    return (qtd_pequenas * preco_pequena) + (qtd_medias * preco_media) + (qtd_grandes * preco_grande)

# Entrada de dados
qtd_pequenas = int(input("Camisetas pequenas: "))
qtd_medias = int(input("Camisetas médias: "))
qtd_grandes = int(input("Camisetas grandes: "))

# Resultado
valor_total = calcular_valor_total(qtd_pequenas, qtd_medias, qtd_grandes)
valor_formatado = f"{valor_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
print(f"Valor total arrecadado: R$ {valor_formatado}")