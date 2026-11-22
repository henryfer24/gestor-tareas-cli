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
