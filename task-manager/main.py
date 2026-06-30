from task_manager import TaskManager
from ai_service import create_simple_tasks, AIException

def print_menu():
    print("\n--- Gestor de Tareas Inteligente---")
    print("1. Añadir tarea")
    print("2. Añadir tarea compleja (con IA)")
    print("3. Listar tareas")
    print("4. Completar tarea")
    print("5. Eliminar tarea")
    print("6. Salir")

def main():
    manager = TaskManager()

    while True:
        print_menu()    

        try:
            choice = int(input("Elige una opcion: "))

            match choice:
                case 1:
                    description = input("Ingresa la descripcion: ")
                    manager.add_task(description)
                case 2:
                    description = input("Ingresa la descripcion de la tarea compleja: ")
                    subtasks = create_simple_tasks(description)
                    for subtask in subtasks:
                        manager.add_task(subtask)
                case 3:
                    manager.list_task()
                case 4:
                    id = int(input("Id de la tarea a completar: "))
                    manager.complete_task(id)
                case 5:
                    id = int(input("Id de la tarea a eliminar: "))
                    manager.delete_task(id)
                case 6:
                    print("Saliendo...")
                    break
                case _:
                    print("Opcion no valida. Selecciona otra.")
        except ValueError:
            print("Opcion no valida. Selecciona otra.")
        except AIException as e:
            print(e)

# Si el nombre del fichero corresponde con main, se ejecuta
if __name__ == "__main__":
    main()