# Definición
mi_tupla = (10, "Hola", 3.14)

# Acceso (Igual que listas)
print(mi_tupla[1])  # Salida: "Hola"

# Intento de modificación (ESTO DARÁ ERROR)
# mi_tupla[0] = 99
# Error: 'tuple' object does not support item assignment

# No necesitamos paréntesis, Python entiende que es una tupla | Empaquetamiento
datos = "Juan", 25, "Ingeniero"

a = 5
b = 10

# Python crea una tupla (10, 5) y la desempaqueta en a y b | Desempaquetamiento
# El número de variables a la izquierda debe coincidir exactamente con el número de elementos en la tupla
a, b = b, a

# Ejemplo con desempaquetado avanzado *
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Tomamos el primero, el último, y guardamos el resto en 'medio'
primero, *medio, ultimo = numeros


print("Tipo de primero: " + str(type(primero)))  # Salida: <class 'int'>
