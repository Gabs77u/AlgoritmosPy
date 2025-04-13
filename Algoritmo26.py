#Biblioteca
import math

# Calculando a hipotenusa de um triângulo retângulo
cateto1 = float(input("Digite o valor do primeiro cateto: ").replace(',', '.'))
cateto2 = float(input("Digite o valor do segundo cateto: ").replace(',', '.'))
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
print("Hipotenusa:", str(hipotenusa).replace('.', ','))