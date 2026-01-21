# Creación de una lista (Heterogénea y Ordenada)
mi_lista = [10, "Hola", 3.14, True]

# Acceso por índice (El orden se respeta)
print(mi_lista[1])  # Salida: "Hola"

# Mutabilidad (Cambiamos el primer valor)
mi_lista[0] = 99
print(mi_lista)     # Salida: [99, "Hola", 3.14, True]

# Dinamismo (Agregamos un nuevo elemento)
mi_lista.append("Nuevo")
print(mi_lista)     # Salida: [99, "Hola", 3.14, True, "Nuevo"]