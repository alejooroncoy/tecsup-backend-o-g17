# Entrada
table = input("Ingresa tabla de multiplicar: ")
# Proceso
for contador in range(1, 13):
  # Salida
  print("""{0} x {1} = {2}""".format(table, contador, int(table) * contador))