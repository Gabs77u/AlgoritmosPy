# Calculando o peso após engordar 15% e emagrecer 20%

peso = float(input("Digite o seu peso: ").replace(",", "."))

print("Se você engordar 15%, seu novo peso será: " + str(peso * 1.15).replace(".", ",") + " kg")
print("Se você emagrecer 20%, seu novo peso será: " + str(peso * 0.80).replace(".", ",") + " kg")