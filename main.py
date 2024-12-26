from algoritmos.fcfs import algoritmo_fcfs
from algoritmos.rr import algoritmo_round_robin
from algoritmos.sjf import algoritmo_sjf
from funciones.diagrama import generar_diagrama_gantt
from funciones.metricas import calcular_metricas
from funciones.validar import validar_procesos

#funcion npara mostrar el menu
def mostrar_menu():
    print("\n=== Simulador de Planificacion de Procesos en Sistemas Operativos ===")
    print("1. FCFS")
    print("2. Round Robin")
    print("3. SJF")
    print("4. Salir")
    opcion = int(input("Seleccione: "))
    return opcion
#funcion para entrada de datos (procesos)
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
                procesos = recibir_procesos()
                validar_procesos(procesos) 

                if opcion == 1:  # FCFS
                    print("\nSeleccionaste FCFS.")
                    planificacion, tiempo_promedio = algoritmo_fcfs(procesos)
                elif opcion == 2:  # Round Robin
                    print("\nSeleccionaste Round Robin.")
                    quantum = int(input("Ingresa el quantum: "))
                    if quantum <= 0:
                        raise ValueError("El quantum debe ser mayor a cero.")
                    planificacion, tiempo_promedio = algoritmo_round_robin(procesos, quantum)
                elif opcion == 3:  # SJF
                    print("\nSeleccionaste SJF.")
                    planificacion, tiempo_promedio = algoritmo_sjf(procesos)
                print("\nResultados:")
                #tabla de resultados
                for tarea in planificacion:
                    print(f"Proceso {tarea['id']} - Inicio: {tarea['inicio']} - Fin: {tarea['fin']}")
                print(f"\nTiempo promedio de finalizacion: {tiempo_promedio:.2f}")
                
                #promedios
                metricas = calcular_metricas(planificacion, procesos)
                print("\nMetricas de rendimiento:")
                print(f"Tiempo promedio de retorno: {metricas['retorno_promedio']:.2f}")
                print(f"Tiempo promedio de espera: {metricas['espera_promedio']:.2f}")
                print(f"Tiempo promedio de respuesta: {metricas['respuesta_promedio']:.2f}")
                #diagrama 
                generar_diagrama_gantt(planificacion)

            elif opcion == 4: 
                break
            else:
                print("\nNo valido.")

        except ValueError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nOcurrio un error inesperado: {e}")

if __name__ == "__main__":
    main()