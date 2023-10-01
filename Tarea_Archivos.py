 
import json
tareas = []

print("Con este programa puedes entregar tus tareas y eliminar o marcar las tareas que ya hiciste\n")

def guardar_tareas(archivo, tareas):
    with open(archivo, 'w') as file:
        json.dump(tareas, file)

def agregar_tarea():
    tarea = input("Ingresa una nueva tarea:\n ")
    tareas.append(tarea)
    print("Tarea agregada con exito")

def eliminar_tarea():
    if tareas:
        tarea = int(input("Ingresa el número de la tarea que deseas marcar como realizada: ")) - 1
        if 0 <= tarea < len(tareas):
            tareas.pop(tarea)
            print("Tarea marcada con exito")
        else:
            print("Esta tarea no existe")
    else:
        print("No tienes tareas")

def mostrar_tareas():
    if tareas:
        print("Lista de las tareas\n")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    else:
        print("No tienes tareas")

def main():
    opcion = 0

    while opcion != 4:
        print("<---Lista de tareas-->\n")
        print("1: Agregar tarea")
        print("2: Marcar una tarea completada")
        print("3: Mostrar las tareas")
        print("4: Salir\n")

        opcion = int(input("Selecciona una opción:\n "))

        if opcion == 1:
            agregar_tarea()
        elif opcion == 2:
            eliminar_tarea()
        elif opcion == 3:
            mostrar_tareas()
        elif opcion == 4:
            guardar_tareas("tareas.txt", tareas)
            print("Gracias por usar este programa:)")
        else:
            print("Error!")

if __name__ == "__main__":
    main()

            



