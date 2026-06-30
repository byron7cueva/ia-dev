import json

class Task:
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    # Se encarga de imprimir el contenido de la clase
    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] #{self.id}: {self.description}"
    
class TaskManager:
    FILE_NAME = "task.json"

    def __init__(self):
        self._tasks = []
        self._next_id = 1
        self.load_tasks()

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        self.save_tasks()
        print(f"Tarea agregada: {description}")

    def list_task(self):
        if not self._tasks:
            print("No hay tareas pendientes")
        else:
            for task in self._tasks:
                print(task)

    def complete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                task.completed = True
                self.save_tasks()
                print(f"Tarea completada: {task}")
                return
        print(f"No se encontro la tarea con el id: {id}")

    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                self.save_tasks()
                print(f"Tarea eliminada: #{id}")
                return
        print(f"Tarea no encontrada: #{id}")

    def load_tasks(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file) # Cargando el json desde el archivo
                self._tasks = [Task(item["id"], item["description"], item["completed"]) for item in data]
                if self._tasks:
                    self._next_id = self._tasks[-1].id + 1
                else:
                    self._next_id = 1
        
        except FileNotFoundError:
            self._tasks = []

    def save_tasks(self):
        with open(self.FILE_NAME, "w") as file:
            json.dump([{"id": task.id, "description": task.description, "completed": task.completed} for task in self._tasks], file, indent=4)