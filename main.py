import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

"""
Simulador de Osmosis en Tejido Vegetal

Este programa permite a los estudiantes simular la variación de masa de trozos de papa o zanahoria
tras ser sumergidos en soluciones de NaCl a diferentes concentraciones.

Autor: Tu Nombre
Repositorio: https://github.com/tu_usuario/simulador-osmosis
"""

# Modelo simplificado de osmosis por tipo de vegetal
sensitivity = {
    "Papa": 0.15,
    "Zanahoria": 0.10
}

def calcular_masa_final(vegetal, masa_inicial, concentracion, tiempo):
    """
    Calcula la masa final del vegetal tras el proceso de osmosis.

    Args:
        vegetal (str): "Papa" o "Zanahoria"
        masa_inicial (float): masa inicial en gramos
        concentracion (float): concentración de NaCl en g/mol
        tiempo (float): tiempo de inmersión en minutos

    Returns:
        float: masa final estimada en gramos
    """
    factor = sensitivity[vegetal]
    delta = - factor * concentracion * (tiempo / 10)

    # Agua pura (0 g/mol): posibilidad de ganancia de masa
    if concentracion == 0:
        delta = + factor * 0.05 * (tiempo / 10)

    masa_final = masa_inicial * (1 + delta)
    return max(0, masa_final)

def simular():
    """Función para manejar el botón de simulación."""
    try:
        vegetal = vegetal_var.get()
        masa_inicial = float(masa_entry.get())
        concentracion = float(concentracion_var.get())
        tiempo = float(tiempo_entry.get())

        masa_final = calcular_masa_final(vegetal, masa_inicial, concentracion, tiempo)

        resultado_label.config(text=f"Masa final estimada: {masa_final:.2f} g")

    except Exception as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Simulador de Osmosis en Tejido Vegetal")
root.geometry("400x350")

# Widgets
vegetal_label = tk.Label(root, text="Seleccione el vegetal:")
vegetal_label.pack()

vegetal_var = tk.StringVar(value="Papa")
vegetal_menu = ttk.Combobox(root, textvariable=vegetal_var, values=["Papa", "Zanahoria"])
vegetal_menu.pack()

masa_label = tk.Label(root, text="Ingrese la masa inicial (g):")
masa_label.pack()

masa_entry = tk.Entry(root)
masa_entry.pack()

concentracion_label = tk.Label(root, text="Seleccione la concentración de NaCl (g/mol):")
concentracion_label.pack()

concentracion_var = tk.StringVar(value="0.0")
concentracion_menu = ttk.Combobox(root, textvariable=concentracion_var,
                                  values=["0.0", "0.2", "0.4", "0.6", "0.8"])
concentracion_menu.pack()

tiempo_label = tk.Label(root, text="Ingrese el tiempo de inmersión (min):")
tiempo_label.pack()

tiempo_entry = tk.Entry(root)
tiempo_entry.pack()

simular_button = tk.Button(root, text="Simular", command=simular)
simular_button.pack(pady=10)

resultado_label = tk.Label(root, text="Masa final estimada: ---")
resultado_label.pack(pady=10)

# Iniciar el loop principal
tk.mainloop()
