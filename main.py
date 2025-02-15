from algoritmos.fcfs import algoritmo_fcfs
from algoritmos.rr import algoritmo_round_robin
from algoritmos.sjf import algoritmo_sjf
from funciones.diagrama import generar_diagrama_gantt
from funciones.validar import validar_procesos
from funciones.metricas import calcular_metricas


def mostrar_menu():
    print("\n=== Simulador de Planificacion de Procesos en Sistemas Operativos ===")
    print("1. FCFS")
    print("2. Round Robin")
    print("3. SJF")
    print("4. Salir")
    opcion = int(input("Seleccione: "))
    return opcion

def recibir_procesos():
    procesos = []
    n = int(input("Ingrese el numero de procesos: "))

    for i in range(n):
        print(f"\nProceso {i + 1}:")
        id_proceso = i + 1
        llegada = int(input("Tiempo de llegada: "))
        duracion = int(input("Duracion rafaga de CPU: "))
        procesos.append({"id": id_proceso, "llegada": llegada, "duracion": duracion})

    return procesos

def main():
    while True:
        try:
            opcion = mostrar_menu()

            if opcion in [1, 2, 3]:
                # Mostrar mensaje antes de recibir procesos
                if opcion == 1:
                    print("\nSeleccionaste FCFS.")
                elif opcion == 2:
                    print("\nSeleccionaste Round Robin.")
                elif opcion == 3:
                    print("\nSeleccionaste SJF.")

                procesos = recibir_procesos()
                validar_procesos(procesos)

                if opcion == 1:  # FCFS
                    planificacion, tiempo_promedio = algoritmo_fcfs(procesos)
                elif opcion == 2:  # Round Robin
                    quantum = int(input("Ingresa el quantum: "))
                    if quantum <= 0:
                        raise ValueError("El quantum debe ser mayor a cero.")
                    planificacion, tiempo_promedio = algoritmo_round_robin(procesos, quantum)
                elif opcion == 3:  # SJF
                    planificacion, tiempo_promedio = algoritmo_sjf(procesos)

                # Mostrar resultados
                print("\nResultados:")
                for tarea in planificacion:
                    print(f"Proceso {tarea['id']} - Inicio: {tarea['inicio']} - Fin: {tarea['fin']}")
                print(f"\nTiempo promedio: {tiempo_promedio:.2f}")

                # Calcular y mostrar métricas
                try:
                    calcular_metricas(planificacion, procesos)
                except ValueError as e:
                    print(f"\nError al calcular métricas: {e}")

                # Generar diagrama de Gantt
                generar_diagrama_gantt(planificacion)

            elif opcion == 4:  # Salir
                break
            else:
                print("\nOpcion no valida")

        except ValueError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nOcurrio un error inesperado: {e}")

if __name__ == "__main__":
    main()
