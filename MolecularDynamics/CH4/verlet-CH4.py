# Simulación de dinámica molecular para una molécula de metano (CH4) usando el método de Verlet
# Este código simula la vibración de los enlaces C-H en el metano, mostrando la evolución de las posiciones, energías y distancias a lo largo del tiempo.
# Parámetros físicos, configuración inicial, cálculo de fuerzas, integración de las ecuaciones de movimiento y visualización se incluyen en el código.
# Al final de la simulación, se analizan las distancias y ángulos para evaluar la estabilidad de la molécula y su conformación final.

# Nota: Este código es para fines educativos y no incluye efectos cuánticos ni interacciones más complejas como fuerzas de Van der Waals o enlaces múltiples.
# Requiere las bibliotecas numpy, matplotlib y IPython para su ejecución. Asegúrate de tenerlas instaladas antes de correr el código.
# Para ejecutar este código, simplemente cópialo en un entorno de Python (como Jupyter Notebook) y ejecútalo. Verás la evolución de la molécula de metano en tiempo real, junto con gráficos de las distancias C-H y las energías potencial, cinética y total.
# Al finalizar la simulación, se imprimirán las distancias finales entre el carbono y los hidrógenos, los ángulos H-C-H y una medida de la desviación del tetraedro ideal.
# ¡Disfruta explorando la dinámica molecular del metano!
# Nota: Este código es una simplificación y no representa completamente la complejidad de las interacciones moleculares reales. Para simulaciones más precisas, se podrían incluir términos adicionales en el potencial, como fuerzas de Van der Waals, enlaces múltiples, o efectos cuánticos. Sin embargo, este ejemplo proporciona una base sólida para entender los conceptos fundamentales de la dinámica molecular y la simulación de sistemas moleculares simples.
# Además, ten en cuenta que la elección de los parámetros (como la constante de enlace y el paso de tiempo) puede afectar la estabilidad y precisión de la simulación. Experimenta con diferentes valores para ver cómo afectan el comportamiento de la molécula.


# Si estás utilizando otro entorno, asegúrate de instalar las bibliotecas adecuadas para tu configuración.
# Este código es una simulación básica de la dinámica molecular de una molécula de metano (CH4) utilizando el método de Verlet para integrar las ecuaciones de movimiento. La simulación incluye un potencial armónico para los enlaces C-H, un término de amortiguamiento viscoso para evitar oscilaciones excesivas, y visualizaciones en tiempo real de la evolución de la molécula, las distancias C-H y las energías potencial, cinética y total.
# Al final de la simulación, se analizan las distancias y ángulos para evaluar la estabilidad de la molécula y su conformación final. Este código es ideal para fines educativos y para entender los conceptos básicos de la dinámica molecular. Para simulaciones más avanzadas, se podrían incluir términos adicionales en el potencial, como fuerzas de Van der Waals, enlaces múltiples, o efectos cuánticos.
# ¡Disfruta explorando la dinámica molecular del metano y aprendiendo sobre los fundamentos de la simulación de sistemas moleculares!
# Recuerda que la simulación es una herramienta poderosa para entender el comportamiento de las moléculas, pero siempre es importante interpretar los resultados con cuidado y considerar las limitaciones del modelo utilizado. En este caso, el modelo es una simplificación que no incluye todas las interacciones posibles, pero proporciona una base sólida para aprender sobre la dinámica molecular y la simulación de sistemas moleculares simples.
# ¡Buena suerte y diviértete aprendiendo sobre dinámica molecular!
 

# Importación de bibliotecas necesarias para la simulación y visualización
# numpy para cálculos numéricos, matplotlib para gráficos, mpl_toolkits para gráficos 3D, IPython.display para limpiar la salida en cada paso y time para medir el tiempo de ejecución.
# Asegúrate de tener estas bibliotecas instaladas en tu entorno de Python para ejecutar el código correctamente.
# Si estás utilizando un entorno como Jupyter Notebook, puedes instalar las bibliotecas necesarias usando pip:
# !pip install numpy matplotlib ipython 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from IPython.display import clear_output
import time

# ======================
# PARÁMETROS FÍSICOS
# ======================
m_C = 12.011  # masa del carbono [uma]
m_H = 1.008   # masa del hidrógeno [uma]
k_bond = 450.0  # constante de enlace [kcal/mol/Å²]
r_eq = 1.09    # distancia de equilibrio [Å]
dt = 0.002    # paso de tiempo reducido [fs]
steps = 3000   # pasos totales

# ======================
# CONFIGURACIÓN INICIAL
# ======================
np.random.seed(42)
positions = np.zeros((5, 3))  # [C, H1, H2, H3, H4]
positions[1:] = np.random.uniform(-0.3, 0.3, (4, 3))  # H cerca del centro
velocities = np.zeros_like(positions)
masses = np.array([m_C] + [m_H]*4)  # Definición de masas

# ======================
# FUNCIÓN DE FUERZAS
# ======================
def compute_forces(pos):
    forces = np.zeros_like(pos)
    C = pos[0]
    
    # Fuerzas de enlace C-H (armónico)
    for i in range(1, 5):
        r_vec = pos[i] - C
        r = max(np.linalg.norm(r_vec), 0.01)  # Evitar división por cero
        f_mag = -k_bond * (r - r_eq)
        forces[i] = f_mag * (r_vec/r)
        forces[0] -= f_mag * (r_vec/r)
    
    # Amortiguamiento viscoso (γ = 0.1)
    forces -= 0.1 * velocities
    
    return forces

# ======================
# SIMULACIÓN
# ======================
trajectory = []
energies = []
dist_history = []

plt.figure(figsize=(12, 5))
start_time = time.time()

for step in range(steps):
    # Velocity Verlet
    forces = compute_forces(positions)
    positions += velocities * dt + 0.5 * forces/masses[:, None] * dt**2
    new_forces = compute_forces(positions)
    velocities += 0.5 * (forces + new_forces)/masses[:, None] * dt
    
    # Energías y almacenamiento
    pe = 0.5 * k_bond * sum((np.linalg.norm(positions[i]-positions[0])-r_eq)**2 for i in range(1,5))
    ke = 0.5 * sum(m * np.sum(v**2) for m, v in zip(masses, velocities))
    
    if step % 10 == 0:
        trajectory.append(positions.copy())
        energies.append((pe, ke, pe+ke))
        dist_history.append([np.linalg.norm(positions[i]-positions[0]) for i in range(1,5)])
    
    # Visualización cada 50 pasos
    if step % 50 == 0:
        clear_output(wait=True)
        elapsed = time.time() - start_time
        print(f"Paso {step}/{steps} | Tiempo: {elapsed:.1f}s | PE: {pe:.2f} kcal/mol")
        
        # Gráfico 3D
        ax = plt.subplot(131, projection='3d')
        ax.scatter(*positions[0], c='black', s=200, label='C')
        ax.scatter(*positions[1:].T, c='red', s=100, label='H')
        for i in range(1,5):
            ax.plot(*np.array([positions[0], positions[i]]).T, 'b-', alpha=0.4)
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_zlim(-1.5, 1.5)
        ax.set_title(f'Paso {step}')
        
        # Distancias C-H
        plt.subplot(132)
        plt.plot(np.array(dist_history))
        plt.axhline(r_eq, color='black', linestyle='--')
        plt.title('Distancias C-H')
        plt.ylabel('Å')
        plt.xlabel('Paso (x10)')
        
        # Energías
        plt.subplot(133)
        if energies:
            pe, ke, te = zip(*energies)
            plt.plot(pe, label='Potencial', c='red')
            plt.plot(ke, label='Cinética', c='blue')
            plt.plot(te, label='Total', c='black', linestyle='--')
            plt.title('Energías')
            plt.xlabel('Paso (x10)')
            plt.legend()
        
        plt.tight_layout()
        plt.pause(0.001)

# ======================
# ANÁLISIS FINAL
# ======================
final_pos = trajectory[-1]
distances = [np.linalg.norm(final_pos[i]-final_pos[0]) for i in range(1,5)]
angles = []
for i in range(1,5):
    for j in range(i+1,5):
        vec1 = final_pos[i] - final_pos[0]
        vec2 = final_pos[j] - final_pos[0]
        cos_theta = np.dot(vec1, vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2))
        angles.append(np.degrees(np.arccos(np.clip(cos_theta, -1, 1))))

print("\n=== RESULTADOS FINALES ===")
print(f"Distancias C-H: {np.array(distances).round(3)} Å")
print(f"Ángulos H-C-H: {np.array(angles).round(1)}°")
print(f"\nDesviación media del tetraedro: {np.mean(np.abs(np.array(angles)-109.47)):.1f}°")
print(f"Distancia promedio final: {np.mean(distances):.3f} ± {np.std(distances):.3f} Å")