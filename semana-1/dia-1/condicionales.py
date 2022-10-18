# Entrada
numero1 = input("Número 1: ")
numero2 = input("Número 2: ")
operacion = input("Operación a ejecutar(suma[+], resta[-]): ")

# Proceso
if(operacion == "suma" or operacion == "+"):
  resultado = int(numero1) + int(numero2)
elif(operacion == "resta" or operacion == "-"):
  resultado = int(numero1) - int(numero2)
else:
  resultado = 0
  print("Debe ingresar una operación valida")


# Salida 
if(resultado != 0):
  print("""El resultado es {0}""".format(resultado))