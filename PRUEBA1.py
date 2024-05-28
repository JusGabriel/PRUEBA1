print("***************** BIENVENIDO A BURGUER KING *****************")
print("")
print("Ingrese los datos para su factura electronica:")
print("")

nombre = input("Ingrese su nombre por favor: ")
cedula = int(input("Ingrese su numero de cedula: "))
correo = input("Ingrese su correo electronico: ")
numeroHamburguesas = int(input("Ingrese el numero de hamburguesas que compro: "))

print("")

print("Ingrese el tipo de hamburguesa que esta comprando:")
print("1) Sencilla: $1.50")
print("2) Doble: $2.50")
print("3) Triple: $3.25")

opcion = input("Ingrese la opcion: ")

print("")

if opcion == "1":
    valorPagar = numeroHamburguesas * 1.50
elif opcion == "2":
    valorPagar = numeroHamburguesas * 2.50
elif opcion == "3":
    valorPagar = numeroHamburguesas * 3.25
else:
    print("Este tipo de hamburguesa no existe.")
    exit()

print("Ingrese su forma de pago")
print("1) Tarjeta de credito")
print("2) Efectivo")

formaPago = input("Ingrese la opcion: ")

print("")
print("")

if formaPago == "1":
    recargo = valorPagar * 0.05
    pagoTotal = valorPagar + recargo
    print(f"Excelente, {nombre} con numero de cedula {cedula}, tu pago total seria ${pagoTotal:.2f}.")
    print(f"La factura se enviará al siguiente correo: {correo}")
elif formaPago == "2":
    pagoTotal = valorPagar
    print(f"Excelente, {nombre} con numero de cedula {cedula}, tu pago total seria ${pagoTotal:.2f}.")
    print(f"La factura se enviara al siguiente correo: {correo}")
else:
    print("No existe este tipo de pago.")
    print("Muchas gracias.")
    exit()



    