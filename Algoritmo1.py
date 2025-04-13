# Entrada de dados
quantidade_cavalos = input("Digite a quantidade de cavalos do haras: ").strip().replace(',', '.')

# Validação da entrada
if not quantidade_cavalos.replace('.', '').isdigit() or float(quantidade_cavalos) < 0:
    print("Entrada inválida. Digite um número inteiro não negativo.")
else:
    # Conversão e cálculo
    quantidade_cavalos = int(float(quantidade_cavalos))
    total_ferraduras = quantidade_cavalos * 4

    # Saída
    print(f"Para equipar {quantidade_cavalos} cavalos, serão necessárias {total_ferraduras:,}".replace('.', ',') + " ferraduras.")