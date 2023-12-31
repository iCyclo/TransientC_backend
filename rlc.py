import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import io
import json
import base64

# Definir las funciones para el sistema de ecuaciones diferenciales
def model(y, t, R, L, C, V):
    Vc, I = y
    if C == 0:
        raise ValueError("La capacitancia (C) no puede ser cero.")
    dydt = [I/C, (V - R*I - Vc)/L]
    return dydt

"""
    R: Resistencia
    L: Inductancia
    C: Capacitancia
    V: Voltaje
"""
def rlc(R, L , C, V,time):
   


    # R = 10  # Resistencia (ohmios)
    # L = 0.25  # Inductancia (henrios)
    # C = 1e-3  # Capacitancia (faradios)
    # V = 5  # Voltaje de la fuente (voltios)

    # Condiciones iniciales
    y0 = [0.0, 0.0]

    # Tiempo de integración
    t = np.linspace(0, time, 1000)

    # Resolver el sistema de ecuaciones diferenciales
    sol = odeint(model, y0, t, args=(R, L, C, V))

    # Obtener los puntos de la simulación
    simulation_data = {"time": t.tolist(), "voltage": sol[:, 0].tolist(), "current": sol[:, 1].tolist()}

    return simulation_data