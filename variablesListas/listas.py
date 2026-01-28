# Creación de una lista (Heterogénea y Ordenada)
mi_lista = [10, "Hola", 3.14, True]
print(mi_lista)  # Salida: [10, "Hola", 3.14, True]
"""""
# Acceso por índice (El orden se respeta)
print(mi_lista[1])  # Salida: "Hola"

# Mutabilidad (Cambiamos el primer valor)
mi_lista[0] = 99
print(mi_lista)     # Salida: [99, "Hola", 3.14, True]

# Dinamismo (Agregamos un nuevo elemento)
mi_lista.append("Nuevo")
print(mi_lista)     # Salida: [99, "Hola", 3.14, True, "Nuevo"]

# Inserción en una posición específica
mi_lista.insert(2, "Insertado")
print(mi_lista)     # Salida: [99, "Hola", "Insertado", 3.14, True, "Nuevo"]

# Traer el último valor
print(mi_lista[-1])  # Salida: "Nuevo"

# ******************Eliminación de elementos******************
# Eliminación por índice
del mi_lista[2]
print(mi_lista)     # Salida: [99, "Hola", 3.14, True, "Nuevo"]

# Eliminación por índice usando pop
ultimo_elemento = mi_lista.pop()
print(ultimo_elemento)  # Salida: "Nuevo"
print(mi_lista)         # Salida: [99, "Hola", 3.14, True]

# Eliminación del último valor
mi_lista.pop()
print(mi_lista)     # Salida: [99, "Hola", 3.14]

# Eliminación de un elemento
mi_lista.remove(3.14)
print(mi_lista)     # Salida: [99, "Hola", True, "Nuevo"]
# *******************************************

# Longitud de la lista
print(len(mi_lista))  # Salida: 4

# Comprobación de pertenencia
print("Hola" in mi_lista)  # Salida: True
print(3.14 in mi_lista)    # Salida: False

# Slicing (Sublista)
sublista = mi_lista[1:3]
print(sublista)  # Salida: ["Hola", True]
print(type(mi_lista))  # Salida: <class 'list'>
print(type(sublista))   # Salida: <class 'list'>

# Uso de funciones integradas con listas
numeros = [5, 2, 9, 1]
print(sorted(numeros))  # Salida: [1, 2, 5, 9]
print(min(numeros))     # Salida: 1
print(max(numeros))     # Salida: 9
print(sum(numeros))     # Salida: 17
numeros.reverse()
print(numeros)          # Salida: [1, 9, 2, 5]
numeros.sort()
print(numeros)          # Salida: [1, 2, 5, 9]

# Iteración sobre la lista
for elemento in mi_lista:
    print(elemento)

# Que es enumerate
print(enumerate(mi_lista))
# ¿Que paso?
# *****************************List Comprehension***************************
# for normal
numeros = [1, 2, 3, 4]
cuadrados = []
for n in numeros:
    cuadrados.append(n ** 2)
print(cuadrados)

# list comprehension
cuadrados = [n ** 2 for n in numeros]
print(cuadrados)


# Lista con índices y valores
indices = [i for i in enumerate(mi_lista)]
print(indices)
# Solo index
indices = [i for i, _ in enumerate(mi_lista)]
print(indices)

# Lista anidada
lista_anidada = [1, 2, [3, 4], 5]
print(lista_anidada[2])      # Salida: [3, 4]
print(lista_anidada[2][1])   # Salida: 4
# Modificación de un elemento en la lista anidada
lista_anidada[2][0] = 99
print(lista_anidada)         # Salida: [1, 2, [99, 4], 5]"""


"""********************* POR 1 MONEDA *********************
Si tuvieras esta lista: datos = ["A", ["B", "C", ["D", "E"]]]
¿Qué corchetes tendrías que poner para imprimir solamente la letra "E"?"""
