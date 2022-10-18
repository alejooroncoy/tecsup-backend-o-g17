# Programa que convierte de soles a dólares

# Entrada
moneda = "soles"
montoSoles = input("Ingrese el monto en soles: ")
valorDeCambio = 3.977

# Proceso
montoDolares = float(montoSoles) / valorDeCambio

# Salida

print("""El monto en dólares es : {0}""".format(montoDolares))