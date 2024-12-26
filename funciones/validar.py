def validar_procesos(procesos):
    #excepciones
    for proceso in procesos:
        if "id" not in proceso or "llegada" not in proceso or "duracion" not in proceso:
            raise ValueError(f"El proceso {proceso.get('id', 'desconocido')} tiene datos incompletos.")
        if proceso["llegada"] < 0:
            raise ValueError(f"El tiempo de llegada no puede ser negativo (Proceso {proceso['id']}).")
        if proceso["duracion"] <= 0:
            raise ValueError(f"La duración debe ser mayor a cero (Proceso {proceso['id']}).")
