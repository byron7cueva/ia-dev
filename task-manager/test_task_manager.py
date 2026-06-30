import unittest
import json
import os
from task_manager import Task, TaskManager


class TestTask(unittest.TestCase):
    """Tests para la clase Task"""
    
    def test_task_creation(self):
        """Prueba la creación de una tarea"""
        task = Task(1, "Test task")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Test task")
        self.assertEqual(task.completed, False)
    
    def test_task_completion(self):
        """Prueba el estado completado de una tarea"""
        task = Task(1, "Test task", completed=True)
        self.assertEqual(task.completed, True)
    
    def test_task_str_representation(self):
        """Prueba la representación en string de una tarea"""
        task_pending = Task(1, "Test task", completed=False)
        task_completed = Task(2, "Completed task", completed=True)
        
        self.assertIn("[ ]", str(task_pending))
        self.assertIn("✓", str(task_completed))
        self.assertIn("#1", str(task_pending))
        self.assertIn("Test task", str(task_pending))


class TestTaskManager(unittest.TestCase):
    """Tests para la clase TaskManager"""
    
    def setUp(self):
        """Se ejecuta antes de cada test para preparar el ambiente"""
        self.test_file = "task_test.json"
        # Cambiar el nombre del archivo temporalmente para las pruebas
        TaskManager.FILE_NAME = self.test_file
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def tearDown(self):
        """Se ejecuta después de cada test para limpiar"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        TaskManager.FILE_NAME = "task.json"
    
    def test_task_manager_initialization(self):
        """Prueba la inicialización del TaskManager"""
        manager = TaskManager()
        self.assertEqual(len(manager._tasks), 0)
        self.assertEqual(manager._next_id, 1)
    
    def test_add_task(self):
        """Prueba agregar una tarea"""
        manager = TaskManager()
        manager.add_task("Nueva tarea")
        
        self.assertEqual(len(manager._tasks), 1)
        self.assertEqual(manager._tasks[0].description, "Nueva tarea")
        self.assertEqual(manager._tasks[0].id, 1)
        self.assertEqual(manager._tasks[0].completed, False)
    
    def test_add_multiple_tasks(self):
        """Prueba agregar múltiples tareas"""
        manager = TaskManager()
        manager.add_task("Tarea 1")
        manager.add_task("Tarea 2")
        manager.add_task("Tarea 3")
        
        self.assertEqual(len(manager._tasks), 3)
        self.assertEqual(manager._tasks[0].id, 1)
        self.assertEqual(manager._tasks[1].id, 2)
        self.assertEqual(manager._tasks[2].id, 3)
        self.assertEqual(manager._next_id, 4)
    
    def test_complete_task(self):
        """Prueba completar una tarea"""
        manager = TaskManager()
        manager.add_task("Tarea a completar")
        
        self.assertEqual(manager._tasks[0].completed, False)
        manager.complete_task(1)
        self.assertEqual(manager._tasks[0].completed, True)
    
    def test_complete_nonexistent_task(self):
        """Prueba completar una tarea que no existe"""
        manager = TaskManager()
        manager.add_task("Tarea 1")
        # Esto debería imprimir un mensaje de error
        manager.complete_task(999)
        # La tarea existente no debe cambiar
        self.assertEqual(manager._tasks[0].completed, False)
    
    def test_delete_task(self):
        """Prueba eliminar una tarea"""
        manager = TaskManager()
        manager.add_task("Tarea a eliminar")
        manager.add_task("Tarea a mantener")
        
        self.assertEqual(len(manager._tasks), 2)
        manager.delete_task(1)
        self.assertEqual(len(manager._tasks), 1)
        self.assertEqual(manager._tasks[0].id, 2)
    
    def test_delete_nonexistent_task(self):
        """Prueba eliminar una tarea que no existe"""
        manager = TaskManager()
        manager.add_task("Tarea 1")
        manager.delete_task(999)
        # La tarea no debe ser eliminada
        self.assertEqual(len(manager._tasks), 1)
    
    def test_save_tasks(self):
        """Prueba guardar tareas en archivo"""
        manager = TaskManager()
        manager.add_task("Tarea 1")
        manager.complete_task(1)
        manager.add_task("Tarea 2")
        
        # Verificar que el archivo existe
        self.assertTrue(os.path.exists(self.test_file))
        
        # Verificar el contenido del archivo
        with open(self.test_file, "r") as file:
            data = json.load(file)
        
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["id"], 1)
        self.assertEqual(data[0]["completed"], True)
        self.assertEqual(data[1]["id"], 2)
        self.assertEqual(data[1]["completed"], False)
    
    def test_load_tasks(self):
        """Prueba cargar tareas desde archivo"""
        # Crear datos de prueba en el archivo
        test_data = [
            {"id": 1, "description": "Tarea cargada 1", "completed": False},
            {"id": 2, "description": "Tarea cargada 2", "completed": True}
        ]
        
        with open(self.test_file, "w") as file:
            json.dump(test_data, file)
        
        # Crear un nuevo manager que cargará las tareas
        manager = TaskManager()
        
        self.assertEqual(len(manager._tasks), 2)
        self.assertEqual(manager._tasks[0].id, 1)
        self.assertEqual(manager._tasks[0].description, "Tarea cargada 1")
        self.assertEqual(manager._tasks[0].completed, False)
        self.assertEqual(manager._tasks[1].id, 2)
        self.assertEqual(manager._tasks[1].completed, True)
        self.assertEqual(manager._next_id, 3)
    
    def test_load_tasks_from_empty_file(self):
        """Prueba cargar tareas desde un archivo vacío"""
        manager = TaskManager()
        self.assertEqual(len(manager._tasks), 0)
        self.assertEqual(manager._next_id, 1)
    
    def test_persistence(self):
        """Prueba que las tareas persisten entre instancias"""
        # Crear tareas con el primer manager
        manager1 = TaskManager()
        manager1.add_task("Tarea persistente 1")
        manager1.add_task("Tarea persistente 2")
        
        # Crear un nuevo manager que debería cargar las tareas
        manager2 = TaskManager()
        
        self.assertEqual(len(manager2._tasks), 2)
        self.assertEqual(manager2._tasks[0].description, "Tarea persistente 1")
        self.assertEqual(manager2._tasks[1].description, "Tarea persistente 2")
    
    def test_task_id_increments(self):
        """Prueba que los IDs de las tareas se incrementan correctamente"""
        manager = TaskManager()
        manager.add_task("Tarea 1")
        manager.delete_task(1)
        manager.add_task("Tarea 2")
        
        # El siguiente ID debe ser 2, no 1 nuevamente
        self.assertEqual(manager._tasks[0].id, 2)
        self.assertEqual(manager._next_id, 3)


if __name__ == "__main__":
    unittest.main()
