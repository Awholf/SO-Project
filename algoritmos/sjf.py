def algoritmo_sjf(procesos):
    
    procesos.sort(key=lambda x: (x["llegada"], x["duracion"]))
    tiempo_actual = 0
    planificacion = []

    while procesos:
        disponibles = [p for p in procesos if p["llegada"] <= tiempo_actual]
        if disponibles:
            proceso = min(disponibles, key=lambda x: x["duracion"])
            procesos.remove(proceso)
            tiempo_inicio = max(tiempo_actual, proceso["llegada"])
            tiempo_fin = tiempo_inicio + proceso["duracion"]
            planificacion.append({"id": proceso["id"], "inicio": tiempo_inicio, "fin": tiempo_fin})
            tiempo_actual = tiempo_fin
        else:
            tiempo_actual += 1

    tiempo_promedio = sum(tarea["fin"] for tarea in planificacion) / len(planificacion)
    return planificacion, tiempo_promedio
