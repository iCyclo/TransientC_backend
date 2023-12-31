import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Definir las funciones para el sistema de ecuaciones diferenciales
def modelo(y, t, R, L, V):
    I = y
    dIdt = (V - R * I) / L
    return dIdt
# R, L, V, time
def rl(R,L,V,time):

    print("DATA", R, L, V, time)
    # # Parámetros del circuito RL
    # R = 5  # Resistencia (ohmios)
    # L = 0.1  # Inductancia (henrios)
    # V = 10  # Voltaje de la fuente (voltios)

    # Condiciónes iniciales
    y0 = [0.0, 0.0] 

    # Tiempo de integración
    t = np.linspace(0, time, 1000)

    # Resolver el sistema de ecuaciones diferenciales
    sol = odeint(modelo, y0, t, args=(R, L, V))

    simulation_data = {"time": t.tolist(), "voltage": sol[:, 0].tolist(), "current": sol[:, 1].tolist()}
    
    return simulation_data