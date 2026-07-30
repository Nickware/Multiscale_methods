"""
Construcción de la configuración inicial del etano (conformación escalonada aproximada).
"""

import numpy as np
from params import r_eq, r_CC_eq


def init_positions(seed=None):
    """
    Genera las posiciones iniciales de los 8 átomos del etano
    (índices: 0=C1, 1=C2, 2-4=H de C1, 5-7=H de C2).

    seed: si se pasa un entero, fija la semilla aleatoria para reproducibilidad
          de la pequeña perturbación inicial.
    """
    if seed is not None:
        np.random.seed(seed)

    positions = np.zeros((8, 3))

    # Posición de los carbonos
    positions[0] = [0, 0, 0]        # C1
    positions[1] = [r_CC_eq, 0, 0]  # C2

    # Vectores base tetraédricos
    tetra_vecs = [
        [1, 1, 1],
        [-1, -1, 1],
        [-1, 1, -1],
        [1, -1, -1],
    ]
    tetra_vecs = [np.array(v) / np.linalg.norm(v) * r_eq for v in tetra_vecs]

    # Hidrógenos en C1 (3 de las 4 direcciones tetraédricas)
    for i in range(3):
        positions[2 + i] = positions[0] + tetra_vecs[i]

    # Hidrógenos en C2, rotados 60° para aproximar la conformación escalonada
    rot_angle = np.radians(60)
    rot_matrix = np.array([
        [1, 0, 0],
        [0, np.cos(rot_angle), -np.sin(rot_angle)],
        [0, np.sin(rot_angle), np.cos(rot_angle)],
    ])

    for i in range(3):
        rotated_vec = np.dot(rot_matrix, tetra_vecs[i])
        positions[5 + i] = positions[1] + rotated_vec

    # Pequeña perturbación aleatoria para romper simetría exacta
    for i in range(2, 8):
        positions[i] += np.random.normal(0, 0.1, 3)

    return positions
