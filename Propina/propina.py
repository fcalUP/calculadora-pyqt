cuenta = float(input("Cuanto les cobraron?\n"))
personas = int(input("Cuantas personas van a pagar?\n"))
if personas < 2 and cuenta < 200:
    print("\n****** Y qué? no se querían tomar una cervecita? ******\n")
    propina = float(input("Cuanto van a dejar de propina?\n 10, 15 o 20%"))
    cuentaPersonal = (cuenta/personas) * (1-(propina/100))
    print(f"Cada persona debe pagar: {cuentaPersonal} pesos")

elif personas > 2 and cuenta > 500:
    print("Llamen a la patruylla, esto es un robo!")
    propina = float(input("Cuanto van a dejar de propina? 10, 15 o 20%\n"))
    cuentaPersonal = round((cuenta/personas) * (1-(propina/100)), 2)
    print(f"Cada persona debe pagar: {cuentaPersonal}")
else:
    propina = float(input("Cuanto van a dejar de propina? 10, 15 o 20%\n"))
    cuentaPersonal = (cuenta/personas) * (1-(propina/100))
    print(f"Cada persona debe pagar: {round(cuentaPersonal, 2)}\n")
