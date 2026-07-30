"""
Salida a archivo: trayectoria molecular en formato XYZ y registro de energías.
"""

ATOM_SYMBOLS = ["C", "C", "H", "H", "H", "H", "H", "H"]


def init_xyz_file(filename):
    """Limpia/crea el archivo XYZ antes de empezar a escribir frames."""
    open(filename, "w").close()


def write_xyz_frame(filename, positions, step, energy=None):
    """Agrega un frame al archivo XYZ (formato estándar: N átomos, comentario, coords)."""
    with open(filename, "a") as f:
        f.write(f"{len(positions)}\n")
        if energy is not None:
            f.write(f"Step: {step}, Energy: {energy:.4f} kcal/mol\n")
        else:
            f.write(f"Step: {step}\n")
        for symbol, pos in zip(ATOM_SYMBOLS, positions):
            f.write(f"{symbol} {pos[0]:.6f} {pos[1]:.6f} {pos[2]:.6f}\n")


def write_energy_file(filename, pe_history, ke_history, te_history):
    """Escribe el historial completo de energías, una fila por paso."""
    with open(filename, "w") as f:
        f.write("# Paso Energia_Potencial Energia_Cinetica Energia_Total\n")
        for i, (pe, ke, te) in enumerate(zip(pe_history, ke_history, te_history)):
            f.write(f"{i} {pe} {ke} {te}\n")


def print_visualization_instructions(xyz_filename):
    print(f"\nArchivos generados:")
    print(f"- {xyz_filename}: trayectoria molecular (formato XYZ)")
    print(f"- ethane_energy.dat: datos de energía por paso")
    print(f"\nPara visualizar la trayectoria:")
    print(f"1. Con xmakemol: xmakemol -f {xyz_filename}")
    print(f"2. Con VMD: vmd {xyz_filename}")
    print(f"3. Con Ovito: ovito {xyz_filename}")
