cuenta = float(input("Cuanto les cobraron?"))
personas = int(input("Cuantas personas van a pagar?"))
if personas <2 and cuenta < 200:
  print("Y qué? no se querían tomar una cervecita?")
  propina = float(input("Cuanto van a dejar de propina?\n 10, 15 o 20%"))
  cuentaPersonal = (cuenta/personas) *(1-(propina/100))
  print(f"Cada persona debe pagar: {cuentaPersonal}")

elif personas > 2 and cuenta > 500:
  print("Llamen a la patruylla, esto es un robo!")
  propina = float(input("Cuanto van a dejar de propina?\n 10, 15 o 20%"))
  cuentaPersonal = (cuenta/personas) *(1-(propina/100))
  print(f"Cada persona debe pagar: {cuentaPersonal}")
