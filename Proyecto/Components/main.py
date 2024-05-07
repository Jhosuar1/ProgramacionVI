from Crud.crud import CRUD  # Importa la clase CRUD desde un módulo llamado crud

def mostrar_menu():  # Define una función para mostrar el menú del sistema
    print("Bienvenido al sistema de facturación agrícola")
    print("Seleccione una opción:")
    print("1. Mostrar todas las facturas.")
    print("2. Buscar una factura por fecha.")
    print("3. Eliminar una factura por fecha.")
    print("4. Modificar el valor de una factura por fecha.")
    print("5. Generar una nueva factura manualmente.")
    print("6. Buscar facturas por cédula de cliente.")
    print("7. Salir")

def mostrar_facturas(facturas):  # Define una función para mostrar todas las facturas almacenadas
    if not facturas:
        print("No hay facturas almacenadas.")
    else:
        print("Facturas almacenadas:")
        for factura in facturas:
            print("Fecha:", factura["fecha"])
            print("Cédula del cliente:", factura["cedula_cliente"])
            print("Nombre del cliente:", factura["nombre_cliente"])
            print("Valor total:", factura["valor_total"])
            print("Nombre del producto:", factura["nombre_producto"])
            print()

def main():  # Define la función principal del programa
    facturas = [  # Lista de facturas predefinidas
        {"fecha": "2024-01-01", "cedula_cliente": "1234567890", "nombre_cliente": "Juan", "valor_total": 100.0, "nombre_producto": "Antibiótico X", },
        {"fecha": "2024-02-01", "cedula_cliente": "2345678901", "nombre_cliente": "María", "valor_total": 200.0, "nombre_producto": "Fertilizante Y"},
        {"fecha": "2024-03-01", "cedula_cliente": "3456789012", "nombre_cliente": "Pedro", "valor_total": 300.0, "nombre_producto": "Plaguicida Z"},
        # Añade más facturas aquí según sea necesario
    ]

    while True:  # Bucle principal que muestra el menú y realiza acciones según la opción seleccionada
        mostrar_menu()
        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":  # Muestra todas las facturas
            mostrar_facturas(facturas)
        elif opcion == "2":  # Busca una factura por fecha
            fecha_buscar = input("\nIngrese la fecha de la factura a buscar (YYYY-MM-DD): ")
            factura_encontrada = CRUD.buscar_factura_por_fecha(facturas, fecha_buscar)
            if factura_encontrada:
                print("\nFactura encontrada:")
                print("Fecha:", factura_encontrada["fecha"])
                print("Cédula del cliente:", factura_encontrada["cedula_cliente"])
                print("Nombre del cliente:", factura_encontrada["nombre_cliente"])
                print("Valor total:", factura_encontrada["valor_total"])
                print("Nombre del producto:", factura_encontrada["nombre_producto"])
            else:
                print("\nNo se encontró ninguna factura para la fecha especificada.")
        elif opcion == "3":  # Elimina una factura por fecha
            fecha_eliminar = input("\nIngrese la fecha de la factura a eliminar (YYYY-MM-DD): ")
            if CRUD.eliminar_factura_por_fecha(facturas, fecha_eliminar):
                print("\nFactura eliminada exitosamente.")
            else:
                print("\nNo se encontró ninguna factura para la fecha especificada.")
        elif opcion == "4":  # Modifica el valor de una factura por fecha
            fecha_modificar = input("\nIngrese la fecha de la factura a modificar (YYYY-MM-DD): ")
            nuevo_valor = float(input("Ingrese el nuevo valor total de la factura: "))
            if CRUD.modificar_valor_factura_por_fecha(facturas, fecha_modificar, nuevo_valor):
                print("\nValor de la factura modificado exitosamente.")
            else:
                print("\nNo se encontró ninguna factura para la fecha especificada.")
        elif opcion == "5":  # Genera una nueva factura manualmente
            fecha = input("Ingrese la fecha de la nueva factura (YYYY-MM-DD): ")
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            cedula_cliente = input("Ingrese la cédula del cliente: ")
            valor_total = float(input("Ingrese el valor total de la nueva factura: "))
            nombre_producto = input("Ingrese el nombre del producto vendido: ")
            factura_nueva = {"fecha": fecha, "cedula_cliente": cedula_cliente, "nombre_cliente": nombre_cliente, "valor_total": valor_total, "nombre_producto": nombre_producto}
            facturas.append(factura_nueva)
            print("\nNueva factura creada exitosamente.")
        elif opcion == "6":  # Busca facturas por cédula de cliente
            cedula_cliente = input("\nIngrese la cédula del cliente para buscar sus facturas: ")
            facturas_cliente = CRUD.buscar_facturas_por_cedula(facturas, cedula_cliente)
            if facturas_cliente:
                print("\nFacturas asociadas al cliente con cédula", cedula_cliente + ":")
                mostrar_facturas(facturas_cliente)
            else:
                print("\nNo se encontraron facturas asociadas al cliente con cédula", cedula_cliente + ".")
        elif opcion == "7":  # Sale del programa
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido del menú.")

if __name__ == "__main__":  # Llama a la función main si el script es ejecutado directamente
    main()
