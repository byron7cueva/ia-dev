# Task Manager

Gestor de tareas interactivo por línea de comandos con soporte de descomposición automática de tareas complejas mediante OpenAI.

## Descripción

Este proyecto es una aplicación CLI que permite administrar tareas con persistencia local en un archivo JSON. Se puede:

- Añadir tareas simples.
- Listar tareas existentes.
- Completar tareas.
- Eliminar tareas.
- Transformar tareas complejas en subtareas simples usando un servicio de IA.

## Características principales

- Persistencia local en `task.json`.
- API de OpenAI para descomponer tareas complejas en subtareas.
- Interfaz basada en texto con menú de opciones.
- Pruebas unitarias para la gestión de tareas.

## Estructura del proyecto

- `main.py` - Punto de entrada de la aplicación y menú de la CLI.
- `task_manager.py` - Definición de `Task`, `TaskManager` y lógica de persistencia.
- `ai_service.py` - Comunicación con OpenAI para generar subtareas.
- `requirements.txt` - Dependencias del proyecto.
- `test_task_manager.py` - Pruebas unitarias para `TaskManager`.
- `task.json` - Archivo de almacenamiento de tareas generado en tiempo de ejecución.

## Requisitos

- Python 3.11+ (recomendado)
- Dependencias del proyecto en `requirements.txt`
- Clave de API de OpenAI para la funcionalidad de IA

## Instalación

1. Clona el repositorio o descarga los archivos al directorio del proyecto.
2. Crea y activa un entorno virtual de Python:

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Instala `python-dotenv` si no está incluida en `requirements.txt`:

```bash
pip install python-dotenv
```

## Configuración de la API de OpenAI

1. Crea un archivo `.env` en la raíz del proyecto.
2. Añade la variable de entorno con tu clave de OpenAI:

```env
OPENAI_API_KEY=tu_api_key_aqui
```

3. La aplicación usa `dotenv` para cargar `OPENAI_API_KEY` desde `.env`.

## Uso

Ejecuta la aplicación desde el directorio del proyecto:

```bash
python main.py
```

Verás un menú con las siguientes opciones:

1. Añadir tarea
2. Añadir tarea compleja (con IA)
3. Listar tareas
4. Completar tarea
5. Eliminar tarea
6. Salir

### Flujo de uso

- `Añadir tarea`: escribe la descripción de la tarea y se guardará en `task.json`.
- `Añadir tarea compleja (con IA)`: ingresa una tarea compleja y el servicio de OpenAI intentará generar subtareas automáticas.
- `Listar tareas`: muestra todas las tareas guardadas.
- `Completar tarea`: marca una tarea como completada por su ID.
- `Eliminar tarea`: elimina una tarea por su ID.

## Formato de almacenamiento

Las tareas se guardan en `task.json` con la siguiente estructura:

```json
[
  {
    "id": 1,
    "description": "Ejemplo de tarea",
    "completed": false
  }
]
```

## Pruebas

Ejecuta las pruebas unitarias con:

```bash
python -m unittest test_task_manager.py
```

## Notas importantes

- Si no se configura `OPENAI_API_KEY`, la opción de tarea compleja mostrará un error informativo.
- `TaskManager` usa el último ID almacenado para asignar nuevos identificadores.
- El archivo `task.json` se crea automáticamente cuando se añade la primera tarea.

## Posibles mejoras

- Añadir edición de tareas.
- Permitir fechas de vencimiento y prioridades.
- Mejorar el manejo de formatos de respuestas de OpenAI.
- Añadir soporte para eliminar tareas completadas en lote.
