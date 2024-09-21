reservas_hotel = {}
reservas_vuelo = {}
clientes = {}
paquetes_turisticos = {
    1: {'nombre_paquete': 'Escapada Romántica', 'destino': 'Paris', 'fecha_salida': '09-30-2024', 'precio': 1200000},
    2: {'nombre_paquete': 'Aventura en la Selva', 'destino': 'Amazonas', 'fecha_salida': '10-10-2024', 'precio': 1500000},
    3: {'nombre_paquete': 'Tour por Europa', 'destino': 'Varios países de Europa', 'fecha_salida': '20-11-2024', 'precio': 3000000},
    4: {'nombre_paquete': 'Vacaciones en la Playa', 'destino': 'Maldivas', 'fecha_salida': '15-12-2024', 'precio': 2500000}
}

def agregar_informacion(diccionario, tipo):
    id = int(input(f"Introduce el ID para la nueva {tipo}: "))

    if tipo == "reserva de hotel":
        cliente = str(input("Introduce el nombre del cliente: "))
        while True:
            if cliente.isalpha() != True:
                print("\nEl nombre del cliente debe ser texto, intentelo de nuevo.")
                cliente = (input("Introduce el nombre del cliente: "))
            
            elif len(cliente) == 0():
                print("\nEl nombre del cliente debe ser texto, intentelo de nuevo.")
                cliente = (input("Introduce el nombre del cliente: "))
            else:
                break

        fecha_entrada = input("Introduce la fecha de entrada (DD-MM-YYYY): ")
        while True: 
            if len(fecha_entrada) == 0:
                print("\nLa fecha de entrada debe ser valida, por favor intentelo de nuevo.")
                fecha_entrada = (input("Introduce la fecha de entrada (DD-MM-YYYY): "))
            else:
                break

        fecha_salida = input("Introduce la fecha de salida (DD-MM-YYYY): ")
        while True: 
            if len(fecha_salida) == 0:
                print("\nLa fecha de salida debe ser valida, por favor intentelo de nuevo.")
                fecha_salida = (input("Introduce la fecha de salida (DD-MM-YYYY): "))
            else:
                break
        
        habitacion = input("Introduce el número de habitación: ")
        while True: 
            if habitacion.isdigit() != True:
                print("\nEl numero de habitacion debe ser valido, por favor ingreselo de nuevo.")
                habitacion = input("Introduce el número de habitación: ")
            else:
                break

        diccionario[id] = {
            'cliente': cliente,
            'fecha_entrada': fecha_entrada,
            'fecha_salida': fecha_salida,
            'habitacion': habitacion
        }

    elif tipo == "reserva de vuelo":
        cliente = input("Introduce el nombre del cliente: ")
        while True:
            if cliente.isalpha() != True:
                print("\nEl nombre del cliente debe ser texto, intentelo de nuevo.")
                cliente = (input("Introduce el nombre del cliente: "))
            
            elif len(cliente) == 0:
                print("\nEl nombre del cliente debe ser texto, intentelo de nuevo.")
                cliente = (input("Introduce el nombre del cliente: "))
            else:
                break

        fecha_vuelo = input("Introduce la fecha del vuelo (DD-MM-YYYY): ")
        while True: 
            if len(fecha_vuelo) == 0:
                print("\nLa fecha del vuelo debe ser valida, por favor intentelo de nuevo.")
                fecha_vuelo = (input("Introduce la fecha del vuelo (DD-MM-YYYY): "))
            else:
                break

        destino = input("Introduce el destino: ")
        while True: 
            if len(destino) == 0:
                print("\nEl destino debe ser valida, por favor intentelo de nuevo.")
                destino = (input("Introduce el destino: "))
            else:
                break
        asiento = input("Introduce el número de asiento: ")
        while True: 
            if asiento.isdigit() != True:
                print("\nEl numero de habitacion debe ser valido, por favor ingreselo de nuevo.")
                asiento = input("Introduce el número de habitación: ")
            else:
                break
        
        diccionario[id] = {
            'cliente': cliente,
            'fecha_vuelo': fecha_vuelo,
            'destino': destino,
            'asiento': asiento
        }

    elif tipo == "cliente":
        nombre = input("Introduce el nombre del cliente: ")
        while True:
            if cliente.isalpha() != True:
                print("\nEl nombre del cliente debe ser texto, intentelo de nuevo.")
                cliente = (input("Introduce el nombre del cliente: "))
            
            elif len(cliente) == 0:
                print("\nEl nombre del cliente debe ser texto, intentelo de nuevo.")
                cliente = (input("Introduce el nombre del cliente: "))
            else:
                break

        telefono = input("Introduce el teléfono del cliente: ")
        while True: 
            if telefono.isdigit() != True:
                print("\nEl numero de habitacion debe ser valido, por favor ingreselo de nuevo.")
                telefono = input("Introduce el número de habitación: ")
            else:
                break
        email = input("Introduce el email del cliente: ")
        while True:
            if email.isalpha() != True:
                print("\nEl nombre del cliente debe ser texto, intentelo de nuevo.")
                cliente = (input("Introduce el nombre del cliente: "))
            
            elif len(email) == 0:
                print("\nEl nombre del cliente debe ser texto, intentelo de nuevo.")
                email = (input("Introduce el nombre del cliente: "))
            else:
                break

        diccionario[id] = {
            'nombre': nombre,
            'telefono': telefono,
            'email': email
        }

    elif tipo == "paquete turístico":
        nombre_paquete = input("Introduce el nombre del paquete turístico: ")
        destino = input("Introduce el destino: ")
        while True: 
            if len(destino) == 0:
                print("\nEl destino debe ser valida, por favor intentelo de nuevo.")
                destino = (input("Introduce el destino: "))
            else:
                break
        fecha_salida = input("Introduce la fecha de salida (DD-MM-YYYY): ")
        while True: 
            if len(fecha_salida) == 0:
                print("\nLa fecha de salida debe ser valida, por favor intentelo de nuevo.")
                fecha_salida = (input("Introduce la fecha de salida (DD-MM-YYYY): "))
            else:
                break

        precio = input("Introduce el precio del paquete: ")
        while True: 
            if precio.isdigit() != True:
                print("\nEl numero de habitacion debe ser valido, por favor ingreselo de nuevo.")
                precio = input("Introduce el número de habitación: ")
            else:
                break

        diccionario[id] = {
            'nombre_paquete': nombre_paquete,
            'destino': destino,
            'fecha_salida': fecha_salida,
            'precio': precio
        }
    print("\n-----------------------------------------")
    print(f"Nueva {tipo} agregada correctamente.\n")


def ver_informacion(diccionario, tipo):
    if diccionario:
        print(f"\nMostrando todas las {tipo}s:")
        for id, info in diccionario.items():
            print(f"ID {id}: {info}")
    else:
        print(f"No hay {tipo}s disponibles.")


def actualizar_informacion(diccionario, tipo):
    id = int(input(f"Introduce el ID de la {tipo} a actualizar: "))

    if id in diccionario:
        print(f"Información actual: {diccionario[id]}")
        campo = input("¿Qué campo deseas actualizar? (Escribe el nombre del campo): ")
        nuevo_valor = input(f"Introduce el nuevo valor para {campo}: ")
        if campo in diccionario[id]:
            diccionario[id][campo] = nuevo_valor
            print(f"{tipo.capitalize()} actualizada correctamente.")
        else:
            print("Campo no encontrado.")
    else:
        print("ID no encontrado.")


def borrar_informacion(diccionario, tipo):
    id = int(input(f"Introduce el ID de la {tipo} a borrar: "))

    if id in diccionario:
        diccionario.pop(id)
        print(f"{tipo.capitalize()} eliminada correctamente.")
    else:
        print("ID no encontrado.")


def menu():
    while True:
        print("\nMenú Principal")
        print("1. Gestionar reservas de hotel")
        print("2. Gestionar reservas de vuelo")
        print("3. Gestionar paquetes turísticos")
        print("4. Gestionar información de clientes")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            submenu(reservas_hotel, "reserva de hotel")
        elif opcion == '2':
            submenu(reservas_vuelo, "reserva de vuelo")
        elif opcion == '3':
            submenu(paquetes_turisticos, "paquete turístico")
        elif opcion == '4':
            submenu(clientes, "cliente")
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def submenu(diccionario, tipo):
    while True:
        print(f"\nSubmenú - {tipo.capitalize()}")
        print("1. Agregar nueva información")
        print("2. Actualizar información")
        print("3. Borrar información")
        print("4. Ver información")
        print("5. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == '4':
            ver_informacion(diccionario, tipo)
        elif opcion == '2':
            actualizar_informacion(diccionario, tipo)
        elif opcion == '3':
            borrar_informacion(diccionario, tipo)
        elif opcion == '1':
            agregar_informacion(diccionario, tipo)
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

menu()