import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ==============================================
# PARÁMETROS FÍSICOS (UNIDADES REALISTAS)
# ==============================================
m_C = 12.011  # masa del carbono [uma]
m_H = 1.008   # masa del hidrógeno [uma]
k_bond = 450.0  # constante de enlace [kcal/mol/Å²]
k_angle = 60.0  # constante angular [kcal/mol/rad²]
r_eq = 1.09    # distancia de equilibrio C-H [Å]
r_CC_eq = 1.54  # distancia de equilibrio C-C [Å]
theta_eq = 109.47  # ángulo de equilibrio tetraédrico [grados]
dt = 0.001    # paso de tiempo [ps]
steps = 20000  # más pasos para BD
temperature = 300.0  # temperatura [K]
k_B = 0.0019872041  # constante de Boltzmann [kcal/mol/K]
gamma = 100.0  # coeficiente de fricción [1/ps]

# ==============================================
# INICIALIZACIÓN DEL SISTEMA (ETANO)
# ==============================================
def init_positions():
    """Configuración inicial tetraédrica para el etano"""
    positions = np.zeros((8, 3))  # 2 carbonos + 6 hidrógenos
    
    # Posición de los carbonos
    positions[0] = [0, 0, 0]  # C1
    positions[1] = [r_CC_eq, 0, 0]  # C2
    
    # Vectores base para posiciones tetraédricas
    tetra_vecs = [
        [1, 1, 1],
        [-1, -1, 1],
        [-1, 1, -1],
        [1, -1, -1]
    ]
    
    # Normalizar vectores tetraédricos
    tetra_vecs = [np.array(v)/np.linalg.norm(v) * r_eq for v in tetra_vecs]
    
    # Posicionar hidrógenos en C1
    for i in range(3):
        positions[2+i] = positions[0] + tetra_vecs[i]
    
    # Para C2, rotamos 60 grados
    rot_angle = np.radians(60)
    rot_matrix = np.array([
        [1, 0, 0],
        [0, np.cos(rot_angle), -np.sin(rot_angle)],
        [0, np.sin(rot_angle), np.cos(rot_angle)]
    ])
    
    for i in range(3):
        rotated_vec = np.dot(rot_matrix, tetra_vecs[i])
        positions[5+i] = positions[1] + rotated_vec
    
    # Añadir pequeña perturbación aleatoria
    for i in range(2, 8):
        positions[i] += np.random.normal(0, 0.2, 3)
    
    return positions

# ==============================================
# CÁLCULO DE FUERZAS SISTEMÁTICAS PARA ETANO
# ==============================================
def compute_systematic_forces(pos):
    """Calcula solo las fuerzas sistemáticas (sin amortiguamiento)"""
    forces = np.zeros_like(pos)
    C1 = pos[0]
    C2 = pos[1]
    
    # Fuerzas de enlace C-C
    r_cc_vec = C2 - C1
    r_cc = np.linalg.norm(r_cc_vec)
    if r_cc > 0.01:
        f_mag_cc = -k_bond * (r_cc - r_CC_eq)
        force_dir = r_cc_vec / r_cc
        forces[1] += f_mag_cc * force_dir
        forces[0] -= f_mag_cc * force_dir
    
    # Fuerzas de enlace C-H
    for carbon_idx in [0, 1]:
        carbon_pos = pos[carbon_idx]
        # Índices de hidrógenos unidos a este carbono
        if carbon_idx == 0:
            h_indices = range(2, 5)  # H1, H2, H3
        else:
            h_indices = range(5, 8)  # H4, H5, H6
        
        for i in h_indices:
            r_vec = pos[i] - carbon_pos
            r = np.linalg.norm(r_vec)
            if r > 0.01:
                f_mag = -k_bond * (r - r_eq)
                forces[i] += f_mag * (r_vec/r)
                forces[carbon_idx] -= f_mag * (r_vec/r)
    
    # Fuerzas angulares H-C-H
    for carbon_idx in [0, 1]:
        carbon_pos = pos[carbon_idx]
        if carbon_idx == 0:
            h_indices = list(range(2, 5))
        else:
            h_indices = list(range(5, 8))
        
        for i in range(len(h_indices)):
            for j in range(i+1, len(h_indices)):
                hi = h_indices[i]
                hj = h_indices[j]
                
                r1 = pos[hi] - carbon_pos
                r2 = pos[hj] - carbon_pos
                
                r1_norm = np.linalg.norm(r1)
                r2_norm = np.linalg.norm(r2)
                
                if r1_norm > 0.01 and r2_norm > 0.01:
                    cos_theta = np.dot(r1, r2) / (r1_norm * r2_norm)
                    theta = np.arccos(np.clip(cos_theta, -1, 1))
                    
                    # Fuerza angular
                    delta_theta = theta - np.radians(theta_eq)
                    f_angle = -k_angle * delta_theta
                    
                    # Direcciones de fuerza aproximadas
                    dir1 = r1 / r1_norm
                    dir2 = r2 / r2_norm
                    
                    forces[hi] += f_angle * dir1
                    forces[hj] += f_angle * dir2
                    forces[carbon_idx] -= f_angle * (dir1 + dir2)
    
    return forces

# ==============================================
# INTEGRADOR BROWNIAN DYNAMICS (EULER-MARUYAMA)
# ==============================================
def brownian_step(pos, masses, dt, temperature):
    """Un paso de integración Brownian Dynamics"""
    # Calcular fuerzas sistemáticas
    systematic_forces = compute_systematic_forces(pos)
    
    # Calcular coeficiente de difusión
    D = k_B * temperature / (masses[:, None] * gamma)
    
    # Término determinista (deriva)
    deterministic = systematic_forces * dt / (masses[:, None] * gamma)
    
    # Término estocástico (ruido)
    noise_std = np.sqrt(2 * D * dt)
    stochastic = np.random.normal(0, noise_std, pos.shape)
    
    # Actualizar posiciones
    new_pos = pos + deterministic + stochastic
    
    return new_pos, systematic_forces

# ==============================================
# ESCRITURA DE ARCHIVO XYZ
# ==============================================
def write_xyz_frame(filename, positions, step, energy=None):
    """Escribe un frame en formato XYZ"""
    with open(filename, 'a') as f:
        f.write(f"8\n")
        if energy is not None:
            f.write(f"Step: {step}, Energy: {energy:.4f} kcal/mol, T: {temperature}K\n")
        else:
            f.write(f"Step: {step}, T: {temperature}K\n")
        
        # Escribir átomos de carbono
        f.write(f"C {positions[0][0]:.6f} {positions[0][1]:.6f} {positions[0][2]:.6f}\n")
        f.write(f"C {positions[1][0]:.6f} {positions[1][1]:.6f} {positions[1][2]:.6f}\n")
        
        # Escribir átomos de hidrógeno
        for i in range(2, 8):
            f.write(f"H {positions[i][0]:.6f} {positions[i][1]:.6f} {positions[i][2]:.6f}\n")

# ==============================================
# CÁLCULO DE ENERGÍA POTENCIAL
# ==============================================
def compute_potential_energy(pos):
    """Calcula la energía potencial del sistema"""
    pe = 0.0
    C1 = pos[0]
    C2 = pos[1]
    
    # Energía de enlace C-C
    r_cc = np.linalg.norm(C2 - C1)
    pe += 0.5 * k_bond * (r_cc - r_CC_eq)**2
    
    # Energía de enlaces C-H
    for carbon_idx in [0, 1]:
        carbon_pos = pos[carbon_idx]
        if carbon_idx == 0:
            h_indices = range(2, 5)
        else:
            h_indices = range(5, 8)
        
        for i in h_indices:
            r = np.linalg.norm(pos[i] - carbon_pos)
            pe += 0.5 * k_bond * (r - r_eq)**2
    
    # Energía angular
    for carbon_idx in [0, 1]:
        carbon_pos = pos[carbon_idx]
        if carbon_idx == 0:
            h_indices = list(range(2, 5))
        else:
            h_indices = list(range(5, 8))
        
        for i in range(len(h_indices)):
            for j in range(i+1, len(h_indices)):
                hi = h_indices[i]
                hj = h_indices[j]
                
                r1 = pos[hi] - carbon_pos
                r2 = pos[hj] - carbon_pos
                
                r1_norm = np.linalg.norm(r1)
                r2_norm = np.linalg.norm(r2)
                
                if r1_norm > 0.01 and r2_norm > 0.01:
                    cos_theta = np.dot(r1, r2) / (r1_norm * r2_norm)
                    theta = np.arccos(np.clip(cos_theta, -1, 1))
                    pe += 0.5 * k_angle * (theta - np.radians(theta_eq))**2
    
    return pe

# ==============================================
# SIMULACIÓN BROWNIAN DYNAMICS CON VISUALIZACIÓN
# ==============================================
def run_brownian_dynamics_simulation():
    # Configuración inicial
    positions = init_positions()
    masses = np.array([m_C, m_C] + [m_H]*6)
    
    # Preparar archivo XYZ
    xyz_filename = "ethane_brownian_trajectory.xyz"
    open(xyz_filename, 'w').close()
    write_xyz_frame(xyz_filename, positions, 0)
    
    # Preparar gráficos
    plt.ion()
    fig = plt.figure(figsize=(18, 6))
    
    # Gráfico 3D
    ax1 = fig.add_subplot(131, projection='3d')
    ax1.set_title(f'Etano - Brownian Dynamics (T={temperature}K)')
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(-3, 3)
    ax1.set_zlim(-3, 3)
    
    # Gráfico de distancias
    ax2 = fig.add_subplot(132)
    ax2.set_title('Distancias')
    ax2.set_xlabel('Paso')
    ax2.set_ylabel('Distancia (Å)')
    ax2.axhline(r_eq, color='r', linestyle='--', label='C-H eq')
    ax2.axhline(r_CC_eq, color='b', linestyle='--', label='C-C eq')
    
    # Gráfico de energía
    ax3 = fig.add_subplot(133)
    ax3.set_title('Energía Potencial')
    ax3.set_xlabel('Paso')
    ax3.set_ylabel('Energía (kcal/mol)')
    
    # Datos para gráficos
    dist_CH_history = [[] for _ in range(6)]
    dist_CC_history = []
    pe_history = []
    
    # Bucle principal de simulación
    for step in range(1, steps + 1):
        # Paso de Brownian Dynamics
        positions, forces = brownian_step(positions, masses, dt, temperature)
        
        # Calcular energía potencial
        pe = compute_potential_energy(positions)
        
        # Actualizar datos históricos
        for i in range(3):  # Hidrógenos en C1
            dist_CH_history[i].append(np.linalg.norm(positions[i+2] - positions[0]))
        for i in range(3):  # Hidrógenos en C2
            dist_CH_history[i+3].append(np.linalg.norm(positions[i+5] - positions[1]))
        
        dist_CC_history.append(np.linalg.norm(positions[1] - positions[0]))
        pe_history.append(pe)
        
        # Escribir frame XYZ cada 100 pasos
        if step % 100 == 0:
            write_xyz_frame(xyz_filename, positions, step, pe)
        
        # Actualizar gráficos cada 500 pasos
        if step % 500 == 0:
            # Limpiar gráficos
            ax1.cla()
            ax2.cla()
            ax3.cla()
            
            # Estructura 3D
            ax1.scatter(*positions[0], c='black', s=200, label='C1')
            ax1.scatter(*positions[1], c='gray', s=200, label='C2')
            ax1.scatter(*positions[2:5].T, c='red', s=100, label='H (C1)')
            ax1.scatter(*positions[5:8].T, c='blue', s=100, label='H (C2)')
            
            # Dibujar enlaces
            ax1.plot(*np.array([positions[0], positions[1]]).T, 'k-', linewidth=3, alpha=0.7)
            for i in range(2, 5):
                ax1.plot(*np.array([positions[0], positions[i]]).T, 'r-', alpha=0.5)
            for i in range(5, 8):
                ax1.plot(*np.array([positions[1], positions[i]]).T, 'b-', alpha=0.5)
            
            ax1.set_title(f'Brownian Dynamics - Paso {step}')
            ax1.set_xlim(-3, 3)
            ax1.set_ylim(-3, 3)
            ax1.set_zlim(-3, 3)
            ax1.legend()
            
            # Distancias
            for i in range(6):
                if i < 3:
                    ax2.plot(dist_CH_history[i], 'r-', alpha=0.7, label=f'C1-H{i+1}' if i == 0 else "")
                else:
                    ax2.plot(dist_CH_history[i], 'b-', alpha=0.7, label=f'C2-H{i-2}' if i == 3 else "")
            
            ax2.plot(dist_CC_history, 'k-', label='C-C')
            ax2.axhline(r_eq, color='r', linestyle='--', label='C-H eq')
            ax2.axhline(r_CC_eq, color='b', linestyle='--', label='C-C eq')
            ax2.set_title('Evolución de Distancias')
            ax2.legend()
            ax2.grid(True)
            
            # Energía
            ax3.plot(pe_history, 'r-', label='Potencial')
            ax3.set_title('Energía Potencial')
            ax3.legend()
            ax3.grid(True)
            
            plt.tight_layout()
            plt.draw()
            plt.pause(0.001)
    
    # Escribir frame final
    write_xyz_frame(xyz_filename, positions, steps, pe_history[-1])
    
    # Guardar datos de energía
    with open("ethane_brownian_energy.dat", "w") as f:
        f.write("# Paso Energía_Potencial\n")
        for i in range(len(pe_history)):
            f.write(f"{i} {pe_history[i]}\n")
    
    plt.ioff()
    return positions, dist_CH_history, dist_CC_history, pe_history

# ==============================================
# ANÁLISIS FINAL
# ==============================================
def analyze_final_state(final_pos):
    # Calcular distancias C-H
    dist_CH_C1 = [np.linalg.norm(final_pos[i] - final_pos[0]) for i in range(2, 5)]
    dist_CH_C2 = [np.linalg.norm(final_pos[i] - final_pos[1]) for i in range(5, 8)]
    
    # Calcular distancia C-C
    dist_CC = np.linalg.norm(final_pos[1] - final_pos[0])
    
    # Calcular ángulos H-C-H
    angles_C1 = []
    angles_C2 = []
    
    # Para C1
    for i in range(2, 5):
        for j in range(i+1, 5):
            vec1 = final_pos[i] - final_pos[0]
            vec2 = final_pos[j] - final_pos[0]
            cos_theta = np.dot(vec1, vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2))
            angles_C1.append(np.degrees(np.arccos(np.clip(cos_theta, -1, 1))))
    
    # Para C2
    for i in range(5, 8):
        for j in range(i+1, 8):
            vec1 = final_pos[i] - final_pos[1]
            vec2 = final_pos[j] - final_pos[1]
            cos_theta = np.dot(vec1, vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2))
            angles_C2.append(np.degrees(np.arccos(np.clip(cos_theta, -1, 1))))
    
    return dist_CH_C1, dist_CH_C2, dist_CC, angles_C1, angles_C2

# ==============================================
# EJECUCIÓN PRINCIPAL
# ==============================================
if __name__ == "__main__":
    print("Iniciando simulación de Brownian Dynamics para el etano...")
    print(f"Temperatura: {temperature} K")
    print(f"Coeficiente de fricción: {gamma} 1/ps")
    print(f"Pasos de tiempo: {steps}")
    print(f"Δt: {dt} ps")
    
    # Ejecutar simulación Brownian Dynamics
    final_pos, dist_CH_hist, dist_CC_hist, pe_history = run_brownian_dynamics_simulation()
    
    # Análisis final
    dist_CH_C1, dist_CH_C2, dist_CC, angles_C1, angles_C2 = analyze_final_state(final_pos)
    
    print("\n=== RESULTADOS FINALES ===")
    print(f"Distancias C-H en C1: {np.array(dist_CH_C1).round(4)} Å")
    print(f"Distancias C-H en C2: {np.array(dist_CH_C2).round(4)} Å")
    print(f"Distancia C-C: {dist_CC:.4f} Å")
    print(f"Ángulos H-C-H en C1: {np.array(angles_C1).round(2)}°")
    print(f"Ángulos H-C-H en C2: {np.array(angles_C2).round(2)}°")
    print(f"Energía potencial final: {pe_history[-1]:.4f} kcal/mol")
    
    print(f"\nArchivos generados:")
    print(f"- ethane_brownian_trajectory.xyz: Trayectoria Brownian Dynamics")
    print(f"- ethane_brownian_energy.dat: Datos de energía potencial")
    
    print(f"\nPara visualizar la trayectoria:")
    print(f"xmakemol -f ethane_brownian_trajectory.xyz")
    print(f"vmd ethane_brownian_trajectory.xyz")
    print(f"ovito ethane_brownian_trajectory.xyz")
    
    # Mostrar gráficos finales
    plt.show()