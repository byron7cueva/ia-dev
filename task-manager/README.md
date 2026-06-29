# Task Manager

Es un gestor de tareas a traves de lineas de comandos.

## Definicion de MVP

* Una apliacion CLI para gestionar una lista de tareas
* El usuario podra añadir, listar, completar y eliminar tareas.
* El usuario va poder pedirle a la apliación que desglose una tarea compleja en sub tareas más pequeñas y esta parte será automática.

## Dividir el problema

1. Gestion de la colección de las tareas.
2. La posibilidad de iteractuar con el usuario a traves de la terminal.
3. Se debe almacenar las tareas para que no se pierdan.
4. Comunicarse con un servicio de inteligencia artificial externo

## Patrones

* Añadir, eliminar y completar son patrones similares que manipulan los elementos de la lista. Una Tarea es una entidad con un nombre, un estado y un Id.