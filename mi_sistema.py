import sqlite3
from datetime import datetime  

def crear_base_datos():
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()

    cursor.execute('''

        CREATE TABLE IF NOT EXISTS productos (
                   
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT NOT NULL,
                   precio REAL NOT NULL,
                   cantidad INTEGER NOT NULL,
                   fecha TEXT

                   )
     ''')
    
    conn.commit()
    conn.close()
    print("Base de datos creada")


productos = []

def agregar_producto():

    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad en stock: "))

    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()

    fecha = datetime.now().strftime("%Y=%m-%d %H:%M")

    cursor.execute('''
        INSERT INTO productos(nombre,precio,cantidad,fecha)
        VALUES (?,?,?,?)
    ''' , (nombre,precio,cantidad,fecha))

    conn.commit()
    conn.close()
    
    print(f"Producto {nombre} agregado exitosamente.")

def mostrar_productos():

    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, nombre, precio, cantidad, fecha FROM productos")
    productos_db = cursor.fetchall()

    conn.close()

    if len(productos_db) == 0:
        print("No hay productos en el inventario")
        return
    
    print("\n === INVENTARIO (desde db)===")
    for producto in productos_db:
        id_prod, nombre, precio, cantidad, fecha = producto
        print(f"ID: {id_prod} - {nombre}")
        print(f"    Precio: ${precio}")
        print (f"   Cantidad: {cantidad}")
        print(f"    Fecha: {fecha}")
        print("-" * 30)

def calcular_valor_total():

    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()

    cursor.execute("SELECT nombre, precio, cantidad FROM productos")
    productos_db = cursor.fetchall()

    conn.close()

    if len(productos_db) == 0:
        print("No hay productos para calcular")
        return 0
    
    total = 0
    for producto in productos_db:

        nombre, precio, cantidad = producto
        valor_producto = precio * cantidad
        total += valor_producto

    print(f"\n VALOR TOTAL DEL INVENTARIO: ${total:,.2f}")
    print("-" * 40)
    return total


def main():
    crear_base_datos()
    while True:
        print("=== Sistema de Inventario ===")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Calcular valor total")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            calcular_valor_total()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
        

if __name__ == "__main__":
    main()
    