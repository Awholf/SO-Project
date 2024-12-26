def calcular_metricas(planificacion, procesos):
  
    tiempos_retorno = []
    tiempos_espera = []
    tiempos_respuesta = []

    for proceso in procesos:
        plan = [tarea for tarea in planificacion if tarea["id"] == proceso["id"]]
        if not plan:
            continue
        tiempo_finalizacion = plan[-1]["fin"]
        # Tiempo de retorno
        tiempo_retorno = tiempo_finalizacion - proceso["llegada"]
        tiempos_retorno.append(tiempo_retorno)

        # Tiempo de espera
        tiempo_espera = tiempo_retorno - proceso["duracion"]
        tiempos_espera.append(tiempo_espera)

        # Tiempo de respuesta
        tiempo_respuesta = plan[0]["inicio"] - proceso["llegada"]
        tiempos_respuesta.append(tiempo_respuesta)

    #Promedios
    retorno_promedio = sum(tiempos_retorno) / len(tiempos_retorno)
    espera_promedio = sum(tiempos_espera) / len(tiempos_espera)
    respuesta_promedio = sum(tiempos_respuesta) / len(tiempos_respuesta)

    return {
        "retorno_promedio": retorno_promedio,
        "espera_promedio": espera_promedio,
        "respuesta_promedio": respuesta_promedio
    }
