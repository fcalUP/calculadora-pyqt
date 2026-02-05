ventas = [
    (101, "Laptop", 800, 750, "Completado"),
    (102, "Mouse", 25, "Pendiente"),
    (103, "Teclado", 45, 40, 42, "Completado")
]
precio_total=0
for registro in ventas:
    # Usamos desempaquetado extendido para capturar los precios variables
    id_venta, producto, *precios, estado = registro
    
    # Calculamos el promedio de precios si hay más de uno
    promedio = sum(precios) / len(precios)
    precio_total += sum(precios)
    
    print(f"Venta {id_venta}: {producto} | Promedio: ${promedio:.2f} | Status: {estado}")
print(f"Gran total de todas las ventas: ${precio_total:.2f}")