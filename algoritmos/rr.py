def algoritmo_round_robin(procesos, quantum):
    
    #https://gist.github.com/fitorec/57344289af3d2da8a7a255f2448d26b1
    
    # ordena los procesos por tiempo de llegada
    procesos.sort(key=lambda x: x["llegada"])
    cola = []  # mantiene la cola para procesos pendientes
    tiempo_actual = 0  # tiempo actual de la CPU
    planificacion = []  #almacena tiempos de inicio y fin de cada proceso
    tiempos_finalizacion = {}  # registra los tiempos finales 
    procesos_restantes = procesos[:]  # copia la lista de procesos originales

    while procesos_restantes or cola:

        while procesos_restantes and procesos_restantes[0]["llegada"] <= tiempo_actual:
            cola.append(procesos_restantes.pop(0))

        if cola:
            # elige el primer proceso en la cola
            proceso = cola.pop(0)
            tiempo_inicio = max(tiempo_actual, proceso["llegada"])
            # calcular el tiempo de ejecucion en el quantum
            tiempo_ejecucion = min(proceso["duracion"], quantum)
            tiempo_fin = tiempo_inicio + tiempo_ejecucion

            # registrar la planificacion del proceso
            planificacion.append({
                "id": proceso["id"],
                "inicio": tiempo_inicio,
                "fin": tiempo_fin
            })

            tiempo_actual = tiempo_fin

            tiempo_restante = proceso["duracion"] - tiempo_ejecucion
            if tiempo_restante > 0:
                # volver a añadir a la cola si el proceso no ha terminado
                cola.append({"id": proceso["id"], "llegada": tiempo_actual, "duracion": tiempo_restante})
            else:
                # registrar el tiempo de finalizacion unico
                tiempos_finalizacion[proceso["id"]] = tiempo_fin
        else:
            # avanzar el tiempo si no hay procesos listos
            tiempo_actual += 1

    #tiempo promedio de finalizacion
    tiempo_promedio = sum(tiempos_finalizacion.values()) / len(tiempos_finalizacion)
    return planificacion, tiempo_promedio
