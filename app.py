tareas = []


def mostrar_menu():
    print("=" * 30)
    print("     GESTOR DE TAREAS CLI")
    print("=" * 30)
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("=" * 30)


def completar_tarea():
    if not tareas:
        print("No hay tareas para completar.\n")
        return
    try:
        numero = int(input("Número de la tarea a completar: "))
        tareas[numero - 1]["completada"] = True
        print("Tarea marcada como completada.\n")
    except (ValueError, IndexError):
        print("Número de tarea no válido.\n")


def eliminar_tarea():
    if not tareas:
        print("No hay tareas para eliminar.\n")
        return
    try:
        numero = int(input("Número de la tarea a eliminar: "))
        eliminada = tareas.pop(numero - 1)
        print(f"Tarea '{eliminada['titulo']}' eliminada.\n")
    except (ValueError, IndexError):
        print("Número de tarea no válido.\n")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción aún no implementada.\n")


if __name__ == "__main__":
    main()def mostrar_menu():
    print("=" * 30)
    print("     GESTOR DE TAREAS CLI")
    print("=" * 30)
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("=" * 30)


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "5":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción aún no implementada.\n")


if __name__ == "__main__":
    main()
