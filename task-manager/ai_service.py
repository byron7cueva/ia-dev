import os
from dotenv import load_dotenv
from openai import OpenAI

# Cargar las variables de entorno
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_simple_tasks(description):
    if not client.api_key:
        raise AIException("Error: La API key de OpenAI no esta configurada.")
    
    try:
        prompt = f"""
        Desglosa la siguiente tarea compleja en una lista de 3 a 5 subtareas simples y accionables.
        Tarea: {description}
        Formato de respuesta:
        - Subtarea 1
        - Subtarea 2
        - Subtarea 3
        - etc.

        Responde solo con la lista de subtareas, una pot línea, empezando cada línea con un guión. 
        """

        params = {
            "model": "gpt-5",
            "messages": [
                {"role": "system", "content": "Eres un asistente experto en gestión de tareas que ayuda a dividir tareas complejas en pasos simples y accionables"},
                {"role": "user", "content": prompt}
            ],
            "max_completion_tokens": 300,
            "verbosity": "medium",
            "reasoning_effort": "minimal"
        }

        response = client.chat.completions.create(**params) # ** desempaqueta todo el contenido del diccionario
        content = response.choices[0].messaje.content.strip() # Se toma la primera iteracion de la respuesta

        subtasks = []
        for line in content.split("\n"):
            line = line.strip()
            if line and line.startswith("-"):
                subtask = line[1:] #Quiero todo el contenido a partir del caracter de la posicion 1
                if subtask:
                    subtasks.append(subtask)
        
        if subtasks:
            return subtasks
        raise AIException("Error: No se han podido generar las subtareas.")


    except Exception:
        raise AIException("Error: No se a podido conectar a OpenAI")
    

class AIException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"AIError: {self.message}"