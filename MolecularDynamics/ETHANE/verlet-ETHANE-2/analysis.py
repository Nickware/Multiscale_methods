"""
Análisis geométrico y energético del estado final de la simulación.
"""

import numpy as np
from params import theta_eq
from forces import hch_angles, H_C1, H_C2


def analyze_final_state(final_pos):
    dist_CH_C1 = [np.linalg.norm(final_pos[i] - final_pos[0]) for i in H_C1]
    dist_CH_C2 = [np.linalg.norm(final_pos[i] - final_pos[1]) for i in H_C2]
    dist_CC = np.linalg.norm(final_pos[1] - final_pos[0])

    angles_C1 = hch_angles(final_pos, 0, H_C1)
    angles_C2 = hch_angles(final_pos, 1, H_C2)

    return dist_CH_C1, dist_CH_C2, dist_CC, angles_C1, angles_C2


def print_summary(dist_CH_C1, dist_CH_C2, dist_CC, angles_C1, angles_C2, te_final):
    print("\n=== RESULTADOS FINALES ===")
    print(f"Distancias C-H en C1: {np.array(dist_CH_C1).round(4)} Å")
    print(f"Distancias C-H en C2: {np.array(dist_CH_C2).round(4)} Å")
    print(f"Distancia C-C: {dist_CC:.4f} Å")
    print(f"Ángulos H-C-H en C1: {np.array(angles_C1).round(2)}°")
    print(f"Ángulos H-C-H en C2: {np.array(angles_C2).round(2)}°")
    print(f"Desviación media del tetraedro en C1: {np.mean(np.abs(np.array(angles_C1) - theta_eq)):.2f}°")
    print(f"Desviación media del tetraedro en C2: {np.mean(np.abs(np.array(angles_C2) - theta_eq)):.2f}°")
    print(f"Energía total final: {te_final:.4f} kcal/mol")
