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
