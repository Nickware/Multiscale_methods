"""
Simulación con Velocity Verlet y visualización en tiempo real:
estructura 3D, distancias, energías y (nuevo) convergencia de ángulos H-C-H.
"""

import numpy as np
import matplotlib.pyplot as plt

from params import m_C, m_H, r_eq, r_CC_eq, theta_eq, dt, steps, ACCEL_CONV
from init import init_positions
from forces import compute_forces, bond_and_angle_energy, hch_angles, H_C1, H_C2
from io_output import init_xyz_file, write_xyz_frame, write_energy_file


def run_simulation_with_visualization(seed=None, plot_every=100,
                                       xyz_filename=None, energy_filename=None,
                                       xyz_every=100):
    """
    xyz_filename / energy_filename: si se pasan, se exportan la trayectoria en
    formato XYZ y el historial de energías a esos archivos (cada `xyz_every`
    pasos para el XYZ). Si se omiten, la simulación corre igual que antes,
    solo con la visualización en pantalla.
    """
    positions = init_positions(seed=seed)
    velocities = np.zeros_like(positions)
    masses = np.array([m_C, m_C] + [m_H] * 6)

    export_xyz = xyz_filename is not None
    if export_xyz:
        init_xyz_file(xyz_filename)
        write_xyz_frame(xyz_filename, positions, 0)

    plt.ion()
    fig = plt.figure(figsize=(20, 6))

    ax1 = fig.add_subplot(141, projection='3d')
    ax2 = fig.add_subplot(142)
    ax3 = fig.add_subplot(143)
    ax4 = fig.add_subplot(144)

    # Historiales
    dist_CH_history = [[] for _ in range(6)]
    dist_CC_history = []
    pe_history, ke_history, te_history = [], [], []
    angles_C1_history = []  # cada elemento: lista de 3 ángulos H-C-H de C1
    angles_C2_history = []

    for step in range(steps):
        forces = compute_forces(positions, velocities)
        accel = ACCEL_CONV * forces / masses[:, None]
        positions += velocities * dt + 0.5 * accel * dt**2
        new_forces = compute_forces(positions, velocities)
        new_accel = ACCEL_CONV * new_forces / masses[:, None]
        velocities += 0.5 * (accel + new_accel) * dt

        pe = bond_and_angle_energy(positions)
        # 0.5*m*v^2 con m en uma y v en Å/fs da un valor en unidades "reducidas";
        # se divide por ACCEL_CONV para expresarlo en kcal/mol, consistente con pe.
        ke = 0.5 * sum(m * np.sum(v**2) for m, v in zip(masses, velocities)) / ACCEL_CONV

        for i in range(3):
            dist_CH_history[i].append(np.linalg.norm(positions[i + 2] - positions[0]))
        for i in range(3):
            dist_CH_history[i + 3].append(np.linalg.norm(positions[i + 5] - positions[1]))

        dist_CC_history.append(np.linalg.norm(positions[1] - positions[0]))
        pe_history.append(pe)
        ke_history.append(ke)
        te_history.append(pe + ke)

        angles_C1_history.append(hch_angles(positions, 0, H_C1))
        angles_C2_history.append(hch_angles(positions, 1, H_C2))

        if export_xyz and (step + 1) % xyz_every == 0:
            write_xyz_frame(xyz_filename, positions, step + 1, te_history[-1])

        if step % plot_every == 0:
            ax1.cla(); ax2.cla(); ax3.cla(); ax4.cla()

            # --- Estructura 3D ---
            ax1.scatter(*positions[0], c='black', s=200, label='C1')
            ax1.scatter(*positions[1], c='gray', s=200, label='C2')
            ax1.scatter(*positions[2:5].T, c='red', s=100, label='H (C1)')
            ax1.scatter(*positions[5:8].T, c='blue', s=100, label='H (C2)')
            ax1.plot(*np.array([positions[0], positions[1]]).T, 'k-', linewidth=3, alpha=0.7)
            for i in range(2, 5):
                ax1.plot(*np.array([positions[0], positions[i]]).T, 'r-', alpha=0.5)
            for i in range(5, 8):
                ax1.plot(*np.array([positions[1], positions[i]]).T, 'b-', alpha=0.5)
            ax1.set_title(f'Estructura del Etano (Paso {step})')
            ax1.set_xlim(-3, 3); ax1.set_ylim(-3, 3); ax1.set_zlim(-3, 3)
            ax1.legend()

            # --- Distancias ---
            for i in range(6):
                if i < 3:
                    ax2.plot(dist_CH_history[i], 'r-', alpha=0.7, label='C1-H' if i == 0 else "")
                else:
                    ax2.plot(dist_CH_history[i], 'b-', alpha=0.7, label='C2-H' if i == 3 else "")
            ax2.plot(dist_CC_history, 'k-', label='C-C')
            ax2.axhline(r_eq, color='r', linestyle='--', label='C-H eq')
            ax2.axhline(r_CC_eq, color='b', linestyle='--', label='C-C eq')
            ax2.set_title('Evolución de Distancias')
            ax2.set_xlabel('Paso'); ax2.set_ylabel('Distancia (Å)')
            ax2.legend(); ax2.grid(True)

            # --- Energías ---
            ax3.plot(pe_history, 'r-', label='Potencial')
            ax3.plot(ke_history, 'b-', label='Cinética')
            ax3.plot(te_history, 'k--', label='Total')
            ax3.set_title('Energías del Sistema')
            ax3.set_xlabel('Paso'); ax3.set_ylabel('Energía (kcal/mol)')
            ax3.legend(); ax3.grid(True)

            # --- Ángulos H-C-H (nuevo) ---
            angles_C1_arr = np.array(angles_C1_history)  # (n_steps, 3)
            angles_C2_arr = np.array(angles_C2_history)
            for k in range(3):
                ax4.plot(angles_C1_arr[:, k], 'r-', alpha=0.6, label='C1 H-C-H' if k == 0 else "")
            for k in range(3):
                ax4.plot(angles_C2_arr[:, k], 'b-', alpha=0.6, label='C2 H-C-H' if k == 0 else "")
            ax4.axhline(theta_eq, color='k', linestyle='--', label='109.47° (ideal)')
            ax4.set_title('Convergencia de Ángulos H-C-H')
            ax4.set_xlabel('Paso'); ax4.set_ylabel('Ángulo (°)')
            ax4.legend(); ax4.grid(True)

            plt.tight_layout()
            plt.draw()
            plt.pause(0.001)

    plt.ioff()

    if export_xyz:
        write_xyz_frame(xyz_filename, positions, steps, te_history[-1])
    if energy_filename is not None:
        write_energy_file(energy_filename, pe_history, ke_history, te_history)

    history = {
        "dist_CH": dist_CH_history,
        "dist_CC": dist_CC_history,
        "pe": pe_history,
        "ke": ke_history,
        "te": te_history,
        "angles_C1": angles_C1_history,
        "angles_C2": angles_C2_history,
    }
    return positions, history
