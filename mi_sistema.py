
productos = []

def agregar_producto():

    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad en stock: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad 
    }

    productos.append(producto)
    print(f"Producto {nombre} agregado exitosamente.")

def mostrar_productos():

    if len(productos) == 0:
        print("No hay productos en el inventario")
        return
    
    print("\n === INVENTARIO ===")
    for i, producto in enumerate(productos,1):
        print(f"{i}. {producto['nombre']}")
        print(f"    Precio: ${producto['precio']}")
        print (f"   Cantidad: {producto['cantidad']}")
        print("-" * 20)


def main():
    while True:
        print("=== Sistema de Inventario ===")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            print("Saliendo del sistema...")
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
    