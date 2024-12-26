import  matplotlib.pyplot as plt

def generar_diagrama_gantt(planificacion):
  
    fig, ax = plt.subplots()
    for tarea in planificacion:
        ax.broken_barh(
            [(tarea["inicio"], tarea["fin"] - tarea["inicio"])],  # duracion
            (tarea["id"] * 10, 9),  # posicion del proceso en el eje Y
            facecolors=('tab:blue')
        )
        ax.text(
            tarea["inicio"] + (tarea["fin"] - tarea["inicio"]) / 2,
            tarea["id"] * 10 + 5,
            f"P{tarea['id']}",
            ha='center', va='center', color='white'
        )

    ax.set_ylim(0, (len(planificacion) + 1) * 10)  # Altura
    ax.set_xlim(0, max(t["fin"] for t in planificacion) + 1)  # Ancho
    ax.set_xlabel("Tiempo")
    ax.set_ylabel("Procesos")
    ax.set_yticks([t["id"] * 10 + 5 for t in planificacion])
    ax.set_yticklabels([f"P{t['id']}" for t in planificacion])
    ax.set_title("Diagrama de Gantt")
    plt.grid(True)
    plt.show()
