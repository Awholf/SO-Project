def algoritmo_round_robin(procesos, quantum):
    """
    Algoritmo Round Robin simplificado, mantiene id, inicio, y fin.
    :param procesos: Lista de procesos con 'id', 'llegada', y 'duracion'.
    :param quantum: Tiempo de quantum para cada proceso.
    :return: Lista de planificacion con tiempos de inicio y fin, y tiempo promedio de finalización.
    """
    cola = procesos[:]
    tiempo_actual = 0
    planificacion = []

    while cola:
        proceso = cola.pop(0)
        tiempo_inicio = max(tiempo_actual, proceso["llegada"])
        tiempo_ejecucion = min(proceso["duracion"], quantum)
        tiempo_fin = tiempo_inicio + tiempo_ejecucion
        planificacion.append({"id": proceso["id"], "inicio": tiempo_inicio, "fin": tiempo_fin})
        tiempo_actual = tiempo_fin

        tiempo_restante = proceso["duracion"] - tiempo_ejecucion
        if tiempo_restante > 0:
            cola.append({"id": proceso["id"], "llegada": tiempo_fin, "duracion": tiempo_restante})

    tiempo_promedio = sum(tarea["fin"] for tarea in planificacion) / len(procesos)
    return planificacion, tiempo_promedio