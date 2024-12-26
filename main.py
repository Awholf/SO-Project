from algoritmos.fcfs import algoritmo_fcfs
from algoritmos.rr import algoritmo_round_robin
from algoritmos.sjf import algoritmo_sjf
import matplotlib.pyplot as plt

def mostrar_menu():
    
    print("\n=== Simulador de Planificacion de Procesos en Sistemas Operativos ===")
    print("1. FCFS")
    print("2. Round Robin")
    print("3. SJF")
    print("4. Salir")
    opcion = int(input("Seleccione "))
    return opcion

def recibir_procesos():
   
    procesos = []
    n = int(input("Ingrese el numero de procesos "))

    for i in range(n):
        print(f"\nProceso {i + 1}:")
        id_proceso = i + 1
        llegada = int(input("Tiempo de llegada: "))
        duracion = int(input("Duracion de la ráfaga de CPU: "))
        procesos.append({"id": id_proceso, "llegada": llegada, "duracion": duracion})

    return procesos

def main():
    while True:
        opcion = mostrar_menu()

        if opcion == 1:  # FCFS
            print("\nSeleccionaste FCFS.")
            procesos = recibir_procesos()
            planificacion, tiempo_promedio = algoritmo_fcfs(procesos)
        elif opcion == 2:  # Round Robin
            print("\nSeleccionaste Round Robin.")
            procesos = recibir_procesos()
            quantum = int(input("Ingresa el quantum: "))
            planificacion, tiempo_promedio = algoritmo_round_robin(procesos, quantum)
        elif opcion == 3:  # SJF
            print("\nSeleccionaste SJF.")
            procesos = recibir_procesos()
            planificacion, tiempo_promedio = algoritmo_sjf(procesos)
        elif opcion == 4:  # Salir
            break
        else:
            print("\nOpcion no valida.")
            continue

        # Mostrar resultados
        print("\nResultados:")
        for tarea in planificacion:
            print(f"Proceso {tarea['id']} - Inicio: {tarea['inicio']} - Fin: {tarea['fin']}")
        print(f"\nTiempo promedio: {tiempo_promedio:.2f}")

if __name__ == "__main__":
    main()

