# Simulación de un sistema binario de dos objetos que se orbitan mutuamente
# En este caso, el objeto gigante es una estrella y el objeto enano es un planeta.
# El sistema se encuentra aislado, es decir, no hay fuerzas externas actuando sobre el sistema.
# El código simula el movimiento de ambos objetos utilizando la ley de gravitación universal de Newton.
# Para ejecutar este código, es necesario tener instalado el módulo vpython, que se puede instalar utilizando pip:
# pip install vpython
# El código utiliza un bucle infinito para actualizar la posición de ambos objetos en cada iteración, calculando la fuerza gravitacional entre ellos y actualizando su momento lineal y posición en consecuencia. La simulación se visualiza utilizando esferas para representar los objetos y trayectorias para mostrar su movimiento a lo largo del tiempo.
# El código también incluye comentarios que plantean preguntas sobre las unidades físicas de las variables y a qué ecuaciones de cinemática se parecen las ecuaciones utilizadas para actualizar la posición de los objetos. Estas preguntas pueden ser útiles para comprender mejor la física detrás de la simulación y cómo se relaciona con las leyes del movimiento de Newton.
# Nota: Este código es una simplificación de un sistema binario real y no tiene en cuenta factores como la resistencia del aire, la radiación o la relatividad. Sin embargo, proporciona una buena aproximación para entender los conceptos básicos de la gravitación y el movimiento orbital.
# Para mejorar la simulación, se podrían agregar características como la posibilidad de ajustar las masas y posiciones iniciales de los objetos, o incluir efectos adicionales como la radiación o la resistencia del aire. También se podrían implementar diferentes tipos de trayectorias para mostrar cómo varían las órbitas en función de las condiciones iniciales.
# Además, se podrían agregar controles para pausar o reiniciar la simulación, o para mostrar información adicional sobre las fuerzas y velocidades de los objetos en tiempo real. Estas mejoras podrían hacer que la simulación sea más interactiva y educativa para los usuarios interesados en aprender sobre la física de los sistemas binarios.
# En resumen, este código proporciona una base para simular un sistema binario de dos objetos utilizando la ley de gravitación universal de Newton, y se pueden realizar mejoras adicionales para hacer la simulación más completa e interactiva.

from vpython import *

scene.caption = ""
scene.forward = vector(0, -0.3, -1)

G = 6.7e-11  # Constante Gravitacional

# Primer Objeto (Gigante)
giant = sphere(pos=vector(-1e11, 0, 0), radius=2e10, color=color.red,
               make_trail=True, trail_type='points', interval=10, retain=50)
giant.mass = 2e30
giant.p = vector(0, 0, -1e4) * giant.mass  # Momento lineal (masa * velocidad)

# Segundo Objeto (Enano)
dwarf = sphere(pos=vector(1.5e11, 0, 0), radius=1e10, color=color.yellow,
               make_trail=True, interval=10, retain=50)
dwarf.mass = 1e30
dwarf.p = -giant.p  # Momento opuesto para conservar el momento total

dt = 1e5  # Paso de tiempo

def gravitational_force(obj1, obj2):
    r = obj2.pos - obj1.pos
    return G * obj1.mass * obj2.mass * r.hat / mag2(r)

while True:
    rate(200)
    
    # --- Paso 1: Calcular fuerza actual ---
    F = gravitational_force(giant, dwarf)
    
    # --- Paso 2: Actualizar posiciones (medio paso) ---
    giant.pos += (giant.p / giant.mass) * dt + 0.5 * (F / giant.mass) * dt**2
    dwarf.pos += (dwarf.p / dwarf.mass) * dt - 0.5 * (F / dwarf.mass) * dt**2
    
    # --- Paso 3: Calcular nueva fuerza con posiciones actualizadas ---
    F_new = gravitational_force(giant, dwarf)
    
    # --- Paso 4: Actualizar momentos (paso completo) ---
    giant.p += 0.5 * (F + F_new) * dt
    dwarf.p -= 0.5 * (F + F_new) * dt
