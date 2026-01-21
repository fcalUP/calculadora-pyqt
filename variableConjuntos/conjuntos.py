lista_sucia = [1, 2, 2, 3, 3, 3, 4]

# Convertimos a set
conjunto_limpio = set(lista_sucia)

# ¿Cómo creo un conjunto vacío?

# Digagramas de Venn
A = {"Ana", "Beto", "Carla"}
B = {"Beto", "Daniel", "Ana"}

# 1. INTERSECCIÓN (&): ¿Quiénes están en ambos grupos?
print(A & B)
# Salida: {'Ana', 'Beto'}

# 2. UNIÓN (|): Todos los amigos sin repetir
print(A | B)
# Salida: {'Ana', 'Beto', 'Carla', 'Daniel'}

# 3. DIFERENCIA (-): ¿Quién está en A pero NO en B?
print(A - B)
# Salida: {'Carla'}
