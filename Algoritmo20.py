# Calculando 10% de desconto
preco = float(input("Digite o preço do produto: ").replace(',', '.'))
novo_preco = preco * 0.90
print("O novo preço com desconto é: R$", str(novo_preco).replace('.', ','))