# Manejo de variables en python 
# Suma de 2 números

# Datos de entrada

from tokenize import Number


numero1 = input("Ingrese número 1: ")
numero2 = input("Ingrese número 2: ")

# Proceso

resultado = int(numero1) + int(numero2)

# Datos salida

print("""La suma de {0} y {1} es {2} """.format(numero1, numero2, resultado))