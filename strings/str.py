nombre = "Francisco Cal y Mayor"
edad = 28

"""función incorporada en Python que toma dos números (dividendo y divisor) y devuelve una tupla con dos
valores: el cociente (el resultado de la división entera) y el residuo (el resto) de esa división, 
en una sola operación eficiente"""
edad_primer_valor, edad_segundo_valor = divmod(edad, 10)
suma_de_edad = edad_primer_valor + edad_segundo_valor
valor_edad = divmod(edad, 10)
len_nombre = len(nombre)
print("Tu nombre es: ", nombre, " y tiene ", len_nombre, " caracteres.", "\nTienes ", edad, " años, cuya suma de dígitos es: ", suma_de_edad,
      "\nSi a tu nombre, le quitamos el número de caracteres de la suma de tu edad, tu nombre sería: ", nombre[0:-suma_de_edad])
