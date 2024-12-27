def validar_procesos(procesos):
    
    if not procesos:
        raise ValueError("La lista de procesos está vacía.")

    for proceso in procesos:
        if proceso["llegada"] < 0:
            raise ValueError(f"El tiempo de llegada no puede ser negativo (Proceso {proceso['id']}).")
        if proceso["duracion"] <= 0:
            raise ValueError(f"La duración debe ser mayor a cero (Proceso {proceso['id']}).")
