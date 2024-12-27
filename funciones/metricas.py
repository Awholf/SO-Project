def calcular_metricas(planificacion, procesos):

    if not planificacion:
        raise ValueError("La planificación está vacía. No se pueden calcular métricas.")
    if not procesos:
        raise ValueError("La lista de procesos está vacía. No se pueden calcular métricas.")

    # Inicializar listas para métricas
    tiempos_retorno = []
    tiempos_espera = []
    tiempos_respuesta = []

    for proceso in procesos:
        # Obtener las tareas relacionadas con el proceso actual
        tareas = [tarea for tarea in planificacion if tarea["id"] == proceso["id"]]
        if not tareas:
            continue  # Saltar procesos sin planificación

        # Calcular métricas para el proceso actual
        tiempo_finalizacion = max(tarea["fin"] for tarea in tareas)
        tiempo_inicio = min(tarea["inicio"] for tarea in tareas)

        tiempo_retorno = tiempo_finalizacion - proceso["llegada"]
        tiempo_espera = tiempo_retorno - proceso["duracion"]
        tiempo_respuesta = tiempo_inicio - proceso["llegada"]

        # Agregar a las listas
        tiempos_retorno.append(tiempo_retorno)
        tiempos_espera.append(tiempo_espera)
        tiempos_respuesta.append(tiempo_respuesta)

    # Calcular promedios
    retorno_promedio = sum(tiempos_retorno) / len(tiempos_retorno) if tiempos_retorno else 0
    espera_promedio = sum(tiempos_espera) / len(tiempos_espera) if tiempos_espera else 0
    respuesta_promedio = sum(tiempos_respuesta) / len(tiempos_respuesta) if tiempos_respuesta else 0

    # Mostrar métricas
    print("\nMetricas de rendimiento:")
    print(f"Tiempo promedio de retorno: {retorno_promedio:.2f}")
    print(f"Tiempo promedio de espera: {espera_promedio:.2f}")
    print(f"Tiempo promedio de respuesta: {respuesta_promedio:.2f}")
