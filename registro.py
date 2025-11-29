# ---------------------------------------------------------
# PROGRAMA SENCILLO: Registro de aprendices
# Cumple con:
# listas, tuplas, diccionarios, cadenas, f-strings,
# condicionales y bucle while.
# ---------------------------------------------------------

aprendices = []   # lista para guardar los aprendices

while True:
    print("\n=== MENÚ ===")
    print("1. Registrar estudiante")
    print("2. Ver todos los aprendices")
    print("3. Salir")

    opcion = input("Elige una opción: ").strip()

    # Opción 1: Registrar estudiante
    if opcion == "1":
        print("\n--- REGISTRO DE ESTUDIANTE ---")

        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        edad = int(input("Edad: "))

        # Tupla con los datos personales
        datos = (nombre, apellido)

        # Diccionario con toda la información del aprendiz
        aprendiz = {
            "datos": datos,
            "edad": edad
        }

        # Guardamos el diccionario dentro de la lista
        aprendices.append(aprendiz)

        print(f"\nEstudiante {nombre} registrado correctamente.")

    # Opción 2: Ver todos los aprendices
    elif opcion == "2":
        print("\n--- LISTA DE TODOS LOS APRENDICES ---")

        if len(aprendices) == 0:
            print("No hay aprendices registrados.")
        else:
            print(f"Total de aprendices: {len(aprendices)}\n")

            for i, apr in enumerate(aprendices):
                nombre, apellido = apr["datos"]
                print(f"{i+1}. {nombre} {apellido} - {apr['edad']} años")

    # Opción 3: Salir
    elif opcion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")
