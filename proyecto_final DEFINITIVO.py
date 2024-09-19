# Base de datos de clientes
clientes = {}

# Base de datos de paquetes turísticos
paquetes_turisticos = {
    "vuelos": {
        "1. Bogota-Medellin": {"precio": 90, "disponibles": 10},
        "2. Cali-San Andres": {"precio": 200, "disponibles": 5},
        "3. Manizales-Cartagena": {"precio": 145, "disponibles": 8}
    },
    "hoteles": {
        "1. Cali": {"precio": 50, "disponibles": 20},
        "2. Bogota": {"precio": 60, "disponibles": 15},
        "3. Medellin": {"precio": 40, "disponibles": 25}
    },
    "tours": {
        "1. City Tour Cali": {"precio": 20, "disponibles": 30},
        "2. Monserrate Bogota": {"precio": 30, "disponibles": 20},
        "3. Parque Arví Medellin": {"precio": 40, "disponibles": 25}
    }
}

def reservar_paquete():
    global clientes
    print("\nMenú de Reservas:")
    print("1. Vuelo")
    print("2. Hotel")
    print("3. Tour")
    opcion = input("Ingrese su opción: ")
    
    if opcion == "1":
        paquete = "vuelos"
    elif opcion == "2":
        paquete = "hoteles"
    elif opcion == "3":
        paquete = "tours"
    else:
        print("Opción inválida.")
        return
    
    print("\nOpciones de", paquete)
    for i, (nombre, detalles) in enumerate(paquetes_turisticos[paquete].items(), start=1):
        print(f"{i}. {nombre}: ${detalles['precio']}")
    
    seleccion = input("Ingrese el número del paquete deseado: ")
    nombre_paquete = list(paquetes_turisticos[paquete].keys())[int(seleccion) - 1]
    precio = paquetes_turisticos[paquete][nombre_paquete]["precio"]
    
    confirmar = input("Desea reservar? (s/n): ")
    if confirmar.lower() == "s":
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        email = input("Ingrese su correo electrónico: ")
        
        # Agregar cliente a la base de datos
        clientes[nombre + " " + apellido] = {
            "email": email,
            "reservas": [{ "paquete": nombre_paquete, "precio": precio }]
        }
        
        # Restar disponibilidad del paquete
        paquetes_turisticos[paquete][nombre_paquete]["disponibles"] -= 1
        
        print("Reserva exitosa!")
        print("Detalle de la reserva:")
        print(f"Nombre: {nombre} {apellido}")
        print(f"Correo electrónico: {email}")
        print(f"Paquete: {nombre_paquete}")
        print(f"Precio: ${precio}")


def buscar_cliente():
    global clientes
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    cliente = nombre + " " + apellido
    
    if cliente in clientes:
        print("Cliente encontrado.")
        print("Detalle del cliente:")
        print(f"Nombre: {cliente}")
        print(f"Correo electrónico: {clientes[cliente]['email']}")
        print("Reservas:")
        for reserva in clientes[cliente]["reservas"]:
            print(f"Paquete: {reserva['paquete']}")
            print(f"Precio: ${reserva['precio']}")
        
        # Opciones para actualizar o eliminar cliente
        print("\nMenú de Opciones:")
        print("1. Actualizar información")
        print("2. Eliminar cliente")
        print("3. Agregar paquete")
        opcion = input("Ingrese su opción: ")
        
        if opcion == "1":
            # Actualizar información del cliente
            clientes[cliente]["email"] = input("Ingrese nuevo correo electrónico: ")
            print("Información actualizada.")
        elif opcion == "2":
            # Eliminar cliente
            del clientes[cliente]
            print("Cliente eliminado.")
        elif opcion == "3":
            # Agregar paquete al cliente
            paquete = input("Ingrese el nombre del paquete: ")
            precio = float(input("Ingrese el precio del paquete: "))
            clientes[cliente]["reservas"].append({
                "paquete": paquete,
                "precio": precio
            })
            print("Paquete agregado.")
        else:
            print("Opción inválida.")
    else:
        print("Cliente no encontrado.")


def menu():
    while True:
        print("\nMenú Principal:")
        print("1. Reservar paquete")
        print("2. Buscar cliente")
        print("3. Mostrar paquetes")
        print("4. Salir")
        opcion = input("Ingrese su opción: ")
        
        if opcion == "1":
            reservar_paquete()
        elif opcion == "2":
            buscar_cliente()
        elif opcion == "3":
            print("\nPaquetes Disponibles:")
            for tipo, paquetes in paquetes_turisticos.items():
                print(f"\n{tipo.capitalize()}:")
                for nombre, detalles in paquetes.items():
                    print(f"{nombre}: ${detalles['precio']} ({detalles['disponibles']} disponibles)")
        elif opcion == "4":
            print("Gracias por utilizar nuestro sistema de reservas.")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    menu()