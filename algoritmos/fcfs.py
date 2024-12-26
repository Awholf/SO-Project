def algoritmo_fcfs(procesos):
    """
    Algoritmo FCFS simplificado, mantiene id, inicio, y fin.
    :param procesos: Lista de procesos con 'id', 'llegada', y 'duracion'.
    :return: Lista de planificacion con tiempos de inicio y fin, y tiempo promedio de finalización.
    """
    procesos.sort(key=lambda x: x["llegada"])  # Ordenar por tiempo de llegada
    tiempo_actual = 0
    planificacion = []

    for proceso in procesos:
        tiempo_inicio = max(tiempo_actual, proceso["llegada"])
        tiempo_fin = tiempo_inicio + proceso["duracion"]
        planificacion.append({"id": proceso["id"], "inicio": tiempo_inicio, "fin": tiempo_fin})
        tiempo_actual = tiempo_fin

    tiempo_promedio = sum(tarea["fin"] for tarea in planificacion) / len(procesos)
    return planificacion, tiempo_promedio