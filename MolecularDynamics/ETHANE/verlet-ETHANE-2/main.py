"""
Punto de entrada: ejecuta la minimización de energía del etano con
visualización en tiempo real (estructura 3D, distancias, energías y ángulos)
y muestra el análisis final.
"""

import matplotlib.pyplot as plt

from simulation import run_simulation_with_visualization
from analysis import analyze_final_state, print_summary
from io_output import print_visualization_instructions


if __name__ == "__main__":
    print("Iniciando simulación de minimización de energía para el etano...")

    xyz_filename = "ethane_trajectory.xyz"
    energy_filename = "ethane_energy.dat"

    final_pos, history = run_simulation_with_visualization(
        seed=42,
        xyz_filename=xyz_filename,
        energy_filename=energy_filename,
        xyz_every=100,
    )

    dist_CH_C1, dist_CH_C2, dist_CC, angles_C1, angles_C2 = analyze_final_state(final_pos)
    print_summary(dist_CH_C1, dist_CH_C2, dist_CC, angles_C1, angles_C2, history["te"][-1])
    print_visualization_instructions(xyz_filename)

    plt.show()
