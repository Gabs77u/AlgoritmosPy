# Função para converter peso de quilos para gramas
def converter_peso_para_gramas(peso_em_kg):
    return peso_em_kg * 1000

# Entrada
peso_em_kg = float(input("Digite o peso em quilos: ").replace(",", "."))

# Saída
print("O peso em gramas é: {}".format(str(converter_peso_para_gramas(peso_em_kg)).replace(".", ",")))