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
