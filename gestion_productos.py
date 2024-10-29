import os

productos = []

def cargar_datos():
    if os.path.exists("productos.txt"):
        with open("productos.txt", "r") as file:
            for line in file:
                nombre, precio, cantidad = line.strip().split(", ")
                productos.append({
                    'nombre': nombre,
                    'precio': float(precio),
                    'cantidad': int(cantidad)
                })

def guardar_datos():
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n")

def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    precio = float(input("Introduce el precio del producto: "))
    cantidad = int(input("Introduce la cantidad del producto: "))
    
    producto = { 'nombre': nombre, 'precio': precio, 'cantidad': cantidad }
    productos.append(producto)
    print(f"Producto '{nombre}' añadido.")

def ver_productos():
    if not productos:
        print("No hay productos en el inventario.")
    else:
        print("Lista de productos:")
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def actualizar_producto():
    nombre = input("Introduce el nombre del producto a actualizar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            nuevo_precio = float(input("Introduce el nuevo precio: ") or producto['precio'])
            producto['precio'] = nuevo_precio
            
            nueva_cantidad = int(input("Introduce la nueva cantidad: ") or producto['cantidad'])
            producto['cantidad'] = nueva_cantidad
            
            print(f"Producto '{nombre}' actualizado.")
            return
    print(f"No se encontró el producto '{nombre}'.")

def eliminar_producto():
    nombre = input("Introduce el nombre del producto a eliminar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado.")
            return
    print(f"No se encontró el producto '{nombre}'.")

def menu():
    cargar_datos()
    while True:
        print("\n1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")
        
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            print("Datos guardados. Saliendo del programa.")
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    menu()
