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


def agregar_tarea():
    titulo = input("Título de la tarea: ")
    tareas.append({"titulo": titulo, "completada": False})
    print("Tarea agregada correctamente.\n")


def listar_tareas():
    if not tareas:
        print("No hay tareas registradas.\n")
        return
    print("\n--- LISTA DE TAREAS ---")
    for i, tarea in enumerate(tareas, start=1):
        estado = "x" if tarea["completada"] else " "
        print(f"{i}. [{estado}] {tarea['titulo']}")
    print()


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
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
