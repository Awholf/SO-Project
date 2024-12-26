def calcular_metricas(planificacion, procesos):
    """
    Calcula métricas de rendimiento: retorno promedio, espera promedio y respuesta promedio.
    :param planificacion: Lista de planificación con 'id', 'inicio' y 'fin'.
    :param procesos: Lista de procesos con 'id', 'llegada' y 'duracion'.
    :return: Diccionario con métricas calculadas.
    """
    if not planificacion or not procesos:
        raise ValueError("La planificación o la lista de procesos está vacía.")

    tiempos_retorno = []
    tiempos_espera = []
    tiempos_respuesta = []

    for proceso in procesos:
        # Filtrar las tareas relacionadas con el proceso actual
        tareas = [tarea for tarea in planificacion if tarea["id"] == proceso["id"]]
        if not tareas:
            continue

        # Calcular tiempos de finalización, retorno, espera y respuesta
        tiempo_finalizacion = tareas[-1]["fin"]
        tiempo_retorno = tiempo_finalizacion - proceso["llegada"]
        tiempos_retorno.append(tiempo_retorno)

        tiempo_espera = tiempo_retorno - proceso["duracion"]
        tiempos_espera.append(tiempo_espera)

        tiempo_respuesta = tareas[0]["inicio"] - proceso["llegada"]
        tiempos_respuesta.append(tiempo_respuesta)

    # Calcular promedios
    retorno_promedio = sum(tiempos_retorno) / len(tiempos_retorno) if tiempos_retorno else 0
    espera_promedio = sum(tiempos_espera) / len(tiempos_espera) if tiempos_espera else 0
    respuesta_promedio = sum(tiempos_respuesta) / len(tiempos_respuesta) if tiempos_respuesta else 0

    return {
        "retorno_promedio": retorno_promedio,
        "espera_promedio": espera_promedio,
        "respuesta_promedio": respuesta_promedio
    }
