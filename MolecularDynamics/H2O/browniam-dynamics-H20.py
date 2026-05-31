# Simulación de dinámica browniana para una molécula de agua (H2O)
# En esta simulación, modelamos la molécula de agua como un sistema de tres partículas (oxígeno y dos hidrógenos) conectadas por resortes que representan los enlaces O-H. La dinámica se simula utilizando un enfoque de Langevin overdamped, que incluye tanto las fuerzas de resorte como el ruido térmico.
# El código a continuación realiza la simulación y grafica la evolución de la posición x de cada átomo a lo largo del tiempo.
# Nota: Este código es una simplificación y no incluye todas las interacciones presentes en una molécula de agua real, como las interacciones de ángulo o las fuerzas de van der Waals. Sin embargo, proporciona una base para entender la dinámica browniana en un sistema molecular simple.
# Requisitos:
# - Python 3.x
# - NumPy
# - Matplotlib
# Para ejecutar el código, asegúrate de tener las bibliotecas necesarias instaladas. Puedes instalar NumPy y Matplotlib usando pip:
# pip install numpy matplotlib
# Al ejecutar el código, se generará una gráfica que muestra la evolución de la posición x de cada átomo (oxígeno y dos hidrógenos) a lo largo del tiempo, lo que permite visualizar cómo se mueve cada átomo bajo la influencia de las fuerzas de resorte y el ruido térmico.
# Importar bibliotecas necesarias
# Este código simula la dinámica browniana de una molécula de agua (H2O) utilizando un modelo simplificado de resortes para representar los enlaces O-H. La simulación se realiza utilizando un enfoque de Langevin overdamped, que incluye tanto las fuerzas de resorte como el ruido térmico. Al final, se grafica la evolución de la posición x de cada átomo a lo largo del tiempo.
import numpy as np
import matplotlib.pyplot as plt

# Parámetros físicos y de simulación
k = 100.0              # Constante del resorte (kcal/mol/Å²)
r_eq = 0.96            # Longitud de enlace O-H (Å)
dt = 0.001             # Paso de tiempo
gamma = 1.0            # Coeficiente de fricción
kT = 0.001             # Energía térmica (kcal/mol)
steps = 10000

# Posiciones iniciales
positions = np.array([
    [0.0, 0.0],         # Oxígeno
    [1.5, 0.0],         # H1 desplazado
    [-1.0, 1.0]         # H2
])

trajectory = [positions.copy()]

# Función de fuerza por resorte
def spring_force(r_vec, r0, k):
    dist = np.linalg.norm(r_vec)
    if dist == 0:
        return np.zeros_like(r_vec)
    direction = r_vec / dist
    return -k * (dist - r0) * direction

# Simulación
for step in range(steps):
    forces = np.zeros_like(positions)

    # O-H1 y O-H2
    for i in [1, 2]:
        r_vec = positions[i] - positions[0]
        f = spring_force(r_vec, r_eq, k)
        forces[i] += f
        forces[0] -= f

    # Movimiento tipo Langevin overdamped
    noise = np.random.normal(scale=np.sqrt(2 * gamma * kT * dt), size=positions.shape)
    positions += dt / gamma * forces + noise

    trajectory.append(positions.copy())

# Convertir trayectoria a array
trajectory = np.array(trajectory)

# Graficar trayectoria en tiempo para cada átomo (coordenada x)
plt.figure(figsize=(10, 6))
labels = ['Oxígeno', 'Hidrógeno 1', 'Hidrógeno 2']
for i in range(3):
    plt.plot(trajectory[:, i, 0], label=f'{labels[i]} - x')
plt.xlabel('Tiempo (pasos)')
plt.ylabel('Posición x (Å)')
plt.title('Evolución de posición x con el tiempo')
plt.legend()
plt.grid()
plt.show()