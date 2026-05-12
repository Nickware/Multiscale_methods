# Simulación de un sistema binario usando el método Leapfrog
# Este código simula la interacción gravitacional entre dos cuerpos (una estrella gigante y una enana)
# utilizando el método Leapfrog para actualizar las posiciones y velocidades de manera eficiente.
# El método Leapfrog es un método de integración numérica que es especialmente útil para sistemas dinámicos como este, ya que es simétrico y conserva la energía a largo plazo mejor que otros métodos como Euler.
# En esta simulación, se inicializan las posiciones y velocidades de los dos cuerpos, y luego se actualizan iterativamente en un bucle infinito. Las fuerzas gravitacionales se calculan en cada paso para actualizar las velocidades y posiciones de los cuerpos.
# Para ejecutar este código, asegúrate de tener instalada la biblioteca VPython, que se utiliza para la visualización de los objetos en 3D. Puedes instalarla usando pip:
# pip install vpython
# Al ejecutar el código, verás dos esferas representando la estrella gigante y la enana, moviéndose en sus órbitas debido a la interacción gravitacional entre ellas. Las trayectorias de los cuerpos se mostrarán como líneas de puntos detrás de ellos, lo que te permitirá visualizar claramente sus movimientos a lo largo del tiempo.
# Nota: Asegúrate de ajustar los parámetros como las masas, posiciones iniciales y velocidades según sea necesario para observar diferentes comportamientos en el sistema binario.
# Autor: [Tu Nombre]
# Fecha: [Fecha de creación]
# Importamos la biblioteca VPython para la visualización
# Configuramos la escena para una mejor visualización del sistema binario
# Definimos la constante gravitacional y los objetos que representan la estrella gigante y la enana, asignándoles masas, posiciones iniciales y velocidades.
# Implementamos la función para calcular la fuerza gravitacional entre los dos cuerpos.
# Inicializamos las velocidades de los cuerpos para el método Leapfrog, ajustándolas para que estén en t = -dt/2.
# En el bucle principal, actualizamos las posiciones de los cuerpos, calculamos las fuerzas en las nuevas posiciones y luego actualizamos las velocidades para el siguiente paso de tiempo.
# El resultado es una simulación visual de un sistema binario en movimiento, mostrando cómo las dos estrellas interactúan gravitacionalmente a lo largo del tiempo.

from vpython import *

scene.caption = ""
scene.forward = vector(0, -0.3, -1)

G = 6.7e-11  # Constante Gravitacional

# Objetos (giant y dwarf)
giant = sphere(pos=vector(-1e11, 0, 0), radius=2e10, color=color.red,
               make_trail=True, trail_type='points', interval=10, retain=50)
giant.mass = 2e30
giant.v = vector(0, 0, -1e4)  # Velocidad inicial (no momento lineal)

dwarf = sphere(pos=vector(1.5e11, 0, 0), radius=1e10, color=color.yellow,
               make_trail=True, interval=10, retain=50)
dwarf.mass = 1e30
dwarf.v = -giant.v * (giant.mass / dwarf.mass)  # Conservación de momento

dt = 1e5  # Paso de tiempo

def gravitational_force(obj1, obj2):
    r = obj2.pos - obj1.pos
    return G * obj1.mass * obj2.mass * r.hat / mag2(r)

# Inicialización tipo Leapfrog: velocidades en t = -dt/2
F = gravitational_force(giant, dwarf)
giant.v -= 0.5 * (F / giant.mass) * dt
dwarf.v += 0.5 * (F / dwarf.mass) * dt

while True:
    rate(200)
    # Paso 1: Actualizar posiciones (con velocidades en t = n-1/2)
    giant.pos += giant.v * dt
    dwarf.pos += dwarf.v * dt
    
    # Paso 2: Calcular fuerzas en nuevas posiciones
    F = gravitational_force(giant, dwarf)
    
    # Paso 3: Actualizar velocidades (a t = n+1/2)
    giant.v += (F / giant.mass) * dt
    dwarf.v -= (F / dwarf.mass) * dt
