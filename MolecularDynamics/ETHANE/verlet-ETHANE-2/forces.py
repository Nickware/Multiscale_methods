"""
Cálculo de fuerzas para el modelo armónico simplificado del etano.

Incluye:
  - Fuerzas de enlace C-C y C-H (armónicas).
  - Fuerzas angulares H-C-H, corregidas para que la componente aplicada
    sea perpendicular al vector radial (dentro del plano H-C-H), que es
    la dirección que realmente modifica el ángulo sin estirar el enlace.
  - Amortiguamiento proporcional a la velocidad.

No incluye fuerzas dihedrales explícitas ni efectos electrónicos/estéricos.
"""

import numpy as np
from params import k_bond, k_angle, r_eq, r_CC_eq, theta_eq, damping

H_C1 = range(2, 5)
H_C2 = range(5, 8)


def _bond_forces(pos, forces):
    C1, C2 = pos[0], pos[1]

    # Enlace C-C
    r_cc_vec = C2 - C1
    r_cc = np.linalg.norm(r_cc_vec)
    if r_cc > 0.01:
        f_mag_cc = -k_bond * (r_cc - r_CC_eq)
        force_dir = r_cc_vec / r_cc
        forces[1] += f_mag_cc * force_dir
        forces[0] -= f_mag_cc * force_dir

    # Enlaces C-H
    for carbon_idx, h_indices in [(0, H_C1), (1, H_C2)]:
        carbon_pos = pos[carbon_idx]
        for i in h_indices:
            r_vec = pos[i] - carbon_pos
            r = np.linalg.norm(r_vec)
            if r > 0.01:
                f_mag = -k_bond * (r - r_eq)
                forces[i] += f_mag * (r_vec / r)
                forces[carbon_idx] -= f_mag * (r_vec / r)


def _angle_forces(pos, forces):
    """
    Fuerza angular H-C-H corregida.

    Para theta = angulo(r1, r2), con U = 1/2 * k_angle * (theta - theta_eq)^2,
    el gradiente de theta respecto a la posición de cada hidrógeno apunta en la
    dirección perpendicular al radio correspondiente (dentro del plano r1-r2),
    con magnitud 1/|r|. Aplicar la fuerza a lo largo del radio (como en la
    versión original) no cambia theta y por lo tanto no corrige el ángulo.
    """
    theta_eq_rad = np.radians(theta_eq)

    for carbon_idx, h_indices in [(0, list(H_C1)), (1, list(H_C2))]:
        carbon_pos = pos[carbon_idx]

        for i in range(len(h_indices)):
            for j in range(i + 1, len(h_indices)):
                hi, hj = h_indices[i], h_indices[j]

                r1 = pos[hi] - carbon_pos
                r2 = pos[hj] - carbon_pos
                r1_norm = np.linalg.norm(r1)
                r2_norm = np.linalg.norm(r2)

                if r1_norm <= 0.01 or r2_norm <= 0.01:
                    continue

                u1 = r1 / r1_norm
                u2 = r2 / r2_norm

                cos_theta = np.clip(np.dot(u1, u2), -1, 1)
                theta = np.arccos(cos_theta)
                sin_theta = np.sqrt(max(1 - cos_theta**2, 1e-8))

                delta_theta = theta - theta_eq_rad
                dUdtheta = k_angle * delta_theta

                # Direcciones perpendiculares a u1 y u2, en el plano r1-r2.
                # d(theta)/d(r1) = -perp1/r1_norm, d(theta)/d(r2) = -perp2/r2_norm,
                # y F = -dU/dtheta * d(theta)/dr, así que el signo neto es positivo.
                perp1 = (u2 - cos_theta * u1) / sin_theta
                perp2 = (u1 - cos_theta * u2) / sin_theta

                f_hi = dUdtheta / r1_norm * perp1
                f_hj = dUdtheta / r2_norm * perp2

                forces[hi] += f_hi
                forces[hj] += f_hj
                forces[carbon_idx] -= (f_hi + f_hj)


def compute_forces(pos, vel):
    forces = np.zeros_like(pos)
    _bond_forces(pos, forces)
    _angle_forces(pos, forces)
    forces -= damping * vel
    return forces


def bond_and_angle_energy(pos):
    """
    Energía potencial de enlaces (C-C, C-H) y angular (H-C-H).
    Esta expresión no cambió respecto a la versión original: el bug
    estaba solo en la fuerza derivada de ella, no en la energía misma.
    """
    theta_eq_rad = np.radians(theta_eq)

    pe_bonds = 0.0
    r_cc = np.linalg.norm(pos[1] - pos[0])
    pe_bonds += 0.5 * k_bond * (r_cc - r_CC_eq) ** 2

    for carbon_idx, h_indices in [(0, H_C1), (1, H_C2)]:
        carbon_pos = pos[carbon_idx]
        for i in h_indices:
            r = np.linalg.norm(pos[i] - carbon_pos)
            pe_bonds += 0.5 * k_bond * (r - r_eq) ** 2

    pe_angles = 0.0
    for carbon_idx, h_indices in [(0, list(H_C1)), (1, list(H_C2))]:
        carbon_pos = pos[carbon_idx]
        for i in range(len(h_indices)):
            for j in range(i + 1, len(h_indices)):
                hi, hj = h_indices[i], h_indices[j]
                r1 = pos[hi] - carbon_pos
                r2 = pos[hj] - carbon_pos
                r1_norm = np.linalg.norm(r1)
                r2_norm = np.linalg.norm(r2)
                if r1_norm > 0.01 and r2_norm > 0.01:
                    cos_theta = np.dot(r1, r2) / (r1_norm * r2_norm)
                    theta = np.arccos(np.clip(cos_theta, -1, 1))
                    pe_angles += 0.5 * k_angle * (theta - theta_eq_rad) ** 2

    return pe_bonds + pe_angles


def hch_angles(pos, carbon_idx, h_indices):
    """Devuelve la lista de ángulos H-C-H (en grados) para un carbono dado."""
    carbon_pos = pos[carbon_idx]
    angles = []
    h_indices = list(h_indices)
    for i in range(len(h_indices)):
        for j in range(i + 1, len(h_indices)):
            vec1 = pos[h_indices[i]] - carbon_pos
            vec2 = pos[h_indices[j]] - carbon_pos
            cos_theta = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
            angles.append(np.degrees(np.arccos(np.clip(cos_theta, -1, 1))))
    return angles
