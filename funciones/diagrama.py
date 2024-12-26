import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def generar_diagrama_gantt(planificacion):
  
    if not planificacion:
        raise ValueError("La planificación está vacía. No se puede generar el diagrama de Gantt.")
    # Configuración inicial
    fig, ax = plt.subplots(figsize=(10, 5))
    colores = plt.cm.tab20.colors  # Paleta de colores
    etiquetas = []
    # Dibujar los bloques para cada proceso
    for tarea in planificacion:
        proceso_id = tarea["id"]
        inicio = tarea["inicio"]
        duracion = tarea["fin"] - tarea["inicio"]
        ax.broken_barh([(inicio, duracion)], (proceso_id - 0.4, 0.8), facecolors=colores[proceso_id % len(colores)])
        etiquetas.append(f"Proceso {proceso_id}")
    # Etiquetas y configuraciones
    ax.set_xlabel("Tiempo")
    ax.set_ylabel("Procesos")
    ax.set_yticks([tarea["id"] for tarea in planificacion])
    ax.set_yticklabels(etiquetas)
    ax.set_title("Diagrama de Gantt")
    ax.grid(True)
    # Crear una leyenda
    legend_handles = [Patch(color=colores[i % len(colores)], label=f"Proceso {i + 1}") for i in range(len(planificacion))]
    ax.legend(handles=legend_handles, loc="upper right")

    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()

